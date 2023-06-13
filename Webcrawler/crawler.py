from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument('--disable-notifications')
 
chrome = webdriver.Chrome('./chromedriver', options=options)
chrome.get("https://www.binance.com/zh-TW/markets")

my_list = list()

time.sleep(5)
# click button
python_button = chrome.find_elements_by_xpath('//*[@id="__APP"]/div[1]/main/div/div[2]/div/div/div[2]/div[1]/div[1]/div/button[4]')[0]
python_button.click()
# click button
python_button = chrome.find_elements_by_xpath('//*[@id="__APP"]/div[1]/main/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]')[0]
python_button.click()
crypts = chrome.find_elements_by_class_name('css-1c1ahuy')
for crypt in crypts:
    my_list.append(crypt)
    print(crypt.text)
ele = crypts[19]
while True:
    chrome.execute_script("arguments[0].scrollIntoView();", ele)
    time.sleep(1)
    crypts1 = chrome.find_elements_by_class_name('css-1c1ahuy')
    temp = set(crypts1).difference(my_list)
    if(len(temp)<=0):
        break
    for crypt in set(crypts1).difference(crypts):
        my_list.append(crypt)
        print(crypt.text)
    ele = crypts1[len(crypts1) - 1]
    
