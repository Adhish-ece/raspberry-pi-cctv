```
# 🎯 Raspberry Pi Motion Detection with Video Recording and Discord Alerts

This project turns your Raspberry Pi into a simple security system using a PIR motion sensor and a USB webcam. When motion is detected, it records a 5-second video and sends the clip to a Discord channel via a bot.

---

## 🚀 Features

- Motion detection using a PIR sensor (GPIO2)
- 5-second video recording with a USB webcam (OpenCV)
- Automatic video upload to a Discord channel
- Lightweight and works offline on a Raspberry Pi

---

## 🧰 Hardware Required

- Raspberry Pi 4 (or compatible model)
- PIR motion sensor
- USB webcam
- Internet connection (Wi-Fi or Ethernet)

---

## ⚙️ Circuit Setup

| PIR Sensor Pin | Raspberry Pi Pin |
|----------------|------------------|
| VCC            | 5V (Pin 2)       |
| GND            | GND (Pin 6)      |
| OUT            | GPIO2 (Pin 3)    |

---

## 📦 Software Installation

Install system dependencies:

sudo apt update
sudo apt install python3-opencv

Then install required Python packages from the provided requirements.txt:

pip3 install -r requirements.txt

---

## 🛠️ Discord Bot Setup

1. Go to the Discord Developer Portal: https://discord.com/developers/applications
2. Create a new application and add a bot
3. Copy the bot token
4. Under OAuth2 → URL Generator:
   - Select scopes: bot
   - Select permissions: Send Messages, Attach Files
5. Generate the invite URL and add the bot to your server
6. Enable Developer Mode in Discord (User Settings → Advanced)
7. Right-click your target channel and click "Copy Channel ID"

---

## 💻 Running the Project

1. Clone the repository:

git clone https://github.com/Adhish-ece/raspberry-pi-cctv.git
cd pi-motion-discord-bot

2. Open motion_bot.py and replace:
   - BOT_TOKEN with your actual bot token
   - CHANNEL_ID with your Discord channel ID

3. Run the script:

sudo python3 motion_bot.py

---

## 📝 How It Works

- Waits for motion input from the PIR sensor
- On detection, captures a 5-second video using OpenCV
- Sends the video to your specified Discord channel via bot

---

## 📂 Project Structure

pi-motion-discord-bot/
├── motion_bot.py         # Main script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

---

## 🔐 Security Notes

Do not share your bot token publicly. It gives full control of the bot to anyone who has it.

---

## 💡 Future Improvements

- Face detection or recognition before uploading
- Upload videos to cloud storage for backup
- Add buzzer or LED feedback on detection
- Telegram integration as alternative

---

## 📸 Demo

You can upload a demo GIF or video in this section showing motion detection in action.

---

## 🧑‍💻 Author

Adhish

---

## 🧾 License

This project is licensed under the MIT License. See the LICENSE file for details.
```
