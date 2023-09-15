# Road to Ultra Music Festival Scrapper "rumf_scrapper"
# The idea of this script is to obtain the countdown info from the page https://costarica.roadtoultra.com/
# Dont Forget to install all the imports: 
# Selenium: pip install selenium
# webdriver: pip install webdriver-manager
# BeautifulSoup: pip install beautifulsoup4 
# Pandas: pip install pandas

import time
import sys


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Funtion
def getInfo():
# instantiate options 
	options = webdriver.ChromeOptions()

	# instantiate driver 
	driver = webdriver.Chrome(service=ChromeService( 
		ChromeDriverManager().install()), options=options) 

	# minimize the window to not interrupt 
	driver.minimize_window()

	# URL to the website 
	url="https://costarica.roadtoultra.com/"

	# get the entire website content 
	driver.get(url) 


	data=""
	# select elements by class name 
	elements = driver.find_elements(By.ID, 'countdown') 
	for element in elements: 
		# obtain the .text data from the element
		data = element.text 
		# print p
		print(data)
	driver.close()
	driver.quit()
      
	return data



#now that we have the data que have to export it to another file

def main():
    print(getInfo())

if __name__ == "__main__":
    main()
