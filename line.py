# Импортируем библиотеку для запуска скрипта по расписанию
import json
import schedule
# Импортируем библиотеку для отправки запросов
import requests
# Импортируем библиотеку для установки VPN соединения
# from expressvpn import connect
# Импортируем библиотеку для работы с логом
import traceback
# Подключаем функцию форматирования лога из другого исполняющего файла
from format_log import format_admin_log
# Подключаем функцию формирования резервного лога из другого исполняющего файла
from error_log_compiler import compile_error
# Импортируем все функции из файла парсинга ответа 
from response_parse import igra
import time
# Содаем пустой массив для аккумулирования сообщений лога 
log = []

# Основная стартовая функция
def main():
    # Обрабатываем ошибки vpn соединения
    try:
        # Выполняем VPN соединение
        # connect()
        # Отправляем метку и сообщение о неудачном выполнении для форматирования и отправки административного лога
        log.append('VPN соединение успешно установлено\n:OK-SYSTEM')                
        # Обрабатываем ошибки отправки GET-запроса
        try:   
            # Отправляем GET-запрос
            cookies = {
                'sid': 'v4vcse5v6ut0l49kk75ct64o3c',
                '__utmzz': 'utmcsr=(direct)|utmcmd=(none)|utmccn=(not set)|utmcct=(not set)|utmctr=(not set)',
                '__utmzzses': '1',
                'cookie_test': '1',
                '_ga': 'GA1.2.787085034.1701932389',
                '_gid': 'GA1.2.1236899613.1701932389',
                'tmr_lvid': 'bb25253498585793933f9cb1d80120d6',
                'tmr_lvidTS': '1701932389291',
                '_ym_uid': '1701932389425003929',
                '_ym_d': '1701932389',
                '_ym_isad': '2',
                '_bge_ci': 'BA1.1.9829344224.1701932390',
                '_ym_visorc': 'w',
                '_tt_enable_cookie': '1',
                '_ttp': 'CGbdO1z4MJ8DgAd_uHw0bpHUMZE',
                '_fbp': 'fb.1.1701932390957.63298086',
                '_ga_WBJR2T2B3R': 'GS1.2.1701932391.1.0.1701932391.60.0.0',
                '_ga_4X19GXYYF0': 'GS1.2.1701932391.1.0.1701932391.60.0.0',
                '_ga_6G3GYJ0KG3': 'GS1.2.1701932391.1.0.1701932391.0.0.0',
                'afUserId': 'b1ad9fa7-5c22-452a-8727-6d94f10e8efd-p',
                'AF_SYNC': '1701932393039',
                'tmr_detect': '0%7C1701932393089',
                '_ga_VEWNK2RRS2': 'GS1.1.1701932388.1.1.1701932406.0.0.0',
            }

            headers = {
                'Accept': '*/*',
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Cookie': 'sid=v4vcse5v6ut0l49kk75ct64o3c; __utmzz=utmcsr=(direct)|utmcmd=(none)|utmccn=(not set)|utmcct=(not set)|utmctr=(not set); __utmzzses=1; cookie_test=1; _ga=GA1.2.787085034.1701932389; _gid=GA1.2.1236899613.1701932389; tmr_lvid=bb25253498585793933f9cb1d80120d6; tmr_lvidTS=1701932389291; _ym_uid=1701932389425003929; _ym_d=1701932389; _ym_isad=2; _bge_ci=BA1.1.9829344224.1701932390; _ym_visorc=w; _tt_enable_cookie=1; _ttp=CGbdO1z4MJ8DgAd_uHw0bpHUMZE; _fbp=fb.1.1701932390957.63298086; _ga_WBJR2T2B3R=GS1.2.1701932391.1.0.1701932391.60.0.0; _ga_4X19GXYYF0=GS1.2.1701932391.1.0.1701932391.60.0.0; _ga_6G3GYJ0KG3=GS1.2.1701932391.1.0.1701932391.0.0.0; afUserId=b1ad9fa7-5c22-452a-8727-6d94f10e8efd-p; AF_SYNC=1701932393039; tmr_detect=0%7C1701932393089; _ga_VEWNK2RRS2=GS1.1.1701932388.1.1.1701932406.0.0.0',
                'Referer': 'https://maxline.by/live-sport/15',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = {
                'sport': '15',
                'hash': '518cb16be5ff3b603bf6d271aeae8786',
            }
            proxies = {
                "http": "36.6.145.224",
                "https": "http://PROXY_SERVER_URL",
            }
            # Строка запроса с передачей параметров
            response = requests.get('https://maxline.by/api/event/live-data', params=params, cookies=cookies, headers=headers, proxies=proxies)
            # Отправляем метку и сообщение об успешном выполнении для форматирования и отправки административного лога
            log.append('GET запрос успешно отправлен\n:OK-SYSTEM')
            # Обрабатываем ошибки преобразования ответа в json
            
            # Преобразуем ответ в JSON
            resultline = response.json()
            # Отправляем метку и сообщение об успешном выполнении для форматирования и отправки административного лога
            log.append('Ответ успешно преобразован в JSON\n:OK-SYSTEM')
            # Обрабатываем исключения передачи JSON в функцию обработки данных
            try:
                try:
                    # Передаем JSON в функцию обработки данных
                    igra(resultline)
                    # Отправляем метку и сообщение о неудачном выполнении для форматирования и отправки административного лога
                    log.append('JSON успешно передан в функцию преобразования igra()\n:OK-SYSTEM')
                    # Обрабатываем исключения формирования и отправки лога на формативание
                except:
                     pass
                try:
                    # Обрабатываем исключения форматирования traceback
                    try:
                        # Получаем и форматируем traceback
                        tr = traceback.format_exc()
                    # Выполняется в случае возникновения ошибки
                    except:
                        # Формируем сообщение для отправки в лог при невозможности получить traceback
                        # Переменная с названием ошибки
                        error = (' JSON успешно передан в функцию преобразования igra().Однако возникло исключение.\n')
                        # Переменная с описанием ошибки
                        tr = ('Не удалось сформировать traceback. Ошибка обработчика исключений. line.py -> line 99')
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
                        print('JSON успешно передан в функцию преобразования igra().Однако возникло исключение.Не удалось сформировать traceback. Ошибка обработчика исключений. line.py -> line 99. compile_error - не доступен')
                        print ('Информация выведена только в консоль. Запись в логи осуществить не удалось.')
                
                
            except:
                # Отправляем метку и сообщение о неудачном выполнении для форматирования и отправки административного лога
                log.append('Не удалось передать JSON в функцию преобразования igra()\n:TRUBLE-SYSTEM')
                # Обрабатываем исключения формирования и отправки лога на формативание
                try:
                    # Обрабатываем исключения форматирования traceback
                    try:
                        # Получаем и форматируем traceback
                        tr = traceback.format_exc()
                    # Выполняется в случае возникновения ошибки
                    except:
                        # Формируем сообщение для отправки в лог при невозможности получить traceback
                        # Переменная с названием ошибки
                        error = (' Не удалось передать JSON в функцию преобразования igra().\n')
                        # Переменная с описанием ошибки
                        tr = ('Не удалось сформировать traceback. Ошибка обработчика исключений. line.py -> line 130')
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
                        print('Не удалось передать JSON в функцию преобразования igra().Не удалось сформировать traceback. Ошибка обработчика исключений. line.py -> line 130. compile_error - не доступен')
                        print ('Исключение выведено только в консоль.')
        
        except:
            # Отправляем метку и сообщение о неудачном выполнении для форматирования и отправки административного лога
                    log.append('Не удалось отправить GET-запрос\n:TRUBLE-SYSTEM')
                    # Обрабатываем исключения формирования и отправки лога на формативание
                    try:
                        # Обрабатываем исключения форматирования traceback
                        try:
                            # Получаем и форматируем traceback
                            tr = traceback.format_exc()
                        # Выполняется в случае возникновения ошибки
                        except:
                            # Формируем сообщение для отправки в лог при невозможности получить traceback
                            # Переменная с названием ошибки
                            error = (' Не удалось отправить GET-запрос\n')
                            # Переменная с описанием ошибки
                            tr = ('Не удалось сформировать traceback. Ошибка обработчика исключений. line.py -> line 188')
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
                            print('Не удалось отправить GET-запрос. Не удалось сформировать traceback. Ошибка обработчика исключений. line.py -> line 188. compile_error - не доступен')
                            print ('Исключение выведено только в консоль.')
    except:
        # Отправляем метку и сообщение о неудачном выполнении для форматирования и отправки административного лога
                    log.append('Не удалось установить VPN соединение\n:TRUBLE-SYSTEM')
                    # Обрабатываем исключения формирования и отправки лога на формативание
                    try:
                        # Обрабатываем исключения форматирования traceback
                        try:
                            # Получаем и форматируем traceback
                            tr = traceback.format_exc()
                        # Выполняется в случае возникновения ошибки
                        except:
                            # Формируем сообщение для отправки в лог при невозможности получить traceback
                            # Переменная с названием ошибки
                            error = (' Не удалось установить VPN соединение\n')
                            # Переменная с описанием ошибки
                            tr = ('Не удалось сформировать traceback. Ошибка обработчика исключений. line.py -> line 217')
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
                            print('Не удалось установить VPN соединение. Не удалось сформировать traceback. Ошибка обработчика исключений. line.py -> line 217. compile_error - не доступен')
                            print ('Исключение выведено только в консоль.')
   
if __name__ == '__main__':
    main()
schedule.every(30).seconds.do(main)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    # time.sleep(1) 
