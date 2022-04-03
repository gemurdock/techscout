from bs4 import BeautifulSoup

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

driver.get("https://www.google.com/")

src = driver.page_source

soup = BeautifulSoup(src, 'lxml')

print(soup.find('title'))