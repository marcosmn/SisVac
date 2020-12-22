# Titulo do projeto

Implementação do sistema de vacinação proposto pelo LAIS (EDITAL Nº 046/2020).

## Descrição

URL para o site no Heroku [enigmatic-citadel-38291](https://enigmatic-citadel-38291.herokuapp.com/#/).

O SisVac(Nome escolhido para o projeto), é um sistema onde usuarios cadastrados podem agendar vacinas em lugar e horario de preferencia, de forma remota, e monitorar a sua carteira virtual de vacinação.

### Funcionalidades usadas

* Django
* Django Rest Framework
* Postgres
* VueJs
* Google OAuth2
* Heroku

## Rodando localmente

Necessario ter:
* Python 3.7 [instalado localmente](http://install.python-guide.org).
* Django 3.1 [instalado localmente](https://www.djangoproject.com/download/).
```sh 
pip install django
```
* Postgresql 13 [instalado localmente](https://www.postgresql.org/download/).
* VueJS 
```sh 
npm install vue
```
* Django Rest Framework
```sh 
pip install djangorestframework
```
Para enviar aoa Heroku, você precisa instalar [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

Crie um banco de dado no postgre com o nome 'vacinacao', depois rode o comando:
```sh 
python manage.py migrate
```
Depois basta rodar o servidor com:
```sh 
python manage.py runserver
```

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

Para mais informações sobre o uso de Python no Heroku, veja o artigo:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
