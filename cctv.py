import RPi.GPIO as GPIO
import time
import cv2
import discord
import asyncio

# ==== CONFIGURATION ====
PIR_PIN = 2                    # GPIO2 for PIR
VIDEO_FILE = "motion_video.avi"
RECORD_SECONDS = 5
BOT_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # Replace this
CHANNEL_ID = 123456789012345678       # Replace this with your channel ID

# ==== SETUP PIR SENSOR ====
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# ==== RECORD VIDEO FUNCTION ====
def record_video(filename, duration=5):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot access camera.")
        return False

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    print("[INFO] Recording video...")
    start_time = time.time()
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        out.write(frame)

    cap.release()
    out.release()
    print("[INFO] Video saved as", filename)
    return True

# ==== SEND VIDEO TO DISCORD ====
async def send_to_discord(video_path):
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")
        channel = client.get_channel(CHANNEL_ID)
        if channel:
            await channel.send("🎥 Motion detected! Here's the video:")
            await channel.send(file=discord.File(video_path))
        await client.close()

    await client.start(BOT_TOKEN)

# ==== MAIN LOOP ====
print("[INFO] Motion detection started. Press Ctrl+C to stop.")
try:
    while True:
        if GPIO.input(PIR_PIN):
            print("[ALERT] Motion detected!")
            if record_video(VIDEO_FILE, RECORD_SECONDS):
                asyncio.run(send_to_discord(VIDEO_FILE))
            time.sleep(10)  # prevent multiple triggers in a row
        time.sleep(1)

except KeyboardInterrupt:
    print("\n[INFO] Exiting program...")

finally:
    GPIO.cleanup()
