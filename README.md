# Cardex

Sitio web de Cardex, desarrollado con Django.

documentacion extra para exportar archivos
https://django-import-export.readthedocs.io/en/latest/getting_started.html

Somos la segunda Generacion de programadores en Digimundo
Los pasados programadores no documentaron, no seas como ellos
CHUERK te lo dice
att: Edgar Alcocer

⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆ Documenta
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇Paso a pasito
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

1: Primero para que puedas tener tu conjunto de entornos virtuales mas comodo
instala Anaconda Navigator.

2: Dile al encargado de la cuenta de GitHub que te agregue a los proyectos digimundo
o que coloquen tu SSH para tener acceso al repositorio. Puedes mandarme correo o marcarme

campero980103@outlook.com

3:Cuando tengas el link clonalo en tu computadora
-| git clone [LINK]

4:Una ves clonado cambia a la rama correcta que vayas a trabajar.

5:para este proyecto necesitaras instalar Python 3.9

6:Crea un entorno virtual con la version de python 3.9

7:Te recomiendo descargar y usar Cmder

8:abres tu Cmder y haces un Cd a tu carpeta del proyecto

9:activas el servidor virtual con conda activate [NombreServidor] y debes instalar lo siguiente:

-| python -m pip install pipfile
-| python -m pip install pipenv
-| pip install django
-| pip install psycopg2
-| pip install pylint
-| pip install djangorestframework
-| pip install djangorestframework-simplejwt
pip install django-admin-rangefilter

10:En caso de que falten librerias y no estés del todo seguro puede poner el siguiente código el cuál saca los requirements del proyecto
pip freeze > requirements.txt



11:Cuando saques los requirements los instalas con un el código
-| py -m pip install -r requirements.txt
si te da error prueba con éste otro:
-| pip install -r requirements.txt

lista:
appdirs==1.4.4
asgiref==3.5.2
astroid==2.8.6
awscli==1.22.33
bcrypt==3.2.2
boto==2.49.0
boto3==1.20.33
botocore==1.23.33
certifi==2021.5.30
cffi==1.15.0
colorama==0.4.3
cryptography==37.0.2
defusedxml==0.7.1
diff-match-patch==20200713
dill==0.3.5.1
distlib==0.3.2
Django==3.2.10
django-import-export==2.8.0
django-storages==1.12.3
djangorestframework==3.12.4
djangorestframework-simplejwt==5.0.0
docutils==0.15.2
et-xmlfile==1.1.0
filelock==3.0.12
gunicorn==20.1.0
isort==5.10.1
jmespath==0.10.0
lazy-object-proxy==1.6.0
MarkupPy==1.14
mccabe==0.6.1
odfpy==1.4.1
openpyxl==3.0.10
paramiko==2.11.0
Pillow==8.4.0
pipenv==2021.5.29
pipfile==0.0.2
platformdirs==2.4.0
psycopg2==2.9.1
psycopg2-binary==2.9.2
pyasn1==0.4.8
pycparser==2.21
PyJWT==2.3.0
pylint==2.11.1
PyNaCl==1.5.0
python-dateutil==2.8.2
pytz==2020.1
PyYAML==5.4.1
rsa==4.7.2
s3transfer==0.5.0
six==1.16.0
sqlparse==0.3.1
storage==0.0.4.3
tablib==3.2.1
toml==0.10.2
tomli==2.0.1
tomlkit==0.11.0
typing_extensions==4.0.0
tzdata==2022.1
urllib3==1.26.8
virtualenv==20.4.7
virtualenv-clone==0.5.4
wincertstore==0.2
wrapt==1.13.3
xlrd==2.0.1
xlwt==1.3.0


si te da error por el psycopg2 cambia la version mas reciente y en el requirements escribe

psycopg2-binary==version

///////// OPCIONAL SOLO CON POSTGRES /////////////
12:Una ves instalados tienes que crear PostgreSQL en tu computadora.
-hacer una base de datos
-un usuario
-Dar permisos al usuario en esa base de datos
-crear un esquema es la base de datos.
/////////////////////////////////////////////////

13:La base de datos esta ves es la de db.sqlite3


Configuramos el archivo settings en la parte de databases

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}

14:Una ves configurado todo pasaremos a la migración

- python manage.py migrate

15:Si se hace la migracion con exito revisa que se haya exportado las tablas a tu base de datos. Igualmente te dejo unos códigos que te pueden servir.
Con el comando siguiente podemos ver que migraciones tenemos

-| python manage.py showmigrations

Con el comando siguiente podemos crear migraciones

-| python manage.py makemigrations

///////// OPCIONAL SOLO CON POSTGRES /////////////
Introducimos el comando en consola para saber si está bien instaladas psql

-| psql -h 127.0.0.1 -p 5432 -U postgres
///////////////////////////////

16: para correr el servidor solo es con el codigo

-| python manage.py runserver

y listo

       ┏┓      ┏┓
      ┏┛┻━━━━━━┛┻┓
      ┃        ☃ ┃
      ┃   ┳┛ ┗┳   ┃
      ┃     ┻     ┃
      ┗━┓       ┏━┛
        ┃       ┗━━━┓
        ┃           ┣┓
        ┃SUCCESSFULL┏┛
        ┗┓┓┏  ━  ┳┓┏┛
         ┃┫┫     ┃┫┫
         ┗┻┛     ┗┻┛

para iniciarlo cada ves que vayas a usarlo solo seran 3 codigos
abres Cmder

-| cd a tu carpeta de proyecto
-| conda activate [NombreDelEntornoVirtual]
-| python manage.py runserver

LISTO!!!!


