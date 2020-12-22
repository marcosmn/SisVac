# Titulo do projeto

Implementação do sistema de vacinação proposto pelo LAIS (EDITAL Nº 046/2020).

## Descrição

URL para o site no Heroku [enigmatic-citadel-38291](https://enigmatic-citadel-38291.herokuapp.com/#/).

O SisVac(Nome escolhido para o projeto), é um sistema onde usuarios cadastrados podem agendar vacinas em lugar e horario de preferencia, de forma remota, e monitorar a sua carteira virtual de vacinação.

### Ferramentas e tecnologias utilizadas

* Django
* Django Rest Framework
* Postgres
* VueJs
* Google OAuth2
* Heroku

## Executar localmente

**Necessario instalar as seguintes ferramentas**
* [Python 3.8](http://install.python-guide.org).
* [Postgresql 13](https://www.postgresql.org/download/).

**Comando para instalar as dependencias necessárias**

```sh 
pip install -r requirements.txt
```
**Fazer o deploy do projeto front no backend**

Executar os seguintes comandos na pasta ./frontend
```sh 
npm install
npm run build
```
**Banco de dados**

Crie um banco de dado no postgres com o nome 'vacinacao' e depois rode os comandos:
```sh 
python manage.py migrate
python manage.py runserver
```

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


