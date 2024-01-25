from format_log import format_admin_log
import traceback
from error_log_compiler import compile_error
import requests
from bs4 import BeautifulSoup
log = []
def results_for_periods(resultline,id):
    # Обрабатываем исключения при получении ветки массива для переборки
    try:
        
        # Обрабатываем циклом ветку результатов
        for fact in resultline['data']['results']:
            
            # Обрабатываем ошибки получения номера события в ветке результатов
            try:
                # Получаем номер события из ветки результатов
                event = fact['event']
            except:
                pass
            # Обрабатываем исключения при сравнивании
            try:
                # Сравниваем идентификатор события и полученный номер события
                if id in event:
                    # Обрабатываем ошибки получения строки 'name'
                    try:
                        # Получаем строку 'name'
                        name = fact['name']
                    except:
                        pass
                    # Обрабатываем исключения при сравнивании
                    try:
                        # Проверяем содержится ли в полученной строке 'score'
                        if 'score' in name:
                            # Обрабатываем ошибки получения строки 'content'
                            try:
                                # Получаем строку 'content'
                                content = fact['content']
                            except:
                                pass
                            # Обрабатываем исключения при сравнивании
                            try:
                                # Проверяем содержится ли в строке 'periods'
                                if 'periods' in content:
                                    try:
                                        # Если в строке присутствует 'periods' - парсим строку и выбираем часть строки с результатами периодов
                                        period = content.split('periods')[0]
                                    except:
                                        pass
                                    try:
                                        # Парсим строку с периодами 
                                        period_parse_1 = period.split('},"itog"')[0]
                                    except:
                                        pass
                                    try:
                                        period_parse_2 = period_parse_1.split('{"general":{"')[1]
                                    except:
                                        pass
                                    try:
                                        win_periods_team1_1 = period_parse_2.split(',')[0]
                                    except:
                                        pass
                                    try:
                                        # Получаем количество партий выигранный первым игроком
                                        win_periods_team1 = win_periods_team1_1.split('first":')[1]
                                    except:
                                        pass
                                    try:
                                        win_periods_team2_1 = period_parse_2.split(',')[1]
                                    except:
                                        pass
                                    try:
                                        # Получаем количество партий выигранных вторым игроком
                                        win_periods_team2 = win_periods_team2_1.split('second":')[1]
                                        
                                    
                                        # Возвращаем полученные параметры
                                        return(win_periods_team1,win_periods_team2)
                                    except:
                                        pass
                                    # Выбираем события где каждый игрок выиграл по одному сету
                                    # if (win_periods_team1 == 1) and (win_periods_team2 == 1):
                                    
                            except:
                                pass
                    except:
                        pass
            except:
                pass
    except:
        pass  
    # Отправляем метку и сообщение об успешном выполнении для форматирования и отправки административного лога
    log.append('Получено количество партий выигранных вторым игроком > results_for_periods()\n:OK-GAME')
    try:
        # Обрабатываем исключения форматирования traceback
        try:
            # Получаем и форматируем traceback
            tr = traceback.format_exc()
        # Выполняется в случае возникновения ошибки
        except:
            # Формируем сообщение для отправки в лог при невозможности получить traceback
            # Переменная с названием ошибки
            error = (' Получено количество партий выигранных вторым игроком -> results_for_periods().Однако возникло исключение.\n')
            # Переменная с описанием ошибки
            tr = ('Не удалось сформировать traceback. Ошибка обработчика исключений. parser_string.py -> line 79')
        # Отправляем сообщение на форматирование в функцию формирования лога 
        format_admin_log(log,tr)
    # Выполняется в случае возникновения ошибки
    except:
        # Обрабатываем исключения отправки сообщения в функцию формирования резервного лога
        try:
            # Отправляем переменные для обработки в функцию формирования резервного лога    
            compile_error(error,tr)
        # Выполняется в случае возникновения ошибки
        except:
            # В случае невозможности отправки переменных ни в одну из функций, выводим сообщения в консоль
            print('Получено количество партий выигранных вторым игроком -> results_for_periods().Однако возникло исключение.Не удалось сформировать traceback. Ошибка обработчика исключений. line.py -> line 99. compile_error - не доступен')
            print ('Информация выведена только в консоль. Запись в логи осуществить не удалось.')              
