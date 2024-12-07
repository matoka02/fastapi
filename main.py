# в корневой директории отключить окружение (использовать луче PowerShell, GitBash не принимает такие команды)
# deactivate
# перейти в директорию lesson-021
# cd lesson-021
# установка свежего окружения в директории
# python.exe -m venv venv
# активировать среду
# windows_activate = ".\venv\Scripts\activate"
# linux_macos_activate = "source venv/bin/activate"
# список установленных пакетов
# pip list
# установить пакеты согласно требований
# pip install -r requirements.txt

# запуск сервера
# uvicorn app.app:app --reload
# запуск сервера (v2)
# python main.py


import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", log_level="info", reload=True)