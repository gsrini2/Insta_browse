'''
Script to browse through your favorite #hastags on Instagram automatically
Tested on Python2.7

Script requires 2 command line arguments.
RUN the script as follows
>python insta_browse.py #hashtag count
   
Arg 1 (#hashtag) = Hastag to be browsed (ex: #nature, #wildlife #macroshots etc,..)
Arg 2 (count) = Number of photos to browse in the search result.
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time,sys

#Locate you chromedriver path below.
chromedriver = 'C:\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)

browser.get('https://www.instagram.com/accounts/login')
browser.maximize_window()

time.sleep(1)
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

#Replace username and password with your Instagram user id and password
username.send_keys("username")
password.send_keys("password")

browser.find_element_by_tag_name("button").click()
time.sleep(3)

search_box = browser.find_element_by_tag_name("input")
search_box.send_keys(str(sys.argv[1]))
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(2)
search_box.send_keys(Keys.ENTER)

time.sleep(3)
pics = browser.find_elements_by_tag_name("a")

#Open a random picture from the search result
pics[10].click()
time.sleep(2)
for i in range(int(sys.argv[2])):
    next_pic = browser.find_element_by_xpath("//a[text()='Next']")
    if (len(next_pic) > 0):
        next_pic.click()
        time.sleep(5)
    else:
        continue
browser.close() 
