import time
import keyboard

def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print(f'{mins:02d}:{secs-1:02d} Beep beep beep \n')

def stopwatch():
    an = input('Press 1 to start the stopwatch. \n')
    
    if an.lower() == '1':
        k = False
        mins, secs = 0, 0

        try:
            while not k:
                if keyboard.is_pressed('esc'):
                    k = True
                    print('here got the kwy')
                    break
                secs += 1
                if secs % 59 == 0:
                    mins += 1
                    secs = 0
                timer = f'{mins:02d}:{secs:02d}'
                print(f"{timer} -- Press ctrl + C to stop", end='\r')
                time.sleep(1)
                                     
        except KeyboardInterrupt: 
            print('Timer has stopped')
        
                   
a = '1'
while a == '1' or a == '2':
    a = input('1: Timer \n2: Stopwatch \n3: Exit\n')

    if a == '1':
        t = input('Enter time in seconds:\n')
        countdown(int(t))
    elif a == '2':
        stopwatch()
    else:
        exit()


