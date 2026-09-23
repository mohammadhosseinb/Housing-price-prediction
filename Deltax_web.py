from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
def read_divar_links():
    url = "https://divar.ir/s/tehran/buy-residential"
    option = webdriver.ChromeOptions()
    option.add_argument("--headless=new")
    option.add_argument("--disable-gpu")
    option.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome() #options= option
    driver.get(url)
    time.sleep(5)
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
    last_height = new_height
        
    links_set = set()
    links = driver.find_elements(By.CSS_SELECTOR, "a.kt-post-card__action")
    for link in links:
        links_set.add(link.get_attribute("href"))
        print(len(links_set),end = "\t")
            
    driver.quit()
    return links_set
    

def read_content():
    url = "https://divar.ir/s/tehran/buy-residential"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    #links_before_scroll = driver.find_elements(By.CSS_SELECTOR, "a.kt-post-card__action")
    ScrollElem = driver.find_element(By.CLASS_NAME, "content-dd848")
    links = set()
    last_count = 0  
    while True:
        try:
            button = driver.find_element(By.XPATH, "//button[.//span[contains(text(),'آگهی‌های بیشتر')]]")
        except:
            print("--scroll--")
        else:
            button.click()
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", ScrollElem)
        time.sleep(2)
        
        link_after_scroll = driver.find_elements(By.CSS_SELECTOR, "a.kt-post-card__action")
        new_count = len(link_after_scroll)
        for link in link_after_scroll:
            links.add(link.get_attribute("href"))
        if len(links)>10:  #------------------------------------count of links---------------------------------------------------------------------------
            break
        print(len(links))
    
    driver.quit()
    return list(links)
def curect_price(text):
    res = re.search(r"(.*)\sتومان", text)
    res = res.group(1)
    res = re.sub(",","",res)
    return int(res)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def info_of_home():
    links = read_content()
    
    driver = webdriver.Chrome() #options = options
    data = []
    for link in links:
        driver.get(link)
        time.sleep(3)
        link_info = dict()
        try:

            zone = driver.find_element(By.CLASS_NAME, "kt-info-row__title")
            #print(zone, zone.text) for test
            #print("zone complete")
            list_fyr = driver.find_elements(By.CLASS_NAME, "kt-group-row-item__value")
            #print("list_fyr complete")
            #print(list_fyr[0],list_fyr[1]) for test
            list_test = driver.find_elements(By.CLASS_NAME, "kt-group-row-item--info-row")
            floorarea = list_fyr[0]
            year_built = list_fyr[1]
            rooms = list_fyr[2]
            
            toc_pppm = driver.find_elements(By.CLASS_NAME, "kt-unexpandable-row__value")
            #print("tocpppm complete")
            price = curect_price(toc_pppm[1].text)         
            #print("toc1 complete")       
            price_per_meter = curect_price(toc_pppm[2].text)
            #print("toc2 complete")  
            home_option = driver.find_elements(By.CLASS_NAME, "kt-group-row-item__value")
            #print("home_option complete")
        except:
            continue

        link_info["zone"] = re.sub(r".*در\s+", "",zone.text)
        link_info["floor_area"] = int(floorarea.text)
        try:
            link_info["year_built"] = int(year_built.text)
            #print("no error ",link_info["year_built"]) #test
        except:
            year_built_int = int(re.search(r"قبل از(.+)", year_built.text).group(1))
            link_info["year_built"] = year_built_int
            #print("error ",link_info["year_built"])  #test
        try:
            link_info["rooms"] = int(rooms.text)
        except:
            link_info["rooms"] = 0
        link_info["price"] = price
        link_info["price_per_meter"] = price_per_meter
        link_info["home_option"] = [item.text for item in home_option]
        link_info["home_option"] = link_info["home_option"][3:6]
        link_info["home_option"] = ",".join(link_info["home_option"])
        link_info["link"] = link
        data.append(link_info)
        #print(link_info)
    driver.quit()
    return data

"""
data = info_of_home()

for info in data:
    print(info,end="\n\n")
"""










