# Road to Ultra Music Festival Scrapper "rumf_scrapper"
# The idea of this script is to obtain the countdown info from the page https://costarica.roadtoultra.com/
# Dont Forget to install all the imports: 
# Selenium: pip install selenium
# webdriver: pip install webdriver-manager
# BeautifulSoup: pip install beautifulsoup4 
# Pandas: pip install pandas

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#driver = webdriver.Firefox()

# Visita la URL
#driver.get("https://costarica.roadtoultra.com/")

#print("\n data: " ,driver.title,"\n")

#countdown = driver.find_element(By.ID, "countdown")
#test = driver.find_element(By.XPATH, "//p[@id='countdown']")
#byTag= driver.find_element(By.TAG_NAME, 'p')

#print(type(byTag))
#print(type(test))


#print("\n Countdown: ",byTag,"\n")
# Cierra el controlador cuando hayas terminado
#driver.quit()

# instantiate options 
options = webdriver.ChromeOptions()

# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 

# URL to the website 
url="https://costarica.roadtoultra.com/"

# get the entire website content 
driver.get(url) 
 
# select elements by class name 
elements = driver.find_elements(By.ID, 'countdown') 
for element in elements: 
	# obtain the .text data from the element
	data = element.text 
	# print p
	print(data)

#now that we have the data que have to export it to another file

