from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
chrome_service = ChromeService(
    '/Users/sirawitchtiyasuttipun/Downloads/chromedriver-mac-arm64_2/chromedriver')
choose = 0
driver = webdriver.Chrome(service=chrome_service)
page=1
f = open("carsome.txt", "w+")
for page in range(1,7):
    driver.get('https://www.carsome.co.th/buy-car/mazda?pageNo='+str(page))
    html_data = driver.page_source
    soup = BeautifulSoup(html_data, "html.parser")
    links = soup.find_all("a")
    laststr="test"
    for link in links:
        if link.get("href") == None:
            continue
        if "/buy-car/mazda/" in link.get("href") and "/en/" not in link.get("href") and "http" not in link.get("href") and "showImage" not in link.get("href"):
            if(laststr == link.get("href")):
                continue
            laststr = link.get("href")
            f.write(link.get("href")+"\n")
driver.quit()
print("Done")