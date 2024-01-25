#  Подключаем функцию получения строки описания события из файла 'get_information_game'
from get_information_game import get_des_string
#  Подключаем функцию получения адреса статистики события из файла 'parser_string'
from parser_string import get_statistic_string
# Подключаем библиотеку для отправки запросов
import requests
# Подключаем библиотеку для парсинга текста
from bs4 import BeautifulSoup

# Функция получения массива данных со всей доступной статистикой
def get_statistic(resultline,id):
    # Вызываем функцию получения строки описания события
    descr = get_des_string(resultline,id)
    # Передаем строку описания в функцию полуения адреса статистики
    url_stat = get_statistic_string(descr)
    
    # Отправляем GET-запрос для получения статистики по полученному URL
    # Отправляемый набор cookies
    cookies = {
        'sid': '3r364v2v8th6t5g5bnorks8si6',
        '__utmzz': 'utmcsr=(direct)|utmcmd=(none)|utmccn=(not set)|utmcct=(not set)|utmctr=(not set)',
        '__utmzzses': '1',
        'cookie_test': '1',
        '_ym_uid': '1702537939809069726',
        '_ym_d': '1702537939',
        'tmr_lvid': '3a5d8619f82987879aa67a9ff8f131b5',
        'tmr_lvidTS': '1702537942411',
        'afUserId': '3c2c8af7-3cf8-4db5-b7a9-30e4772cab11-p',
        '_tt_enable_cookie': '1',
        '_ttp': 'bEX8HFrw5QTol9_wxCSVYFy_Eki',
        '_fbp': 'fb.1.1702537953632.793012134',
        '_bge_ci': 'BA1.1.1561390778.1702537956',
        '_gid': 'GA1.2.1079024401.1702895530',
        'AF_SYNC': '1703148103614',
        'tmr_detect': '0%7C1703226401115',
        '_ga_VEWNK2RRS2': 'GS1.1.1703226346.12.1.1703226401.0.0.0',
        '_ga': 'GA1.1.833772108.1702537936',
        '_ga_4X19GXYYF0': 'GS1.2.1703226407.9.0.1703226407.60.0.0',
        '_ga_WBJR2T2B3R': 'GS1.2.1703226408.12.0.1703226408.60.0.0',
        '_ga_6G3GYJ0KG3': 'GS1.2.1703226408.12.0.1703226408.0.0.0',
    }
    # Отправляемый набор headers
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'sid=3r364v2v8th6t5g5bnorks8si6; __utmzz=utmcsr=(direct)|utmcmd=(none)|utmccn=(not set)|utmcct=(not set)|utmctr=(not set); __utmzzses=1; cookie_test=1; _ym_uid=1702537939809069726; _ym_d=1702537939; tmr_lvid=3a5d8619f82987879aa67a9ff8f131b5; tmr_lvidTS=1702537942411; afUserId=3c2c8af7-3cf8-4db5-b7a9-30e4772cab11-p; _tt_enable_cookie=1; _ttp=bEX8HFrw5QTol9_wxCSVYFy_Eki; _fbp=fb.1.1702537953632.793012134; _bge_ci=BA1.1.1561390778.1702537956; _gid=GA1.2.1079024401.1702895530; AF_SYNC=1703148103614; tmr_detect=0%7C1703226401115; _ga_VEWNK2RRS2=GS1.1.1703226346.12.1.1703226401.0.0.0; _ga=GA1.1.833772108.1702537936; _ga_4X19GXYYF0=GS1.2.1703226407.9.0.1703226407.60.0.0; _ga_WBJR2T2B3R=GS1.2.1703226408.12.0.1703226408.60.0.0; _ga_6G3GYJ0KG3=GS1.2.1703226408.12.0.1703226408.0.0.0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
        'sec-ch-ua': '"Opera";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    # Получаем ответ в виде текста
    response = requests.get(url_stat, cookies=cookies, headers=headers).text
    # Обрабатываем ответ библиотекой для парсинга
    soup = BeautifulSoup(response, 'lxml')
    # Возвращаем полученный результат
    return(soup)

# Функция формирования массива с информацией о личных встречах
def get_ochnye_vstrechi(mass_stat):
    # Создаем пустой массив
    ov_mass = []
    # Цикл переборки массива, переданного в функцию
    # Пробегаем циклом по тэгу <table>
    for body in mass_stat.find_all('table', class_ = ''):
        # Пробегаем циклом по тэгу <tr>
        for tr in body.find_all('tr', class_ = ''):
            # Пробегаем циклом по тэгу <td> в классе 'score'
            for ted in tr.find_all('td', class_ = 'score'):
                # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
                td = ted.get_text()
                # Парсим содержимое тега
                td1 = td.split(' (')[1]
                # Удаляем все знаки ' в строке
                td2 = td1.replace(')', "")
                # Удаляем все знаки , в строке
                td3 = td2.replace(',', "")
                # Добавляем полученный результат в подготовленный нами массив
                ov_mass.append(td3)
    # Возвращаем готовый массив 
    return(ov_mass)


