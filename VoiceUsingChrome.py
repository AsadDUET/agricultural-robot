# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 03:15:27 2019

@author: asado
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
chrome_path=r"E:\project\github\chromedriver.exe"
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument("--use-fake-ui-for-media-stream")
driver = webdriver.Chrome(chrome_path,options=options)
driver.get("https://translate.google.com/#view=home&op=translate&sl=bn&tl=en")
           
driver.find_element_by_id("gt-speech").click()
time.sleep(2)
print("Speak now")
text=''
text2=''
def chrome_speak():
    driver.find_element_by_id("source").send_keys(Keys.CONTROL, 'v')
def chrome_detect():
    global text
    global text2
    if (driver.find_element_by_id("gt-speech").get_attribute('aria-label')=="Turn off voice input"):
        print(driver.find_element_by_id("gt-speech").get_attribute('aria-label')+'if')
#        print(text2)
        time.sleep(.4)
        if (driver.find_element_by_id("gt-speech").get_attribute('aria-label')=="Turn off voice input"):
            text=driver.find_element_by_class_name("text-dummy").get_attribute('innerHTML')
            time.sleep(.4)
        if (driver.find_element_by_id("gt-speech").get_attribute('aria-label')=="Turn off voice input"):
            text2=driver.find_element_by_class_name("text-dummy").get_attribute('innerHTML')
            time.sleep(.4)
        if(text==text2):
            if(text!=''):
                print(text2)
                

                driver.find_element_by_id("gt-speech").click()
                print('off clicked')
                return text2
#                return driver.find_element_by_xpath("//*[@id="input-wrap"]/div[2]").get_attribute('innerHTML')
                time.sleep(.5)
                
                
    else:
        print(driver.find_element_by_id("gt-speech").get_attribute('aria-label')+'else')
        if (driver.find_element_by_id("gt-speech").get_attribute('aria-label')=="Turn on voice input"):
            driver.find_element_by_id("gt-speech").click()
        print('on clicked')
        text=text2=''
if __name__=='__main__':
    while True:
        chrome_speak()
        
#/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/span[1]/span
    
    #aria-label="Turn off voice input"