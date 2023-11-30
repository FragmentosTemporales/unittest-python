# Contenedor Docker Python


## 1. Instalación

Para descargar la aplicación del repo, se debe escribir el siguiente comando:

```
$ git clone https://github.com/FragmentosTemporales/unittest-python.git
```


### Instalación de Docker Compose

Para instalar la aplicación debes ejecutar el siguiente código:

```
$ docker compose build
```


### Variables de entorno

Al interior de la carpeta /Sripts debes crear un documento env.env el cual debe contener las siguiente variables, puedes guiarte con el documento example.env :

```
null
```


## 2. Ejecución

Para ejecutar la aplicación debes ingresar el siguiente comando:

```
$ docker compose run --rm scripts sh -c "python manage.py test"
```

_Este comando ejecuta todos los tests_

Si quieres ejecutar un test en particular lo puedes hacer con el siguiente comando:

```
$ docker compose run --rm scripts sh -c "python manage.py test --test_name samples.test_sample.TestExample.test_add_two_numbers"
```

Para ejecutar tests y flake8 debes ingresar el siguiente comando:

```
$ docker compose run --rm scripts sh -c "python manage.py test && flake8"
```

## 3.- ¿Qué estamos ejecutando?

Al ejecutar el manage.py retornará las opciones que se pueden ejecutar en la app flask. Por el momento no está operativa la creación de bases de datos o modelos.


## 4.- Bibliografía

A continuación te dejo el link de la librería de Flask-testing 0.8.1 en Pypi:

```
https://pypi.org/project/Flask-Testing/
```