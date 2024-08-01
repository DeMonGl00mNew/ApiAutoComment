import requests
import fileReader
import os
from key_api import API_KEY
url = 'https://gptunnel.ru/v1/chat/completions'
headers = {
    'Authorization': API_KEY,  # Используйте ваш API ключ здесь
    'Content-Type': 'application/json'
}
def setDataContent(content):
    data = {
        'model': 'gpt-3.5-turbo',
        'useWalletBalance': True,
        'messages': [

            {
                'role': 'user',
                'content': f'Сделай комментарии к коду на русском и включи их в код {content}'
            }
        ]
    }
    return data

def tryCommentingFile(content_for_data):
    data=setDataContent(content_for_data)
    for _ in range(3):
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                content=response.json()['choices'][0]['message']['content']
                print(content)
                print("-"*60)
                return content
            else:
                continue
        except:
            print("неудачная попытка запроса")
            continue

def writeFile(name_file,file_path,content):
    path=rf"{file_path}{name_file}"
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    with open(path,'w', encoding='windows-1251') as file:

        file.write(content)



if __name__== "__main__":

    fileReader.setFolderPath(input("Откуда будем брать скрипты (путь): "))
    is_recusivly=True if input("Учитывать вложенные папки? ").lower() in ["да","yes"] else False
    setFolderForRecord= rf"{input("Куда будем записывать (путь): ")}"

    fileReader.setExtensionforSriptFiles(extesion=input("Введите тип расширения для скриптов: "),
                                         is_recusivly=is_recusivly)

    for _ in range (fileReader.getCountFiles()):
        content_with_comments=tryCommentingFile(content_for_data=fileReader.getContentFile())
        writeFile(name_file=fileReader.getNameFile(),
                 file_path= setFolderForRecord,
                 content=content_with_comments)


