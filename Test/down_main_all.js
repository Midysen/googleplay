const puppeteer = require('puppeteer');
const account = `zhangdali2020@gmail.com`;
const password = `123abc$%^789`;



/*
npm i nodemailer
使用：

*/
const nodemailer  = require("nodemailer");

// 参数：发件人，邮件标题别名，收件人，主题，正文（支持html格式）
function sendMail(from, aliasName, tos, subject, msg)
{
    const smtpTransport = nodemailer.createTransport({
    host: 'smtp.qq.com',
    secureConnection: true, // use SSL
    secure: true,
    port: 465,
    auth: {
        user: from,
        pass: 'djqeaewplmewbdch',
    }
    });

    smtpTransport.sendMail({
        //from    : '标题别名 <foobar@latelee.org>',
        from    : aliasName + ' ' + '<' + from + '>',
        //收件人邮箱，多个邮箱地址间用英文逗号隔开
        to      : tos,
        subject : subject,//邮件主题
        //text    : msg,
        html    : msg
    }, function(err, res) {
        if (err)
        {
            console.log('error: ', err);
        }
    });
}
/*
function nl2br(str, isXhtml) {
    var breakTag = (isXhtml || typeof isXhtml === 'undefined') ? '<br />' : '<br>';
    var str = (str + '').replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&apos;");
    return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + breakTag + '$2');
};
*/
function email(position,error)
{
    sendMail('759381818@qq.com', '下载apk出现问题', "miaodexing@openthos.org", 
            position,
            error);
}







// This is where we'll put the code to get around the tests.
const preparePageForTests = async (page) => {
    // // Pass the User-Agent Test.
    const userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299';
    await page.setUserAgent(userAgent);

    // Pass the Webdriver Test.
    await page.evaluateOnNewDocument(() => {
        Object.defineProperty(navigator, 'webdriver', {
            get: () => false,
        });
    });

    // Pass the Chrome Test.
    await page.evaluateOnNewDocument(() => {
        // We can mock this in as much depth as we need for the test.
        window.navigator.chrome = {
            runtime: {},
            // etc.
        };
    });


    // Pass the Plugins Length Test.
    await page.evaluateOnNewDocument(() => {
        // Overwrite the `plugins` property to use a custom getter.
        Object.defineProperty(navigator, 'plugins', {
            // This just needs to have `length > 0` for the current test,
            // but we could mock the plugins too if necessary.
            get: () => [1, 2, 3, 4, 5],
        });
    });

    // Pass the Languages Test.
    await page.evaluateOnNewDocument(() => {
        // Overwrite the `plugins` property to use a custom getter.
        Object.defineProperty(navigator, 'languages', {
            get: () => ['zh-cn', 'en'],
        });
    });
}

async function isDownload(downloadUrl) {
    var MongoClient = require('mongodb').MongoClient;
    var url = "mongodb://localhost:27017/";

    var  test = require('assert');
    MongoClient.connect(url,{ useNewUrlParser: true },(err,db)=>{

        if (err) {
            console.log("connect failed");
            return;
        }
        console.log("connect succssed");

        var dbo = db.db("apps");
        dbo.collection("apkinfo").update({
            "apk_packageName": downloadUrl.split("&")[0].split("=")[1]
        },{'$set' : {'flag':'true'}},{ safe: true }, function (err, result) {
            if (err) {
                console.log("update failed");
                return;
            }
            console.log("update succssed");
            db.close();
        })

});


}



async function download(url) {
    const browser = await puppeteer.launch({headless: false});//
    const page = await browser.newPage();//
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299') 
    page.setDefaultNavigationTimeout(30000)


    //反探测代码
    await preparePageForTests(page);

    try{
        await page.goto(url)
        await page.waitFor(3000);
    
        console.log("login");
    
        //登录按钮
        await page.waitForSelector('.XfpsVe > div:nth-child(1) > button:nth-child(2)');
        await page.click('.XfpsVe > div:nth-child(1) > button:nth-child(2)');
        //用户名输入
        await page.waitForSelector('#identifierId');
        await page.type('#identifierId', account,{delay: 10});    
    
        //下一步
        await page.click('#identifierNext');
    
        console.log("passwd");
        await page.waitFor(2000);
    
        //密码输入
        await page.waitForSelector('.I0VJ4d > div:nth-child(1) > input:nth-child(1)');
        await page.type('.I0VJ4d > div:nth-child(1) > input:nth-child(1)', password,{delay: 10});
    
        //下一步
        await page.waitForSelector('#passwordNext');
        await page.click('#passwordNext');
        console.log("passwordNext");
        await page.waitFor(6000);
        let frame = page.frames()[2];
        
        //console.log(frame)
        console.log("1");
       
        await page.waitFor(6000);
        console.log("2");
        //#purchase-ok-button
        //await page.waitForSelector("#purchase-ok-button",{timeout: 30000});
        await frame.click('#purchase-ok-button');
        //await page.waitForSelector('#purchase-ok-button',{timeout: 6000});
        await page.waitFor(6000);
        console.log("purchase-ok-button");
        await isDownload(url);
        console.log("insertOK");
        
    }catch(e){
        console.log("exception");
        email(url,e.stack);
        console.log(e.stack);
        await browser.close();
    }finally{
        console.log("end");
        await browser.close();
    }


}


//connect mongodb
//const get_down_url = async () => {
async function get_down_url(){

    var MongoClient = require('mongodb').MongoClient;
    var url = "mongodb://localhost:27017/";
    var downUrls = new Array();
    var flags = new Array();
    var num = 1;
   

     MongoClient.connect(url,{useNewUrlParser:true}, function(err, db) {
        if (err) throw err;
        var dbo = db.db("apps");
        
       
         dbo.collection("apkinfo"). find().toArray(function(err, result) { // 返回集合中所有数据
            if (err) throw err;
         
                for(x in result)
                {
                    downUrls[x] = result[x]['apk_downurl'];
                    flags[x] = result[x]['flag'];
                }
             
                db.close();

               
                async function test(downUrls){    
                    for(x in  downUrls)
                    {
                        console.log(downUrls[x]);
                        if(flags[x] != "true")
                        {
                            await download(downUrls[x]); 
                            console.log(num++); 
                        }
                        else
                        {
                            console.log("installed");
                        }
                    }
                }
                test(downUrls);
               

        });
       
    });
   
}




(async(url)=>{


     await get_down_url();

})();
