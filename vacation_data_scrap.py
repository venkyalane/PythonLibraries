import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

def scrap_airdna_page(url):
    response = requests.get(url)
    soap = BeautifulSoup(response.text, 'html.parser')
    scrapped_data = []
    for item in soap.find_all('div', class_ = 'data-item'):
        name = item.find('h3').text
        value = item.find('span', class_ = 'value').text
        scrapped_data.append({'name':name, 'value':value})
    return scrapped_data


def login_airdna(url, username, password):
    driver.get(url)
    login_button = driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-0']//a[@class='MuiTypography-root MuiTypography-body2 MuiLink-root MuiLink-underlineAlways css-1ojajs7'][normalize-space()='Log in']")
    login_button.click()
    driver.implicitly_wait(10)
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys(username)
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    driver.find_element(By.XPATH, "//input[@id=':r0:']").send_keys("oakland")
    driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-c2akat']//*[name()='svg']")

login_airdna("https://app.airdna.co/login", "vyankateshalane@gmail.com", "Tn@*bDUSp$Vw9Ys")
time.sleep(30)
# data = scrap_airdna_page("https://app.airdna.co/data/us/airdna-131")
# final_data = pd.DataFrame(data)
# print(final_data)
driver.close()

