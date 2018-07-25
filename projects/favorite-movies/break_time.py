import webbrowser
import time

total_breaks = 3
break_count = 0

print("This Program started on " + time.ctime())
while(break_count < total_breaks):
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=t3Mqi-Tv7q0")
    break_count = break_count + 1