def result_1set(resultline,id):
    # Обрабатываем циклом ветку результатов
        for fact in resultline['data']['results']:
            # Обрабатываем ошибки получения номера события в ветке результатов
            try:
                # Получаем номер события из ветки результатов
                event = fact['event']
            except:
                pass
            # Сравниваем идентификатор события и полученный номер события
            if id in event:
                # Обрабатываем ошибки получения строки 'name'
                try:
                    # Получаем строку 'name'
                    name = fact['name']
                except:
                    pass
                # Проверяем содержится ли в полученной строке 'score'
                if 'score' in name:
                    # Обрабатываем ошибки получения строки 'content'
                    try:
                        # Получаем строку 'content'
                        content = fact['content']
                    except:
                        pass
                    # Проверяем содержится ли в строке 'periods'
                    if 'periods' in content:
                        # Если в строке присутствует 'periods' - парсим строку и выбираем часть строки с результатами периодов
                        schet = content.split('periods')[1]
                        try:
                            # Получаем часть строки со счетом первого сета 
                            schet_1set_1 = schet.split('},{')[0]
                            # Парсим счет первого игрока в первом сете
                            schet_1set_team1_1 = schet_1set_1.split(',')[0]
                            schet_1set_team1_2 = schet_1set_team1_1.split('first":')[1]
                            # Присваиваем переменной счет первого игрока в первом сете
                            schet_1set_team1 = schet_1set_team1_2.replace('"', "")
                            # Парсим счет второго игрока в первом сете
                            schet_1set_team2_1 = schet_1set_1.split(',')[1]
                            schet_1set_team2_2 = schet_1set_team2_1.split('"second":')[1]
                            # Присваиваем переменной счет второго игрока в первом сете
                            schet_1set_team2_3 = schet_1set_team2_2.replace('"', "")
                            schet_1set_team2_4 = schet_1set_team2_3.replace('}', "")
                            schet_1set_team2_5 = schet_1set_team2_4.replace(']', "")
                            schet_1set_team2 = schet_1set_team2_5.replace('"', "")
                            return(schet_1set_team1,schet_1set_team2)
                        except:
                            pass

def result_2set(resultline,id):
    # Обрабатываем циклом ветку результатов
        for fact in resultline['data']['results']:
            # Обрабатываем ошибки получения номера события в ветке результатов
            try:
                # Получаем номер события из ветки результатов
                event = fact['event']
            except:
                pass
            # Сравниваем идентификатор события и полученный номер события
            if id in event:
                # Обрабатываем ошибки получения строки 'name'
                try:
                    # Получаем строку 'name'
                    name = fact['name']
                except:
                    pass
                # Проверяем содержится ли в полученной строке 'score'
                if 'score' in name:
                    # Обрабатываем ошибки получения строки 'content'
                    try:
                        # Получаем строку 'content'
                        content = fact['content']
                    except:
                        pass
                    # Проверяем содержится ли в строке 'periods'
                    if 'periods' in content:
                        # Если в строке присутствует 'periods' - парсим строку и выбираем часть строки с результатами периодов
                        schet = content.split('periods')[1]
                        try:
                            # Получаем часть строки со счетом второго сета 
                            schet_2set_1 = schet.split('},{')[1]
                            # Парсим счет первого игрока во втором сете
                            schet_2set_team1_1 = schet_2set_1.split(',')[0]
                            schet_2set_team1_2 = schet_2set_team1_1.split('first":')[1]
                            # Присваиваем переменной счет первого игрока в первом сете
                            schet_2set_team1 = schet_2set_team1_2.replace('"', "")
                            # Парсим счет второго игрока в первом сете
                            schet_2set_team2_1 = schet_2set_1.split(',')[1]
                            schet_2set_team2_2 = schet_2set_team2_1.split('"second":')[1]
                            # Присваиваем переменной счет второго игрока в первом сете
                            schet_2set_team2_3 = schet_2set_team2_2.replace('"', "")
                            schet_2set_team2_4 = schet_2set_team2_3.replace(']', "")
                            schet_2set_team2 = schet_2set_team2_4.replace('}', "")
                            return(schet_2set_team1,schet_2set_team2)
                        except:
                            pass

def result_3set(resultline,id):
    # Обрабатываем циклом ветку результатов
        for fact in resultline['data']['results']:
            # Обрабатываем ошибки получения номера события в ветке результатов
            try:
                # Получаем номер события из ветки результатов
                event = fact['event']
            except:
                pass
            # Сравниваем идентификатор события и полученный номер события
            if id in event:
                # Обрабатываем ошибки получения строки 'name'
                try:
                    # Получаем строку 'name'
                    name = fact['name']
                except:
                    pass
                # Проверяем содержится ли в полученной строке 'score'
                if 'score' in name:
                    # Обрабатываем ошибки получения строки 'content'
                    try:
                        # Получаем строку 'content'
                        content = fact['content']
                    except:
                        pass
                    # Проверяем содержится ли в строке 'periods'
                    if 'periods' in content:
                        # Если в строке присутствует 'periods' - парсим строку и выбираем часть строки с результатами периодов
                        schet = content.split('periods')[1]
                        try:
                            # Парсим строку со счетом и получаем счет 3 сета
                            schet_3set_1 = schet.split('},{')[2]
                            schet_3set_team1_1 = schet_3set_1.split('","')[0]
                            schet_3set_team1 = schet_3set_team1_1.split('"first":"')[1]
                            schet_3set_team2_1 = schet_3set_1.split('","')[1]
                            schet_3set_team2_2 = schet_3set_team2_1.split('second":"')[1]
                            schet_3set_team2_3 = schet_3set_team2_2.replace('}', "")
                            schet_3set_team2_4 = schet_3set_team2_3.replace(']', "")
                            schet_3set_team2 = schet_3set_team2_4.replace('"', "")
                            return(schet_3set_team1,schet_3set_team2)
                        except:
                            pass
        
