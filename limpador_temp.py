# Limpador De Temp

# LIVRARIA #    
import pyautogui
import time
import os

# -------------------------------------------------------------- #
# TECLADO
pyautogui.PAUSE = 0.5
pyautogui.hotkey('win', 'r')
pyautogui.write('temp')
pyautogui.press('enter')
time.sleep(0.4)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('del')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5)
# MOUSE 1
pyautogui.click(490, 292)
# MOUSE 2
pyautogui.click(719, 320)
time.sleep(0.3)
# MOUSE 2
pyautogui.click(1160, 23)
# -------------------------------------------------------------- #
# TECLADO
pyautogui.hotkey('win', 'r')
pyautogui.write('%temp%')
pyautogui.press('enter')
time.sleep(0.4)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('del')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5)
# MOUSE 1
pyautogui.click(490, 293)
time.sleep(0.3)
# MOUSE 2
pyautogui.click(721, 321)
time.sleep(0.3)
# MOUSE 2
pyautogui.click(1160, 23)
# -------------------------------------------------------------- #
# TECLADO
pyautogui.hotkey('win', 'r')
pyautogui.write('prefetch')
pyautogui.press('enter')
time.sleep(0.4)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('del')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5)
# MOUSE 1
pyautogui.click(1160, 23)