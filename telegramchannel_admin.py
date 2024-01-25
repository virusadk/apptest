import requests

def send_channel_admin_log(text: str):
    token = '6547233557:AAGhUx8Fuq3BqjEpkkGIVcXLOy43LcuktD4'
    url = "https://api.telegram.org/bot"
    channel_id = '-1001869001929'
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text,
        "parse_mode": "HTML"
    })

    if r.status_code != 200:
        raise Exception("post_text error")





def main():
    send_channel_admin_log('Привет, чувак!')


if __name__ == '__main__':
    main()
