# 软件环境 
- ubuntu18.10
- python3.6
- mongodb3.6
- scrapy 1.5.1

# 创建工程
- 此项目是以apkpure.com为参照，以google play作为主站，基于scrapy框架来实现对匹配openthos系统的android应用信息抓取，因此在使用scrapy来创建项目时，基于的网址是https://play.google.com/store/apps,
过程如下：
   - scrapy startproject apkinfo
   - cd apkinfo/
   - scrapy genspider google https://play.google.com/
   
# 工程目录树如下：
![blockchain](https://github.com/Midysen/googleplay/blob/master/2018-12-19%2013-59-46%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)


- 在spiders文件夹下编写自己的爬虫 
- 在items中编写容器用于存放爬取到的数据
- 在pipelines中对数据进行各种操作
- 在settings中进行项目的各种设置。


# 爬虫定义
- 修改spiders文件夹下的goole.py ，内容修改为：
  ```
      class GoogleSpider(scrapy.Spider):
         name = 'google'
         allowed_domains = ['https://play.google.com/']
         start_urls = ['https://play.google.com/store/apps/']
  ```
- 其中：  
   -  name : 爬虫的唯一标识符
   -   allowed_domains: 爬虫域名
   -   start_urls : 初始爬取的url列表
   
   


# 修改items.py文件，添加要保存的应用程序的具体信息
```
 class ApkinfoItem(scrapy.Item):
     # define the fields for your item here like:
     # name = scrapy.Field()
     apk_name = scrapy.Field()
     apk_star = scrapy.Field()
     apk_downurl = scrapy.Field()
     apk_icon = scrapy.Field()
     apk_review = scrapy.Field()
     apk_movie = scrapy.Field()
```
#  重写parse()函数，编写google.py(spider)
- 在google.py文件中存在parse()函数，是需要我们重写的函数 ， 每个初始url访问后生成的Response对象作为唯一参数传给该方法，该方法解析返回的Response，提取数据，生成item，同时生成进一步要处理的url的request对象。
- 解析https://play.google.com/store/apps 页面，根据“类别”得到每个类型对应页面的地址

```
 def parse(self, response):
         selector = scrapy.Selector(response)
         
         #获得每个类别的地址
         urls = selector.xpath('//ul[@class="submenu-item-wrapper"]/li[@class="child-submenu-link-wrapper"]/a/@href').extract()
         
         link_flag=0
 
         #yield Request要求传递的是list
         links = []
         for link in urls:
                 links.append(link)
         
         for each in urls:
             yield Request(links[link_flag], callback=self.parse_next,dont_filter=True)
             link_flag += 1                                                                     
```
   - 使用yield迭代调用每个“查看更多”地址的页面，使用自定义函数parse_next处理

- 得到每个类别多对应的每个应用程序的地址
```
  def parse_next(self,response):
         selector = scrapy.Selector(response) 
         #获得See more 地址对应的页面的每一个app的链接地址
         app_urls = selector.xpath('//div[@class="details"]/a[@class="title"]/@href').extract()
         print(app_urls)
 
         urls = []
         for url in app_urls:
             url = "https://play.google.com" + url
             print(url)
             urls.append(url)
                                                                         
         link_flag = 0
         for each in app_urls:
             yield Request(urls[link_flag], callback=self.parse_detail,dont_filter=True)
             link_flag += 1


```
- 根据每个应用程序的地址，  调用函数parse_detail来解析每个应用程序的详细信息，并和每个item对应
```
      #获取具体应用的相信信息并存储到数据库
      def parse_detail(self,response):
          selector = Selector(response)
          item = ApkinfoItem()
  
          app = selector.xpath('//div[@class="JNury Ekdcne"]')
  
          #app name                                                                                                                                                                                       
          names = app.xpath('//h1[@class="AHFaub"]/span/text()').extract()
          item['apk_name'] = names
          
          #App rating
          stars = app.xpath('//div[@class="BHMmbe"]/text()').extract()
          item['apk_star'] = stars
          
          #App review
          infos = app.xpath('//div[@jsname="sngebd"]/text()').extract()
          item['apk_review'] = infos
          
          #App download url
          download_urls = app.xpath('//span[@itemprop="offers"]/meta[@itemprop="url"]/@content').extract()
          item['apk_downurl'] = download_urls
          
          #App icon url
          icon_urls = app.xpath('//button[@class="NIc6yf"]/img[@class="T75of lxGQyd"]/@src').extract()
          item['apk_icon'] = icon_urls
          
          #App icon url
          movie_urls = app.xpath('//button[@class="lgooh  "]/@data-trailer-url').extract()
          
          if len(movie_urls) == 0:
              print('movie url is empty!')
          else:
              item['apk_movie'] = movie_urls
              
          yield item


```
# 修改pipelines.py,实现与数据库进行连接
```
class ApkinfoPipeline(object):
      def __init__(self):
          host = settings['MONGODB_HOST']
          port = settings['MONGODB_PORT']
          dbName = settings['MONGODB_DBNAME']
          client = pymongo.MongoClient(host=host, port=port)
          tdb = client[dbName]
          self.post = tdb[settings['MONGODB_DOCNAME']]
 
 
      def process_item(self, item, spider):
          apkInfo = dict(item)
          self.post.insert(apkInfo)
          return item

```

# 修改setting.py文件，注册pipeline
```
ITEM_PIPELINES = {
       'apkinfo.pipelines.ApkinfoPipeline': 100
   }
```
# 修改setting.py文件，模拟浏览器登录，防止谷歌反爬取
```
 USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
```
# 修改setting.py文件， 配置本地mongodb数据库
```
  MONGODB_HOST = '127.0.0.1'
  MONGODB_PORT = 27017
  MONGODB_DBNAME = 'apps'           
  MONGODB_DOCNAME = 'apkinfo'       

```
   - MONGODB_DBNAME = 'apps'           #数据库名
   - MONGODB_DOCNAME = 'apkinfo'       #表名
   
 # 测试运行
 - 在apkinfo目录下运行 scrapy crawl google ，可以查看到一些打印信息，并且会在本地数据库中存储应用程序信息，在ubuntu上可以使用robomongo图形化查看mongodb中的信息，如下图:
    - ![blockchain](https://img-blog.csdnimg.cn/20181219163112451.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21keDIwMDcyNDE5,size_16,color_FFFFFF,t_70)
    
    
# 注意：
- 此项目是使用python3版本进行开发运行，所以在运行此项目程序前，请确认您的python版本
- 开发此项目，需要安装多个第三方库，如果遇到“Python importError: No module named 'requests' 此类问题，请使用pip安装相应的库即可
- 开发前，请先对scrapy框架做一定的了解
- VPN必须全局


# 实现功能：

- 根据类别抓取google play应用程序信息，包括应用程序名称、评分、介绍、图标、更新日期、公司名称、类别以及应用程序安装地址，储存在本地数据库mongodb中