def result_4set(resultline,id):
    # Обрабатываем циклом ветку результатов
        for fact in resultline['data']['results']:
            # Обрабатываем ошибки получения номера события в ветке результатов
            try:
                # Получаем номер события из ветки результатов
                event = fact['event']
            except:
                pass
            # Сравниваем идентификатор события и полученный номер события
            if id in event:
                # Обрабатываем ошибки получения строки 'name'
                try:
                    # Получаем строку 'name'
                    name = fact['name']
                except:
                    pass
                # Проверяем содержится ли в полученной строке 'score'
                if 'score' in name:
                    # Обрабатываем ошибки получения строки 'content'
                    try:
                        # Получаем строку 'content'
                        content = fact['content']
                    except:
                        pass
                    # Проверяем содержится ли в строке 'periods'
                    if 'periods' in content:
                        # Если в строке присутствует 'periods' - парсим строку и выбираем часть строки с результатами периодов
                        schet = content.split('periods')[1]
                        try:
                            # Парсим строку со счетом и получаем счет 3 сета
                            schet_4set_1 = schet.split('},{')[3]
                            schet_4set_team1_1 = schet_4set_1.split('","')[0]
                            schet_4set_team1 = schet_4set_team1_1.split('"first":"')[1]
                            schet_4set_team2_1 = schet_4set_1.split('","')[1]
                            schet_4set_team2_2 = schet_4set_team2_1.split('second":"')[1]
                            schet_4set_team2_3 = schet_4set_team2_2.replace('}', "")
                            schet_4set_team2_4 = schet_4set_team2_3.replace(']', "")
                            schet_4set_team2 = schet_4set_team2_4.replace('"', "")
                            return(schet_4set_team1,schet_4set_team2)
                        except:
                            pass

def result_5set(resultline,id):
    # Обрабатываем циклом ветку результатов
        for fact in resultline['data']['results']:
            # Обрабатываем ошибки получения номера события в ветке результатов
            try:
                # Получаем номер события из ветки результатов
                event = fact['event']
            except:
                pass
            # Сравниваем идентификатор события и полученный номер события
            if id in event:
                # Обрабатываем ошибки получения строки 'name'
                try:
                    # Получаем строку 'name'
                    name = fact['name']
                except:
                    pass
                # Проверяем содержится ли в полученной строке 'score'
                if 'score' in name:
                    # Обрабатываем ошибки получения строки 'content'
                    try:
                        # Получаем строку 'content'
                        content = fact['content']
                    except:
                        pass
                    # Проверяем содержится ли в строке 'periods'
                    if 'periods' in content:
                        # Если в строке присутствует 'periods' - парсим строку и выбираем часть строки с результатами периодов
                        schet = content.split('periods')[1]
                        try:
                            # Парсим строку со счетом и получаем счет 3 сета
                            schet_5set_1 = schet.split('},{')[4]
                            schet_5set_team1_1 = schet_5set_1.split('","')[0]
                            schet_5set_team1 = schet_5set_team1_1.split('"first":"')[1]
                            schet_5set_team2_1 = schet_5set_1.split('","')[1]
                            schet_5set_team2_2 = schet_5set_team2_1.split('second":"')[1]
                            schet_5set_team2_3 = schet_5set_team2_2.replace('}', "")
                            schet_5set_team2_4 = schet_5set_team2_3.replace(']', "")
                            schet_5set_team2 = schet_5set_team2_4.replace('"', "")
                            return(schet_5set_team1,schet_5set_team2)
                        except:
                            pass
        
       
def get_statistic_string(descr):
    stat_1 = descr.split('"stat\":')[1]
    stat_2 = stat_1.split(',')[0]
    stat_3 = stat_2.replace('"', "")
    stat_string = stat_3.replace('}', "")
    url_stat = f'https://maxline.by/mstat.php?p={stat_string}'
    return (url_stat)


    
    