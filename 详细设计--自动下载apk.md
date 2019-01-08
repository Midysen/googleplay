# 实现功能：
-根据类别在数据库查找某一类别的所有应用的下载地址，使用多线程自动实现某一类别的应用下载，包括用户自动登录
# 参考代码：
[login_all.py](https://github.com/Midysen/googleplay/blob/master/login_all.py)

# 代码设计：
- 代码入口
```
if __name__ == "__main__":
    get_all()
    print("end")
```
- get_all()函数定义：
```
def get_all():
    
    items=get_category()
    threads = [] 

    for category in items:
        if category=='GAME_STRATEGY':
            username="miaodexing@126.com"
            passwd="Nx%bmd_881225"
            t=threading.Thread(target=download,args=(category,username,passwd))
            threads.append(t)
            #download(category,username,passwd)
            #continue
        if category=='GAME_RACING':
            username="zhangdali2020@gmail.com"
            passwd="123abc$%^789"
            t=threading.Thread(target=download,args=(category,username,passwd))
            threads.append(t)
    
    for thread in threads:
        thread.start()

    print("get_all")
```
   --- 此函数的作用是根据get_category()函数获得不重复的所有类别，根据不同类别，对应不同账号，启动对应线程，执行download函数，传递类别和用户名、密码，下载对应apk文件




- get_category()函数定义：
```
def get_category():
     #从数据库中获得所有类别
    categorys=db.apkinfo.find({},{"apk_category_1":1})
    news = []
    for each in categorys:
        news.append(each['apk_category_1'])
        
    news_items = []
    for item in news:
        if item not in news_items:
            news_items.append(item)
    print(news_items)
    return news_items
```

- download函数定义：
```
def download(category,username,passwd):
    
    print(category)
    #根据类别名查寻数据库，得到此类别中所有应用的app下载地址

    for sets in db.apkinfo.find({"apk_category_1":category}):
        print(sets.get('apk_downurl','null'))
    
        label .start
        desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
        desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
        # create a new Firefox session
        driver = webdriver.Firefox()
        try:
            driver.get(sets.get('apk_downurl','null'))
            print('sign in 0');
            driver.find_element_by_xpath('//div[@class="XfpsVe J9fJmf"]/div[@style="dIodBf"]/button[@class="LkLjZd ScJHi  nMZKrb mgVrBf xjAeve  "]').click()
            print('sign in 1');
            driver.implicitly_wait(5)
            print('sign in 2');
        
            time.sleep(3)
        
            ## 找到用户名的输入框
            account_field = driver.find_elements_by_id('Email')
            #用户名输入框有两种形式，一种是标签Email,还有一种是identifierId
            if not account_field:
                print('if start')
                nowhandle=driver.current_window_handle
                print(nowhandle)
                time.sleep(3)
                print('name')
                ## 找到用户名的输入框输入用户名并点击下一步输入密码
                account_field = driver.find_element_by_id('identifierId')
                print(account_field)
                account_field.clear()
                driver.implicitly_wait(30)
                account_field.send_keys(username)
                #account_field.send_keys('zhangdali2020@gmail.com')
                driver.find_element_by_id('identifierNext').click()
                driver.implicitly_wait(30)
            
                time.sleep(3)
            
                nowhandle=driver.current_window_handle
                print(nowhandle)
                print('password')
            
                #找到密码框并输入密码，点击下一步登录
                password_field = driver.find_element_by_name('password')
                password_field.clear()
                driver.implicitly_wait(1)
                password_field.send_keys(passwd)
                #password_field.send_keys('123abc$%^789')
                driver.find_element_by_id('passwordNext').click()
                driver.implicitly_wait(10)
                print("downnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
                driver.implicitly_wait(10)
                
            else:
                print('else start')
                ## 找到用户名的输入框输入用户名并点击下一步输入密码
                account_field = driver.find_element_by_id('Email')
                print(account_field)
                account_field.clear()
                driver.implicitly_wait(10)
                #account_field.send_keys('zhangdali2020@gmail.com')
                account_field.send_keys(username)
                driver.find_element_by_id('next').click()
                driver.implicitly_wait(10)
                time.sleep(3)
                #找到密码框并输入密码，点击下一步登录
                password_field = driver.find_element_by_name('Passwd')
                password_field.clear()
                driver.implicitly_wait(10)
                #password_field.send_keys('123abc$%^789')
                password_field.send_keys(passwd)
                driver.find_element_by_id('signIn').click()
                driver.implicitly_wait(10)
                print("downnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
                driver.implicitly_wait(10)
                
            aalhandles=driver.window_handles
            print(aalhandles)
                
            iframe = driver.find_elements_by_tag_name("iframe")[3]
            driver.switch_to_frame(iframe)
            time.sleep(5)
            install=driver.find_element_by_xpath("//button[@id='purchase-ok-button']").get_attribute("class")
            driver.implicitly_wait(30)
            #判断是否已经安装过此应用，如果已经安装过，直接退出浏览器
            if(install == "play-button apps loonie-ok-button disabled"):
                driver.find_element_by_xpath("//button[@id='purchase-cancel-button']").click()
                driver.quit()
            else:
                driver.find_element_by_xpath("//button[@id='purchase-ok-button']").click()
                time.sleep(4)
                driver.find_element_by_xpath("//button[@id='close-dialog-button']").click()
                time.sleep(3)
                driver.implicitly_wait(30)
                
                print('-- download finished -- ')
                print()
        except BaseException:
            driver.quit()
            #goto .start
            continue
        driver.quit()
```
