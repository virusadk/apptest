from datetime import datetime
import schedule
# import time
import requests
from datetime import timedelta
from telegram import send_telegram
from telegramchannel import send_channel

def format_message_fora(message,period):
    try:
        
        sgi = period['SGI']
    except:
        print('Нет SGI') 
    try:

    

        headers = {
            'authority': 'eventsstat.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://eventsstat.com/statisticpopup/game/10/6347c72ff75a663f6947def9/main?hs=1&fh=1&ln=ru&w=899&rtl=0&r=51&g=44&tz=3&geo=22&mh=200',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-statistic-api': '1',
        }

        params = {
            'gameId': sgi,
            'ln': 'ru',
            'partner': '51',
            'geo': '22',
        }

        response = requests.get('https://eventsstat.com/sf/Game', params=params, headers=headers)
        game_stat = response.json()
    
        for gs in game_stat['RTS']:
            TT = gs['TT']
            try:
                
                if TT == 'Рейтинг в день игры':
                    RDIV1 = gs['V1']
                    RDIV2 = gs['V2']
                    print(TT,RDIV1,RDIV2)
            except:
                RDIV1 = 'Нет'
                RDIV2 = 'Нет'
            try:
                if TT == 'Процент выигрыша своей подачи':
                    PVSPV1 = gs['V1']
                    PVSPV2 = gs['V2']
                    print(TT,PVSPV1,PVSPV2)
            except:
                PVSPV1 = 'Нет'
                PVSPV2 = 'Нет'
            try:
                if TT == 'История личных встреч':
                    ILVV1 = gs['V1']
                    ILVV2 = gs['V2']
                    print(TT,ILVV1,ILVV2)
            except:
                ILVV1 = 'Нет'
                ILVV2 = 'Нет' 
        # print(gs)
        # print (V1,'-',V2) 
        SN, L, O1, O2,S,CPS,S1,S2,ST = message.values()
        SP = S + 3*60*60
        Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')
   
        mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                f'\U0001F3C6 {L} \n' \
                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                f'\n' \
                    f'\U0001F9FE Статистика:\n' \
                        f'\U0001F9FE Рейтинг:{RDIV1}-{RDIV2}\n' \
                            f'\U0001F9FE Л.встречи:{ILVV1}-{ILVV2}\n' \
                                f'\U0001F9FE Свои подачи:{PVSPV1}-{PVSPV2}\n' \
                     \
                    f'\U0001F4B5 Ставка: 2-сет {ST}\n' \
                        f'\n' \
               
                
            
    
    
        send_telegram(mess)
        send_channel(mess)
        # print('send')            
        print(mess)
    except:
        pass
        
                          
def format_message_pred(message,period):
    try:
        
        sgi = period['SGI']
    except:
        print('Нет SGI') 
    try:

    

        headers = {
            'authority': 'eventsstat.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://eventsstat.com/statisticpopup/game/10/6347c72ff75a663f6947def9/main?hs=1&fh=1&ln=ru&w=899&rtl=0&r=51&g=44&tz=3&geo=22&mh=200',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-statistic-api': '1',
        }

        params = {
            'gameId': sgi,
            'ln': 'ru',
            'partner': '51',
            'geo': '22',
        }

        response = requests.get('https://eventsstat.com/sf/Game', params=params, headers=headers)
        game_stat = response.json()
    
        for gs in game_stat['RTS']:
            TT = gs['TT']
            try:
                
                if TT == 'Рейтинг в день игры':
                    RDIV1 = gs['V1']
                    RDIV2 = gs['V2']
                    print(TT,RDIV1,RDIV2)
            except:
                RDIV1 = 'Нет'
                RDIV2 = 'Нет'
            try:
                if TT == 'Процент выигрыша своей подачи':
                    PVSPV1 = gs['V1']
                    PVSPV2 = gs['V2']
                    print(TT,PVSPV1,PVSPV2)
            except:
                PVSPV1 = 'Нет'
                PVSPV2 = 'Нет'
            try:
                if TT == 'История личных встреч':
                    ILVV1 = gs['V1']
                    ILVV2 = gs['V2']
                    print(TT,ILVV1,ILVV2)
            except:
                ILVV1 = 'Нет'
                ILVV2 = 'Нет' 
        # print(gs)
        # print (V1,'-',V2) 
        SN, L, O1, O2,S,CPS,S1,S2,ST = message.values()
        SP = S + 3*60*60
        Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')
   
        mess =  f'\U0001F4B5 {ST}\n' \
                f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                f'\U0001F3C6 {L} \n' \
                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                f'\n' \
                    f'\U0001F9FE Статистика:\n' \
                        f'\U0001F9FE Рейтинг:{RDIV1}-{RDIV2}\n' \
                            f'\U0001F9FE Л.встречи:{ILVV1}-{ILVV2}\n' \
                                f'\U0001F9FE Свои подачи:{PVSPV1}-{PVSPV2}\n' \
                     \
                    \
                        f'\n' \
               
                
            
    
    
        send_telegram(mess)
        send_channel(mess)
        # print('send')            
        print(mess)
    except:
        pass
    
   

