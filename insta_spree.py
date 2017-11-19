'''
Instagram auto likes on posts
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time,sys
import random

adj = ['Excellent','Good','Cool','Nice','Great']
word = ['picture','shot','click',' ']

chromedriver = 'C:\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)

browser.get('https://www.instagram.com/accounts/login')

time.sleep(1)
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("username")
password.send_keys("password")

browser.find_element_by_tag_name("button").click()
time.sleep(3)

search_box = browser.find_element_by_tag_name("input")
search_box.send_keys("#mypixeldiary")
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(2)
search_box.send_keys(Keys.ENTER)

time.sleep(3)
pics = browser.find_elements_by_tag_name("a")

pics[10].click()
time.sleep(2)
for i in range(150):
    next_pic = browser.find_element_by_xpath("//a[text()='Next']")
    next_pic.click()
    time.sleep(3)
    try:
        like_btn = browser.find_element_by_xpath("//span[text()='Like']")
        like_btn.click()
        time.sleep(2)
        print "Liked",i," pictures"
    except:
        print("Already you liked this picture. Moving to next picture")
        continue
    '''
    comment_box = browser.find_elements_by_xpath("//textarea")
    comment_box[0].click()
    time.sleep(1)
    #comment_box[0].send_keys("Nice")
    comment_box[0].send_keys(random.choice(adj)+' '+random.choice(word))
    time.sleep(1)
    comment_box[0].send_keys(Keys.ENTER)
    time.sleep(1)
    '''
    
 