# Функция получения дат последних игр соперников
def get_date_last_vstrechi(mass_stat):
    # Создаем пустой массив
    lv_date_mass = []
    # Цикл переборки массива, переданного в функцию
    # Пробегаем циклом по тэгу <table>
    for body in mass_stat.find_all('table', class_ = 'ev-mstat-tbl'):
        # Пробегаем циклом по тэгу <tr>
        for tr in body.find_all('tr', class_ = ''):
            # Пробегаем циклом по тэгу <td> в классе 'score'
            for ted in tr.find_all('td', class_ = 'date'):
                # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
                td = ted.get_text()
                
                # Добавляем полученный результат в подготовленный нами массив
                lv_date_mass.append(td)
    # Возвращаем готовый массив 
    return(lv_date_mass)


# Функция формирования массива с информацией о последних играх соперников
def get_last_vstrechi(mass_stat):
    # Создаем пустой массив
    lv_mass = []
    # Цикл переборки массива, переданного в функцию
    # Пробегаем циклом по тэгу <table>
    for body in mass_stat.find_all('table', class_ = 'ev-mstat-tbl'):
        # Пробегаем циклом по тэгу <tr>
        for tr in body.find_all('tr', class_ = ''):
            # Пробегаем циклом по тэгу <td> в классе 'score'
            for ted in tr.find_all('td', class_ = 'ev-mstat-sc'):
                # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
                td = ted.get_text()
                # Парсим содержимое тега
                td1 = td.split(' (')[1]
                # Удаляем все знаки ' в строке
                td2 = td1.replace(')', "")
                # Удаляем все знаки , в строке
                td3 = td2.replace(',', "")
                # Добавляем полученный результат в подготовленный нами массив
                lv_mass.append(td3)
    # Возвращаем готовый массив 
    return(lv_mass)


def get_last_v_1_set(lv_mass):
    set1lastv = []
    for lvmass in lv_mass:
        set1 = lvmass.split(' ')[0]
        set1lastv.append(set1)
    return set1lastv





# Функция получения количества партий с тоталом меньше 18.5 из переданного массива с суммами очков по партиям
def get_kol_menshe(summ_point):
    # Создаем переменную и присваиваем ей 0
    i = 0
    # Цикл переборки полученного массива
    for bolshe in summ_point:
        # Проверяем число полученное циклом
        if int(bolshe) <= 18:
            # Если условие выполняется прибавляем 1 к переменной
            i+=1
    # Возвращаем полученное количество
    return (i)

# Функция получения количества партий с тоталом больше 18.5 из переданного массива с суммами очков по партиям
def get_kol_bolshe(summ_point):
    # Создаем переменную и присваиваем ей 0
    i = 0
    # Цикл переборки полученного массива
    for bolshe in summ_point:
        # Проверяем число полученное циклом
        if int(bolshe) >= 19:
            # Если условие выполняется прибавляем 1 к переменной
            i+=1
            # Возвращаем полученное количество
    return (i)


# Функцтя формирования массива с суммами очков по партиям
def summ_point_set_mass(set_mass):
    # Создаем пустой массив
    summ_set_mass = []
    # Цикл переборки полученного массива
    for si in (set_mass):
        
        # Обработка исключений счетчика сумм
        try:
            # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
            s1 = si.split(':')[0] 
            # Парсим строку по заданному символу и присваиваем нужную часть строки переменной           
            s2 = si.split(':')[1]    
            # Получаем сумму переменных    
            summ = int(s1) + int(s2)
            # Добавляем полученную сумму в массив
            summ_set_mass.append(summ)
        # Выполняется в случае возникновения исключения
        except:
            # Пропустить - ничего не выполнять
            pass
    # Возвращаем полученный массив значений
    return(summ_set_mass)

# Функция формирования массива со счетом первых партий очных встреч
def get_o_v_1set(ov_mass):
    # Создаем пустой массив
    ov_1set_mass = []
    # Цикл переборки полученного массива
    for set_1 in ov_mass:
        # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
        set_1_1 = set_1.split(' ')[0]
        # Добавляем полученное значение в массив
        ov_1set_mass.append(set_1_1)
    # Возвращаем полученный массив значений    
    return(ov_1set_mass)
    
