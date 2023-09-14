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