_Функциональный прототип_

**MIDAS VPN** - сервис для оплаты подписок на VPN (URI-ссылка)

Подключение происходит через стороннее ПО (~~AmneziaVPN~~, v2rayNG, WireGuard и др.)

Django работает на :8000

React работает на :3000

Использованы шрифты Google Fonts

---------------------------------------------------------

git clone https://github.com/paidtxexist-tech/backend.git

cd backend

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

---------------------------------------------------------

git clone https://github.com/paidtxexist-tech/frontend.git

cd frontend

npm start

---------------------------------------------------------