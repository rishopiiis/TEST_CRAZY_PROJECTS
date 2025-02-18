import pyttsx3
import time
from datetime import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 150)  

while True:
    now = datetime.now().strftime("%H:%M:%S")
    engine.say(f"The time is now {now}")
    engine.runAndWait()
    time.sleep(60)  # Announce every minute
