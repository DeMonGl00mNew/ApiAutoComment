from pathlib import Path
from typing import List

folder_path =""
filesPath = ""
current_name_file=""
lengthfilesPath = len(filesPath)


def setFolderPath(path: str):
    global folder_path
    folder_path = Path(rf"{path}")

def setExtensionforSriptFiles(extesion: str, is_recusivly:bool=False):
    global filesPath
    if is_recusivly:
        filesPath = list(folder_path.rglob(f'*.{extesion}'))
    else:
        filesPath = list(folder_path.glob(f'*.{extesion}'))
def getCountFiles():
    return len(filesPath)

def getNameFile():
    return current_name_file

def getPathFolder():
    return folder_path
def getContentFile():
    global current_name_file
    try:
        reading_file = filesPath.pop()
        with reading_file.open('r', encoding='utf-8') as file:
            current_name_file=str(reading_file).replace(str(folder_path),"")
            print(current_name_file)

            content = file.read()
            return content
    except:
        return "filesPath is Empty"


if __name__ == "__main__":
    setFolderPath(input("Введите путь до папки: "))
    is_recusivly=True if input("Учитывать вложенные папки? ").lower() in ["да","yes"] else False
    setExtensionforSriptFiles(input(("Введите тип расширения скриптов: ")),is_recusivly)
    content=getContentFile()
    print(f"\n-----{getNameFile()}-----\n")
    print(content)
