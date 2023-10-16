#This idea was not achieved since as the page is dynamic the "requests" library cannot obtain the information from javascript
#<p data-datetime="2023-11-03T00:00:00-06:00" data-timezone="America/Costa_Rica" id="countdown"> </p>
# that is why the result shows the p tag empty

import requests
from bs4 import BeautifulSoup

URL = "https://costarica.roadtoultra.com/"
page = requests.get(URL)

#print(page.text)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="countdown")

print(results.text.strip())
print(results)

