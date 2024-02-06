import pyautogui as pg
import time

try:
    time.sleep(6)
    current_position = pg.position()
    print(f"Mouse position: {current_position}")
except Exception as e:
    print(f"Error: {e}")
