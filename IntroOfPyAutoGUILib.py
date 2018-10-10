import pyautogui #import lib pyautogui
pyautogui.size() #check size of monitor
pyautogui.click(300,300) #control cursor to position x=300 y=300 and click
pyautogui.click(300,600) #control cursor to position x=300 y=600 and click
pyautogui.position() #control cursor to position x=300 y=600 but no click
option = (181,27) #assume "option" button is position as x=181 y=27
pyautogui.click(option)
pyautogui.position()
edit = (48,31) #assume "edit" button is position as x=48 y=31
pyautogui.click(edit)
pyautogui.moveTo(option) #move cursor from "edit" to "option"
#define function
def moveMouse():
	pyautogui.click(edit)
	pyautogui.moveTo(option)
	print('Mouse is moving')
#access the moveMouse function
moveMouse()
''' cursor is controlled to click edit button, move to option button and give 
"Mouse is moving" to step by step '''
