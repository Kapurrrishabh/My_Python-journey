import datetime
import time
import pygame

def set_alarm(alarm_time):
    is_running =True
    sound_file="starter/alarm clock/Spaceship Alarm.mp3"
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time==alarm_time:
            print("Wake UP!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running=False

        time.sleep(1)

if __name__=="__main__":
    alarm_time=input("Enter the alarm time in HH:MM:SS-->")
    set_alarm(alarm_time)