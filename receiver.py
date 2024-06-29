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
    'w': keyboard.press_and_release,
    'a': keyboard.press_and_release,
    's': keyboard.press_and_release,
    'd': keyboard.press_and_release,
    'up': keyboard.press_and_release,
    'left': keyboard.press_and_release,
    'down': keyboard.press_and_release,
    'right': keyboard.press_and_release,
    'space': keyboard.press_and_release,
    'move': mouse.Controller().move,
    'click': mouse.Controller().click,
    'scroll': mouse.Controller().scroll
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
        print(f'Performed action: {command}')
    else:
        print(f'Unknown command: {command}')

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
