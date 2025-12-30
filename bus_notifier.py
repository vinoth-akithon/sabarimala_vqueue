import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

from bs4 import BeautifulSoup

def parse_bus_info(bus_parent):
    """
    Parses the HTML content to extract useful information about a bus and returns it as a dictionary.

    Args:
        html_content (str): The HTML content to parse.

    Returns:
        dict: A dictionary containing the extracted information.
    """

    # Extract the bus information
    bus_info = {}

    # Extract the bus type and time from the parent div
    bus_info['bus_type'] = bus_parent.get('data-bus-type')
    bus_info['time'] = bus_parent.get('data-time')

    # Extract details from the bus item
    bus_item = bus_parent.find('div', class_='bus-item')
    if bus_item:
        # Operator name and bus type
        # operator_name = bus_item.find('span', class_='operator-name')
        # if operator_name:
        #     bus_info['operator_name'] = operator_name.text.strip()

        # Trip code
        # trip_code_link = bus_item.find('a', href=True)
        # if trip_code_link:
        #     bus_info['trip_code'] = trip_code_link.text.strip()

        # Departure time and location
        # departure_time = bus_item.find('span', class_='text-4 text-dark')
        # if departure_time:
        #     bus_info['departure_time'] = departure_time.text.strip()

        # departure_location = bus_item.find('small', class_='text-muted d-block')
        # if departure_location:
        #     bus_info['departure_location'] = departure_location.text.strip()

        # Duration and via information
        # duration = bus_item.find('span', class_='text-3 duration')
        # if duration:
        #     bus_info['duration'] = duration.text.strip()

        # via_info = bus_item.find('small', style=True)
        # if via_info:
        #     bus_info['via'] = via_info.text.strip()

        # Arrival time and location
        # arrival_time = bus_item.find('span', class_='text-5 text-dark')
        # if arrival_time:
        #     bus_info['arrival_time'] = arrival_time.text.strip()

        # arrival_location = bus_item.find('small', class_='text-muted d-block')
        # if arrival_location:
        #     bus_info['arrival_location'] = arrival_location.text.strip()

        # Price
        price = bus_item.find('div', class_='text-dark text-5 price mb-sm-1')
        if price:
            bus_info['price'] = price.text.strip()

        # Seats available
        seats_available_container = bus_item.find('div', id=re.compile(r"selectButton*"))
        seats_available = seats_available_container.find('span', class_='text-1')
        if seats_available:
            bus_info['seats_available'] = seats_available.text.strip()

    return bus_info

