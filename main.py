import datetime
import time
import pygame

def tym():
    current_tym = datetime.datetime.now().time()
    current_tym = f"{int(current_tym.hour)}:{int(current_tym.minute)}:{int(current_tym.second)}"
    return current_tym

def timestamp(activity):
    file = open(f"temp\\{activity}.txt", "a+")
    file.write(f"{datetime.datetime.now().date()} {tym()} {activity} confirmed! \n")

def remind(music, msg, activity):
    pygame.mixer.init()
    pygame.mixer.music.load(music)

    print("Now Playing")
    x = ""
    pygame.mixer.music.play(-1)
    while x.lower() != "stop":
        x = input("Here: ")
    timestamp(activity)
    pygame.mixer.music.fadeout(1500)
    print(msg)
    time.sleep(1.51)
    pygame.mixer.music.unload()
    return 0


def tym_addition(num1, num2):
    summn = int(num1) + int(num2)
    if summn >= 60:
        return summn - 60
    else:
        return summn



print("---------------------------------------")


def main():
    msg = "-------------------------------"

    print("Activating reminder protocol.....")

    activity_music = "temp\\activity.mp3"
    water_music = "temp\\water.mp3"
    eyes_music = "temp\\eyes.mp3"

    temp_tym_activity = 0
    temp_tym_water = 0
    temp_tym_eyes = 0
    while int(tym().split(":")[0]) in range(9, 17):
        activity_activity = "Exercise"
        water_activity = "Water"
        eyes_activity = "Rest Eyes"

        if int(tym().split(":")[1]) == int(tym_addition(45, temp_tym_activity)) and int(tym().split(":")[2]) <= 10:  # int(tym_addition(45, temp_tym)):
            print(tym())
            print("You like to move it--move it.")
            remind(activity_music, msg, activity_activity)
            print("-----------------------------")
            temp_tym_activity = tym_addition(int(tym().split(":")[1]), temp_tym_activity)

        if int(tym().split(":")[1]) == int(tym_addition(30, temp_tym_eyes)) and int(tym().split(":")[2]) in range(10,20):  # int(tym_addition(45, temp_tym)):
            print(tym())
            print("It's time for you to take a rest and close your eyes.")
            remind(eyes_music, msg, eyes_activity)
            print("-----------------------------")
            temp_tym_eyes = tym_addition(int(tym().split(":")[1]), temp_tym_eyes)

        if int(tym().split(":")[1]) == int(tym_addition(57, temp_tym_water)) and int(tym().split(":")[2]) in range(20,30):  # int(tym_addition(45, temp_tym)):
            print(tym())
            print("Drink atleast a glass of water.")
            remind(eyes_music, msg, water_activity)
            print("-----------------------------")
            temp_tym_water = tym_addition(int(tym().split(":")[1]), temp_tym_water)

        else:
            print(tym(), tym_addition(45, temp_tym_water), "---------")
            time.sleep(1)
    pass

if __name__ == '__main__':
    main()
