import pyautogui as pg
import time

n = int(input("Enter Total Bits - "))
time.sleep(4)
pg.hotkey('fn','f11')
for i in range(n):
    time.sleep(0.7)
    pg.hotkey('win','printscreen')
    time.sleep(0.5)
    pg.moveTo(1658,1015)
    time.sleep(0.5)
    pg.click()   