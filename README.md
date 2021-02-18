# idaprojectDjangoHosting
Django image hosting for ideaproject

Тестовый проект для ideaproject
Для разворачивания проекта необходимо инициализировать виртуальное окружение ( я использую venv, включенный в третий питон ):

python3 -m venv myvenv

активировать окружение через:

source myvenv/bin/activate

Установить все зависимости через pip3 install -r requirements.txt (учитывая, что питон3 установлен глобально)
Провести необходимые миграции в дб через:
python manage.py makemigrations
python manage.py migrate

Запустить сервер через:
python manage.py runserver


