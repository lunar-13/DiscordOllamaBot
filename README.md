# DiscordOllamaBot
A python powered discord bot that uses ollama as a core

This project is a Discord bot with a Tkinter-based graphical interface for starting and stopping the bot. The application also minimizes to the system tray when closed.

## Features
- Start and stop the Discord bot via GUI
- Log messages displayed in a text box
- Minimize to system tray instead of closing

## Requirements
- Python 3.8+
- A valid Discord bot token
- Ollama API running locally at `http://localhost:11434`

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Install Dependencies
This script automatically installs required dependencies, but you can also install them manually:
```sh
pip install -r requirements.txt
```

If `requirements.txt` is missing, install the necessary packages manually:
```sh
pip install discord requests pystray Pillow
```

### 3. Set Up Your Bot Token
Replace `YOUR_DISCORD_BOT_TOKEN` in the script with your actual Discord bot token or set it as an environment variable:
```sh
export DISCORD_BOT_TOKEN=your_token_here  # Linux/macOS
set DISCORD_BOT_TOKEN=your_token_here  # Windows (CMD)
```

### 4. Run the Bot
```sh
python bot.py
```

## Usage
- Click **Start Bot** to run the bot.
- Click **Stop Bot** to shut it down.
- Closing the window will minimize it to the system tray. Right-click the tray icon to restore or exit.

## Notes
- Ensure the Ollama API is running before asking the bot questions.
- The bot syncs commands on startup, which may take a moment.
- Modify `MODEL_LIST` in the script to add or remove supported AI models.

## Troubleshooting
If you encounter issues, try the following:
- Verify Python and pip are installed (`python --version`, `pip --version`).
- Ensure all dependencies are installed.
- Check that your Discord bot token is correct.
- Ensure Ollama API is accessible at `http://localhost:11434`.

For additional help, open an issue on GitHub.