# Функция формирования массива со счетом вторых партий очных встреч
def get_o_v_2set(ov_mass):
    # Создаем пустой массив
    ov_2set_mass = []
    # Цикл переборки полученного массива
    for set_2 in ov_mass:
        # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
        set_2_1 = set_2.split(' ')[0]
        # Добавляем полученное значение в массив
        ov_2set_mass.append(set_2_1)
    # Возвращаем полученный массив значений
    return(ov_2set_mass)

# Функция формирования массива со счетом третьих партий очных встреч
def get_o_v_3set(ov_mass):
    # Создаем пустой массив
    ov_3set_mass = []
    # Цикл переборки полученного массива
    for set_3 in ov_mass:
        # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
        set_3_1 = set_3.split(' ')[2]
        # Добавляем полученное значение в массив
        ov_3set_mass.append(set_3_1)
    # Возвращаем полученный массив значений
    return(ov_3set_mass)

# Функция формирования массива со счетом четвертых партий очных встреч
def get_o_v_4set(ov_mass):
    # Создаем пустой массив
    ov_4set_mass = []
    # Цикл переборки полученного массива
    for set_4 in ov_mass:
        # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
        set_4_1 = set_4.split(' ')[3]
        # Добавляем полученное значение в массив
        ov_4set_mass.append(set_4_1)
    # Возвращаем полученный массив значений
    return(ov_4set_mass)

# Функция формирования массива со счетом пятых партий очных встреч
def get_o_v_5set(ov_mass):
    # Создаем пустой массив
    ov_5set_mass = []
    # Цикл переборки полученного массива
    for set_5 in ov_mass:
        # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
        set_5_1 = set_5.split(' ')[3]
        # Добавляем полученное значение в массив
        ov_5set_mass.append(set_5_1)
    # Возвращаем полученный массив значений
    return(ov_5set_mass)

# Функция подсчета количества очных встреч
def kol_ochnyh_vstrech(ov_mass):
    # Создаем переменную и присваиваем ей 0
    i = 0
    # Цикл переборки полученного массива
    for vstrecha in ov_mass:
        # Прибавляем 1 к переменной при пробегании массива
        i = i + 1
    # Возвращаем полученный массив значений
    return(i)



# Функция получения количества игр с тремя партиями
def kol_game_3_sets(lv_mass):
    # Создаем пустой массив
    
    g = 0
    # Цикл переборки полученного массива
    for game in lv_mass:
        game_mass = []
        try:
            set = game.split(' ')[0]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[1]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[2]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[3]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[4]
            
            game_mass.append(set)
        except:
            pass
        
        i = 0
        sets_mass = []
        for sets in game_mass:
            
            
            if ':' in sets:
                i += 1
            
        if i == 3:
            g += 1

        
    # Возвращаем полученный массив значений
    return(g)

# Функция получения количества игр с 4 партиями
def kol_game_4_sets(lv_mass):
    # Создаем пустой массив
    
    g = 0
    # Цикл переборки полученного массива
    for game in lv_mass:
        game_mass = []
        try:
            set = game.split(' ')[0]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[1]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[2]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[3]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[4]
            
            game_mass.append(set)
        except:
            pass
        
        i = 0
        sets_mass = []
        for sets in game_mass:
            
            
            if ':' in sets:
                i += 1
            
        if i == 4:
            g += 1

        
    # Возвращаем полученный массив значений
    return(g)

# Функция получения количества игр с 5 партиями
def kol_game_5_sets(lv_mass):
    # Создаем пустой массив
    
    g = 0
    # Цикл переборки полученного массива
    for game in lv_mass:
        game_mass = []
        try:
            set = game.split(' ')[0]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[1]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[2]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[3]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[4]
            
            game_mass.append(set)
        except:
            pass
        
        i = 0
        sets_mass = []
        for sets in game_mass:
            
            
            if ':' in sets:
                i += 1
            
        if i == 5:
            g += 1

        
    # Возвращаем полученный массив значений
    return(g)


