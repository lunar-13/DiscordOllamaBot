import discord
import requests
import json
import os
import re
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import sys
import pystray
from pystray import MenuItem as item, Icon
from PIL import Image, ImageDraw
from discord import app_commands

# Load your bot token from environment variables or replace with a string
TOKEN = "YOUR_BOT_TOKEN_HERE"
OLLAMA_URL = "http://localhost:11434/api/generate"

# Predefined models
MODEL_LIST = ["deepseek-r1:14b", "llama3.2"]  # Add/remove models as needed
current_model = MODEL_LIST[0]  # Default model

# Set up Discord bot with command tree
intents = discord.Intents.default()
client = discord.Client(intents=intents, heartbeat_timeout=60)  # Increase timeout to avoid disconnections
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()  # Sync slash commands
    print(f'Logged in as {client.user}')
    log_message("Bot started.")  # Log that the bot started in the text box

@tree.command(name="ask", description="Ask The AI a question.")
async def ask(interaction: discord.Interaction, prompt: str):
    """Handles the /ask command."""
    await interaction.response.defer()  # Defer response to avoid timeout

    response = await ollama_request(prompt)

    # Remove DeepSeek's <think> block if present
    cleaned_response = filter_deepseek_thoughts(response)

    # Ensure response is a string
    cleaned_response = str(cleaned_response)

    # Split response into chunks of 2000 characters max
    chunks = [cleaned_response[i:i+2000] for i in range(0, len(cleaned_response), 2000)]

    # Send the first part as the initial response
    await interaction.followup.send(chunks[0])

    # Send remaining parts as follow-ups
    for chunk in chunks[1:]:
        await interaction.followup.send(chunk)

@tree.command(name="model", description="Change the AI model.")
async def model(interaction: discord.Interaction, model_name: str):
    """Handles the /model command to change the AI model."""
    global current_model

    if model_name not in MODEL_LIST:
        await interaction.response.send_message(
            f"Invalid model. Available models: {', '.join(MODEL_LIST)}", ephemeral=True
        )
        return

    current_model = model_name
    await interaction.response.send_message(f"Model changed to **{current_model}**.", ephemeral=True)

async def ollama_request(prompt):
    """Sends a request to the local Ollama instance with a system prompt identifying it as 'AI'."""
    payload = {
        "model": current_model,
        "prompt": prompt,
        "system": "You are a helpful AI assistant.",
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(OLLAMA_URL, data=json.dumps(payload), headers=headers, stream=True)
        response.raise_for_status()
        
        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))  # Parse each line
                    if "response" in data:
                        full_response += data["response"]
                except json.JSONDecodeError:
                    continue  # Skip invalid JSON lines
        
        return full_response if full_response else "No response from AI."
    except Exception as e:
        return f"Error: {e}"

def filter_deepseek_thoughts(response):
    """Removes DeepSeek's '<think>...</think>' block from the response."""
    response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)  # Remove entire <think> block
    return response.strip()

# Tkinter GUI setup
def start_bot():
    log_message("Starting bot...")  # Log bot starting
    client.run(TOKEN)

def stop_bot():
    os._exit(0)

def on_closing():
    hide_window()

def hide_window():
    root.withdraw()
    tray_icon.visible = True

def show_window(icon, item):
    root.deiconify()
    tray_icon.visible = False

def create_tray_icon():
    icon_image = Image.new('RGB', (64, 64), (0, 0, 255))
    draw = ImageDraw.Draw(icon_image)
    draw.rectangle((10, 10, 54, 54), fill=(255, 255, 255))
    menu = (item('Show', show_window), item('Exit', lambda icon, item: exit_app()))
    return pystray.Icon("tray_icon", icon_image, "Bot Controller", menu)

def exit_app():
    tray_icon.stop()
    root.quit()
    os._exit(0)

def log_message(message):
    log_box.insert(tk.END, f"{message}\n")
    log_box.yview(tk.END)

root = tk.Tk()
root.title("Discord Bot Controller")
root.geometry("400x300")
root.protocol("WM_DELETE_WINDOW", on_closing)

start_button = tk.Button(root, text="Start Bot", command=lambda: threading.Thread(target=start_bot, daemon=True).start())
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Bot", command=stop_bot)
stop_button.pack(pady=5)

log_box = scrolledtext.ScrolledText(root, height=10, width=50)
log_box.pack(padx=10, pady=10)

tray_icon = create_tray_icon()
thr = threading.Thread(target=tray_icon.run, daemon=True)
thr.start()

root.mainloop()
