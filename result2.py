from datetime import datetime
import schedule
import time
import requests
from datetime import timedelta
from telegram import send_telegram
from telegramchannel import send_channel
def igrau(resultline):
    # print(result)
    
    for period in resultline['Value']:
        try:
            idl = period['I']
            o21 = period['SC']['PS'][2]['Value']['S1']
            o22 = period['SC']['PS'][2]['Value']['S2']
            prov_result(period,idl)
        except:
            pass
            # if (cps == '3-я Партия'):
                # print('3-я Партия')
            # idlive = period['I']
                # print(idlive)
            
                
        
                
def prov_result(period,idl):
    
    liga = period['L']
    liga1 = liga.split('.')[0]
    
    with open('db.txt','r') as file:
                                
        for item in file.readlines():
            
            line = item.strip()
            print(line)
            idid = line.split('-')[0]
            print(idid)
            print(idl)
            # if ('Лига Про'== liga1) or ('Челленджер'==liga1) or ('Кубок ТТ' == liga1):  
            # print('Лига подходит')            
            if str(idl) == idid:
                print('Была сделана ставка')    
                stavka = line.split('-')[-1]
                print (stavka)
                if str(stavka) == 'TB':
                    print('Проверяем результат ТБ')
                    o21 = period['SC']['PS'][1]['Value']['S1']
                    o22 = period['SC']['PS'][1]['Value']['S2']
                    if int(o21) + int(o22) >= 19:
                        print('ТБ есть. Отправляется сообщение')
                        message = {}
                                                
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                                
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = '2 сет: ТБ 18.5'
                        message['RES'] = 'Ставка зашла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                    if int(o21) + int(o22) <= 18:
                        print('ТБ нет. Отправляется сообщение')
                        message = {}
                                                
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                                
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = '2 сет: ТБ 18.5'
                                
                        message['RES'] = 'Ставка проиграла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                        
                if str(stavka) == 'TM':
                    print('Проверяем результат ТБ')
                    o21 = period['SC']['PS'][1]['Value']['S1']
                    o22 = period['SC']['PS'][1]['Value']['S2']
                    if int(o21) + int(o22) <= 18:
                        print('ТM есть. Отправляется сообщение')
                        message = {}
                                                
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                                
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = '2 сет: ТM 18.5'
                        message['RES'] = 'Ставка зашла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                    if int(o21) + int(o22) >= 19:
                        print('ТM нет. Отправляется сообщение')
                        message = {}
                                                
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                                
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = '2 сет: ТM 18.5'
                                
                        message['RES'] = 'Ставка проиграла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                
                
                if str(stavka) == 'F1':
                    print('Проверяем результат Ф1')
                    o21 = period['SC']['PS'][1]['Value']['S1']
                    o22 = period['SC']['PS'][1]['Value']['S2']
                    if int(o21) > int(o22):
                        print('Ф1 есть. Отправляется сообщение')
                        message = {}
                                                
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                                
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = '2 сет: П1'
                        message['RES'] = 'Ставка зашла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                    else:
                        print('Ф1 нет. Отправляется сообщение')
                        message = {}
                                                
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                                
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = '2 сет: П1'
                                
                        message['RES'] = 'Ставка проиграла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                if str(stavka) == 'F2':
                    print('Проверяем результат Ф2')
                    o21 = period['SC']['PS'][1]['Value']['S1']
                    o22 = period['SC']['PS'][1]['Value']['S2']
                    if int(o22) > int(o21):
                        print('Ф2 есть. Отправляется сообщение')
                        message = {}
                                                
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                                
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = '2 сет: П2'
                        message['RES'] = 'Ставка зашла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                    else:
                        print('Ф2 нет. Отправляется сообщение')
                        message = {}
                                                
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                                
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = '2 сет: П2'
                                
                        message['RES'] = 'Ставка проиграла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                                    

def format_message_result(message,idl,period):
    with open('sr.txt','r') as file:
        list1 = []                                            
        for item in file.readlines():
            line = item.strip()
            
                                                # print(idid)
            list1.append(line)
                            # ln = int(line)
            file.close()
                                            
                                        
        print(list1)
        if str(idl) in list1:
            print('Событие уже есть ')
                
        else:
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
            except:
                print('Не удалось получить статистику')
                RDIV1 = 'Нет'
                RDIV2 = 'Нет'
                PVSPV1 = 'Нет'
                PVSPV2 = 'Нет'
                ILVV1 = 'Нет'
                ILVV2 = 'Нет'

            try:
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
            except:
                print('Не удалось прочитать масссив')
                RDIV1 = 'Нет'
                RDIV2 = 'Нет'
                PVSPV1 = 'Нет'
                PVSPV2 = 'Нет'
                ILVV1 = 'Нет'
                ILVV2 = 'Нет'                                    
            
            with open('sr.txt','a') as file:
                
                file.write(f'\n{idl}')          
                file.close()
                
                SN, L, O1, O2,S,CPS,S1,S2,S21,S22,ST,RES = message.values()
                SP = S + 3*60*60
                Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')
                if RES == 'Ставка зашла':
                    mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                                f'\U0001F3C6 {L} \n' \
                                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                                        f'\U0001F9FE 2- Партия:{S21} - {S22}\n' \
                                f'\n' \
                                    f'\U0001F9FE Статистика:\n' \
                        f'\U0001F9FE Рейтинг:{RDIV1}-{RDIV2}\n' \
                            f'\U0001F9FE Л.встречи:{ILVV1}-{ILVV2}\n' \
                                f'\U0001F9FE Свои подачи:{PVSPV1}-{PVSPV2}\n' \
                                    \
                                    f'\U0001F4B5 Ставка: {ST} \n' \
                                        f'\U0001F4B5 Результат: {RES} \U0001F37B \U00002705	\U00002705 \U00002705 \U0001F37B \n' \
                                        f'\n' \
                    
                    send_telegram(mess)
                    send_channel(mess)

                    # print('send')            
                    print(mess) 
                                            
                if RES == 'Ставка проиграла':
                    mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                                f'\U0001F3C6 {L} \n' \
                                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                                        f'\U0001F9FE 2- Партия:{S21} - {S22}\n' \
                                f'\n' \
                                    \
                                    f'\U0001F4B5 Ставка: {ST} \n' \
                                        f'\U0001F4B5 Результат: {RES} \U0001F36D \U0000274C	\U0000274C \U0000274C \U0001F36D \n' \
                                        f'\n' \
                
                    send_telegram(mess)
                    send_channel(mess)

                    # print('send')            
                    print(mess)          

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
        resultline = response.json()
        # print(result)
        igrau(resultline)
    except:
        pass
    
if __name__ == '__main__':
    main()
schedule.every(15).seconds.do(main)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
