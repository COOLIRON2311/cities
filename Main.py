#Game Start
#//////////////
from cities import City
from readcities import Cities
from  search_on_letter import search
from  funnctionforassert import assertfortown


def Turn(player, last_letter):
    if last_letter == "":
        return
    if player == 1:
        print('Введи название города  на ',last_letter)
        Turn(0, PlayerTurn(last_letter))
    if player == 0:
        print('Ход Машины')
        Turn(1, ComputerTurn(last_letter))
    if player > 1:
        print('Ошибка')

        
def PlayerTurn(last_letter):
    player_word = input()
    print('ok')
    city = City(player_word)
    while (city.first != last_letter.upper()) or (not assertfortown(city.name, Cities)):
        print('Неправильный город Введите новый')
        player_word = input()
        city = City(player_word)
    print('Игрок1 ввёл город', city.name)
    return city.last

    
def ComputerTurn(last_letter):
    computer_word = search(last_letter,Cities)
    if not computer_word:
        print('Компьютер сдаётся')
        return ""
    city = City(computer_word.name)
    print('Игрок2 ввёл город', city.name)
    return city.last

    
#GameCikl
#//////////////
Turn(1,'А')
        
