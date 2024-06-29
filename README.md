# What It Does
This Program uses discord to communicate similarly to a modem but using a discord channel it sends inputs from one device to another were it is then simulated this allows playing games which have  "On Same Couch MultiPlayer".

# How To Use It

#### 1. Install Python
- Download and install Python from [python.org](https://www.python.org/downloads/).

#### 2. Create a Discord Server
- If you don't already have a Discord account, create one at [discord.com](https://discord.com/).
- Create a new Discord server:
  1. Open Discord.
  2. Click the "+" button on the left sidebar.
  3. Follow the prompts to create a new server with only yourself as a member.

#### 3. Create the First Bot (Sender)
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click "New Application" and name it "Sender".
3. On the sidebar, click "Bot".
4. Click "Add Bot" and confirm.
5. Click "Reset Token", enter your password, and copy the token somewhere safe.
6. Scroll down to "Privileged Gateway Intents" and enable all options.
7. On the sidebar, click "OAuth2".
8. Scroll to "OAuth2 URL Generator":
    - Select "bot" under the scopes.
    - Under "Bot Permissions", select "Connect" and "Speak".
9. At the bottom, there should be a URL. Paste this into your browser and invite the bot to your Discord server.

#### 4. Create the Second Bot (Receiver)
- Repeat steps 3-9, but create a bot named "Receiver".

#### 5. Set Up Your Server
1. In your Discord server, you should see both bots under the offline members.
2. (Optional) Delete all categories and channels from the Discord server by right-clicking on them and selecting "Delete".

#### 6. Enable Developer Mode
1. Click on the settings icon at the bottom of your screen.
2. Scroll to "Advanced" (near the bottom) and enable "Developer Mode".

#### 7. Create a Voice Channel
1. In your Discord server, right-click the server sidebar and click on "Create Channel".
2. Click "Voice Channel" and name it whatever you want.
3. Right-click on the voice channel you just created and select "Copy Channel ID". If you don't see this option, make sure Developer Mode is enabled (step 6).

#### 8. Save Bot Tokens and Channel ID
- Save the voice channel ID next to both bot tokens that you saved before.

#### 9. Download and Set Up the Repository
1. Go to [this repository](#) and click on the green "Code" button, then download the zip file.
2. Unzip the file and run `Setup.py`.
3. Fill in all the fields with the information you obtained beforehand.
4. Zip the folder again and send it to someone.

#### 10. Running the Program
- The other person needs to have Python installed (install it from [python.org](https://www.python.org/)).
- They must run the `main.py` file.
- You and your friend have to decide who will play the game and who will send inputs.
- Each of you must run the `main.py` file and select accordingly.
- The friend playing the game will stream the gameplay to you while you have the program in focus. Anytime you press a button, it will be pressed on their side, allowing you to play games together remotely.
