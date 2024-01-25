from telegram import send_telegram
from telegramchannel import send_channel

def format_message(message):
    time_game, league_name, team1, team2,bolshe,menshe,s1i1,s1i2,s2i1,s2i2,g3sets,stavka,des = message.values()
    # SP = S + 3*60*60
    # Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')
    date = time_game.split(' ')[0]
    time = time_game.split(' ')[1]
    mess = f'\U0001F3D3 {date} - \U0001F4C6 {time} \n' \
                f'\U0001F3C6 {league_name} \n' \
                f'\U0001F9D1 {team1} - {team2}\U0001F9D1 \n' \
                  f'\n' \
                \
                f'Доп. информация:\n' \
                f'Cчет: {s1i1}:{s1i2} {s2i1}:{s2i2}\n'\
                f'Больше: {bolshe} \n'\
                f'Меньше: {menshe} \n'\
                f'Игр с 3 сетами: {g3sets} \n'\
                 f'\n' \
                 f'Ставка: {stavka} \n'\
                 f'Примечание: \n'\
                 f'{des} '\
             
             
                
            
    
    
    send_telegram(mess)
    send_channel(mess)
    # print('send')            
    print(mess)
    