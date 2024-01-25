# Импортируем функцию форматирования лога из другого исполняющего файла
from format_log import format_admin_log
from get_information_game import get_vid_sporta
from get_information_game import get_status
from get_information_game import get_name_team1
from get_information_game import get_name_team2
from get_information_game import get_name_league
from get_information_game import get_time_game
from get_information_game import get_des_string
from get_information_game import get_kef_win
from filter_events import get_events_finish_2_sets
from filter_events import veroyatnost
from filter_events import get_game_not_start
from parser_string import get_statistic_string
from parser_stat import get_statistic
from parser_stat import get_ochnye_vstrechi
from parser_stat import kol_ochnyh_vstrech
from parser_stat import kol_set_19_bolshe
from parser_stat import kol_set_19_ravno
from parser_stat import kol_set_18_menshe
from parser_stat import kol_set_18_ravno
from parser_stat import get_last_vstrechi
from parser_stat import kol_game_3_sets
from parser_stat import kol_game_4_sets
from parser_stat import kol_game_5_sets
from parser_stat import get_date_last_vstrechi
from parser_stat import get_last_v_1_set
from parser_stat import summ_point_set_mass
from parser_stat import kol_set_18_5_bolshe_1set
from parser_stat import kol_set_18_5_menshe_1set
from parser_stat import kol_set_18_5_bolshe_2set
from parser_stat import kol_set_18_5_menshe_2set
from parser_stat import kol_set_18_5_bolshe_3set
from parser_stat import kol_set_18_5_menshe_3set
from format_message import format_message
from get_information_game import get_content
from parser_string import results_for_periods
from parser_string import result_1set
from parser_string import result_2set
from parser_stat import get_o_v_3set
from parser_stat import get_o_v_4set
from parser_stat import get_kol_bolshe
from parser_stat import get_kol_menshe
from parser_stat import kol_game_3_sets
# Создаем пустой масссив для аккумулирования сообщений лога 
log=[]

