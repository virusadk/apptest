from get_information_game import get_des_string
from parser_string import results_for_periods
from parser_string import result_3set
from parser_string import result_1set
from parser_string import result_2set
from parser_string import result_4set
from parser_string import result_5set
from parser_string import get_statistic_string
from get_information_game import get_name_team1
from get_information_game import get_name_team2
from parser_stat import get_statistic
from parser_stat import get_ochnye_vstrechi
from parser_stat import get_o_v_3set
from parser_stat import get_o_v_4set
from parser_stat import summ_point_set_mass
from parser_stat import get_kol_bolshe
from parser_stat import get_kol_menshe

def get_game_not_start(resultline):
    not_start_id = []
    for event in resultline['data']['events']:
        # Обрабатываем ошибки получения идентификатора события
        
        # Получаем идентификатор события
        id = event['id']
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
                        pass
                    else:
                        not_start_id.append(id)
    print(not_start_id)
    if not_start_id is None:
        print('Нет не начавшихся событий')
    return (not_start_id)

def veroyatnost(resultline,id):
    pass

def get_events_finish_2_sets(resultline,id):
    try:
        

        team1 = get_name_team1(resultline,id)
        team2 = get_name_team2(resultline,id)
        # print(team1,'-',team2)
        # Получаем результат счета по сетам
        win_periods_team1,win_periods_team2 = results_for_periods(resultline,id)
        print('Побед по периодам:',win_periods_team1,'-',win_periods_team2)
        # if (win_periods_team1 == 1) and (win_periods_team2 == 1):

        # Получаем счет 3 сета
        try:
            schet_3set_team1,schet_3set_team2 = result_3set(resultline,id)
            print('Счет 3 сет:',schet_3set_team1,'-',schet_3set_team2)
        except:
            print('Информация о 3 сете отсутствует')

    
        
        # Проверяем не начался ли 3 сет
        # if (schet_3set_team1 == 0) and (schet_3set_team2 == 0):
        # Парсим строку и получаем счет первых двух сетов
        try:
            schet_1set_team1,schet_1set_team2 = result_1set(resultline,id)
            print('1сет:',schet_1set_team1,'-',schet_1set_team2)
        except:
            print('Информация о 1 сете отсутствует')
        try:
            schet_2set_team1,schet_2set_team2 = result_2set(resultline,id)
            print('2сет:',schet_2set_team1,'-',schet_2set_team2)
        except:
            print('Информация о 2 сете отсутствует')
        # try:
        #     schet_4set_team1,schet_4set_team2 = result_4set(resultline,id)
        #     print('4сет:',schet_4set_team1,'-',schet_4set_team2)
        # except:
        #     print('Информация о 4 сете отсутствует')
        # try:
        #     schet_5set_team1,schet_5set_team2 = result_5set(resultline,id)
        #     print('5сет:',schet_5set_team1,'-',schet_5set_team2)
        # except:
        #     print('Информация о 5 сете отсутствует')

        # Получаем общее количество очков по сетам
        ochki_set1 = int(schet_1set_team1) + int(schet_1set_team2)
        ochki_set2 = int(schet_2set_team1) + int(schet_2set_team2)
        print(ochki_set1,'-',ochki_set2)

        # Выбираем события с нужным количеством очков
        # if ((ochki_set1 <= 17) and (ochki_set2 <= 17)) or ((ochki_set1 >= 20) and (ochki_set2 >= 20)):
        # получаем строку описания нужного события
        set_mass = []
        try:
            
            mass_stat = get_statistic(resultline,id)
            ov_mass = get_ochnye_vstrechi(mass_stat)
            o_v_3_set = get_o_v_3set(ov_mass)
            o_v_4_set = get_o_v_4set(ov_mass)
            
            for s_3 in o_v_3_set:
                set_mass.append(s_3)
            for s_4 in o_v_4_set:
                set_mass.append(s_4)
            print(o_v_3_set,o_v_4_set)
            print(set_mass)
            summ_point = summ_point_set_mass(set_mass)
            kol_b = get_kol_bolshe(summ_point)
            kol_m = get_kol_menshe(summ_point)
            
            print(summ_point)
            print(kol_b,kol_m)
        except:
            print('Нет подходящих событий')

        

        
        
        
        
        # return(period)
    



                    # Если в строке отсутствует 'periods' - продолжаем итерацию 
    except:
        print('Нет подходящих событий')