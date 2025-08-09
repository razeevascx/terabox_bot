<div align="center">

# Terabox Bot

_Seamless Telegram integration for Terabox file management_

![Last Commit](https://img.shields.io/github/last-commit/razeevascx/terabox_bot?label=last%20commit&color=blue&style=flat-square)
![Python](https://img.shields.io/badge/python-100%25-blue?style=flat-square)
![Languages](https://img.shields.io/github/languages/count/razeevascx/terabox_bot?label=languages&color=orange&style=flat-square)

**Built with the tools and technologies:**

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Telegram](https://img.shields.io/badge/-Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white)

</div>

---

## Key Features

- **Effortless Deployment** – Launch with Docker or locally in minutes
- **Customizable & Scalable** – Adapt the bot to your workflow and needs
- **Secure Token Management** – Environment-based configuration for safety
- **Cross-Platform** – Works on Windows, Linux, and macOS

## Tech Stack

- **Bot Framework:** Python 3.8+
- **Containerization:** Docker, Docker Compose
- **Messaging:** Telegram Bot API
- **Deployment:** Windows, Linux, macOS

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- Docker and Docker Compose
- A Telegram bot token ([Get one from BotFather](https://core.telegram.org/bots#botfather))

### Installation & Setup

1. **Clone the Repository**
   ```powershell
   git clone https://github.com/razeevascx/terabox_bot.git
   ```
2. **Navigate to Project**
   ```powershell
   cd terabox_bot
   ```
3. **Install Python Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables**
   Create a `.env` file in the root of your project and add your Telegram bot token:
   ```plaintext
   TELEGRAM_API_KEY="token"
   ```
5. **Run the Bot**
   ```powershell
   python bot.py
   ```

### Running with Docker

1. **Build the Docker Image**
   ```powershell
   docker-compose build
   ```
2. **Run the Bot**
   ```powershell
   docker-compose up
   ```

### Verification

- Open Telegram and interact with your bot to confirm it is running.

---

## Notes

- Replace `"token"` in the `.env` file with your actual Telegram bot token.
- For Docker, set your API key in the Docker Compose file at line 7.
- Update the volume in Docker Compose as needed for your environment.
- The project is tested and used in Docker; for local use, ensure the code reads the `.env` file correctly.

---
