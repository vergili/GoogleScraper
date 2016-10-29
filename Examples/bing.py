
import os,sys,random,time,datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

search_terms = ['mehmet']

email = 'email'
password = 'password'


class account(object):
    def __init__(self, email, password):
        super(account, self).__init__()
        self.email = email
        self.password = password
        self.current_points = 0
        self.earned_points = 0
        self.page_searches = 0

    def login(self):
        now = datetime.datetime.now()
        if now.strftime('%A') == 'Tuesday' and now.strftime('%B') == 'May':
            print ('Day of week: ',now.strftime('%A'))
            print ('Every Tuesday in May gets up to 30 searches rewarded.')
            max_searches = 70
        else:
            print ('Day of week: ',now.strftime('%A'))
            print ('Up to 15 searches rewarded today.')
            max_searches = 40

        #--- Create instance of Firefox
        driver = webdriver.Chrome()
        driver.set_window_size(300,300)
        driver.set_window_position(-300,-300)

        #--- Open live.com to login
        driver.get('http://www.live.com')
        email = driver.find_element_by_id("i0116")
        password = driver.find_element_by_id("i0118")

        #--- Enter login details and submit
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(1)

        #--- Open Bing.com
        driver.get("http://www.bing.com")
        time.sleep(3)
        assert 'Bing' in driver.title


        for term in search_terms:
            #--- Print current point count
            rewards = driver.find_element_by_id('id_rc')
            print ('Current Points: ',rewards.text)
            time.sleep(2.5)

            #--- Find the search bar
            searchbar = driver.find_element_by_id('sb_form_q')

            #--- Select everything in the search bar and delete it
            searchbar.send_keys(Keys.CONTROL,'a')
            searchbar.send_keys(Keys.DELETE)

            #--- Enter the search term:
            searchbar.clear()
            searchbar.send_keys(term,Keys.ENTER)
            time.sleep(3.5)

            driver.find_element_by_class_name("fs_label").click()
            time.sleep(1)

            driver.execute_script("document.getElementById('date_range_start').value='05/01/2015'")
            driver.execute_script("document.getElementById('date_range_end').value='02/09/2016'")

            driver.find_element_by_css_selector(".cbtn input").click()
            time.sleep(2)

            while True:
                try:
                    for result in driver.find_elements_by_css_selector("#b_results li"):
                        title = result.find_element_by_css_selector("strong").text
                        print(title)
                    next = driver.find_element_by_css_selector(".sb_pagN")
                    next.click()

                except Exception as ex:
                    print (ex)
                    break

        driver.quit()


if __name__ == "__main__":
    bot = account(email,password)
    bot.login()
