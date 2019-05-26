from requests import get
from bs4 import BeautifulSoup
import pandas as pd

country = input("Enter 1 for England \t\t 2 for India \t\t 3 for Afghanistan \n 4 for Bermuda \t\t\t 5 for Canada \t\t 6 for EAST AND CENTRAL AFRICA \n 7 for HonG Kong \t\t 8 for Ireland \t\t 9 for Namibia \n 10 for Kenya \t\t\t 11 for Nepal \t\t 12 for Nethlands\n 13 for Newzealand \t\t 14 for Oman \t\t 15 for Pakistan \n 16 for Papua New Guinea \t 17 for Scotland \t 18 for South Africa \n 19 for Sri Lanka \t\t 20 for UAE \t\t 21 for USA \n 22 for West Indies \t\t 23 for Zimbabwe \t 24 for Bangladesh \t 25 for Australia:- ")

def main_code(url,country):


    response = get(url)



    html_soup = BeautifulSoup(response.text, 'html.parser')

    movie_containers = html_soup.find_all('li', class_ = 'sep')

    cap_no = []
    names= []
    ground_year = []

    for container in movie_containers:
        if container.find('li', class_ = 'ciPlayerserialno') is not None:
            name=container.find('li', class_ = 'ciPlayerserialno')
            cap_no.append(int(name.text))
            year=container.find('li', class_ = 'ciPlayername')
            names.append(year.text)
            rate=container.find('li', class_ = 'ciPlayerplayed')
            ground_year.append(rate.text)

    

    test_df = pd.DataFrame({'cap_no': cap_no,
    'name': names,
    'ground_year': ground_year
    })
    test_df.to_csv(country+'.csv',index=False)





if country == "1":
	url="http://www.espncricinfo.com/england/content/player/caps.html?country=1;class=2"
	main_code(url,country)
    

elif country == "2":
	url="http://www.espncricinfo.com/india/content/player/caps.html?country=6;class=2"
	main_code(url,country)

    
elif country == "3":
	url="http://www.espncricinfo.com/afghanistan/content/player/caps.html?country=40;class=2"
	main_code(url,country)

    
elif country == "4":
	url="http://www.espncricinfo.com/ci/content/player/caps.html?country=12;class=2"
	main_code(url,country)


elif country == "5":
	url="http://www.espncricinfo.com/canada/content/player/caps.html?country=17;class=2"
	main_code(url,country)

   
elif country == "6":
	url="http://www.espncricinfo.com/india/content/player/caps.html?country=14;class=2"
	main_code(url,country)


elif country == "7":
	url="http://www.espncricinfo.com/action-cricket-t20-2011/content/player/caps.html?country=19;class=2"
	main_code(url,country)


elif country == "8":
	url="http://www.espncricinfo.com/cricket/content/player/caps.html?country=29;class=2"
	main_code(url,country)


elif country == "9":
	url="http://www.espncricinfo.com/cid/content/player/caps.html?country=28;class=2"
	main_code(url,country)


elif country == "10":
	url="http://www.espncricinfo.com/kenya/content/player/caps.html?country=26;class=2"
	main_code(url,country)


elif country == "11":
	url="http://www.espncricinfo.com/ci/content/player/caps.html?country=32;class=2"
	main_code(url,country)


elif country == "12":
	url="http://www.espncricinfo.com/netherlands/content/player/caps.html?country=15;class=2"
	main_code(url,country)


elif country == "13":
	url="http://www.espncricinfo.com/newzealand/content/player/caps.html?country=5;class=2"
	main_code(url,country)



elif country == "14":
	url="http://www.espncricinfo.com/ci/content/player/caps.html?country=37;class=2"
	main_code(url,country)


elif country == "15":
	url="http://www.espncricinfo.com/pakistan/content/player/caps.html?country=7;class=2"
	main_code(url,country)


elif country == "16":
	url="http://www.espncricinfo.com/columns/content/player/caps.html?country=20;class=2"
	main_code(url,country)


elif country == "17":
	url="http://www.espncricinfo.com/scotland/content/player/caps.html?country=30;class=2"
	main_code(url,country)


elif country == "18":
	url="http://www.espncricinfo.com/southafrica/content/player/caps.html?country=3;class=2"
	main_code(url,country)


elif country == "19":
	url="http://www.espncricinfo.com/srilanka/content/player/caps.html?country=8;class=2"
	main_code(url,country)


elif country == "20":
	url="http://www.espncricinfo.com/unitedarabemirates/content/player/caps.html?country=27;class=2"
	main_code(url,country)


elif country == "21":
	url="http://www.espncricinfo.com/ci/content/player/caps.html?country=11;class=2"
	main_code(url,country)


elif country == "22":
	url="http://www.espncricinfo.com/usa/content/player/caps.html?country=4;class=2"
	main_code(url,country)


elif country == "23":
	url="http://www.espncricinfo.com/cricket/content/player/caps.html?country=9;class=2"
	main_code(url,country)

elif country == "24":
	url="http://www.espncricinfo.com/bangladesh/content/player/caps.html?country=25;class=2"
	main_code(url,country)


elif country == "25":
	url="http://www.espncricinfo.com/australia/content/player/caps.html?country=2;class=2"
	main_code(url,country)











































































       

   

