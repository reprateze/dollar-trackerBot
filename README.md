Dollar Tracker Telegram Bot

Automation project built with Python that scrapes the current USD exchange rate and sends it directly to Telegram.

---

## Overview

This project uses browser automation to fetch the latest USD exchange rate and delivers it as a message via Telegram Bot.

It’s designed as a simple automation project focusing on:

* Web scraping
* API integration
* Environment variable security
* Automation workflows

---

## Technologies

* Python
* Playwright
* Requests
* python-dotenv
* Telegram Bot API

---

## Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/dollar-tracker-telegram-bot.git
cd dollar-tracker-telegram-bot
```

### 2. Install dependencies

```
pip install -r requirements.txt
playwright install
```

### 3. Configure environment variables

Create a `.env` file:

```
TELEGRAM_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

## Running the project

```
python envia_telegram.py
```

Or using the `.bat` file (Windows):

```
run.bat
```

---

## How it works

1. Playwright opens the browser in headless mode
2. Scrapes the USD exchange rate from the website
3. Sends the value via Telegram using Bot API

---
## Future Improvements

* Add scheduling (run automatically daily)
* Store historical data
* Add logging system
* Handle website structure changes

######################################