def get_list_of_buses():
    """
    Fetches an HTML page from the given URL, parses it, and returns the length of items in a list element with the specified class.

    Args:
        url (str): The URL of the external service to fetch the HTML from.
        list_class (str): The class attribute of the list element to find.

    Returns:
        int: The number of items in the list element with the specified class.
    """

    url = "https://www.tnstc.in/OTRSOnline/jqreq.do?hiddenAction=SearchService"
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.tnstc.in',
    'Referer': 'https://www.tnstc.in/OTRSOnline/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    }

    # Payload for Pampa bus
    payload = 'hiddenStartPlaceID=74&hiddenEndPlaceID=900&txtStartPlaceCode=TRI&txtEndPlaceCode=PPA&hiddenStartPlaceName=TRICHY&hiddenEndPlaceName=PAMPA&matchStartPlace=TRICHY&matchEndPlace=PAMPA&txtJourneyDate=DD%2FMM%2FYYYY&txtReturnDate=DD%2FMM%2FYYYY&hiddenCurrentDate=30%2F12%2F2025&hiddenMaxNoOfPassengers=16&hiddenMaxValidReservDate=29%2F01%2F2026&selectOnwardTimeSlab=&hiddenOnwardJourneyDate=13%2F01%2F2026&hiddenReturnJourneyDate=DD%2FMM%2FYYYY&hiddenTotalMales=&txtAdultMales=&txtChildMales=&selectStartPlace=TRI&selectEndPlace=PPA&txtAdultFemales=&txtChildFemales=&hiddenTotalFemales=&selectClass=&hiddenOnwardTimeSlab=&hiddenClassCategoryLookupID=&chkTatkal=&languageType=E&hiddenAction=SearchService&hiddenClassName=&matchPStartPlace=&matchPEndPlace=&txtdeptDatePtrip=&checkSingleLady=N&txtUserLoginID=&txtPassword=&txtCaptchaCode=&txtRUserLoginID=&txtRMobileNo=&txtRUserFullName=&txtRPassword=&hiddenUserType=G'
    
    # Payload for Chennai Bus for testing (as pampa buses not available)
    # payload = 'hiddenStartPlaceID=74&hiddenEndPlaceID=1358&txtStartPlaceCode=TRI&txtEndPlaceCode=CZZ&hiddenStartPlaceName=TRICHY&hiddenEndPlaceName=CHENNAI&matchStartPlace=TRICHY&matchEndPlace=CHENNAI&txtJourneyDate=DD%2FMM%2FYYYY&txtReturnDate=DD%2FMM%2FYYYY&hiddenCurrentDate=30%2F12%2F2025&hiddenMaxNoOfPassengers=16&hiddenMaxValidReservDate=29%2F01%2F2026&selectOnwardTimeSlab=&hiddenOnwardJourneyDate=31%2F12%2F2025&hiddenReturnJourneyDate=DD%2FMM%2FYYYY&hiddenTotalMales=&txtAdultMales=&txtChildMales=&selectStartPlace=TRI&selectEndPlace=CZZ&txtAdultFemales=&txtChildFemales=&hiddenTotalFemales=&selectClass=&hiddenOnwardTimeSlab=&hiddenClassCategoryLookupID=&chkTatkal=&languageType=E&hiddenAction=SearchService&hiddenClassName=&matchPStartPlace=&matchPEndPlace=&txtdeptDatePtrip=&checkSingleLady=N&txtUserLoginID=&txtPassword=&txtCaptchaCode=&txtRUserLoginID=&txtRMobileNo=&txtRUserFullName=&txtRPassword=&hiddenUserType=G'

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the list element with the specified class
    list_element = soup.find_all('div', class_="bus-list")  # Assuming it's a <ul> tag
    bus_info = [parse_bus_info(element) for element in list_element]
    return bus_info

from datetime import datetime

def get_message(list_of_buses: list[dict]) -> str:
    if len(list_of_buses) > 0:
        # Group buses by time and format the message
        buses_by_time = {}
        for bus in list_of_buses:
            time = bus['time']
            if time not in buses_by_time:
                buses_by_time[time] = []
            buses_by_time[time].append(bus)

        # Create the message blocks for each time slot
        time_blocks = []
        for time, buses in buses_by_time.items():
            bus_details = []
            for bus in buses:
                bus_type = bus['bus_type']
                seats_available = bus.get('seats_available', 'N/A')
                bus_details.append(f"      ➤ ⏰ {time} - {bus_type} - {seats_available}")
            # time_blocks.append(f"      ⏰ {time}:")
            time_blocks.extend(bus_details)

        # Join all time blocks into a single string
        time_blocks_str = "\n".join(time_blocks)

        return f"""
        🟢  BOOKING STATUS UPDATE (Test)  🟢

🎉 *Booking Slot is NOW OPEN!*

⏰ Time: {datetime.now().strftime("%Y-%m-%d %I.%M %p")}

📅 Available buses:
{time_blocks_str}

"""
    else:
        return f"""
        🔴  BOOKING STATUS UPDATE (Test) 🔴

⏳ *Booking Slot is NOT opened yet*

⏰ Time: {datetime.now().strftime("%Y-%m-%d %I.%M %p")}

"""

def send_telegram_alert(message):   
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload, verify=False)

if __name__ == "__main__":
    list_of_buses = get_list_of_buses()
    message = get_message(list_of_buses)
    send_telegram_alert(message)
