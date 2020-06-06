import time
import pyautogui as a
time.sleep(2)
# 30 30
# 407 235
# 478 432
a.moveTo(30, 30, 1)
time.sleep(0.5)
a.click(clicks = 1, interval = 0, button = 'right')
time.sleep(0.5)
a.moveTo(407, 235, 1)
a.click(clicks = 1, interval = 0, button = 'left')
a.moveTo(488, 469, 1)
time.sleep(0.5)
a.click(clicks = 1, interval = 0, button = 'left')
time.sleep(0.5)
a.moveTo(180, 50, 1)
a.click(clicks = 1, interval = 0, button = 'left')
a.moveTo(30, 30, 1)
time.sleep(2)
time.sleep(3)
a.typewrite('LIKA KAKASHKA', 0)
