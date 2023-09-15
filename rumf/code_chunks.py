countdown=[]
driver.get("https://costarica.roadtoultra.com/")

content = driver.page_source
soup = BeautifulSoup(content)

#revisar , attrs={'class':'_31qSD5'}
for a in soup.findAll('p',href=False):  
    #, attrs={'class':'_3wU53n'} 
    data=a.find('p')
    print("data: ",a)
    #revisar
    countdown.append(data.text)


    
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