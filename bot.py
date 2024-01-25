
from datetime import datetime
import schedule
import time
import requests
from datetime import timedelta
from telegram import send_telegram
from telegramchannel import send_channel

def format_message_fora(message): 
    
    SN, L, O1, O2,S,CPS,S1,S2,ST = message.values()
    SP = S + 3*60*60
    Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')
   
    mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                f'\U0001F3C6 {L} \n' \
                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                f'\n' \
                     \
                    f'\U0001F4B5 Ставка: 2-сет {ST} -2.5\n' \
                        f'\n' \
               
                
            
    
    
    send_telegram(mess)
    # send_channel(mess)
    # print('send')            
    print(mess)

def format_message(message): 
    
    SN, L, O1, O2,S,CPS,S1,S2 = message.values()
    SP = S + 3*60*60
    Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')
   
    mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                f'\U0001F3C6 {L} \n' \
                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                f'\n' \
                     \
                    f'\U0001F4B5 Ставка: 2-сет ТБ 18.5\n' \
                        f'\n' \
               
                
            
    
    
    send_telegram(mess)
    # send_channel(mess)
    # print('send')            
    print(mess)
    
def prov_pobed(pobeda,idlive,period):
        
    
    with open('outs.txt','r') as file:
                                
        for item in file.readlines():
            line = item.strip()
                # print(line)
            idid = line.split('-')[0]
                
                
            if str(idlive) == idid:
                
                out = line.split('-')[-1]
                print(out)
                print(pobeda)
                if (str(out) == 'out1') and (str(pobeda) == 'p1'): 
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
                        
                        message['ST'] = 'Ф2'
                        format_message_fora(message)
                        print('Отправлено на форматирование') 
                        try:    
                            with open('db.txt','a') as file:
                                file.write(f'\n{idlive}-F2')            
                                file.close()
                                print('Событие записано в db.txt') 
                        except:
                            print('Невозможно записать в файл db.txt')
                if (str(out) == 'out2') and (str(pobeda) == 'p2'): 
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
                        
                        message['ST'] = 'Ф1'
                        format_message_fora(message)
                        print('Отправлено на форматирование') 
                        try:    
                            with open('db.txt','a') as file:
                                file.write(f'\n{idlive}-F1')            
                                file.close()
                                print('Событие записано в db.txt') 
                        except:
                            print('Невозможно записать в файл db.txt')        
        file.close()                
    

def poisk_pred_total(idlive,period):
    
    with open('retro.txt','r') as file:
                                
        for item in file.readlines():
            line = item.strip()
                # print(line)
            
                
                
            if str(idlive) == line:
                
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
                    format_message(message)
                    print('Отправлено на форматирование') 
                    try:    
                        with open('db.txt','a') as file:
                            file.write(f'\n{idlive}-TB')            
                            file.close()
                            print('Событие записано в db.txt') 
                    except:
                        print('Невозможно записать в файл db.txt')
                
                # except:
                    # print('Нет событий для сравнения')                
        file.close()                
    



                

def get_1x2(result):
    # print(result)
    
    for period in result['Value']:
        liga = period['L']
        liga1 = liga.split('.')[0]
        try:
            
            cps = period['SC']['CPS']
            if (cps == '2-я Партия'):
                print('Проверка счета первой партии')        
                try:    
                    nf = period['SC']['PS'][0]['Value']['NF']
                except:
                    print('Нет NF')
                if nf == '1-я Партия':
                    o1 = period['SC']['PS'][0]['Value']['S1']
                    o2 = period['SC']['PS'][0]['Value']['S2']
                    if (int(o1) + int(o2) <= 16) and (int(o1) == 11 or int(o2) == 11):
                        print('Счет меньше 16')
                        idlive = period['I']
                        poisk_pred_total(idlive,period)
                    else:
                        print('Счет больше 16')
                    if int(o1) > int(o2):
                        print('Победил 2')
                        idlive = period['I'] 
                        pobeda = 'p1'
                        prov_pobed(pobeda,idlive,period)
                        print('передано в пров побед')
                    if int(o1) < int(o2):
                        print('Победил 1')
                        idlive = period['I'] 
                        pobeda = 'p2'
                        prov_pobed(pobeda,idlive,period)
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
    
    
    
if __name__ == '__main__':
    main()
schedule.every(15).seconds.do(main)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)  
