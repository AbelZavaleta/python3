import pyautogui,time

pyautogui.FAILSAFE=True


for i in range(0,30):
	pyautogui.moveTo(2311,465,2)
	pyautogui.click()
	time.sleep(3)
	pyautogui.moveTo(2500,400,2)
	time.sleep(1)
	pyautogui.dragTo(2180,400,2,button='left')
	time.sleep(1)
	pyautogui.hotkey('ctrl','c')
	time.sleep(1)
	pyautogui.moveTo(1630,52,2)
	pyautogui.click()
	time.sleep(3)
	pyautogui.moveTo(2117,578,3)
	time.sleep(1)
	pyautogui.click()
	time.sleep(1)
	pyautogui.hotkey('ctrl','v')
	pyautogui.moveTo(2567,577,2)
	pyautogui.click()
	time.sleep(3)
	pyautogui.moveTo(1835,45,2)
	pyautogui.click()
	time.sleep(2)

#pyautogui.hotkey('ctrl','alt','delete')
#time.sleep(10)
#pyautogui.click(2390,633)
