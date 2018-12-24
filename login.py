# coding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


class WebDriverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.get('about:blank')
        cls.driver.implicitly_wait(30)
        print(" -- set up finished -- ")
        print()



    def test_login(self):
        #self.driver.get('https://play.google.com/store/apps/details?id=com.app.iod&rdid=com.app.iod&feature=md&offerId')
        self.driver.get('https://play.google.com/store/apps/details?id=net.flixster.android&rdid=net.flixster.android&feature=md&offerId')
        self.driver.find_element_by_xpath('//div[@class="XfpsVe J9fJmf"]/div[@style="dIodBf"]/button[@class="LkLjZd ScJHi  nMZKrb mgVrBf xjAeve  "]').click()
        self.driver.implicitly_wait(30)


        ## 找到用户名的输入框输入用户名并点击下一步输入密码
        self.account_field = self.driver.find_elements_by_id('Email')

        if not self.account_field:
            print('1111111')
            ## 找到用户名的输入框输入用户名并点击下一步输入密码
            self.account_field = self.driver.find_element_by_id('identifierId')
            print(self.account_field)
            self.account_field.clear()
            self.driver.implicitly_wait(30)
            self.account_field.send_keys('miaodexing@126.com')
            self.driver.find_element_by_id('identifierNext').click()
            self.driver.implicitly_wait(30)

            time.sleep(3)
            print('>>> 11111111')
            #找到密码框并输入密码，点击下一步登录
            self.password_field = self.driver.find_element_by_name('password')
            self.password_field.clear()
            self.driver.implicitly_wait(30)
            self.password_field.send_keys('Nx%bmd_881225')
            self.driver.find_element_by_id('passwordNext').click()
            self.driver.implicitly_wait(30)

            self.driver.find_element_by_xpath('//button[@id="purchase-ok-button"]').click()

        else:
            print('22222222')
            ## 找到用户名的输入框输入用户名并点击下一步输入密码
            self.account_field = self.driver.find_element_by_id('Email')
            print(self.account_field)
            self.account_field.clear()
            self.driver.implicitly_wait(30)
            self.account_field.send_keys('miaodexing@126.com')
            self.driver.find_element_by_id('next').click()
            self.driver.implicitly_wait(30)
            time.sleep(3)
            print('>>> 22222222')
            #找到密码框并输入密码，点击下一步登录
            self.password_field = self.driver.find_element_by_name('Passwd')
            self.password_field.clear()
            self.driver.implicitly_wait(30)
            self.password_field.send_keys('Nx%bmd_881225')
            self.driver.find_element_by_id('signIn').click()
            self.driver.implicitly_wait(30)

            self.driver.find_element_by_xpath('//button[@id="purchase-ok-button"]').click()


        print('-- test 02 finished -- ')
        print()




    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()
        pass
        print('-- tear down finished -- ')
        print()
if __name__ == '__main__':
    unittest.main(verbosity=2)
