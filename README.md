# CNAB Parser

---

## Sumário

  - [1. Sobre o projeto](#1-sobre-o-projeto)
  - [2. Instalação](#2-instalacao)
    - [Instalando Dependências](#31-instalando-dependências)
    - [Variáveis de ambiente](#32-variáveis-de-ambiente)
    - [Entrando no ambiente virtual](#33-entrando-no-ambiente-virtual)
    - [Instale as dependências](#34-instale-as-dependências)
    - [Execute as migrações para realizar a persistência de dados](#34-execute-as-migrações-para-realizar-a-persistência-de-dados)
  - [3. Rotas](#3-rotas)
    - [Documentação da API](#documentação-da-api)

---

## 1. Sobre o projeto

Essa API foi estruturada no intuito de facilitar a manipulação de dados de um arquivo CNAB para um banco de dados SQLite3. 
 ### ![image](https://user-images.githubusercontent.com/98785969/204463450-46619bd2-ec39-4769-8f03-5bd33b549bfb.png)
 ### ![image](https://user-images.githubusercontent.com/98785969/204463507-d4d8850a-ab82-48c1-af7c-083b2465f9a1.png)

Tecnologias empregadas nesse projeto:

- [DJango](https://www.djangoproject.com/)
- [DJango Rest Framework](https://www.django-rest-framework.org/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/index.html)

---


## 2. Instalação

### Instalando Dependências

Clone o projeto em sua máquina local e instale o ambiente virtual VENV:

```shell
python -m venv venv
```

### Entrando no ambiente virtual

Entre no ambiente virtual com o comando:

```shell
source venv/Scripts/activate # terminal BASH
```

### Instale as dependências

Dependências necessárias para rodar o projeto:

```shell
pip install -r requirements.txt
```

### Execute as migrações para realizar a persistência de dados

```shell
./manage.py migrate
```

### Inicie o servidor local

```shell
./manage.py runserver
```

## 3. Rotas

### Documentação da API

É possível acessar à documentação completa para poder utilizar a API, no seguinte endpoint:

```shell
http://localhost:8000/docs/
```

---


