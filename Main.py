#Game Start
#//////////////
from cities import City
from readcities import Cities
from  search_on_letter import search
from  funnctionforassert import assertfortown


def Turn(player, last_letter):
    if player == 1:
        print('Введи название города  на ',last_letter)
        PlayerTurn(last_letter)
        player=0
    if player == 0:
        print('Ход Машины')
        ComputerTurn(last_letter)
        player=1
    if player > 1:
        print('Ошибка')

        
def PlayerTurn(last_letter):
    player_word = input()
    print('ok')
    city = City(player_word)
    print(City)
    while (city.first != last_letter) and (assertfortown(city.name, Cities)):
        print('Неправильный город Введите новый')
        player_word = input()
        city = City(player_word)
    print('Игрок1 ввёл город', city.name)
    last_letter = city.last

    
def ComputerTurn(last_letter):
    player_word = search(last_letter,Cities)
    if not(player_word):
        print('Компьютер сдаётся')
        exit
    city= City(player_word)
    print('Игрок2 ввёл город', city.name)
    last_letter = сity.last

    
#GameCikl
#//////////////
while True:
    Turn(1,'А')
        
