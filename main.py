from typing import ItemsView
from selenium import webdriver
from tf2_sku import to_sku,from_sku
import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time


ItemList = []
url = "https://marketplace.tf/browse/all?sterm=hat&ssortfield=min_price&ssortdir=1"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)


time.sleep(30) #delay for login input
content = driver.page_source.encode('utf-8').strip()



soup = BeautifulSoup(content, "html.parser")

item_data=soup.find_all(name="a", class_="item-box-name-link")

for item in item_data:

    Itemlists = item.get("href") #get sku of hat value
    ItemList.append(Itemlists)



print(ItemList)


driver.quit()