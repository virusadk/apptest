from datetime import datetime
from telegram_admin import send_admin_log
from telegramchannel_admin import send_channel_admin_log
import codecs
# Функция форматирования и передачи на отправку административного лога
def format_admin_log(log,tr):
    mess = []
    # Получение текущей даты и времени, преобразование в нужный формат
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    mess.append('Время:  ' + time + '     ' + 'Дата:  ' + date + '\n')
    galka = '\U00002705'
    krestik = '\U0000274C'
    
    for l in log:
        i = l.split(':')[1]
        d = l.split(':')[0]
        vidloga = l.split('-')[1]
        
        sob = f'{time}-{date}-{i}-{d}'

        if 'SYSTEM' in vidloga:
            try:
                with codecs.open('system_log.txt', 'a', 'utf-8') as file:
                                
                    try:
                        if 'OK' in i:
                            
                            
                            file.write(f'\n{sob}') 
                            file.write(f'---------------------------------------------------------------------------------------------------------')
                            
                            
            
                        if 'TRUBLE' in i:
                            
                            
                            file.write(f'\n{sob}') 
                            file.write(f'---------------------------------------------------------------------------------------------------------')
                            
                           
                        
                        try:           
                            file.close()
                                
                        except:
                            
                            print('Не удалось закрыть файл system_log.txt')
                        
                            
                    except:
                    
                        print('Невозможно записать строку в файл system_log.txt') 
                    
                
            except:
                
                print('Невозможно открыть файл system_log.txt')




        try:
            with codecs.open('system_error_log.txt', 'a', 'utf-8') as file:
                            
                try:
                    
                    if 'TRUBLE' in i:
                        
                        file.write(f'\n')
                        file.write(f'\n')
                        file.write(f'\n---------------------------------------------------------------------------------------------------------') 
                        file.write(f'\n{sob}') 
                        file.write(f'---------------------------------------------------------------------------------------------------------')
                        
                        # file.write(f'/n{e}')
                        file.write(f'\n{tr}\n')
                        file.write(f'\n---------------------------------------------------------------------------------------------------------')
                        file.write(f'\n')
                        file.write(f'\n')
                        file.write(f'\n')
                        file.write(f'\n')
                        # print(tr) 
                        # print(e)    
                        print('Событие успешно записано в system_error_log.txt') 

                        try:
                            with codecs.open('admin_log.txt', 'a', 'utf-8') as file:
                                            
                                try:
                                    
                                    if 'TRUBLE' in i:
                                        
                                        file.write(f'\n{date}-{time}-Новое исключение в системных логах')
                                        
                                        file.write(f'\n---------------------------------------------------------------------------------------------------------') 

                                        print('Оповещение записано в admin_log.txt') 
                                    
                                    try:           
                                        file.close()
                                            
                                    except:
                                        
                                        print('Не удалось закрыть файл admin_log.txt')
                                    
                                            
                                except:
                                    
                                    print('Невозможно записать строку в файл admin_log.txt') 
                                    
                                
                        except:
                                
                            print('Невозможно открыть файл admin_log.txt')






                    
                    try:           
                        file.close()
                            
                    except:
                        
                        print('Не удалось закрыть файл system_error_log.txt')
                    
                            
                except:
                    
                    print('Невозможно записать строку в файл system_error_log.txt') 
                    
                
        except:
                
            print('Невозможно открыть файл system_error_log.txt')


        if 'GAME' in vidloga:
            try:
                with codecs.open('game_log.txt', 'a', 'utf-8') as file:
                                
                    try:
                        if 'OK' in i:
                            
                            
                            file.write(f'\n{sob}') 
                            file.write(f'---------------------------------------------------------------------------------------------------------')
                            
                            
            
                        if 'TRUBLE' in i:
                            
                            
                            file.write(f'\n{sob}') 
                            file.write(f'---------------------------------------------------------------------------------------------------------')
                            
                           
                        
                        try:           
                            file.close()
                                
                        except:
                            
                            print('Не удалось закрыть файл game_log.txt')
                        
                            
                    except:
                    
                        print('Невозможно записать строку в файл game_log.txt') 
                    
                
            except:
                
                print('Невозможно открыть файл game_log.txt')

                


        try:
            with codecs.open('game_error_log.txt', 'a', 'utf-8') as file:
                            
                try:
                    
                    if 'TRUBLE' in i:
                        
                        file.write(f'\n')
                        file.write(f'\n')
                        file.write(f'\n---------------------------------------------------------------------------------------------------------') 
                        file.write(f'\n{sob}') 
                        file.write(f'---------------------------------------------------------------------------------------------------------')
                        
                        # file.write(f'/n{e}')
                        file.write(f'\n{tr}\n')
                        file.write(f'\n---------------------------------------------------------------------------------------------------------')
                        file.write(f'\n')
                        file.write(f'\n')
                        file.write(f'\n')
                        file.write(f'\n')
                        # print(tr) 
                        # print(e)    
                        print('Событие успешно записано в game_error_log.txt') 

                        try:
                            with codecs.open('admin_log.txt', 'a', 'utf-8') as file:
                                            
                                try:
                                    
                                    if 'TRUBLE' in i:
                                        
                                        file.write(f'\n{date}-{time}-Новое исключение в игровых логах')
                                        
                                        file.write(f'\n---------------------------------------------------------------------------------------------------------') 

                                        print('Оповещение записано в admin_log.txt') 
                                    
                                    try:           
                                        file.close()
                                            
                                    except:
                                        
                                        print('Не удалось закрыть файл admin_log.txt')
                                    
                                            
                                except:
                                    
                                    print('Невозможно записать строку в файл admin_log.txt') 
                                    
                                
                        except:
                                
                            print('Невозможно открыть файл admin_log.txt')






                    
                    try:           
                        file.close()
                            
                    except:
                        
                        print('Не удалось закрыть файл system_error_log.txt')
                    
                            
                except:
                    
                    print('Невозможно записать строку в файл system_error_log.txt') 
                    
                
        except:
                
            print('Невозможно открыть файл system_error_log.txt')
    
        if 'OK' in i:
            des = f'{galka} {d}'
            # print(des)
            mess.append(des)
        if 'TRUBLE' in i:
            
            des = f'{krestik} {d}'
            print(des)
            mess.append('----------------------------------------------------------------\n')
            mess.append(des)
            mess.append('----------------------------------------------------------------\n')
            # mess.append(e)
            mess.append(tr)
            mess.append('----------------------------------------------------------------\n')
            my_str = ' '.join(mess)
            send_admin_log(my_str)
            send_channel_admin_log(my_str)
            
     # Формируем строку сообщения для консоли
        
    
    
    
    # print(my_str)