def format_message(message,period): 
    
    try:
        
        sgi = period['SGI']
    except:
        print('Нет SGI') 
    try:

    

        headers = {
            'authority': 'eventsstat.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://eventsstat.com/statisticpopup/game/10/6347c72ff75a663f6947def9/main?hs=1&fh=1&ln=ru&w=899&rtl=0&r=51&g=44&tz=3&geo=22&mh=200',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-statistic-api': '1',
        }

        params = {
            'gameId': sgi,
            'ln': 'ru',
            'partner': '51',
            'geo': '22',
        }

        response = requests.get('https://eventsstat.com/sf/Game', params=params, headers=headers)
        game_stat = response.json()
    
        for gs in game_stat['RTS']:
            TT = gs['TT']
            try:
                
                if TT == 'Рейтинг в день игры':
                    RDIV1 = gs['V1']
                    RDIV2 = gs['V2']
                    print(TT,RDIV1,RDIV2)
            except:
                RDIV1 = 'Нет'
                RDIV2 = 'Нет'
            try:
                if TT == 'Процент выигрыша своей подачи':
                    PVSPV1 = gs['V1']
                    PVSPV2 = gs['V2']
                    print(TT,PVSPV1,PVSPV2)
            except:
                PVSPV1 = 'Нет'
                PVSPV2 = 'Нет'
            try:
                if TT == 'История личных встреч':
                    ILVV1 = gs['V1']
                    ILVV2 = gs['V2']
                    print(TT,ILVV1,ILVV2)
            except:
                ILVV1 = 'Нет'
                ILVV2 = 'Нет' 
        # print(gs)
        # print (V1,'-',V2) 
        
    
        SN, L, O1, O2,S,CPS,S1,S2,ST = message.values()
        SP = S + 3*60*60
        Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')
   
        mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                f'\U0001F3C6 {L} \n' \
                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                f'\n' \
                    f'\U0001F9FE Статистика:\n' \
                        f'\U0001F9FE Рейтинг:{RDIV1}-{RDIV2}\n' \
                            f'\U0001F9FE Л.встречи:{ILVV1}-{ILVV2}\n' \
                                f'\U0001F9FE Свои подачи:{PVSPV1}-{PVSPV2}\n' \
                     \
                    f'\U0001F4B5 Ставка: 2-сет {ST} 18.5\n' \
                        f'\n' \
               
                
            
    
    
        send_telegram(mess)
        send_channel(mess)
        # print('send')            
        print(mess)
    except:
        pass
        
    
