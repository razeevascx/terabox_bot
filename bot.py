import os
import requests
import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from tempfile import gettempdir
from datetime import datetime
from telegram.error import BadRequest 

# Function to handle /start command
# Function to handle /start command
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    first_name = user.first_name or "there"  # Fallback if first name is None
    last_name = user.last_name or ""  # Fallback if last name is None
    full_name = f"{first_name} {last_name}".strip()  # Combine first and last name

    update.message.reply_text(f"🙏 Hello {full_name} ! \n \nSend me a Terabox link, and I'll download the file for you.")

# Function to create a user log directory and log file
def setup_user_logging(user_id: int, username: str) -> str:
    user_dir = f"logs/{username}"
    os.makedirs(user_dir, exist_ok=True)

    log_file_path = os.path.join(user_dir, "log.json")
    if not os.path.exists(log_file_path):
        with open(log_file_path, 'w') as log_file:
            json.dump({"logs": []}, log_file, indent=4)
    
    return log_file_path

# Function to log messages to a file
def log_to_file(log_file_path: str, action: str, file_id=None, file_size=None) -> None:
    log_entry = {
        "event_time": datetime.now().isoformat(),
        "action": action
    }
    if file_id:
        log_entry["file_id"] = file_id
        log_entry["file_size_mb"] = file_size
    
    with open(log_file_path, 'r+') as log_file:
        logs = json.load(log_file)
        logs["logs"].append(log_entry)
        log_file.seek(0)
        json.dump(logs, log_file, indent=4)

# Function to download the file from Terabox without progress updates
def download_file_from_terabox(url: str, log_file_path: str, progress_message) -> str:
    file_id = url.split("/")[-1]
    download_url = f"https://apis.forn.fun/tera/data.php?id={file_id}"

    try:
        response = requests.get(download_url, stream=True, timeout=600)
        
        log_to_file(log_file_path, f"Attempting to download from: {download_url}")

        if response.status_code == 200:
            total_size = int(response.headers.get('Content-Length', 0))
            
            if total_size == 0:
                raise Exception("The file size returned by the server is 0 bytes. The file might not be available.")
            
            file_path = os.path.join(gettempdir(), f"downloaded_{file_id}.mp4")
            
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    if chunk:
                        f.write(chunk)

            log_to_file(log_file_path, "Downloaded file", file_id, total_size / (1024 * 1024))
            return file_path, total_size

        elif response.status_code == 503:
            raise Exception("The server is temporarily unavailable (503). Please try again later.")

        else:
            log_to_file(log_file_path, f"Failed to download file. Status code: {response.status_code}, Response: {response.text}")
            raise Exception(f"Failed to download file. Status code: {response.status_code}")

    except requests.Timeout:
        log_to_file(log_file_path, "Download operation timed out.")
        raise
    except requests.ConnectionError:
        log_to_file(log_file_path, "A connection error occurred.")
        raise
    except json.JSONDecodeError as e:
        log_to_file(log_file_path, f"JSON decode error: {str(e)}")
        raise Exception("Failed to parse response from server. It may be down or returning an unexpected response.")
    except Exception as e:
        log_to_file(log_file_path, f"An error occurred: {str(e)}")
        raise

# Function to handle messages and send downloaded file
def handle_message(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    user_id = update.message.from_user.id
    username = update.message.from_user.username if update.message.from_user.username else "unknown_user"

    # Set up logging for the user
    log_file_path = setup_user_logging(user_id, username)

    if "terabox" in url:
        try:
            # Send a message indicating that the download has started
            progress_message = update.message.reply_text("Started downloading...")

            # Download the file from Terabox
            file_path, size_bytes = download_file_from_terabox(url, log_file_path, progress_message)
            size_mb = size_bytes / (1024 * 1024)  # Convert size to MB
            size_mb = round(size_mb, 2)  # Round to two decimal places

            # Directly send the video with a caption containing the video ID and size
            with open(file_path, 'rb') as f:
                update.message.reply_document(
                    f,
                    caption=f"Video ID: {url.split('/')[-1]}\nSize: {size_mb} MB @teraboxtt01_bot"
                )

            # Remove the file after sending
            os.remove(file_path)
            log_to_file(log_file_path, "File sent successfully.")

            # Delete the "Started downloading..." message
            try:
                context.bot.delete_message(chat_id=update.message.chat_id, message_id=progress_message.message_id)
            except BadRequest as e:
                print(f"Warning: Unable to delete message - {str(e)}")

        except Exception as e:
            update.message.reply_text(f"Failed to download the file from {url}: {str(e)}")
            log_to_file(log_file_path, f"Download error: {str(e)}")
    else:
        update.message.reply_text("Please send a valid Terabox link.")
        log_to_file(log_file_path, "Invalid Terabox link received.")


# Main function to set up the bot
def main():
    token = os.getenv("TELEGRAM_API_KEY")
    
    if not token:
        print("Error: TELEGRAM_API_KEY environment variable not set")
        return
    
    updater = Updater(token, use_context=True)
    
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
