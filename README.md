# Работа с платежной системой Stripe

Доступ к админке:
http://51.250.101.137/admin/
Логин: admin
Пароль: admin

#### Пример развернутого проекта можно посмотреть [здесь](http://51.250.101.137/)

# Технологии:
    Django==4.1.1
    Python==3.10
    stripe==4.1.0
    SQLite
    Docker

# Запуск и работа с проектом
Чтобы развернуть проект, вам потребуется:
Клонировать репозиторий GitHub (не забываем создать виртуальное окружение и установить зависимости):
```python
git clone https://github.com/kiselev-pavel-dev/rishat_test_work.git
```
Создать файл ```.env``` в папке проекта _/test_rishat/_ и заполнить его всеми ключами:
```
SECRET_KEY=<секретный ключ Django>
STRIPE_PUBLISHABLE_KEY=<публичный ключ Stripe>
STRIPE_SECRET_KEY=<секретный ключ Stripe>
```
Вы можете сгенерировать ```DJANGO_SECRET_KEY``` следующим образом. 
Из директории проекта, в котором находится файл manage.py выполнить:
```python
python manage.py shell
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```
Полученный ключ скопировать в ```.env```.

Создать миграции:

```
python3 manage.py makemigrations
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Теперь можно зайти в админку _http://<ваш хост>/admin/_ под вашим логином администратора.
