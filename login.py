# coding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
# action行动 chains链
from selenium.webdriver.common.action_chains import ActionChains


class WebDriverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.get('about:blank')
        cls.driver.implicitly_wait(30)
        print(" -- set up finished -- ")
        print()



    def test_01_login(self):
        self.driver.get('https://play.google.com/store/apps/details?id=com.adobe.reader&rdid=com.adobe.reader&feature=md&offerId')
        self.driver.find_element_by_xpath('//div[@class="XfpsVe J9fJmf"]/div[@style="dIodBf"]/button[@class="LkLjZd ScJHi  nMZKrb mgVrBf xjAeve  "]').click()
        self.driver.implicitly_wait(30)


        ## 找到用户名的输入框
        self.account_field = self.driver.find_elements_by_id('Email')
        #根据用户名输入框来区分两种情况
        if not self.account_field:
            print('if start')
            ## 找到用户名的输入框输入用户名并点击下一步输入密码
            self.account_field = self.driver.find_element_by_id('identifierId')
            print(self.account_field)
            self.account_field.clear()
            self.driver.implicitly_wait(10)
            self.account_field.send_keys('miaodexing@126.com')
            self.driver.find_element_by_id('identifierNext').click()
            self.driver.implicitly_wait(10)

            time.sleep(3)
            #找到密码框并输入密码，点击下一步登录
            self.password_field = self.driver.find_element_by_name('password')
            self.password_field.clear()
            self.driver.implicitly_wait(10)
            self.password_field.send_keys('Nx%bmd_881225')
            self.driver.find_element_by_id('passwordNext').click()
        else:
            print('else start')
            ## 找到用户名的输入框输入用户名并点击下一步输入密码
            self.account_field = self.driver.find_element_by_id('Email')
            print(self.account_field)
            self.account_field.clear()
            self.driver.implicitly_wait(10)
            self.account_field.send_keys('miaodexing@126.com')
            self.driver.find_element_by_id('next').click()
            self.driver.implicitly_wait(10)
            time.sleep(3)
            #找到密码框并输入密码，点击下一步登录
            self.password_field = self.driver.find_element_by_name('Passwd')
            self.password_field.clear()
            self.driver.implicitly_wait(10)
            self.password_field.send_keys('Nx%bmd_881225')
            self.driver.find_element_by_id('signIn').click()
        print('-- login sucessfully -- ')
        print()

    def test_02_install(self):
        iframe = self.driver.find_elements_by_tag_name("iframe")[-1]
        print(iframe)
        self.driver.switch_to_frame(iframe)
        time.sleep(4)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//button[@id='purchase-ok-button']").click()
        self.driver.implicitly_wait(10)
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[@id='close-dialog-button']").click()
        time.sleep(3)
        self.driver.implicitly_wait(10)

        print('install ok!')
        print()



    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()
        pass
        print('-- quit -- ')
        print()
if __name__ == '__main__':
    unittest.main(verbosity=2)
