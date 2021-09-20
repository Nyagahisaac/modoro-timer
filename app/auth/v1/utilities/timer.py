import time

class pomodoro:
    def timer(t):
        print("Timer starts now!")  
        for i in range(4):
            t = t*60
            while t:
                mins = t // 60
                secs = t % 60
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(" " + timer, end="\r")
                time.sleep(1)

                t -= 1

            print("Shortbreak Time!!")
 