# -*- coding: utf-8 -*-
import sys
import os
import re

#!/usr/bin/env python

# функция украинской фонетики
# опишем правила фонетики
def ukrrules(stressword):
    # zamena i angliyskoy na ukr
    stressword=stressword.replace("i","і")
    stressword=stressword.replace("o","о")
    stressword=stressword.replace("'","’")
    stressword=stressword.replace("ˈ","’")

    
    # sproschenny grupi prigolosnih
    stressword=stressword.replace("стс","сс")
    stressword=stressword.replace("здц","зьц")
    stressword=stressword.replace("стд","зд")
    stressword=stressword.replace("стч","шч") #???
    stressword=stressword.replace("стц","сьц")
    stressword=stressword.replace("нтст","нст")
    stressword=stressword.replace("нтськ","ньськ")
    # asimilyativni zminy prigolosnih
    stressword=stressword.replace("сш","шш")
    stressword=stressword.replace("зж","жж")
    # блок 
    stressword=stressword.replace("жся","зься")
    stressword=stressword.replace("жсї","зьсї")
    stressword=stressword.replace("жсю","зьсю")
    stressword=stressword.replace("жсі","зьсі")
    stressword=stressword.replace("жсь","зьсь")
    stressword=stressword.replace("жсє","зьсє")

    # блок 
    stressword=stressword.replace("шся","сся")
    stressword=stressword.replace("шсї","ссї")
    stressword=stressword.replace("шсю","ссю")
    stressword=stressword.replace("шсі","ссі")
    stressword=stressword.replace("шсь","ссь")
    stressword=stressword.replace("шсє","ссє")

    # блок 
    stressword=stressword.replace("чся","цься")
    stressword=stressword.replace("чсї","цьсї")
    stressword=stressword.replace("чсю","цьсю")
    stressword=stressword.replace("чсі","цьсі")
    stressword=stressword.replace("чсь","цьсь")
    stressword=stressword.replace("чсє","цьсє")
    
    # блок 
    stressword=stressword.replace("жця","зьця")
    stressword=stressword.replace("жцї","зьцї")
    stressword=stressword.replace("жцю","зьцю")
    stressword=stressword.replace("жці","зьці")
    stressword=stressword.replace("жць","зьць")
    stressword=stressword.replace("жцє","зьцє")
    # блок 
    stressword=stressword.replace("шця","сьця")
    stressword=stressword.replace("шцї","сьцї")
    stressword=stressword.replace("шцю","сьцю")
    stressword=stressword.replace("шці","сьці")
    stressword=stressword.replace("шць","сьць")
    stressword=stressword.replace("шцє","сьцє")
    # блок 
    stressword=stressword.replace("чця","цься")
    stressword=stressword.replace("чцї","цьсї")
    stressword=stressword.replace("чцю","цьсю")
    stressword=stressword.replace("чці","цьсі")
    stressword=stressword.replace("чць","цьсь")
    stressword=stressword.replace("чцє","цьсє")

    # блок замени к на г
    stressword=stressword.replace("кб","ґб")
    stressword=stressword.replace("кд","ґд")
    stressword=stressword.replace("кз","ґз")
    stressword=stressword.replace("кж","ґж")
    stressword=stressword.replace("кг","ґг")
    stressword=stressword.replace("кґ","ґґ")

    # блок замени г на х
    stressword=stressword.replace("гт","хт")
    stressword=stressword.replace("гк","хк")

    # блок замени зч
    stressword=stressword.replace("зч","шч")

    # блок замени стч на шч
    stressword=stressword.replace("стч","шч")

    # блок замени щ на шч
    stressword=stressword.replace("щ","шч")

    # блок замени зш на вначалы
    if stressword.find("зш") == 0:
        stressword=stressword.replace("зш","шш")
    if stressword.find("зш") > 0:
        stressword=stressword.replace("зш","жш")
    # конец блока украинской фонетики
    return stressword

