import os, time
import pyautogui as pag
import tkinter
from tkinter import filedialog
from datetime import datetime
present_time=datetime.now().replace(microsecond = 0)
format_time = "%y_%b_%d_%H_%M_%S"
present_time=datetime.strftime(present_time, format_time)
file_name = 'star' + present_time + '.png'
n = int(input())
for i in range(0, n+1):
    for j in range(i):
        print(i, end=' ')
    print('')
ss = pag.screenshot()
root = tkinter.Tk()
root.withdraw()
folder = filedialog.askdirectory()
file = os.path.join(folder, file_name)
ss.save(file)