def prov_pobed(pobeda,idlive,period,sgi):
        
    try:

    

        headers = {
            'authority': 'eventsstat.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://eventsstat.com/statisticpopup/game/10/6347c72ff75a663f6947def9/main?hs=1&fh=1&ln=ru&w=899&rtl=0&r=51&g=44&tz=3&geo=22&mh=200',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-statistic-api': '1',
        }

        params = {
            'gameId': sgi,
            'ln': 'ru',
            'partner': '51',
            'geo': '22',
        }

        response = requests.get('https://eventsstat.com/sf/Game', params=params, headers=headers)
    except:
        pass
    game_stat = response.json()
    try:
        for gs in game_stat['RTS']:
            TT = gs['TT']
            if TT == 'Рейтинг в день игры':
                RDIV1 = gs['V1']
                RDIV2 = gs['V2']
                print(TT,RDIV1,RDIV2)
            if TT == 'Процент выигрыша своей подачи':
                PVSPV1 = gs['V1']
                PVSPV2 = gs['V2']
                print(TT,PVSPV1,PVSPV2)
            if TT == 'История личных встреч':
                ILVV1 = gs['V1']
                ILVV2 = gs['V2']
                print(TT,ILVV1,ILVV2)
        # print(gs)
        # print (V1,'-',V2) 
    
                          
        with open('outs.txt','r') as file:
                                    
            for item in file.readlines():
                line = item.strip()
                    # print(line)
                idid = line.split('-')[0]
                    
                    
                if str(idlive) == idid:
                    
                    out = line.split('-')[-1]
                    print(out)
                    print(pobeda)
                    if ((str(out) == 'out1') and (str(pobeda) == 'p1') and (int(RDIV2) - int(RDIV1) > 50) and (int(ILVV2) - int(ILVV1) >= 5)) or ((str(out) == 'out1') and (str(pobeda) == 'p1') and (int(ILVV2) + int(ILVV1) == 0) and (int(RDIV2)-int(RDIV1)>=80)) or ((str(out) == 'out1') and (str(pobeda) == 'p1') and (int(ILVV2) - int(ILVV1) >= 5)):
                        print('Победил оутсайдер')
                            # print(totalline)
                        try:
                            listdb = []
                            with open('db.txt','r') as file:
                                                                
                                    for item in file.readlines():
                                        line = item.strip()
                                        iddb = line.split('-')[0]                
                                                            # print(idid)
                                        listdb.append(iddb)
                                                            # ln = int(line)
                                        file.close()
                                        print(listdb)    
                        except:
                            print('невозможно прочитать db.txt')
                        
                    
                                    
                                    
                        if str(idlive) in listdb:
                            print('Событие было отправлено')
                                        
                        else:
                            message = {}
                                            
                            message['SN'] = period['SN']
                            message['L'] = period['L']
                            message['O1'] = period['O1']
                            message['O2'] = period['O2']
                            message['S'] = period['S']
                            message['CPS'] = period['SC']['CPS']
                            message['S1'] = period['SC']['PS'][0]['Value']['S1']
                            message['S2'] = period['SC']['PS'][0]['Value']['S2']
                            
                            message['ST'] = 'П2'
                            format_message_fora(message,period)
                            print('Отправлено на форматирование') 
                            try:    
                                with open('db.txt','a') as file:
                                    file.write(f'\n{idlive}-F2')            
                                    file.close()
                                    print('Событие записано в db.txt') 
                            except:
                                print('Невозможно записать в файл db.txt')
                                
                                
                    
                    if ((str(out) == 'out2') and (str(pobeda) == 'p2') and (int(RDIV1) - int(RDIV2) > 50) and (int(ILVV1) - int(ILVV2) >= 5)) or ((str(out) == 'out2') and (str(pobeda) == 'p2') and (int(ILVV2) + int(ILVV1) == 0) and (int(RDIV1)-int(RDIV2)>=80)) or ((str(out) == 'out2') and (str(pobeda) == 'p2') and (int(ILVV1) - int(ILVV2) >= 5)):
                        print('Победил оутсайдер')
                        try:
                            listdb = []
                            with open('db.txt','r') as file:
                                                                
                                    for item in file.readlines():
                                        line = item.strip()
                                        iddb = line.split('-')[0]                
                                                            # print(idid)
                                        listdb.append(iddb)
                                                            # ln = int(line)
                                        file.close()
                                        print(listdb)    
                        except:
                            print('невозможно прочитать db.txt')
                        
                    
                                    
                                    
                        if str(idlive) in listdb:
                            print('Событие было отправлено')
                                        
                        else:
                            message = {}
                                            
                            message['SN'] = period['SN']
                            message['L'] = period['L']
                            message['O1'] = period['O1']
                            message['O2'] = period['O2']
                            message['S'] = period['S']
                            message['CPS'] = period['SC']['CPS']
                            message['S1'] = period['SC']['PS'][0]['Value']['S1']
                            message['S2'] = period['SC']['PS'][0]['Value']['S2']
                            
                            message['ST'] = 'П1'
                            format_message_fora(message,period)
                            print('Отправлено на форматирование') 
                            try:    
                                with open('db.txt','a') as file:
                                    file.write(f'\n{idlive}-F1')            
                                    file.close()
                                    print('Событие записано в db.txt') 
                            except:
                                print('Невозможно записать в файл db.txt')        
            file.close() 
    except:
        print('Не удалось')                 
                                
                            
                            
                
    

