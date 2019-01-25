const puppeteer = require('puppeteer');
const account = `zhangdali2020@gmail.com`;
const password = `123abc$%^789`;

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


(async () => {
    const browser = await puppeteer.launch({headless: false});//´ò¿ªÓÐ½çÃæµÄä¯ÀÀÆ÷
    const page = await browser.newPage();//´ò¿ªÒ»¸ö¿Õ°×Ò³
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299') 
    page.setDefaultNavigationTimeout(30000)


    // Prepare for the tests (not yet implemented).
    await preparePageForTests(page);

    var url = "https://play.google.com/store/apps/details?id=com.kidsplaylearning.apps.colorbook&rdid=com.kidsplaylearning.apps.colorbook&feature=md&offerId"
    //var url= "https://play.google.com/store/apps/details?id=com.mobility.kpa"
    //await page.goto('https://accounts.google.com/signin/v2/identifier?service=googleplay&passive=1209600&continue=https%3A%2F%2Fplay.google.com%2Fstore&followup=https%3A%2F%2Fplay.google.com%2Fstore&flowName=GlifWebSignIn&flowEntry=ServiceLogin');//´ò¿ª¶¹°êÍøÕ¾
    await page.goto(url)
    await page.waitFor(4000);

    console.log("login");
    /*
    await page.waitForSelector('.HPiPcc');
    await page.click('.HPiPcc');
    */
    //登录按钮
    await page.waitForSelector('.XfpsVe > div:nth-child(1) > button:nth-child(2)');
    await page.click('.XfpsVe > div:nth-child(1) > button:nth-child(2)');
    //用户名输入
    await page.waitForSelector('#identifierId');
    await page.type('#identifierId', account);    
    //#identifierNext.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.nDKKZc.DL0QTb.M9Bg4d content.CwaK9 span.RveJvd.snByac
    //下一步
    await page.click('#identifierNext');
    
    console.log("passwd");
    await page.waitFor(4000);
    //#password.rFrNMe.KSczvd.uyaebd.BlbNGe.zKHdkd.sdJrJc.Tyc9J div.aCsJod.oJeWuf div.aXBtI.I0VJ4d.Wic03c div.Xb9hP input.whsOnd.zHQkBf
    //.I0VJ4d > div:nth-child(1) > input:nth-child(1)
    //密码输入
    await page.waitForSelector('.I0VJ4d > div:nth-child(1) > input:nth-child(1)');
    await page.type('.I0VJ4d > div:nth-child(1) > input:nth-child(1)', password);
    //#passwordNext > content:nth-child(3) > span:nth-child(1)
    //#passwordNext.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.nDKKZc.DL0QTb.M9Bg4d
    //#passwordNext > content:nth-child(3) > span:nth-child(1)
    //#passwordNext.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.nDKKZc.DL0QTb.M9Bg4d content.CwaK9 span.RveJvd.snByac
    //下一步
    await page.click('#passwordNext');
    
    await page.waitFor(6000);
    let frame = page.frames()[2];
   
   
    await page.waitFor(6000);
  
    await frame.click("#purchase-ok-button");
     await page.waitFor(2000);
    console.log("end");
    await browser.close();
    
   /*
    await page.waitForNavigation({
        waitUntil: 'load'
    });//µÈ´ýÒ³Ãæ¼ÓÔØ³öÀ´£¬µÈÍ¬ÓÚwindow.onload
    await page.screenshot({path: 'example.png'});//½Ø¸öÍ¼
    await browser.close();//¹Øµôä¯ÀÀÆ÷
    */
})();
