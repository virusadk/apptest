# Импортируем библиотеки

# Библиотека используется для работы с датой и временеи
import datetime
# Библиотека используется для отображения руских символов в файлах
import codecs
# Импортируем библиотеку для работы с логами
import traceback
# Импортирует только необходимые функции из библиотеки
from datetime import timedelta,timezone,datetime

def compile_error(error,tr):
    # Обрабатываем исключения полученя текущей даты
    try:
        # Получаем текущую дату
        date = datetime.now().strftime("%Y-%m-%d")
        # log.append('Текущая дата успешно получена\n:OK-SYSTEM')
    # Выполняется в случае возникновения ошибки
    except:
        # log_e_f = ('Не удалось получить текущую дату.\n')
        # tr = traceback.format_exc()
        # log_error_functions(log_e_f,tr)
        pass
    # Обрабатываем исключения полученя текущго времени
    try:
        # Получаем текущее время
        time = datetime.now().strftime("%H:%M:%S")
    # Выполняется в случае возникновения ошибки
    except:
        pass
    try:
        sob = f'{time}-{date}-{error}'
    except:
        pass
    try:
        with codecs.open('error-log-compiler.txt', 'a', 'utf-8') as file:
                        
            try:
                
                    
                    
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
                print('Событие успешно записано в error-log-compiler.txt') 
                
                
                try:           
                    file.close()
                # Выполняется в случае возникновения ошибки        
                except:
                    
                    print('Не удалось закрыть файл error-log-compiler.txt')
                
            # Выполняется в случае возникновения ошибки        
            except:
            
                print('Невозможно записать строку в файл error-log-compiler.txt') 
                
    # Выполняется в случае возникновения ошибки        
    except:
        
        print('Невозможно открыть файл error-log-compiler.txt')