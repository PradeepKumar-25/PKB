# import time
# from selenium import webdriver
#
# # Set up the WebDriver
# driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or specify executable_path
#
# # Open a website
# driver.get("https://squareboat::squareboat@admin.squareboat2.squareboat.info")
# driver.maximize_window()
# time.sleep(5)
#
#
# # Keep the browser open
# input("Press Enter to close...")
#
# # Close the browser
# driver.quit()
import BY
import pyautogui
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://salesright.squareboat.info/")
time.sleep(3)  # Wait for popup

# # Enter username
# pyautogui.write("squareboat")
# time.sleep(1)
#
# # Press TAB to switch to password field
# pyautogui.press("tab")
# time.sleep(1)
#
# # Enter password
# pyautogui.write("squareboat")
# time.sleep(1)
#
# # Press ENTER to submit
# pyautogui.press("enter")

print("Logged in successfully!")
driver.maximize_window()

input("Press Enter to close the Browser")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/input").send_keys("sq@admin.com")

