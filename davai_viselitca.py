# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:54:50 2022

@author: dedaster
"""

import pandas as pd
import os
import keyboard

os.system("mode con cols=50 lines=14")

words = pd.read_csv('C://Git/davai_viselitca/words.csv')
score = pd.read_csv('C://Git/davai_viselitca/score.csv')

win = score['score'].iloc[0]
lose = score['score'].iloc[1]

while True:

    while True:
        try:
            os.system('CLS')
            max_let = int(input('Введите максимум букв для слова: '))
            if max_let > 24 or max_let < 2:
                print('Таких слов нет')
                continue
        except ValueError:
            print('Введите число')
        else:
            break
        
    while True:
        try:
            os.system('CLS')
            tries = int(input('Сколько неверных попыток дать от 0 до 13: '))
            if tries > 13 or tries < 0:
                print('Так не интересно')
                continue
        except ValueError:
            print('Введите число')
        else:
            break
        
    word_len = 50
    
    while word_len > max_let:
        word_new = words['word'].sample().tolist()
        word_task =list(word_new[0])
        word_len = len(word_new[0])
    
    os.system('CLS')
    # tries = 9
    last = []
    
    print(f'Количество попыток: {tries}')
    print(f'Слово состоит из {word_len} букв')
    
    word_hide = ['_']
    word_sec = word_len*word_hide
    print((' '.join(word_sec)))

    
    while '_' in word_sec:
    
        guess = str(input('Введите букву: ').lower())
        
        # if guess == 'ё':
        #     guess = 'е'
    
        if len(guess) > 1:
            print("Буква должна быть одна!")
            continue
        elif guess.isdigit():
            print("Должна быть буква, а не цифра!")
            continue
        elif guess not in 'йцукеннгшщзхъфывапролджэячсмитьбёю':
            print("Только русские буквы!")
            continue
        
        if guess in last:
            os.system('CLS')
            print(f'Осталось попыток {tries}')
            print((' '.join(word_sec)))
            print()
            print(f'Буква "{guess}" уже была')
            print()
        elif guess in word_task:
            inds = [i for i in range(0, len(word_task)) if word_task[i]==guess]
            for i in inds:
                word_sec[i] = guess
            os.system('CLS')
            print(f'Осталось попыток {tries}')
            print((' '.join(word_sec)))
            last.append(guess)
            if '_' not in word_sec:
                os.system('CLS')
                print('Победа!')
                print('Верно: '+(''.join(word_task)))
                win += 1
                print(f'Побед: {win} Поражений: {lose}')
                percent = round(100/(win+lose)*win)
                print(f'Процент побед: {percent}%')
                score.iloc[0] = win
                score.to_csv('C://Git/davai_viselitca/score.csv', index = False)
        else:
            os.system('CLS')
            tries -= 1
            print(f'Осталось попыток {tries}')
            print((' '.join(word_sec)))
            last.append(guess)
            if  tries <= 0:
                print()
                os.system('CLS')
                print('======')
                print('||   |')
                print('||   O')
                print('||  /|\ ')
                print('||  / \ ')
                print('||')
                print('')
                print('Проигрыш!')
                print('Слово было: '+(''.join(word_task)))
                lose += 1
                print(f'Побед: {win} Поражений: {lose}')
                percent = round(100/(win+lose)*win)
                print(f'Процент побед: {percent}%')
                score.iloc[1] = lose
                score.to_csv('C://Git/davai_viselitca/score.csv', index = False)
                break
    print()
    print('Для следующей игры нажми "Enter"')
    keyboard.wait('enter')