import discord
import asyncio
import keyboard
import tkinter as tk
from tkinter import ttk
from discord.ext import commands
import threading
import sounddevice as sd
import numpy as np
import vc_id
import sender_token
# Your bot token and voice channel ID
BOT_TOKEN = sender_token.token
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
convert_arrows_to_wasd_var = tk.BooleanVar()
convert_wasd_to_arrows_var = tk.BooleanVar()

send_inputs = False
send_mouse_inputs = False
convert_arrows_to_wasd = False
convert_wasd_to_arrows = False

def toggle_send_inputs():
    global send_inputs
    send_inputs = send_inputs_var.get()

def toggle_convert_arrows_to_wasd():
    global convert_arrows_to_wasd
    convert_arrows_to_wasd = convert_arrows_to_wasd_var.get()

def toggle_convert_wasd_to_arrows():
    global convert_wasd_to_arrows
    convert_wasd_to_arrows = convert_wasd_to_arrows_var.get()

ttk.Checkbutton(root, text="Send Inputs", variable=send_inputs_var, command=toggle_send_inputs).pack()
ttk.Checkbutton(root, text="Convert Arrows to WASD", variable=convert_arrows_to_wasd_var, command=toggle_convert_arrows_to_wasd).pack()
ttk.Checkbutton(root, text="Convert WASD to Arrows", variable=convert_wasd_to_arrows_var, command=toggle_convert_wasd_to_arrows).pack()


# Keyboard and mouse input handlers
async def send_inputs_to_vc(inputs):
    voice_client = discord.utils.get(bot.voice_clients)
    if voice_client and voice_client.is_connected():
        # Generate a tone corresponding to the input
        duration = 0.05  # seconds
        sample_rate = 44100  # Hz
        
        key_frequencies = {
            'a': 261.63,
            'b': 277.18,
            'c': 293.66,
            'd': 311.13,
            'e': 329.63,
            'f': 349.23,
            'g': 369.99,
            'h': 392.00,
            'i': 415.30,
            'j': 440.00,
            'k': 466.16,
            'l': 493.88,
            'm': 523.25,
            'n': 554.37,
            'o': 587.33,
            'p': 622.25,
            'q': 659.25,
            'r': 698.46,
            's': 739.99,
            't': 783.99,
            'u': 830.61,
            'v': 880.00,
            'w': 932.33,
            'x': 987.77,
            'y': 1046.50,
            'z': 1108.73,
            '0': 1174.66,
            '1': 1244.51,
            '2': 1318.51,
            '3': 1396.91,
            '4': 1479.98,
            '5': 1567.98,
            '6': 1661.22,
            '7': 1760.00,
            '8': 1864.66,
            '9': 1975.53,
            'up': 2093.00,
            'down': 2217.46,
            'left': 2349.32,
            'right': 2489.02,
            'space': 2637.02,
            'enter': 2793.83,
            'backspace': 2960.00,
            'tab': 3135.96,
            'shift': 3322.44,
            'ctrl': 3520.00,
            'alt': 3729.31,
            'esc': 3951.07,
            'f1': 4186.01,
            'f2': 4434.92,
            'f3': 4698.63,
            'f4': 4978.03,
            'f5': 5274.04,
            'f6': 5587.65,
            'f7': 5919.91,
            'f8': 6271.93,
            'f9': 6644.88,
            'f10': 7040.00,
            'f11': 7458.62,
            'f12': 7902.13
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

keyboard.on_press(lambda event: process_key_event(event.name))

def run_bot():
    bot.run(BOT_TOKEN)

# Run the bot and Tkinter GUI
if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    root.mainloop()