def poisk_pred_total(idlive,period):
    
    with open('retro.txt','r') as file:
                                
        for item in file.readlines():
            line = item.strip()
                # print(line)
            
                
                
            if str(idlive) == line:
                print('Событие есть в retro.txt')
                try:
                    listdb = []
                    with open('db.txt','r') as file:
                                                        
                            for item in file.readlines():
                                line = item.strip()
                                iddb = line.split('-')[0]            
                                                   # print(idid)
                                listdb.append(iddb)
                                                    # ln = int(line)
                                file.close()
                                print(listdb)    
                except:
                    print('невозможно прочитать db.txt')
                
               
                            
                            
                if str(idlive) in listdb:
                        print('Событие было отправлено')
                                
                else:
                    message = {}
                                    
                    message['SN'] = period['SN']
                    message['L'] = period['L']
                    message['O1'] = period['O1']
                    message['O2'] = period['O2']
                    message['S'] = period['S']
                    message['CPS'] = period['SC']['CPS']
                    message['S1'] = period['SC']['PS'][0]['Value']['S1']
                    message['S2'] = period['SC']['PS'][0]['Value']['S2']
                    message['ST'] = 'ТБ'
                    format_message(message,period)
                    print('Отправлено на форматирование') 
                    try:    
                        with open('db.txt','a') as file:
                            file.write(f'\n{idlive}-TB')            
                            file.close()
                            print('Событие записано в db.txt') 
                    except:
                        print('Невозможно записать в файл db.txt')
                    file.close() 
            
    with open('retrom.txt','r') as file:
                    
        for item in file.readlines():
            line = item.strip()
                # print(line)
            
                
                
            if str(idlive) == line:
                print('Событие есть в retrom.txt')
                try:
                    listdb = []
                    with open('db.txt','r') as file:
                                                        
                            for item in file.readlines():
                                line = item.strip()
                                iddb = line.split('-')[0] 
                                            
                                                    # print(idid)
                                listdb.append(iddb)
                                                    # ln = int(line)
                                file.close()
                                print(listdb)    
                except:
                    print('невозможно прочитать db.txt')
                
            
                            
                            
                if str(idlive) in listdb:
                        print('Событие было отправлено')
                                
                else:
                    message = {}
                                    
                    message['SN'] = period['SN']
                    message['L'] = period['L']
                    message['O1'] = period['O1']
                    message['O2'] = period['O2']
                    message['S'] = period['S']
                    message['CPS'] = period['SC']['CPS']
                    message['S1'] = period['SC']['PS'][0]['Value']['S1']
                    message['S2'] = period['SC']['PS'][0]['Value']['S2']
                    message['ST'] = 'ТМ'
                    format_message(message,period)
                    print('Отправлено на форматирование') 
                    try:    
                        with open('db.txt','a') as file:
                            file.write(f'\n{idlive}-TM')            
                            file.close()
                            print('Событие записано в db.txt') 
                    except:
                        print('Невозможно записать в файл db.txt')
                    file.close() 
                    
                # except:
                    # print('Нет событий для сравнения')                
                       
    
