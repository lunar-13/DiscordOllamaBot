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
git clone https://github.com/lunar-13/DiscordOllamaBot.git
cd DiscordOllamaBot
```

### 2. Install Dependencies
Install dependencies with:
```
pip install discord requests pystray Pillow
```

### 3. Set Up Your Bot Token
Replace `YOUR_DISCORD_BOT_TOKEN` in the script with your actual Discord bot token or set it as an environment variable:
```python
import os
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN', 'your_token_here')
```

## Compile with PyInstaller
### 1. Install pyinstaller
```sh
pip install pyinstaller
```

### 2. Build the executable
Open a command prompt and run:
```sh
python3 -m PyInstaller --onefile --windowed --hidden-import=discord --hidden-import=requests --hidden-import=json --hidden-import=os --hidden-import=re --hidden-import=tkinter --hidden-import=pystray “C:\Path\To\Your\script.py”
```

### 3. Run the compiled exe
The compiled exe will be in the `dist` folder. Double-click `Main.exe` to start the application.

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