def getphonems(world):
    # робимо прості заміни наголошені букви
    line = list(world.strip())

    ### тільки тверді приголосні подовжені  шш , жж,   чч  
    for num in range(1, len(line)):
        if line[num] == 'ш' and line[num-1] == 'ш':
            line[num] = ":"
            line[num-1] == 'ʃ'
        if line[num] == 'ж' and line[num-1] == 'ж':
            line[num] = ":"
            line[num-1] == 'ʒ'
        if line[num] == 'ч' and line[num-1] == 'ч':
            line[num] = ":"
            line[num-1] == 'tʃ'

    ### тільки мякі приголосні складні  дз 
    for num in range(2, len(line)):
        if line[num-2] == 'д' and line[num-1] == 'з' and line[num] in ['є','ю','я','ї','і','ь',]:
            line[num-1] = "dzʲ"
            line.pop(num-2)

    ### тільки мякі приголосні подовжені  нн,рр,сс,цц,дд,зз,тт, лл
    for num in range(2, len(line)):
        if line[num-2] == 'р' and line[num-1] == 'р' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = ":"
            line[num-2] = 'rʲ'
        if line[num-2] == 'с' and line[num-1] == 'с' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = ":"
            line[num-2] = 'sʲ'
        if line[num-2] == 'з' and line[num-1] == 'з' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = ":"
            line[num-2] = 'zʲ'
        if line[num-2] == 'ц' and line[num-1] == 'ц' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = ":"
            line[num-2] = 'tsʲ'
        if line[num-2] == 'т' and line[num-1] == 'т' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = ":"
            line[num-2] = 'tʲ'
        if line[num-2] == 'д' and line[num-1] == 'д' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = ":"
            line[num-2] = 'dʲ'
        if line[num-2] == 'н' and line[num-1] == 'н' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = ":"
            line[num-2] = 'nʲ'
        if line[num-2] == 'л' and line[num-1] == 'л' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = ":"
            line[num-2] = 'lʲ'

    ### тільки мякі приголосні р,л,с,з,ц,т,д,н
    for num in range(1, len(line)):
        if line[num-1] == 'р' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = 'rʲ'
        if line[num-1] == 'л' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = 'lʲ'
        if line[num-1] == 'с' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = 'sʲ'
        if line[num-1] == 'з' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = 'zʲ'
        if line[num-1] == 'ц' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = 'tsʲ'
        if line[num-1] == 'т' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = 'tʲ'
        if line[num-1] == 'д' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = 'dʲ'
        if line[num-1] == 'н' and line[num] in ['є','ю','я','ї','і','ь']:
            line[num-1] = 'nʲ'

    ### тільки тверді приголосні м, б, ґ, п, в, г, ж, ф, ш, х, ч, с, н, д, т, р, л, з, й, щ, ц
    for num in range(0, len(line)):
        if line[num] == 'м':
            line[num] = 'm'
        if line[num] == 'б':
            line[num] = 'b'
        if line[num] == "з":
            line[num] = "z"
        if line[num] == 'ґ':
            line[num] = "ɡ"
        if line[num] == 'п':
            line[num] = "p"
        if line[num] == 'к':
            line[num] = "k"
        if line[num] == 'в':
            line[num] = "w"
        if line[num] == 'г':
            line[num] = "ɦ"
        if line[num] == 'ж':
            line[num] = "ʒ"
        if line[num] == 'ф':
            line[num] = "f"
        if line[num] == 'ш':
            line[num] = "ʃ"
        if line[num] == 'х':
            line[num] = "x"
        if line[num] == 'ч':
            line[num] = "tʃ"
        if line[num] == 'с':
            line[num] = "s"
        if line[num] == 'н':
            line[num] = "n"
        if line[num] == 'н':
            line[num] = "n"
        if line[num] == 'д':
            line[num] = "d"
        if line[num] == 'т':
            line[num] = "t"
        if line[num] == 'р':
            line[num] = "r"
        if line[num] == 'л':
            line[num] = "l"
        if line[num] == 'з':
            line[num] = "z"
        if line[num] == 'й':
            line[num] = "j"
        if line[num] == 'ц':
            line[num] = "ts"

        
    ### наголошені і, и, е, а, у, о
    for i in range(3):
        for num in range(0, len(line)-1):
            if line[num+1] == '́' and line[num] == 'і':
                line[num] = "i"
            if line[num+1] == '́' and line[num] == 'и':
                line[num] = "ɪ"
            if line[num+1] == '́' and line[num] == 'е':
                line[num] = "ɛ"
            if line[num+1] == '́' and line[num] == 'а':
                line[num] = "a"
            if line[num+1] == '́' and line[num] == 'у':
                line[num] = "u"
            if line[num+1] == '́' and line[num] == 'о':
                line[num] = "ɔ"

    ### ненаголошені і, и, е, а, у, о
    for num in range(0, len(line)):
        if line[num] == 'і':
            line[num] = 'ɨ'
        if line[num] == 'и': #
            line[num] = 'ᵻ'
        if line[num] == 'е':  #
            line[num] = 'ɵ'
        if line[num] == 'а':  
            line[num] = 'ɐ'
        if line[num] == 'у': 
            line[num] = 'ʉ'
        if line[num] == 'о':   #
            line[num] = 'o'

    ### ь вже все помякшено видаляем
    for i in range(5):
        for num in range(0, len(line)):
            if line[num] == 'ь':
                line.pop(num)
                break
                
    ### наголошені Я, ю, є, ї
    for num in range(0, len(line)-1):
        if line[num+1] == '́' and line[num] == 'я':
            line[num] = "j"
            line[num+1] = 'a'
        if line[num+1] == '́' and line[num] == 'ю':
            line[num] = "j"
            line[num+1] = 'u'
        if line[num+1] == '́' and line[num] == 'ї':
            line[num] = "j"
            line[num+1] = 'i'
        if line[num+1] == '́' and line[num] == 'є':
            line[num] = "j"
            line[num+1] = 'ɛ'

    ### ненаголошені треба пару раз повторити Я, ю, є, ї
    for i in range(5):
        for num in range(0, len(line)):    
            if line[num] == 'я':
                line[num] = 'j'
                line.insert(num+1, "ɐ")

            if line[num] == 'ю':
                line[num] = 'j'
                line.insert(num+1, "ʉ")

            if line[num] == 'ї':
                line[num] = 'j'
                line.insert(num+1, "ɨ")

            if line[num] == 'є':
                line[num] = 'j'
                line.insert(num+1, "ɵ")
              
    return line
    
    
def convertG2P(word):
    outline=''
    phonems = getphonems(ukrrules(word))
    #print(line, phonems)
    for phon in phonems:
        outline = outline + phon
    ### виправляемо неподобство 
    outline = outline.replace('́',"")
    outline = outline.replace("’", "")
    outline = outline.replace("ʲj", "ʲ")
    outline = outline.replace("ʲ:j", "ʲ:")
    #outline = outline.replace(" ", "")
    #outline = outline.replace("   ", " ")

    #print (outline)
    return outline