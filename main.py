import requests
import bs4
import time
from selenium import webdriver

loginForm = {
    "email": "",
    "password": "",
    "_token": ""
}
chrome_options = webdriver.ChromeOptions()
# 设置代理
chrome_options.add_argument('--proxy-server=socks5://localhost:1080')
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(5)
driver.set_script_timeout(5)
driver.set_page_load_timeout(5)

try:
    driver.get("https://www.hackthebox.eu/login")
except:
    driver.execute_script('window.stop()')
elem = driver.find_element_by_id("email")
secret=input("username:")
elem.send_keys(secret)
elem = driver.find_element_by_id("password")
secret=input("password")
elem.send_keys(secret)

input("手动登录完成后按回车继续")
# 手动登录


with open("list.txt", "r") as listFile:
    for item in listFile:
        while(True):
            try:
                driver.execute_script('window.stop()')
            except:
                pass
            finally:
                break
        try:
            driver.get("https://www.hackthebox.eu/home/machines")
        except:
            driver.execute_script('window.stop()')
        elem = driver.find_element_by_xpath(
            '//*[@id="machinesTable"]/div[1]/div[1]/div[2]')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="machinesTable"]/div[1]/div[2]/h4')
        elem.click()
        elem = driver.find_element_by_xpath('//*[@id="machine_name"]')
        elem.clear()
        elem.send_keys(item.strip())
        for i in range(len(driver.find_elements_by_tag_name('a'))):
            if(driver.find_elements_by_tag_name('a')[i].text.lower() == item.strip().lower()):
                try:
                    driver.get(driver.find_elements_by_tag_name(
                        'a')[i].get_attribute('href'))
                except:
                    driver.execute_script('window.stop()')
                break
        for i in range(len(driver.find_elements_by_tag_name('a'))):
            if('writeup' in driver.find_elements_by_tag_name('a')[i].get_attribute('href')):
                driver.find_elements_by_tag_name('a')[i].click()
                break
