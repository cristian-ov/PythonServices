# Road to Ultra Music Festival Scrapper "rumf_scrapper"
# The idea of this script is to obtain the countdown info from the page https://costarica.roadtoultra.com/
# Dont Forget to install all the imports: 
# Selenium: pip install selenium
# webdriver: pip install webdriver-manager
# BeautifulSoup: pip install beautifulsoup4 

#-------------------------------------
import time
import sys
from internet_checker import check_connection
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#-------------------------------------

# Funtion
def getInfo():

	# URL to the website 
	url="https://costarica.roadtoultra.com"

	if (check_connection(url)):
		print("'https://costarica.roadtoultra.com' esta disponible para usar")
		# instantiate options 
		options = webdriver.ChromeOptions()

		# IMPORTANT!!!!!!
		# work with the try/except concept to catch the erros and avoid the fails
		try:
			# instantiate driver 
			driver = webdriver.Chrome(service=ChromeService( 
				ChromeDriverManager().install()), options=options) 
		except SystemError:
			print(": An exception has occurred trying to execute the driver!")
			input("press 'ENTER' to continue...")


		# minimize the window to not interrupt 
		driver.minimize_window()

		

		try:
			# get the entire website content 
			driver.get(url) 
		except SystemError:
			print("An exception has occurred!")
			input("press 'ENTER' to continue...")


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
	else:
		print("No hay conexion a Internet o a 'https://costarica.roadtoultra.com'")




#now that we have the data que have to export it to another file

def main():
    print(getInfo())

if __name__ == "__main__":
    main()
