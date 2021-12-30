import time


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print("Beep beep beep")


def stopwatch():
    an = input('Press 1 to start the stopwatch. \nPress ctrl + c to stop the stopwatch \n')
    
    if an.lower() == '1':
        stop = False
        mins, secs = 0, 0

        try:
            while not stop:
                secs += 1
                if secs % 59 == 0:
                    mins += 1
                    secs = 0
                timer = f'{mins:02d}:{secs:02d}'
                
                print(timer, end='\r',)
                time.sleep(1)
        except KeyboardInterrupt:
            print('Timer has stopped')
            
        
a = input('1: Timer \n2: Stopwatch \n')
if a == '1':
    t = input('Enter time in seconds:\n')
    countdown(int(t))
else:
    stopwatch()

