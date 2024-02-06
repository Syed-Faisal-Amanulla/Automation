import pyautogui as pg
import time

try:
    time.sleep(5)

    pg.hotkey('fn', 'f11')

    time.sleep(2)

    time.sleep(30 * 60)

    pg.moveTo(1223, 982)
    time.sleep(1)
    pg.click()

    time.sleep(1)

    pg.moveTo(1806, 32)
    time.sleep(1)
    pg.click()

    time.sleep(1)

    pg.moveTo(1253, 711)
    time.sleep(1)
    pg.click()

    time.sleep(1)

    pg.moveTo(892, 463) # 2 star rating
    time.sleep(1)
    pg.click()

    time.sleep(1)

    pg.moveTo(1280, 712)
    time.sleep(1)
    pg.click()

except Exception as e:
    print(f"Error: {e}")