# Функция разбора ответа в виде JSON и получения событий 
def igra(resultline):
    
    for game in resultline['data']['events']:
        id = game['id']
        s1,s2 = results_for_periods(resultline,id)
        if (int(s1) == 1) and (int(s2) == 1):
            s1i1,s1i2 = result_1set(resultline,id)
            s2i1,s2i2 = result_2set(resultline,id)
            print(s1i1,'-',s1i2,' ',s2i1,'-',s2i2)
            summ_set1 = s1i1 + s1i2
            summ_set2 = s2i1 + s2i2
            if ((int(summ_set1) <= 17) and (int(summ_set2) <=17)) :
                
                # Получаем идентификатор лиги
                league_name = get_name_league(resultline,id)
                print(league_name)
                
                
            
            # Обрабатываем ошибки получения имени первого игрока, либо команды
            
                # Получаем имя первого игрока, либо команды
                team1 = get_name_team1(resultline,id)
            
            # Обрабатываем ошибки получения имени второго игрока, либо команды
            
                # Получаем имя второго игрока, либо команды
                team2 = get_name_team2(resultline,id)
                    
                
                print(team1,'-',team2)
                # Обрабатываем ошибки получения времени события
                
                # Получаем время события
                time_game = get_time_game(resultline,id)
                print(time_game)
                
                mass_stat = get_statistic(resultline,id)
                print(mass_stat)
                ov_mass = get_ochnye_vstrechi(mass_stat)
                print(ov_mass)
                ov_3set_mass = get_o_v_3set(ov_mass)
                print(ov_3set_mass)
                ov_4set_mass = get_o_v_4set(ov_mass)
                print(ov_4set_mass)
                summ_point_3set = summ_point_set_mass(ov_3set_mass)
                summ_point_4set = summ_point_set_mass(ov_4set_mass)
                set3_menshe = get_kol_menshe(summ_point_3set)
                set3_bolshe = get_kol_bolshe(summ_point_3set)
                set4_menshe = get_kol_menshe(summ_point_4set)
                set4_bolshe = get_kol_bolshe(summ_point_4set)
                summ_bolshe = set3_bolshe + set4_bolshe
                summ_menshe = set3_menshe + set4_menshe
                delenie = summ_bolshe / summ_menshe
                if (float(delenie) >= 2.0):
                    print('Больше:',summ_bolshe)
                    print('Меньше:',summ_menshe)
                    g3sets = kol_game_3_sets(ov_mass)
                    try:
                        listdb = []
                        with open('message.txt','r') as file:
                                                            
                                for item in file.readlines():
                                    line = item.strip()
                                    
                                    listdb.append(line)
                                                        
                                    file.close()
                                    # print(listdb)    
                    except:
                        print('невозможно прочитать message.txt')
                    
        
                        
                        
                    if str(id) in listdb:
                        print('Событие было отправлено')
                                    
                    else:
                        message = {}
                                        
                        message['time_game'] = time_game
                        message['league_name'] = league_name
                        message['team1'] = team1
                        message['team2'] = team2
                        message['bolshe'] = summ_bolshe
                        message['menshe'] = summ_menshe
                        message['s1i1'] = s1i1
                        message['s1i2'] = s1i2
                        message['s2i1'] = s2i1
                        message['s2i2'] = s2i2
                        message['g3sets'] = g3sets
                        message['stavka'] = '3сет ТБ 19.5'
                        message['des'] = 'В случае неудачи использовать догон в 4 сете'
                        
                        
                        format_message(message)
                        print('Отправлено на форматирование') 
                        try:    
                            with open('message.txt','a') as file:
                                file.write(f'\n{id}')            
                                file.close()
                                print('Событие записано в message.txt') 
                        except:
                            print('Невозможно записать в файл message.txt')
                else:
                    print('Нет требуемого превосходства')
            else:
                print('Возможно не удалось получить статистику')
        else:
            print('Нет событий с чередованием партий')
            for game in resultline['data']['events']:
                id = game['id']
                
                s1i1,s1i2 = result_1set(resultline,id)
                s2i1,s2i2 = result_2set(resultline,id)
                print(s1i1,'-',s1i2,' ',s2i1,'-',s2i2)
            

                


    # Создаем две пустых переменных
    
    # Обрабатываем ошибки доступа к определенной ветке массива
    # try:
        
    #     # Отправляем выбранную ветку из ответа в функцию получения вида спорта и возвращенный из функции ответ присваиваем переменной
    #     vidsporta = get_vid_sporta(resultline)
    #     try:
    #         # Перебираем в цикле ветку массива с событиями
    #         for event in resultline['data']['events']:
    #             # Обрабатываем ошибки получения идентификатора события
    #             try:
    #                 # Получаем идентификатор события
    #                 id = event['id']
                    
    #             except:
    #                 pass

    #             # Создаем пустой массив для отфильтрованных событий
    #             ev_fin_2_set = get_events_finish_2_sets(resultline,id)
                

    #             # Обрабатываем ошибки получения идентификатора лиги
    
    






    # not_start = get_game_not_start(resultline)
    # print (not_start)
    # for game in not_start:
    #     id = game
    #     kef1,kef2 = get_kef_win(resultline,id)
    #     print('Получено из функции:',kef1,kef2)
    #     # if ((float(kef1) >= 1) and (float(kef1) >= 1)):
    #     try:
    #         # Получаем идентификатор лиги
    #         league_name = get_name_league(resultline,id)
    #         print(league_name)
            
            
    #     except:
    #         pass
    #     # Обрабатываем ошибки получения имени первого игрока, либо команды
    #     try:
    #         # Получаем имя первого игрока, либо команды
    #         team1 = get_name_team1(resultline,id)
    #     except:
    #         pass
    #     # Обрабатываем ошибки получения имени второго игрока, либо команды
    #     try:
    #         # Получаем имя второго игрока, либо команды
    #         team2 = get_name_team2(resultline,id)
            
    #     except:
    #         pass
    #     print(team1,'-',team2)
    #     # Обрабатываем ошибки получения времени события
    #     try:
    #         # Получаем время события
    #         time_game = get_time_game(resultline,id)
    #         print(time_game)
    #     except:
    #         pass  
    #     # Обрабатываем ошибки получения строки описания события
    #     try:
    #         mass_stat = get_statistic(resultline,id)
            
    #     except:
    #         pass
    #     # try:
    #     #     ov_mass = get_ochnye_vstrechi(mass_stat)
            
    #     # except:
    #     #     pass

    #     try:
    #         lv_mass = get_last_vstrechi(mass_stat)
            
    #     except:
    #         pass
    #     # try:
    #     #     kol_ov = kol_ochnyh_vstrech(ov_mass)
            
    #     # except:
    #     #     pass
    #     # try:
    #     #     kg3s = kol_game_3_sets(lv_mass)
    #     # except:
    #     #     pass
    #     # try:
    #     #     kg4s = kol_game_4_sets(lv_mass)
    #     # except:
    #     #     pass
    #     # try:
    #     #     kg5s = kol_game_5_sets(lv_mass)
    #     # except:
    #     #     pass
    #     # if kol_ov >= 5:
    #     # kol_s_19_bolshe = kol_set_19_bolshe(lv_mass)
    #     # print('Партий с тоталом больше 19:',kol_s_19_bolshe)
    #     # kol_s_19_ravno = kol_set_19_ravno(lv_mass)
    #     # print('Партий с тоталом равным 19:',kol_s_19_ravno)
    #     # kol_s_18_ravno = kol_set_18_ravno(lv_mass)
    #     # print('Партий с тоталом равным 18:',kol_s_18_ravno)
    #     # kol_s_18_menshe = kol_set_18_menshe(lv_mass)
    #     # print('Партий с тоталом меньше 18:',kol_s_18_menshe)
    #     # print(lv_mass)
    #     # print('Количество игр с 3 сетами:',kg3s)
    #     # print('Количество игр с 4 сетами:',kg4s)
    #     # print('Количество игр с 5 сетами:',kg5s)
    #     # # print(mass_stat)
    #     # lv_date_mass = get_date_last_vstrechi(mass_stat)
    #     # print(lv_date_mass)
    #     # print(lv_mass)
    #     # set1lastv = get_last_v_1_set(lv_mass)
    #     # print(set1lastv)
        
    #     kol_bol_1set = kol_set_18_5_bolshe_1set(lv_mass)
    #     kol_men_1set = kol_set_18_5_menshe_1set(lv_mass)
    #     kol_bol_2set = kol_set_18_5_bolshe_2set(lv_mass)
    #     kol_men_2set = kol_set_18_5_menshe_2set(lv_mass)
    #     kol_bol_3set = kol_set_18_5_bolshe_3set(lv_mass)
    #     kol_men_3set = kol_set_18_5_menshe_3set(lv_mass)
    #     content = get_content(resultline,id)
    #     print(kol_bol_1set,kol_men_1set)
    #     print(kol_bol_2set,kol_men_2set)
    #     print(kol_bol_3set,kol_men_3set)
    #     print(content)
    #     # if ((kol_bol_1set >= 9) or (kol_bol_2set >= 9) or (kol_bol_3set >= 9) or (kol_men_1set >= 9) or (kol_men_2set >= 9) or (kol_men_3set >= 9)):
    #     try:
    #         listdb = []
    #         with open('message.txt','r') as file:
                                                
    #                 for item in file.readlines():
    #                     line = item.strip()
                        
    #                     listdb.append(line)
                                            
    #                     file.close()
    #                     # print(listdb)    
    #     except:
    #         print('невозможно прочитать message.txt')
        
    
                    
                    
    #     if str(id) in listdb:
    #         print('Событие было отправлено')
                        
    #     else:
    #         message = {}
    #         stavka = []                
    #         message['time_game'] = time_game
    #         message['league_name'] = league_name
    #         message['team1'] = team1
    #         message['team2'] = team2
    #         message['set1b'] = kol_bol_1set
    #         message['set1m'] = kol_men_1set
    #         message['set2b'] = kol_bol_2set
    #         message['set2m'] = kol_men_2set
    #         message['set3b'] = kol_bol_3set
    #         message['set3m'] = kol_men_3set
    #         if (kol_bol_1set >= 8):
    #             stavka.append('1 сет > 19.5')
    #         if (kol_bol_2set >= 8):
    #             stavka.append('2 сет > 19.5')
    #         if (kol_bol_3set >= 8):
    #             stavka.append('3 сет > 19.5')
    #         if (kol_men_1set >= 8):
    #             stavka.append('1 сет < 17.5')
    #         if (kol_men_2set >= 8):
    #             stavka.append('2 сет < 17.5')
    #         if (kol_men_3set >= 8):
    #             stavka.append('3 сет < 17.5')
                


    #         message['st'] = stavka
    #         format_message(message)
    #         print('Отправлено на форматирование') 
    #         try:    
    #             with open('message.txt','a') as file:
    #                 file.write(f'\n{id}')            
    #                 file.close()
    #                 print('Событие записано в message.txt') 
    #         except:
    #             print('Невозможно записать в файл message.txt')





















        # else:
        #     print('Коэффициенты данного события не соответствуют требованиям')                                       
    



    # Получение ссылки на видеотрансляцию
    # if (float(kef1) >= 1.75) and (float(kef2) >= 1.75):

    
           
        # for liga in resultline['data']['leagues']:
        #     idliga = liga['id']
        #     if league_id == idliga:
        #         liganame = liga['name']
        
        # if des is not None:
        #     # Парсим строку description
        #     # Проверяем, есть ли адрес статистики в строке и получаем адрес статистики
        #     try:
        #         stat_1 = des.split('stat')[1]
        #         stat_2 = stat_1.split(',')[0]
        #         stat_3 = stat_2[3:]
        #         stat_4 = stat_3.replace('"', "")
        #         stat_5 = stat_4.replace('}', "")
        #         stat = stat_5
        #         # print(stat)
        #     except:
        #         print('Адрес статистики отсутствует, либо не удалось распарсить строку')
        #         pass
        #     try:
        #         tv_1 = des.split('tv-link')[1]
        #         tv_2 = tv_1[3:]
        #         tv_3 = tv_2.replace('/',"")
        #         tv_4 = tv_3.split('"')[0]
        #         tv_url = tv_4                
        #     except:
        #         print('Адрес статистики отсутствует, либо не удалось распарсить строку')
        #         pass
        # else:
        #     print('Строка описания пуста') 
        # mess = f'{team1} - {team2}'
        # url_translate_live = f'<a href="https://anym3u8player.com/?url={tv_url}">Видеотрансляция</a>'
        # # send_video_url(mess,url_translate_live)
        # # send_video_url_channel(mess,url_translate_live)
        
        
        # # print(url_translate_live)




   
    
