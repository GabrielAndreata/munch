import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, responses
from fastapi.staticfiles import StaticFiles
from heart.config import settings
from pages.route_homepage import router


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def include_router(app):
    app.include_router(router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    return app


app = start_application()


@app.get("/stats")
async def read_item(playername: str):
    name = str(playername)
    url = requests.get("https://www.munchymc.com/profile/" + name)
    soup = BeautifulSoup(url.content, 'html.parser')

    if soup.find_all("div", class_="ui red message"):
        return responses.PlainTextResponse("<center><div style=\"padding:10em\">player not found</center></div>")

    bigText = soup.find_all("h2", class_="ui centered red header")
    if bigText[0].text.startswith(" Clan"):
        player = bigText[1].text.replace("\n", " ").replace('\t', '').split(" ")[4]
    else:
        player = bigText[0].text.replace("\n", " ").replace('\t', '').split(" ")[4]

    skin = soup.find_all("div", class_="ui image")[0].find_all("img")[0]["src"]

    statslist = []

    s = soup.find_all('div', class_='ui green right floated label')
    for i in s:
        statslist.append(i.text)

    stats = {
        'skin': skin,
        'player': player,
        'wins': statslist[6],
        'games': statslist[7],
        'kills': statslist[8],
        'winratio': statslist[9].replace('\t', ''),
    }

    result = f'''
    <h2>{stats['player']}'s stats</h2><br>
    <div id="wrapper" style="display:flex;">
    <img src="{stats['skin']}" alt="{stats['player']}'s skin" width="158" height="256">
    <table style="max-width: 500px;margin: auto;">
      <tr>
    <th>wins</th>
    <td>{stats['wins']}</td>
  </tr>
  <tr>
    <th>games</th>
    <td>{stats['games']}</td>
  </tr>
  <tr>
    <th>kills</th>
    <td>{stats['kills']}</td>
  </tr>
  <tr>
    <th>winratio</th>
    <td>{stats['winratio']}</td>
  </tr>
  </table>
  </div>
    '''

    return responses.PlainTextResponse(result)
