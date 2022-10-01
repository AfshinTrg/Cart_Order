```
source venv/bin/activate
pip install -r requirements.txt
cd cart/
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
