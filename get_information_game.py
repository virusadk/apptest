from format_log import format_admin_log
# Содаем пустой массив для аккумулирования сообщений лога 
log = []
# Функция получения вида спорта из массива
def get_vid_sporta(resultline):
    
    # Обрабатываем ошибки переборки ветки массива с видами спорта
    try:
        # Выбираем нужную ветку из массива c видами спорта 
        sport = resultline['data']['sports']
        # Отправляем метку и сообщение о неудачном выполнении для форматирования и отправки административного лога
        log.append('Массив resultline успешно получен функцией get_vid_sporta. Ветка data->sports успешно получена из resultline. \n:OK-GAME')             
        # Перебираем циклом ветку массива с видами спорта и получаем вид спорта
        for vid in sport:
            # Обрабатываем исключения при получении вида спорта
            try:
                # Получаем вид спорта
                vid_sporta = vid['name']
                # Вовзвращаем результат
                return (vid_sporta)
            except:
                pass
        
    except:
        pass

# Функция получения названия спортивной лиги
def get_name_league(resultline,id):
    try: 
        # Перебираем в цикле ветку массива с событиями
        for event in resultline['data']['events']:
            try:
                id_game = event['id']
                try:
                    if id_game == id:
                        try:
                            league_id = event['league_id']
                            try:
                                for liga in resultline['data']['leagues']:
                                    try:
                                        id = liga['id']
                                        try:
                                            if league_id == id:
                                                try:
                                                    league_name = liga['name']
                                                    return (league_name)
                                                except:
                                                    pass
                                        except:
                                            pass
                                    except:
                                        pass
                            except:
                                pass
                        except:
                            pass
                except:
                    pass
            except:
                pass
    except:
        pass

# Функция получения статуса события
def get_status(resultline,id):
    try: 
        # Перебираем в цикле ветку массива с событиями
        for event in resultline['data']['events']:
            try:
                id_game = event['id']
                try:
                    if id_game == id:
                        try:
                            status = event['status']
                            return (status)
                        except:
                            pass
                except:
                    pass
            except:
                pass
    except:
        pass

# Функция получения имени первого игрока, либо команды
def get_name_team1(resultline,id):
    try: 
        # Перебираем в цикле ветку массива с событиями
        for event in resultline['data']['events']:
            try:
                id_game = event['id']
                try:
                    if id_game == id:
                        try:
                            team1 = event['team1']
                            return (team1)
                        except:
                            pass
                except:
                    pass
            except:
                pass
    except:
        pass

# Функция получения имени второго игрока, либо команды
def get_name_team2(resultline,id):
    try: 
        # Перебираем в цикле ветку массива с событиями
        for event in resultline['data']['events']:
            try:
                id_game = event['id']
                try:
                    if id_game == id:
                        try:
                            team1 = event['team2']
                            return (team1)
                        except:
                            pass
                except:
                    pass
            except:
                pass
    except:
        pass

# Функция получения времени события
def get_time_game(resultline,id):
    try: 
        # Перебираем в цикле ветку массива с событиями
        for event in resultline['data']['events']:
            try:
                id_game = event['id']
                try:
                    if id_game == id:
                        try:
                            time_game = event['time']
                            return (time_game)
                        except:
                            pass
                except:
                    pass
            except:
                pass
    except:
        pass

# Функция получения строки состояния
def get_des_string(resultline,id):
    try: 
        # Перебираем в цикле ветку массива с событиями
        for event in resultline['data']['events']:
            try:
                id_game = event['id']
                try:
                    if id_game == id:
                        try:
                            des = event['description']
                            return (des)
                        except:
                            pass
                except:
                    pass
            except:
                pass
    except:
        pass

def get_content(resultline,id):
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
        return(content)


def get_kef_win(resultline,id):
    kef1 = None
    kef2 = None
    # Обрабатываем ошибки переборки циклом ветки результатов из массива
    try:
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
                        # Если в строке присутствует 'periods' - пропускаем итерацию
                        pass
                    # Если в строке отсутствует 'periods' - продолжаем итерацию 
                    else:
                        
                        # Обрабатываем ошибки переборки циклом ветки факторов определенного события
                        try:
                            # Цикл обработки факторов определенного события
                            for factor in resultline['data']['factors'][id]:
                                #  Обрабатываем ошибки получения идентификатора ставки
                                try:  
                                    t = factor['t']
                                    
                                except:
                                    pass
                                # Сравниваем идентификатор ставки с единицей
                                if t == 1:
                                    # Обрабатываем ошибки получения номера игрока
                                    try:
                                        # Получаем номер игрока
                                        i = factor['i'] 
                                        
                                        # Формируем строку лога об успешном выполнении
                                        log.append(f'Номер игрока успешно получен по пути "data->results->factors->id->i"\n:OK')
                                        # Сравниваем номер игрока и проверяем на пустоту переменную
                                        if i == 1 and (kef1 is None):
                                            # Обрабатываем ошибки получения коэффициента первого игрока
                                            try:
                                                # Получаем коэффициент первого игрока
                                                v1 = factor['v']
                                                
                                                # Присваиваем коэффициент нашей переменной
                                                kef1 = v1
                                                
                                                # Формируем строку лога об успешном выполнении
                                                log.append(f'Коэффициент первого игрока  успешно получен по пути "data->results->factors->id->v"\n:OK')                                       
                                            # Код выполняется в случае возникновения ошибки 
                                            except:
                                                # Формируем строку лога о завершении с ошибкой
                                                log.append(f'Не удалось получить коэффициент первого игрока  по пути "data->results->factors->id->v"\n:TRUBLE') 
                                                # Передаем строку лога в функция форматирования сообщений лога
                                                format_admin_log(log)
                                        # Сравниваем номер игрока и проверяем на пустоту переменную                             
                                        if i == 2 and (kef2 is None):
                                            # Обрабатываем ошибки получения коэффициента второго игрока
                                            try:
                                                # Получаем коэффициент второго игрока
                                                v2 = factor['v']
                                                # Присваиваем коэффициент нашей переменной
                                                kef2 = v2
                                                
                                                # Формируем строку лога об успешном выполнении
                                                log.append(f'Коэффициент второго игрока успешно получен по пути "data->results->factors->id->v"\n:OK') 
                                                
                                            # Код выполняется в случае возникновения ошибки     
                                            except:
                                                pass
                                                # Формируем строку лога о завершении с ошибкой
                                                # log.append(f'Не удалось получить коэффициент второго игрока по пути "data->results->factors->id->v"\n:TRUBLE') 
                                    # Код выполняется в случае возникновения ошибки             
                                    except:
                                        pass
                                        # Формируем строку лога о завершении с ошибкой
                                        # log.append(f'Не удалось получить номер игрока по пути "data->results->factors->id->i"\n:TRUBLE') 
                                # log.append(f'Массив "data->results->factors->id" успешно обработан\n:ОК')
                        # Код выполняется в случае возникновения ошибки                  
                        except: 
                            # Формируем строку лога о завершении с ошибкой
                            
                            pass
                            
    
        print(kef1,kef2)            
                    
    # Код выполняется в случае возникновения ошибки                 
    except:
        pass
#     # Код выполняется в случае возникновения ошибки             
#     except:
#         pass
    
# # Код выполняется в случае возникновения ошибки     
# except:
#     pass

    if (kef1 is None) and (kef2 is None):
        print('Не удалось получить коэффициеты')
    return (kef1,kef2)    