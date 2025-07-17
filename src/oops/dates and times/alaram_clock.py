#python alaram clock

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "C:/Users/pavan/Downloads/Demented 90s Cartoon Theme - Rod Kim.mp3"  # Ensure this file is in the same directory
    alarm_triggered = False

    while not alarm_triggered:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")

        if current_time == alarm_time:
            print("Wake up!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # Wait until music finishes
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            alarm_triggered = True

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM, e.g., 16:49): ")
    set_alarm(alarm_time)
