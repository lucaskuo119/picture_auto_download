import bs4, requests
import selenium
import time,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
url = r"https://pic.sogou.com/pic/searchList.jsp?statref=searchlist_hintword_up&spver=0&keyword=%E6%97%A5%E6%9C%AC%E5%8A%A8%E6%BC%AB%E5%A5%B3%E4%B8%BB%E8%A7%92%E7%9A%84%E7%85%A7%E7%89%87"

#urlhead = requests.get(url)

namenum = 0
folder_path = r'C:\Users\hardoff\Desktop\world_json\gf'


drivePath = r"C:\\Users\hardoff\Documents\cronedriver\chromedriver.exe"
chrome_options =webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\\Program Files\Google\Chrome\Application\chrome.exe"
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
i=0

while(i<1):
    time.sleep(5)
    i += 1
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    more_class = "more-box"
    try:
        time.sleep(3)
        browser.find_element(By.CLASS_NAME, more_class).click()
    except:
        print("找不到更多按钮")
    time.sleep(5) 
objsoup = bs4.BeautifulSoup(browser.page_source, "html.parser")

print("解析成功")
time.sleep(5)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)


itemlist = objsoup.find_all("div",id="picWapApp")
for itempage in itemlist:
    print("開始分析")
    piclist = itempage.find_all("div",class_="similar-list")
    for page1 in piclist:
        piclist1 = page1.find_all("img")
        for page2 in piclist1:

            piclist2 = page2.get("src")
            namenum = namenum+1
            download = requests.get(piclist2)
            filename = 'gf_' + str(namenum) + '.jpg'
            filehouse = os.path.join(folder_path,filename)
            
            with open(filehouse, 'wb') as f:
                f.write(download.content)

    time.sleep(5)
    print("結束")
    
    
           



