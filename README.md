# Sabarimala Virtual Queue Notification System

This project is a Python-based notification system designed to monitor the availability of booking slots for the Sabarimala Virtual Queue. It periodically checks the booking status via an external API and sends notifications to a Telegram chat when slots become available.

---

## Features

- **API Monitoring**: Calls the Sabarimala Virtual Queue API to check for available booking slots.
- **Telegram Notifications**: Sends real-time alerts to a specified Telegram chat using the Telegram Bot API.
- **Customizable Schedule**: Runs every 5 minutes using GitHub Actions.
- **Secure Configuration**: Uses environment variables to store sensitive information like API URLs and tokens.

---

## Prerequisites

### 1. Python Environment

- Python 3.9 or higher
- Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 2. Telegram Bot Setup

- Create a Telegram bot using [BotFather](https://core.telegram.org/bots#botfather).
- Obtain the bot token and chat ID.

### 3. Environment Variables

Create a `.env` file in the project directory with the following keys:

```env
API_URL=https://sabarimalaonline.org/api/eDarshan/darshansummary/100001
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```

---

## How It Works

1. The script calls the external API to fetch the booking status.
2. If booking slots are available, it sends a notification to the configured Telegram chat.
3. The script is scheduled to run every 5 minutes using GitHub Actions.

---

## Project Structure

```
.
├── main.py                # Main script to monitor API and send notifications
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not included in GitHub)
├── .github/workflows/     # GitHub Actions workflow files
│   └── check_api.yml      # Workflow to run the script every 5 minutes
└── README.md              # Project documentation
```

---

## GitHub Actions Workflow

The project includes a GitHub Actions workflow (`check_api.yml`) to automate the script execution. The workflow:

1. Runs every 5 minutes.
2. Sets up Python and installs dependencies.
3. Executes the `main.py` script with environment variables passed securely via GitHub Secrets.

---

## Usage

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Set up the `.env` file with your API URL, bot token, and chat ID.
3. Run the script locally:
   ```bash
   python3 main.py
   ```
4. Push the code to GitHub to enable the automated workflow.

---

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
