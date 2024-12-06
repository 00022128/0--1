import time
import datetime
import pygame

def set_alarm(alarm_time):
    is_running = True
    sound_file = "/Users/scorpionn/PycharmProjects/0--1/Silent Night - The Soundlings.mp3"
    print(
        f"Setting up alarm for {alarm_time}...")
    while is_running:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake Up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                    break_music = input("Do you want to break the alarm? (y/n): ").lower()
                    if break_music == "y":
                        pygame.mixer.music.stop()
                    elif break_music == 'n':
                        time.sleep(1)
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")

            is_running = False


if __name__  == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)


