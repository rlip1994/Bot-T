from selenium import webdriver
from time import sleep
from secret import pwd,usr
class TinderBot:
    def __init__(self, user, pwd):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tinder.com")
        sleep(3)
        main = self.driver.current_window_handle
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button").click()
        sleep(2)
        loginpopup=self.get_Popup(main)
        self.driver.switch_to.window(loginpopup)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div/div[1]/div/input").send_keys(user)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div/div[2]/div/input").send_keys(pwd)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input").click()
        sleep(3)
        self.driver.switch_to.window(main)
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[2]").click()
        sleep(2)
        
        
        
    def get_Popup(self,mainWindow):
        for window in self.driver.window_handles:
            if window!=mainWindow:
                return window
    
    def push_likes(self):
        like=0
        while (not self.driver.find_elements_by_css_selector("#modal-manager > div > div > div.Pt\(16px\).Pb\(10px\).Px\(36px\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Fw\(\$semibold\).focus-button-style.D\(b\).Mx\(a\).C\(\$c-secondary\).C\(\$c-base\)\:h")):
            if (self.driver.find_elements_by_css_selector("#modal-manager > div > div > div.Pt\(16px\).Pb\(10px\).Px\(36px\).Px\(24px\)--s > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(42px\)--s.Mih\(50px\)--ml.Fw\(\$semibold\).focus-button-style.D\(b\).Mx\(a\).C\(\$c-secondary\).C\(\$c-base\)\:h")):
                self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/button[2]").click()
                sleep(1)
            self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
            sleep(1)
            like+=1
            print("like",like)
        print("no more")

    def close(self):
        self.driver.quit()

            


x=TinderBot(usr,pwd)
x.push_likes()
x.close()
