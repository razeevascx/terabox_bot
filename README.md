# Terabox Bot

This project is a **Telegram bot** built using Python that allows users to interact with the Terabox. It includes a Docker setup for easy deployment and management as well.

## Features
- Easy to deploy using Docker and Docker Compose.
- Customizable and scalable to meet user needs.

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Docker and Docker Compose
- A Telegram bot token (You can obtain this from [ BotFather](https://core.telegram.org/bots#botfather) )

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/razeevascx/terabox_bot.git
      ```
2. **Cd into Repository**:
   ```bash
   cd terabox_bot
     ```

3. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root of your project and add your Telegram bot token:
   ```plaintext
   TELEGRAM_TOKEN="token"
   ```

5. **Run the Bot**:
   To run the bot, execute:
   ```bash
   python bot.py
   ```

### Running with Docker

To run the bot in a Docker container, follow these steps:

1. **Build the Docker Image**:
   ```bash
   docker-compose build
   ```

2. **Run the Bot**:
   ```bash
   docker-compose up
   ```

## Project Structure

```
.
├── Dockerfile              # Docker configuration for building the bot image
├── docker-compose.yml      # Docker Compose file for setting up services
├── bot.py                  # Main bot logic
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
└── README.md               # This file
```


### Notes:
- Make sure to replace `"token"` in the `.env` file section with your actual Telegram bot token.
- If you are using Docker, set your API key in the Docker Compose file at line 7.

If you need any further changes or have more content to include, just let me know!
