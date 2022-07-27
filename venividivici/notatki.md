#do instalacji requirements

pip install -r ./requirements.txt

#do podniesienia serwera

python3 manage.py runserver 

#po dodaniu rzeczy do bazy danych, lub zmianie czegos w bazie danych

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

#stworzenie modelu - nowej aplikacji
python manage.py startapp <nazwa apki>

# instalacja środowiska env

sudo apt install python3.10-venv


# witrualne środowisko
python3 -m venv env

source env/bin/activate

# wychodznie z wirtualnego środowiska
deactivate




#Instalacja: 

(myvenv) ~$ python -m pip install --upgrade pip
(myvenv) ~$ sudo pip install -r requirements.txt