def kol_set_18_5_bolshe_1set(lv_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in lv_mass:
        
        try:
            set = game.split(' ')[0]
            
            set_mass.append(set)
        except:
            pass
        
    # print(set_mass)
    sum_point = summ_point_set_mass(set_mass)
    i = 0
    for sum_set_point in sum_point:
        if sum_set_point >= 19:
            i+=1
        
    # Возвращаем полученный массив значений
    return(i)

def kol_set_18_5_menshe_1set(lv_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in lv_mass:
        
        try:
            set = game.split(' ')[0]
            
            set_mass.append(set)
        except:
            pass
        
            
            
    # print(set_mass)
    sum_point = summ_point_set_mass(set_mass)
    i = 0
    for sum_set_point in sum_point:
        if sum_set_point <= 18:
            i+=1
        
    # Возвращаем полученный массив значений
    return(i)

def kol_set_18_5_bolshe_2set(lv_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in lv_mass:
        
        try:
            set = game.split(' ')[1]
            
            set_mass.append(set)
        except:
            pass
        
    # print(set_mass)
    sum_point = summ_point_set_mass(set_mass)
    i = 0
    for sum_set_point in sum_point:
        if sum_set_point >= 19:
            i+=1
        
    # Возвращаем полученный массив значений
    return(i)

def kol_set_18_5_menshe_2set(lv_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in lv_mass:
        
        try:
            set = game.split(' ')[1]
            
            set_mass.append(set)
        except:
            pass
        
            
            
    # print(set_mass)
    sum_point = summ_point_set_mass(set_mass)
    i = 0
    for sum_set_point in sum_point:
        if sum_set_point <= 18:
            i+=1
        
    # Возвращаем полученный массив значений
    return(i)

def kol_set_18_5_bolshe_3set(lv_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in lv_mass:
        
        try:
            set = game.split(' ')[2]
            
            set_mass.append(set)
        except:
            pass
        
    # print(set_mass)
    sum_point = summ_point_set_mass(set_mass)
    i = 0
    for sum_set_point in sum_point:
        if sum_set_point >= 19:
            i+=1
        
    # Возвращаем полученный массив значений
    return(i)

def kol_set_18_5_menshe_3set(lv_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in lv_mass:
        
        try:
            set = game.split(' ')[2]
            
            set_mass.append(set)
        except:
            pass
        
            
            
    # print(set_mass)
    sum_point = summ_point_set_mass(set_mass)
    i = 0
    for sum_set_point in sum_point:
        if sum_set_point <= 18:
            i+=1
        
    # Возвращаем полученный массив значений
    return(i)

def kol_set_19_bolshe(ov_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in ov_mass:
        
        try:
            set = game.split(' ')[0]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[1]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[2]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[3]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[4]
            
            set_mass.append(set)
        except:
            pass
    # print(set_mass)
    sum_point = summ_point_set_mass(set_mass)
    i = 0
    for sum_set_point in sum_point:
        if sum_set_point > 19:
            i+=1
        
    # Возвращаем полученный массив значений
    return(i)

def kol_set_19_ravno(ov_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in ov_mass:
        
        try:
            set = game.split(' ')[0]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[1]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[2]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[3]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[4]
            
            set_mass.append(set)
        except:
            pass
    # print(set_mass)
    sum_point = summ_point_set_mass(set_mass)
    i = 0
    for sum_set_point in sum_point:
        if sum_set_point == 19:
            i+=1
        
    # Возвращаем полученный массив значений
    return(i)

def kol_set_18_ravno(ov_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in ov_mass:
        
        try:
            set = game.split(' ')[0]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[1]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[2]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[3]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[4]
            
            set_mass.append(set)
        except:
            pass
    # print(set_mass)
    sum_point = summ_point_set_mass(set_mass)
    i = 0
    for sum_set_point in sum_point:
        if sum_set_point == 18:
            i+=1
        
    # Возвращаем полученный массив значений
    return(i)

def kol_set_18_menshe(ov_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in ov_mass:
        
        try:
            set = game.split(' ')[0]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[1]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[2]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[3]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[4]
            
            set_mass.append(set)
        except:
            pass
    
    sum_point = summ_point_set_mass(set_mass)
    i = 0
    for sum_set_point in sum_point:
        if sum_set_point < 18:
            i+=1
        
    # Возвращаем полученный массив значений
    return(i)
    
    # body2 = body1.replace('[', "")
    # body3 = body2.replace(']', "")
    # print(body3)
    # body2 = body1.find_all('table', class_ = '')
    # score = body3.find_all('td', class_ = 'score').get_text()
    

    # # score = body1.find_all('td', class_ = 'score').get_text()
    # # print(score)
    # # for bod in body1.find_all('tr', class_ = ''):
    # #     for ter in bod.finde_all('td', class_ = 'score'):
    # #         score = ter.get_text()
    # #         print(score)
            
            
    # print(score)
    
    
    # try:
    #     table = body.find_all('table', class_ = '')
    # except:
    #     print('Не удалось выбрать table')
    
    # o_v_2 = o_v_1.find_all('table', class_ = '')
    
    
        
        # print(tables)
        
        # for item in data.find_all('td', class_ = 'booker'):
                        
        #     for a in item.find_all('a', class_ = ''):
        #         buk = a.get_text()
                

        #     for span in item.find_all('span', class_ = 'minor'):
        #         sport = span.get_text()
    # print('')
    # print('Очные встречи')
    # print(body1)
    # print(mass_stat)