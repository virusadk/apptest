import requests

def send_telegram(text: str):
    token = '5529829120:AAGsUqlqofBzekr8wSIj2UZL15YOuvQTtRo'
    url = "https://api.telegram.org/bot"
    channel_id = '634828723'
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text,
        "parse_mode": "Markdown"
    })

    if r.status_code != 200:
        raise Exception("post_text error")
    
def send_video_url(mess,url_translate_live):
    token = '5529829120:AAGsUqlqofBzekr8wSIj2UZL15YOuvQTtRo'
    url = "https://api.telegram.org/bot"
    channel_id = '634828723'
    disable_web_page_preview = True
    # requests.get(f'{url}{token}/sendPhoto?chat_id={channel_id}&photo={img}&text={mess}')
    requests.get('https://api.telegram.org/bot5529829120:AAGsUqlqofBzekr8wSIj2UZL15YOuvQTtRo/sendMessage?chat_id=634828723&disable_web_page_preview=True&parse_mode=html&text='+"​​​​​​​​"+url_translate_live+" - "+mess)
    
def main():
    send_telegram('Привет, чувак!')


if __name__ == '__main__':
    main()