
import requests
from bs4 import BeautifulSoup

def get_league_table(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    tablelist=[]
    league_table=soup.find('table',class_='standing-table_table callfn')
    for team in league_table.find_all('tbody'):
        rows =team.find_all('tr')
        for row in rows:
            p1_team=row.find('td',class_='standing-table_cell standing-table_cell--name').text
            p2_points=row.find('td',class_='standing-table_cell')[9].text
            teaminleague={
                'name':p1_team,
                'points':p2_points
            }
            tablelist.append(teaminleague)
    return tablelist

data = get_league_table('https://www.skysports.com/premier-league-table')
print(data)