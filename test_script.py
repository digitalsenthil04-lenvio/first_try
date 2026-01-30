import pyautogui

print("Move mouse to position and wait 5 seconds...")
pyautogui.sleep(5)

x, y = pyautogui.position()
print(f"Captured Position -> X: {x}, Y: {y}")
