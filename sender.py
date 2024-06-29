import discord
import asyncio
import keyboard
from pynput import mouse
import tkinter as tk
from tkinter import ttk
from discord.ext import commands
import threading
import sounddevice as sd
import numpy as np
import vc_id
# Your bot token and voice channel ID
BOT_TOKEN = '' # Put you Receiver Bot Token
VOICE_CHANNEL_ID = vc_id.vc_id

# Discord setup
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(int(VOICE_CHANNEL_ID))
    if channel and isinstance(channel, discord.VoiceChannel):
        await channel.connect()

# Tkinter GUI setup
root = tk.Tk()
root.title("Input Sender")

# GUI variables
send_inputs_var = tk.BooleanVar()
send_mouse_inputs_var = tk.BooleanVar()
convert_arrows_to_wasd_var = tk.BooleanVar()
convert_wasd_to_arrows_var = tk.BooleanVar()

send_inputs = False
send_mouse_inputs = False
convert_arrows_to_wasd = False
convert_wasd_to_arrows = False

def toggle_send_inputs():
    global send_inputs
    send_inputs = send_inputs_var.get()
    print(f"Send Inputs: {send_inputs}")

def toggle_send_mouse_inputs():
    global send_mouse_inputs
    send_mouse_inputs = send_mouse_inputs_var.get()
    print(f"Send Mouse Inputs: {send_mouse_inputs}")

def toggle_convert_arrows_to_wasd():
    global convert_arrows_to_wasd
    convert_arrows_to_wasd = convert_arrows_to_wasd_var.get()
    print(f"Convert Arrows to WASD: {convert_arrows_to_wasd}")

def toggle_convert_wasd_to_arrows():
    global convert_wasd_to_arrows
    convert_wasd_to_arrows = convert_wasd_to_arrows_var.get()
    print(f"Convert WASD to Arrows: {convert_wasd_to_arrows}")

ttk.Checkbutton(root, text="Send Inputs", variable=send_inputs_var, command=toggle_send_inputs).pack()
ttk.Checkbutton(root, text="Send Mouse Inputs", variable=send_mouse_inputs_var, command=toggle_send_mouse_inputs).pack()
ttk.Checkbutton(root, text="Convert Arrows to WASD", variable=convert_arrows_to_wasd_var, command=toggle_convert_arrows_to_wasd).pack()
ttk.Checkbutton(root, text="Convert WASD to Arrows", variable=convert_wasd_to_arrows_var, command=toggle_convert_wasd_to_arrows).pack()


# Keyboard and mouse input handlers
async def send_inputs_to_vc(inputs):
    voice_client = discord.utils.get(bot.voice_clients)
    if voice_client and voice_client.is_connected():
        # Generate a tone corresponding to the input
        duration = 0.05  # seconds
        sample_rate = 44100  # Hz
        
        frequencies = {
            'w': 523.25,      # Hz (C5)
            'a': 466.16,      # Hz (A#4)
            's': 493.88,      # Hz (B4)
            'd': 440.0,       # Hz (A4)
            'up': 659.25,     # Hz (E5)
            'left': 622.25,   # Hz (D#5)
            'down': 698.46,   # Hz (F5)
            'right': 587.33,  # Hz (D5)
            'space': 880.0    # Hz (A5)
        }

        frequency = frequencies.get(inputs, 440.0)  # Default to 440 Hz (A4) if input not found

        t = np.linspace(0, duration, int(sample_rate * duration), False)
        tone = 0.5 * np.sin(frequency * 2 * np.pi * t)  # Adjust amplitude (0.5 for half volume)
        sd.play(tone, sample_rate)
        sd.wait()
def process_key_event(event_name):
    if send_inputs:
        if convert_arrows_to_wasd:
            if event_name == 'up':
                event_name = 'w'
            elif event_name == 'down':
                event_name = 's'
            elif event_name == 'left':
                event_name = 'a'
            elif event_name == 'right':
                event_name = 'd'
        elif convert_wasd_to_arrows:
            if event_name == 'w':
                event_name = 'up'
            elif event_name == 's':
                event_name = 'down'
            elif event_name == 'a':
                event_name = 'left'
            elif event_name == 'd':
                event_name = 'right'
        asyncio.run(send_inputs_to_vc(event_name))
    print(f"Key pressed: {event_name}")

def process_mouse_event(event_type):
    if send_mouse_inputs:
        asyncio.run(send_inputs_to_vc(event_type))
    print(f"Mouse event: {event_type}")

# Use pynput for mouse events
def on_move(x, y):
    process_mouse_event('move')

def on_click(x, y, button, pressed):
    if pressed:
        process_mouse_event('click')

def on_scroll(x, y, dx, dy):
    process_mouse_event('scroll')

keyboard.on_press(lambda event: process_key_event(event.name))

mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
mouse_listener.start()

def run_bot():
    bot.run(BOT_TOKEN)

# Run the bot and Tkinter GUI
if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    root.mainloop()
