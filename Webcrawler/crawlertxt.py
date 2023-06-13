from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


chrome = webdriver.Firefox()
chrome.get('https://www.wfxs.com.tw/chapter/49859/22128002.html')

title = chrome.find_elements_by_xpath('//*[@id="acontent"]/h1').text
print(title)