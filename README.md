# Cardex

Sitio web de Cardex, desarrollado con Django.

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

10:En caso de que falten librerias y no estés del todo seguro puede poner el siguiente código el cuál saca los requirements del proyecto
pip freeze > requirements.txt

11:Cuando saques los requirements los instalas con un el código
-| py -m pip install -r requirements.txt
si te da error prueba con éste otro:
-| pip install -r requirements.txt

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
