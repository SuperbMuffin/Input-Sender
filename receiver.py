import discord
import asyncio
import keyboard
from pynput import mouse
import sounddevice as sd
import numpy as np
import vc_id
import receiver_token
# Discord bot setup
BOT_TOKEN = receiver_token.token
CHANNEL_ID = vc_id.vc_id

# Discord client
client = discord.Client()

# Keyboard and mouse action mapping
actions = {
    261.63: 'a',
    277.18: 'b',
    293.66: 'c',
    311.13: 'd',
    329.63: 'e',
    349.23: 'f',
    369.99: 'g',
    392.00: 'h',
    415.30: 'i',
    440.00: 'j',
    466.16: 'k',
    493.88: 'l',
    523.25: 'm',
    554.37: 'n',
    587.33: 'o',
    622.25: 'p',
    659.25: 'q',
    698.46: 'r',
    739.99: 's',
    783.99: 't',
    830.61: 'u',
    880.00: 'v',
    932.33: 'w',
    987.77: 'x',
    1046.50: 'y',
    1108.73: 'z',
    1174.66: '0',
    1244.51: '1',
    1318.51: '2',
    1396.91: '3',
    1479.98: '4',
    1567.98: '5',
    1661.22: '6',
    1760.00: '7',
    1864.66: '8',
    1975.53: '9',
    2093.00: 'up',
    2217.46: 'down',
    2349.32: 'left',
    2489.02: 'right',
    2637.02: 'space',
    2793.83: 'enter',
    2960.00: 'backspace',
    3135.96: 'tab',
    3322.44: 'shift',
    3520.00: 'ctrl',
    3729.31: 'alt',
    3951.07: 'esc',
    4186.01: 'f1',
    4434.92: 'f2',
    4698.63: 'f3',
    4978.03: 'f4',
    5274.04: 'f5',
    5587.65: 'f6',
    5919.91: 'f7',
    6271.93: 'f8',
    6644.88: 'f9',
    7040.00: 'f10',
    7458.62: 'f11',
    7902.13: 'f12'
}


# Event handlers
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.id == int(CHANNEL_ID):
        await process_command(message.content.strip().lower())

async def process_command(command):
    if command in actions:
        actions[command]()

# Voice channel handling
@client.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.id == int(CHANNEL_ID):
        print(f'{member.display_name} joined voice channel')

# Audio stream processing (stub for future use)
async def process_audio_stream(stream):
    # Example: Analyze audio stream for commands
    pass

# Main function to start the bot
async def run_bot():
    try:
        await client.start(BOT_TOKEN)
    except KeyboardInterrupt:
        await client.close()

# Run the bot
if __name__ == '__main__':
    asyncio.run(run_bot())
