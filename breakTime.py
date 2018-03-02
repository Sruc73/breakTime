import webbrowser
import time

breakTime = 0

while breakTime < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=WfPu9Jrcpuk")
    breakTime += 1