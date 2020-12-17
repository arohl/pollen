#!/Users/andrew/anaconda3/bin/python3

# <bitbar.title>Perth Pollen</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Andrew Rohl</bitbar.author>
# <bitbar.author.github>arohl</bitbar.author.github>
# <bitbar.desc>Provides current and forecast pollen for Perth</bitbar.desc>
# <bitbar.dependencies>python3</bitbar.dependencies>

import urllib.request
from bs4 import BeautifulSoup
import datetime
import calendar

pollen = "https://weather.news.com.au/wa/perth/perth/pollen-index"
page = urllib.request.urlopen(pollen)
soup = BeautifulSoup(page, "html.parser")
pollen_ul = soup.find(id="pollen-graph")
pollen_week = pollen_ul.find_all("div")
print(f":sunflower: {pollen_week[0].contents[1].string}")
print("---")
for x in range(1, 4):
    next_day = datetime.date.today() + datetime.timedelta(days=x)
    print (f"{calendar.day_name[next_day.weekday()]} {pollen_week[x].contents[1].string}")
