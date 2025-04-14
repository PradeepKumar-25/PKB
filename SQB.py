import time

# PyAutoGUI is a Python module used for GUI automation,it helps automate tasks that involve interacting with the screen, such as clicking buttons, typing text, moving the mouse, and handling pop-ups.
import pyautogui
from pyautogui import click
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin.squareboat2.squareboat.info/")
time.sleep(3)

pyautogui.write("squareboat")
time.sleep(1)

pyautogui.press("Tab")
time.sleep(2)

pyautogui.write("squareboat")
time.sleep(2)

pyautogui.press("Enter")
driver.maximize_window()

# input("Press Enter to close the Browser")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/section/div/div[1]/form/div[1]/div/input").send_keys("nilesh-admin@gmail.com")
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/div/div[2]/div[2]/form/div/button").click()
time.sleep(5)