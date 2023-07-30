import requests
from bs4 import BeautifulSoup

def trending_anime() -> None:
    print('Below are the Trending Animes\n(PS: NOT IN ORDER)\n\n')
    req = requests.get("https://aniwatch.to/")
    soup = BeautifulSoup(req.text,"html.parser")
    Trending_names = soup.findAll("a",attrs={"class":"item"})
    Trending_names_str =''
    for name in Trending_names:
        Trending_names_str += '\n' + name.text
    print(Trending_names_str)

def anime_search() -> str:
    Anime_name = input('Enter the Anime Name to search: ')
    Search_anime =  requests.get('https://123anime.info/search?keyword=' + Anime_name.replace(' ','+'))
    soup = BeautifulSoup(Search_anime.text,"html.parser")
    print("Search Results")
    Tab_contents= soup.findAll("div", attrs="film-list")
    Search_Results = Tab_contents[0].findAll("a",attrs="name")
    cnt = 1
    print("\n\nBelow are the top results: ")
    for name in Search_Results:
        print(cnt, name.text)
        cnt += 1
    Anime = int(input('Enter the option number: '))
    print('You have selected',Search_Results[Anime-1].text)
    Episode = int(input('Enter the episode Number :'))
    Open_anime = requests.get('https://123anime.info/anime/' + Search_Results[Anime-1].text.replace(' ','-') + '/episode/' + str(Episode))
    soup = BeautifulSoup(Search_anime.text,"html.parser")
    print('https://123anime.info/anime/' + Search_Results[Anime-1].text.replace(' ','-') + '/episode/' + str(Episode))

trending_anime()
while True:
    anime_search()
    redo = input('\n\nDo you want to continue[y/n] :\t')
    if redo.lower() == 'n':
        break