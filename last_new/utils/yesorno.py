import requests



# Функция для обработки команды /yesno
def yesno():
    url = 'https://yesno.wtf/api'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        image = data.get('image')
        return image

if __name__ == '__main__':
    print(yesno())