# Apostila de Django

Aqui irei tentar colocar todas as referências e resumos do que eu estiver estudando sobre o Django e os diferentes tipos de ferramentas, além de todas as fontes usadas durante o aprendizado.

****************************

to

# Ambiente Virtual

No VSCode será necessário instalar e iniciar o ambiente virtual com o **virtualenv** dentro da pasta em que iremos trabalhar. Após a instalação da ferramenta poderemos criar uma pasta chamada **env**, e por fim poderemos carregar o ambiente virtual.

```cmd
>> pip install virtualenv
>> virtualenv -p python env
>> ./env/Scripts/activate  
```

Exitem outras formas de instalar e trabalhar com ambientes virtuais, como o **venv** que já vem como padrão dentro do python3, ou então usando o **pyenv**.

```cmd
>> python -m venv env
>> ./env/Scripts/activate  
```

- Pode ser necessário atualizar o pip

```cmd
python -m pip install --upgrade pip
```

************************

# Instalando o Django

Após instalar e iniciar o ambiente virtual, podemos executar o comando abaixo para instalar o django dentro do nosso ambiente.  

```cmd
pip install Django
```

- [Como instalar o Django](https://docs.djangoproject.com/pt-br/3.1/topics/install/#installing-official-release)

## Primeira execução

Após a instalação do Django, iremos executar um sequência de comandos:
- Iniciaremos o projeto Django dentro da pasta pasta atual (. - caso queria criar uma subpasta remova o ponto).
- Criaremos um arquivo chamado **requirements.txt** , que conterá as bibliotecas usadas no projeto.
- Criaremos uma aplicação chamada **core** (pode ser qualquer nome que desejar) e por fim
- iremos executar o projeto (na mesma pasta em que contém o arquivo chamado **manage.py**). 
- Depois basta abrir a página inicial do Django em http://127.0.0.1:8000/.

```cmd
>> pip install django
>> django-admin startproject app
>> cd app/
>> pip freeze > requirements.txt
>> django-admin startapp core
>> python manage.py runserver
```

![Página inicial do Django](img/django-main.png)

O comando **startproject** inicia um projeto, enquanto o comando **startapp** inicia um módulo ou aplicação do projeto.

***********

# Sobre o Django

O Django é um Framework que usa o padrão MTV (basicamente como um MVC sem o controller), onde a comunicação é feita da seguinte forma: 

![Padrão MTV](img/mtv.png)

OBS: Um projeto Django é diferente de uma aplicação Django. Em resumo, um projeto Django é um todo, que irá conter uma ou mais aplicações Django como sistema de login, sistema de postagens, sistema de carrinhos, etc. 


## Estruturas de aquivos de um projeto Django

- app/
    - manage.py
    - app/
        - __ init __.py
        - settings.py
        - urls.py
        - asgi.py
        - wsgi.py

### manage.py

O arquivo **manage.py** dentro do projeto Django é responsável por permitir a execução de comandos Django dentro de um terminal como **migrations**, **makemigrations** ou **createsuperuser**

```
>> python manage.py createsuperuser
```

### settings.py

O arquivo **settings.py** é o responsável polas configurações do projeto. As principais possibilidades de configurações são:

- DEBUG[true] - Permite a exibição de mensagens de erros, e deve ser desativada quando entrar em produção. 
- ALLOWED_HOST['*'] - Contém o domínio que deve executar a aplicação.
- MIDDLEWARE - Um intermediário entre o cliente e o sistema (segurança, autenticação, formulários, etc) 
- TEMPLATES - Configura a parte visível para os usuários
- WSGI_APLICATION - É um padrão para Python Web
- DATABASES - Banco de dados, onde o banco padrão usado pelo Django é o sqlite3.
- USE_I18N - Configura o Django para múltiplos Idiomas
- USE_TZ - É o responsável por configurar o TimeZone da aplicação. 
- STATIC_URL - Responsável com contér o caminho para os arquivos estáticos da aplicação, como o JavaScript, CSS e imagens. 


Além do padrão podemos inserir outras configurações como:

- LANGUAGE_CODE = 'pt-br'
    - responsável por traduzir as aplicações
- TIME_ZONE = 'America/Sao_Paulo'
    - Responsável por definir o fuso-horário das aplicações
- STATIC_URL = '/static/'
    - responsável por definir o caminho dos arquivos estáticos dentro da aplicação
- MEDIA_URL = '/media/'
    - responsável por definir o caminho dos arquivos de mídia dentro da aplicação
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    - responsável por definir o caminho dos arquivos estáticos dentro da projeto (é gerado automáticamente).
- MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    - responsável por definir o caminho dos arquivos de mídia dentro da projeto (é gerado automáticamente). 
- LOGOUT_REDIRECT_URL = 'index'
    - Redefine a rota padrão de logout de um usuário autenticado.

Para ver todas as possibilidades de configuração acesse: [Settings](https://docs.djangoproject.com/pt-br/3.1/ref/settings/).


### urls.py

O arquivo **urls.py** é responsável pelo roteamento das URLS do sistema. De forma abstrata, uma rota é definida por um par (rota, view). Existe uma rota padrão com a ferramente de administração do sistema na rota **admin/**