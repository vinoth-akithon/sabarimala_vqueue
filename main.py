import os
import requests
import dotenv
import warnings
from datetime import datetime


warnings.filterwarnings("ignore")

# Loading Environmental Variable
dotenv.load_dotenv()

# Configuration
API_URL = os.environ["API_URL"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]



def get_message(available_dates: list[str]) -> str:
    if available_dates:
        dates_block = "\n".join(f"      ➤ {d}" for d in available_dates)
        return f"""
        🟢  BOOKING STATUS UPDATE (Test)  🟢

🎉 *Booking Slot is NOW OPEN!*

⏰ Time: {datetime.now().strftime("%Y-%m-%d %I.%M %p")}

📅 Available dates: 
{dates_block}

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
    requests.post(url, json=payload)


def call_api_and_compare():
    # Call the external API
    print(API_URL)
    response = requests.post(API_URL, verify=False)
    response.raise_for_status()
    data = response.json()

    # Extract the attribute value
    available_dates = data.get("availableDatesList")

    # For testing
    # available_dates =  ["2025-12-28", "2026-04-16"]

    # Compare and send telegram notification
    send_telegram_alert(get_message(available_dates))

if __name__ == "__main__":
    call_api_and_compare()