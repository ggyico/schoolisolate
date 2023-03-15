from request import http

api_url = 'api.telegram.org'
bot_token = '6011041577:AAElwzl2Pq8sNtk5aVDAlXtfad0DKgbzzDA'
chat_id = "5507590821"


def telegram():
    http.post(url="https://{}/bot{}/sendMessage".format(api_url, bot_token), data={
        "chat_id": chat_id,
        "text": '成功啦！！',
    })


telegram()
