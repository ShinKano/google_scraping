import requests
from bs4 import BeautifulSoup


with open('keys.csv', encoding='shift_jis') as csv_file:
    with open('result.csv','w') as f:
        for keys in csv_file:
            # print(keys, end='')
            result = requests.get('https://www.google.com/search?q={}/'.format(keys))
            # print(result)
            soup = BeautifulSoup(result.text, 'html.parser')
            # print(soup)
            list = soup.findAll(True, {'class' : 'BNeawe vvjwJb AP7Wnd'})
            
            for i in range(3):
                a = str(list[i]).strip('<div class="BNeawe vvjwJb AP7Wnd">')
                b = a.strip('</')
                print(keys.rstrip("\n"),b)
                f.write('{0},{1}\n'.format(keys.rstrip("\n"), b))


#target divs
    # <div class="BNeawe vvjwJb AP7Wnd">フィリピン人女性5つの特徴
    # <div class="BNeawe vvjwJb AP7Wnd">フィリピン人 - Wikipedia