def preduprezhdenie(idlive,period):
    with open('retro.txt','r') as file:
                                
        for item in file.readlines():
            line = item.strip()
                # print(line)
            
                
                
            if str(idlive) == line:
                print('Событие есть в retro.txt')
                try:
                    listdb = []
                    with open('pred.txt','r') as file:
                                                        
                            for item in file.readlines():
                                line = item.strip()
                                           
                                                   # print(idid)
                                listdb.append(line)
                                                    # ln = int(line)
                                file.close()
                                print(listdb)    
                except:
                    print('невозможно прочитать db.txt')
                
               
                            
                            
                if str(idlive) in listdb:
                        print('Предупреждение было отправлено')
                                
                else:
                    message = {}
                                    
                    message['SN'] = period['SN']
                    message['L'] = period['L']
                    message['O1'] = period['O1']
                    message['O2'] = period['O2']
                    message['S'] = period['S']
                    message['CPS'] = period['SC']['CPS']
                    message['S1'] = period['SC']['PS'][0]['Value']['S1']
                    message['S2'] = period['SC']['PS'][0]['Value']['S2']
                    message['ST'] = 'Возможно будет ставка'
                    format_message_pred(message,period)
                    print('Отправлено на форматирование') 
                    try:    
                        with open('pred.txt','a') as file:
                            file.write(f'\n{idlive}')            
                            file.close()
                            print('Событие записано в pred.txt') 
                    except:
                        print('Невозможно записать в файл db.txt')
                    file.close() 
    


                

def get_1x2(result):
    # print(result)
    
    for period in result['Value']:
        liga = period['L']
        liga1 = liga.split('.')[0]
        try:
            
            cps = period['SC']['CPS']
            if (cps == '1-я Партия'):
                print('Проверка счета первой партии')        
                try:    
                    nf = period['SC']['PS'][0]['Value']['NF']
                except:
                    print('Нет NF')
                if nf == '1-я Партия':
                    o1 = period['SC']['PS'][0]['Value']['S1']
                    o2 = period['SC']['PS'][0]['Value']['S2']
                    if (int(o1) + int(o2) <= 16) and (int(o1) == 9 or int(o2) == 9):
                        print('Счет меньше 16')
                        idlive = period['I']
                        preduprezhdenie(idlive,period)
                    
            if (cps == '2-я Партия'):
                print('Проверка счета первой партии')        
                try:    
                    nf = period['SC']['PS'][0]['Value']['NF']
                except:
                    print('Нет NF')
                if nf == '1-я Партия':
                    o1 = period['SC']['PS'][0]['Value']['S1']
                    o2 = period['SC']['PS'][0]['Value']['S2']
                    if (int(o1) + int(o2) <= 18) and (int(o1) == 11 or int(o2) == 11):
                        print('Счет меньше 16')
                        idlive = period['I']
                        poisk_pred_total(idlive,period)
                    # else:
                        # print('Счет больше 16')
                    if (int(o1) > int(o2)) and (int(o1) + int(o2) <= 19):
                        print('Победил 2')
                        idlive = period['I'] 
                        pobeda = 'p1'
                        sgi = period['SGI']
                        prov_pobed(pobeda,idlive,period,sgi)
                        print('передано в пров побед')
                    if (int(o1) < int(o2)) and (int(o1) + int(o2) <= 19):
                        print('Победил 1')
                        idlive = period['I'] 
                        pobeda = 'p2'
                        sgi = period['SGI']
                        prov_pobed(pobeda,idlive,period,sgi)
                        print('передано в пров побед')
           
                
        except:
            print('Нет cps')
                
        
        
            # print(o1,'-',o2)        
                
                # print('Передано на проверку')
                
                    
        # except:
            # print('Не удалось получить статус игры. Игра не может быть проверена на соответствие')
                    
            # igra_not_start(game) 
            # print('Игра не началась. Отправлена на проверку') 
        # else:
            # igra_start(game) 
            # print('Игра уже идет. Отправлена на проверку')                 
        
        
                          
        
        
            
            
        
    
    
    # print(message)
    # search_db(message)   
    # print('search_db')            
    

def main():
    
    try:

        params = {
        'sports': '10',
        'count': '50',
        'antisports': '188',
        'mode': '4',
        'country': '22',
        'partner': '51',
        'getEmpty': 'true',
        'noFilterBlockEvent': 'true',
        }



        response = requests.get('https://1xstavka.ru/LiveFeed/Get1x2_VZip', params=params)
        result = response.json()
        # print(result)
        get_1x2(result)
        print('Переданы данные LIVE')
    
    except:
        pass
    
if __name__ == '__main__':
    main()
schedule.every(15).seconds.do(main)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    # time.sleep(1) 
