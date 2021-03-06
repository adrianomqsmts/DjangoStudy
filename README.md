# 1. Apostila de Django

Aqui irei tentar colocar todas as referências e resumos do que eu estiver estudando sobre o Django e os diferentes tipos de ferramentas, além de todas as fontes usadas durante o aprendizado.

****************************

- [1. Apostila de Django](#1-apostila-de-django)
- [2. Ambiente Virtual](#2-ambiente-virtual)
- [3. Instalando o Django](#3-instalando-o-django)
  - [3.1. Primeira execução](#31-primeira-execução)
- [4. Sobre o Django](#4-sobre-o-django)
  - [4.1. Estruturas de aquivos de um projeto Django](#41-estruturas-de-aquivos-de-um-projeto-django)
    - [4.1.1. manage.py](#411-managepy)
    - [4.1.2. settings.py](#412-settingspy)
    - [4.1.3. urls.py](#413-urlspy)
    - [4.1.4. wsgi.py](#414-wsgipy)
- [5. Aplicação Django](#5-aplicação-django)
  - [5.1. Estrutura de arquivos de uma aplicação Django](#51-estrutura-de-arquivos-de-uma-aplicação-django)
    - [5.1.1. migrations](#511-migrations)
    - [5.1.2. apps.py](#512-appspy)
    - [5.1.3. admin.py](#513-adminpy)
    - [5.1.4. models.py](#514-modelspy)
    - [5.1.5. tests.py](#515-testspy)
    - [5.1.6. view.py](#516-viewpy)
- [6. Criando rotas](#6-criando-rotas)
  - [6.1. Criando uma view básica](#61-criando-uma-view-básica)
- [7. Algumas bibliotecas](#7-algumas-bibliotecas)
  - [7.1. Configurando algumas bibliotecas](#71-configurando-algumas-bibliotecas)
    - [7.1.1. Configurando o MySQL](#711-configurando-o-mysql)
    - [7.1.2. Configurando o PostGree](#712-configurando-o-postgree)
    - [7.1.3. Configurações de Email](#713-configurações-de-email)
- [8. Modelos de banco de dados com Django - ORM (Object-Relational-Mapping)](#8-modelos-de-banco-de-dados-com-django---orm-object-relational-mapping)
  - [8.1. Campos de models Django](#81-campos-de-models-django)
    - [8.1.1. Os principais parâmetros dos campos](#811-os-principais-parâmetros-dos-campos)
  - [8.2. ForeignKey - Chave Estrangeira com Django](#82-foreignkey---chave-estrangeira-com-django)
  - [8.3. Tipos de Relacionamentos em Models](#83-tipos-de-relacionamentos-em-models)
    - [8.3.1. Relacionamento 1:1 - OneToOne](#831-relacionamento-11---onetoone)
    - [8.3.2. Relacionamento 1:N - ForeignKey](#832-relacionamento-1n---foreignkey)
    - [8.3.3. Relacionamento N:N ManyToMany](#833-relacionamento-nn-manytomany)
  - [8.4. Herança de modelos](#84-herança-de-modelos)
  - [8.5. Classes e métodos para os nossos modelos](#85-classes-e-métodos-para-os-nossos-modelos)
  - [8.6. Gerando os bancos de dados](#86-gerando-os-bancos-de-dados)
  - [8.7. ORM - Consultas](#87-orm---consultas)
    - [8.7.1. objects.create - Criando um objeto e salvando no banco de dados](#871-objectscreate---criando-um-objeto-e-salvando-no-banco-de-dados)
    - [8.7.2. objects.all() - Encontrando um ou vários objetos](#872-objectsall---encontrando-um-ou-vários-objetos)
    - [8.7.3. objects.only() - Consultando apenas alguma colunas](#873-objectsonly---consultando-apenas-alguma-colunas)
    - [8.7.4. objects.values().distinct() - Selecionado apenas os dados distintos](#874-objectsvaluesdistinct---selecionado-apenas-os-dados-distintos)
    - [8.7.5. Limit e Offset - Consultando um número específico de linhas](#875-limit-e-offset---consultando-um-número-específico-de-linhas)
    - [8.7.6. objects.get - Recuperando um único Objeto](#876-objectsget---recuperando-um-único-objeto)
    - [8.7.7. objects.filter - Filtrando a consulta de dados](#877-objectsfilter---filtrando-a-consulta-de-dados)
      - [8.7.7.1. Filtrando pelos operadores de comparação](#8771-filtrando-pelos-operadores-de-comparação)
      - [8.7.7.2. Filtrando com o operador Between](#8772-filtrando-com-o-operador-between)
      - [8.7.7.3. Filtrando com o operador LIKE](#8773-filtrando-com-o-operador-like)
      - [8.7.7.4. Filtrando com o operador IN](#8774-filtrando-com-o-operador-in)
      - [8.7.7.5. Filtrando com o operador AND](#8775-filtrando-com-o-operador-and)
      - [8.7.7.6. Filtrando com o operador OR](#8776-filtrando-com-o-operador-or)
      - [8.7.7.7. Filtrando com o operador NOT](#8777-filtrando-com-o-operador-not)
      - [8.7.7.8. Filtrando com o operador NULL](#8778-filtrando-com-o-operador-null)
      - [8.7.7.9. Filtrando com o operador NOT NULL](#8779-filtrando-com-o-operador-not-null)
    - [8.7.8. objects.order_by - Ordenando consultas](#878-objectsorder_by---ordenando-consultas)
    - [8.7.9. UPDATE](#879-update)
    - [8.7.10. DELETE](#8710-delete)
      - [8.7.10.1. Funções SQL - MIN, MAX, AVG, SUM E COUNT](#87101-funções-sql---min-max-avg-sum-e-count)
    - [8.7.11. GROUP BY](#8711-group-by)
      - [8.7.11.1. HAVING](#87111-having)
    - [8.7.12. Consultas Personalizadas](#8712-consultas-personalizadas)
      - [8.7.12.1. Passando parâmetros para consultas personalizadas](#87121-passando-parâmetros-para-consultas-personalizadas)
      - [8.7.12.2. Referências completas de ORM Django](#87122-referências-completas-de-orm-django)
  - [8.8. Exemplo de Views e Models](#88-exemplo-de-views-e-models)
      - [8.8.0.1. Rota produto](#8801-rota-produto)
- [9. Templates com Django](#9-templates-com-django)
  - [9.1. Variáveis](#91-variáveis)
  - [9.2. TAGS](#92-tags)
    - [9.2.1. comment](#921-comment)
    - [9.2.2. csrf_token](#922-csrf_token)
    - [9.2.3. cycle](#923-cycle)
    - [9.2.4. debug](#924-debug)
    - [9.2.5. filter](#925-filter)
    - [9.2.6. firstof](#926-firstof)
    - [9.2.7. for](#927-for)
    - [9.2.8. for… empty](#928-for-empty)
    - [9.2.9. if](#929-if)
    - [9.2.10. Operadores booleanos](#9210-operadores-booleanos)
    - [9.2.11. lorem](#9211-lorem)
    - [9.2.12. now](#9212-now)
    - [9.2.13. regroup](#9213-regroup)
    - [9.2.14. resetcycle](#9214-resetcycle)
    - [9.2.15. spaceless](#9215-spaceless)
    - [9.2.16. url](#9216-url)
      - [9.2.16.1. url interagindo com o path](#92161-url-interagindo-com-o-path)
      - [9.2.16.2. url com apelidos](#92162-url-com-apelidos)
    - [9.2.17. verbatim](#9217-verbatim)
    - [9.2.18. widthratio](#9218-widthratio)
    - [9.2.19. width](#9219-width)
    - [9.2.20. load](#9220-load)
    - [9.2.21. include](#9221-include)
    - [9.2.22.](#9222)
  - [9.3. Filtros](#93-filtros)
    - [9.3.1. add](#931-add)
    - [9.3.2. addslashes](#932-addslashes)
    - [9.3.3. capfirst](#933-capfirst)
    - [9.3.4. center](#934-center)
    - [9.3.5. cut](#935-cut)
    - [9.3.6. date](#936-date)
    - [9.3.7. Deafult](#937-deafult)
    - [9.3.8. default_if_none](#938-default_if_none)
    - [9.3.9. dictsort](#939-dictsort)
    - [9.3.10. dictsortreversed](#9310-dictsortreversed)
    - [9.3.11. divisibleby](#9311-divisibleby)
    - [9.3.12. escape](#9312-escape)
    - [9.3.13. escapejs](#9313-escapejs)
    - [9.3.14. filesizeformat](#9314-filesizeformat)
    - [9.3.15. first](#9315-first)
    - [9.3.16. floatformat](#9316-floatformat)
    - [9.3.17. get_digit](#9317-get_digit)
    - [9.3.18. iriencode](#9318-iriencode)
    - [9.3.19. join](#9319-join)
    - [9.3.20. json_script](#9320-json_script)
    - [9.3.21. last](#9321-last)
    - [9.3.22. length](#9322-length)
    - [9.3.23. length_is](#9323-length_is)
    - [9.3.24. linebreaks](#9324-linebreaks)
    - [9.3.25. linebreaksbr](#9325-linebreaksbr)
    - [9.3.26. linenumbers](#9326-linenumbers)
    - [9.3.27. force_escape](#9327-force_escape)
    - [9.3.28. ljust](#9328-ljust)
    - [9.3.29. lower](#9329-lower)
    - [9.3.30. make_list](#9330-make_list)
    - [9.3.31. phone2numeric](#9331-phone2numeric)
    - [9.3.32. pluralize](#9332-pluralize)
    - [9.3.33. random](#9333-random)
    - [9.3.34. rjust](#9334-rjust)
    - [9.3.35. safe](#9335-safe)
    - [9.3.36. safeseq](#9336-safeseq)
    - [9.3.37. slice](#9337-slice)
    - [9.3.38. slugify](#9338-slugify)
    - [9.3.39. stringformat](#9339-stringformat)
    - [9.3.40. striptags](#9340-striptags)
    - [9.3.41. time](#9341-time)
    - [9.3.42. timesince](#9342-timesince)
    - [9.3.43. timeuntil](#9343-timeuntil)
    - [9.3.44. title](#9344-title)
    - [9.3.45. truncatechars](#9345-truncatechars)
    - [9.3.46. truncatechars_html](#9346-truncatechars_html)
    - [9.3.47. truncatewords](#9347-truncatewords)
    - [9.3.48. truncatewords_html](#9348-truncatewords_html)
    - [9.3.49. unordered_list](#9349-unordered_list)
    - [9.3.50. upper](#9350-upper)
    - [9.3.51. urlencode](#9351-urlencode)
    - [9.3.52. urlize](#9352-urlize)
    - [9.3.53. urlizetrunc](#9353-urlizetrunc)
    - [9.3.54. wordcount](#9354-wordcount)
    - [9.3.55. wordwrap](#9355-wordwrap)
    - [9.3.56. yesno](#9356-yesno)
  - [9.4. Henraça de templates](#94-henraça-de-templates)
    - [9.4.1. Dicas para usar a herança](#941-dicas-para-usar-a-herança)
  - [9.5. Comentários](#95-comentários)
  - [9.6. Arquivos Estáticos](#96-arquivos-estáticos)
- [10. Formulário com Django](#10-formulário-com-django)
  - [10.1. Campos de formulários DJango](#101-campos-de-formulários-django)
    - [10.1.1. Os principais parâmetros dos campos](#1011-os-principais-parâmetros-dos-campos)
    - [10.1.2. widgets](#1012-widgets)
  - [10.2. Exibindo o formulário em templates](#102-exibindo-o-formulário-em-templates)
    - [10.2.1. Formulário com HTML puro](#1021-formulário-com-html-puro)
    - [10.2.2. Formulário Python-HTML](#1022-formulário-python-html)
    - [10.2.3. Formulário Python com menos HTML](#1023-formulário-python-com-menos-html)
  - [10.3. Exibindo erros](#103-exibindo-erros)
  - [10.4. Exibindo o texto de ajuda](#104-exibindo-o-texto-de-ajuda)
  - [10.5. Iterando sobre um formulário](#105-iterando-sobre-um-formulário)
  - [10.6. Formulário 100% Python](#106-formulário-100-python)
  - [10.7. Trabalhando com Formulários nas Views](#107-trabalhando-com-formulários-nas-views)
    - [10.7.1. Views Baseadas em Funções](#1071-views-baseadas-em-funções)
    - [10.7.2. Views Baseadas em Classes](#1072-views-baseadas-em-classes)
  - [10.8. Validando formulários](#108-validando-formulários)
- [11. Criando Rotas](#11-criando-rotas)
  - [11.1. Conversores de Caminhos](#111-conversores-de-caminhos)
    - [11.1.1. Usando Expressões regulares](#1111-usando-expressões-regulares)
- [12. Generic Views - Visões Genéricas](#12-generic-views---visões-genéricas)
  - [12.1. Base Views](#121-base-views)
    - [12.1.1. View](#1211-view)
    - [12.1.2. TemplateView](#1212-templateview)
    - [12.1.3. Redirect View](#1213-redirect-view)
  - [12.2. Display Views](#122-display-views)
    - [12.2.1. DetailView](#1221-detailview)
    - [12.2.2. ListView](#1222-listview)
  - [12.3. Editing Views](#123-editing-views)
    - [12.3.1. FormView](#1231-formview)
    - [12.3.2. CreateView](#1232-createview)
    - [12.3.3. UpdateView](#1233-updateview)
    - [12.3.4. DeleteView](#1234-deleteview)
  - [12.4. Date Views](#124-date-views)
    - [12.4.1. ArchiveIndexView](#1241-archiveindexview)
    - [12.4.2. YearArchiveView](#1242-yeararchiveview)
    - [12.4.3. Outras DateViews](#1243-outras-dateviews)

# 2. Ambiente Virtual

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

# 3. Instalando o Django

Após instalar e iniciar o ambiente virtual, podemos executar o comando abaixo para instalar o django dentro do nosso ambiente.  

```cmd
pip install Django
```

- [Como instalar o Django](https://docs.djangoproject.com/en/dev/topics/install/#installing-official-release)

## 3.1. Primeira execução

Após a instalação do Django, iremos executar um sequência de comandos:
- Iniciaremos o projeto Django dentro da pasta pasta atual (. - caso queria criar uma subpasta remova o ponto).
- Criaremos um arquivo chamado **requirements.txt** , que conterá as bibliotecas usadas no projeto.
- Criaremos uma aplicação chamada **core** (pode ser qualquer nome que desejar) e por fim
- iremos executar o projeto (na mesma pasta em que contém o arquivo chamado **manage.py**). 
- Depois basta abrir a página inicial do Django em http://127.0.0.1:8000/.

```cmd
>> pip install django
>> django-admin startproject projeto
>> cd app/
>> pip freeze > requirements.txt
>> django-admin startapp core
>> python manage.py runserver
```

![Página inicial do Django](img/django-main.png)

O comando **startproject** inicia um projeto, enquanto o comando **startapp** inicia um módulo ou aplicação do projeto.

***********

# 4. Sobre o Django

O Django é um Framework que usa o padrão MTV (basicamente como um MVC sem o controller), onde a comunicação é feita da seguinte forma: 

![Padrão MTV](img/mtv.png)

OBS: Um projeto Django é diferente de uma aplicação Django. Em resumo, um projeto Django é um todo, que irá conter uma ou mais aplicações Django como sistema de login, sistema de postagens, sistema de carrinhos, etc. 


## 4.1. Estruturas de aquivos de um projeto Django

- projeto/
    - manage.py
    - projeto/
        - __ init __.py
        - settings.py
        - urls.py
        - asgi.py
        - wsgi.py

### 4.1.1. manage.py

O arquivo **manage.py** dentro do projeto Django é responsável por permitir a execução de comandos Django dentro de um terminal como **migrations**, **makemigrations** ou **createsuperuser**

```
>> python manage.py createsuperuser
```

### 4.1.2. settings.py

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

Para ver todas as possibilidades de configuração acesse: [Settings](https://docs.djangoproject.com/en/dev/ref/settings/).


### 4.1.3. urls.py

O arquivo **urls.py** é responsável pelo roteamento das URLS do sistema. De forma abstrata, uma rota é definida por um par (rota, view). Existe uma rota padrão com a ferramenta de administração, que leva ao painel de **admin/**.

### 4.1.4. wsgi.py

O arquivo **wsgi.py** é responsável por executar todas as aplicações Django. Basicamente o Django o usa para fazer a implementação das aplicações.

***********************

# 5. Aplicação Django

Após a criação de uma nova aplicação devemos ir no PROJETO DJANGO e informar em dentro da opção de INSTALLED_APPS o nome da aplicação.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', # nova aplicação
]
```

## 5.1. Estrutura de arquivos de uma aplicação Django

Abaixo temos a estrutura inicial de uma aplicação Django:

- migrations
- admin.py
- apps.py
- models.py
- tests.py
- views.py

Entretanto, a estrutura pode ser alterada pelo programador de acordo com as necessidades, como um diretório de arquivos estáticos, diretório para os templates, um arquivos de rotas (abstraindo do projeto), arquivo para formulários formulários, dentre outras opções.

- migrations
- static
    - js
    - css
    - images
- templates
    - index.html
- admin.py
- apps.py
- forms.py
- models.py
- tests.py
- urls.py 
- views.py


### 5.1.1. migrations

O pacote **migrations** é o responsável por mentar todo um histórico de versões do banco de dados.

### 5.1.2. apps.py

O arquivo **apps.py** é responsável por definir o nome da aplicação.

### 5.1.3. admin.py

O arquivo **admin.py** é usado para que possamos mostrar nossos dados dentro da ferramenta admin do Django, além de podermos trabalhar com todo um CRUD através da ferramenta.

### 5.1.4. models.py

O arquivo **models.py** é usado para criar os modelos de dados, tendo a função de persistir os dados dentro de um banco de dados.

### 5.1.5. tests.py

O arquivo **tests.py** é usado para criar funções e métodos para testar todas a aplicação Django.

### 5.1.6. view.py

O arquivo **view.py** é o principal arquivo da aplicação, onde contém classes e/ou métodos que são chamados dentro do arquivo **urls.py**. Estas classes e/ou métodos irão contextualizar a requisição, podendo tratar formulários, validação de usuários ou simplesmente carregar um template para a visualização. 

************

# 6. Criando rotas

Dado um projeto e uma aplicação, precisamos incluir, no arquivos de rotas **urls.py** do PROJETO, uma referência para o arquivo de rotas **urls.py** que será criado dentro da nossa aplicação. 

Podemos também especificar os caminhos de mídias que foram especificados dentro do arquivo **settings.py**, para que o projeto faça o roteamento correto dos arquivos (caso seja necessário no projeto arquivos de mídias).

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Em seguida precisamos apenas inserir a rota dentro do arquivo **urls.py** da APLICAÇÃO. Entretanto existem duas formas de fazer isso, a primeira é usando views baseadas em funções, ONDE precisamos apenas especificar o caminho, o nome da função dentro do arquivo **views.py** e dar um nome (apelido) para a rota.

```python
from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
]
```

A segunda forma é usando views baseadas em classes, que consiste na mesma ideia, mas ao invés de usar funções, iremos usar classes. 

```python
	from django.urls import path
	from .views import IndexView	
	urlpatterns = [
    		path('', IndexView.as_view(), name='index'),
	]
```

Para ver como criar PATHs mais completos acesse: [django.urls](https://docs.djangoproject.com/en/dev/ref/urls/#django.urls.path)

## 6.1. Criando uma view básica

Podemos criar uma função ou classe simples, apenas para verificarmos se as rotas estão funcionado. Para isso vamos editar o arquivo **views.py** da seguinte forma.

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá mundo!")
```
- Quem é HttpResponse? Basicamente é um método que retorna uma resposta a uma requisição HTTP. Iremos então da maneira mais simples testar a rota que é enviar uma resposta para a requisição.

Outra forma, é redirecionar para o arquivo index.html que criamos dentro do diretório **templates**. 

- render é responsável por tratar de ligar a requisição (dados enviados do browser) com o template.
- o context seria uma variável para enviar dados para o arquivo index.html, que no momento não temos. 

```python
from django.shortcuts import render

def index(request):
  context = {}
  return render(request, 'index.html', context)
```

Por fim, podemos usar as classes, que irá herdar diversas funcionalidades e padrões prontos do Django. 

```python
from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = 'index.html'
```

Para ver mais sobre roteamento básico acesse:
- [Criando o seu primeiro Programa Django - pt2 (criando um projeto)](https://docs.djangoproject.com/en/dev/intro/tutorial01/). 
- [Criando o seu primeiro Programa Django - pt3 (configurando rotas e views)](https://docs.djangoproject.com/en/dev/intro/tutorial03/)
- [Criando o seu primeiro Programa Django - pt4 (configurando rotas e views com classes)](https://docs.djangoproject.com/en/dev/intro/tutorial04/)


**********************

# 7. Algumas bibliotecas 

- whitenoise 
  - Responsável por cuidar dos arquivos estáticos em produção, como o JavaScript e CSS
- gunicorn 
  - Servidor python que irá rodar a aplicação em produção
- django-bootstrap4 
  - Integra o B4 junto ao django 
- PyMySQL 
  - Driver do servidor de conexão python-mysql
- django-stdimage 
  - Trabalha com imagens dentro da aplicação (imagens de um produto, por exemplo)
- dj_database_url 
  - Responsável por configurar o banco em produção. Usado para transmitir os dados do banco de dados local para o heroku
- psycopg2.binary 
  - É o responsável pelo bando PostGreeSQL
- dj-static 
  - Responsável por exibir arquivos estáticos e dinâmicos de forma mais segura, substituindo o whitenoise.

## 7.1. Configurando algumas bibliotecas

- Devemos alterar as aplicações permitidas dentro do arquivo **settings.py** para permitir as novas aplicações, como o **stdimage** e o **bootstrap4**. 
- Caso seja usado o whitenoise, devemos inserir o middleware na segunda linha. com a seguinte sintaxe: 'whitenoise.middleware.WhiteNoiseMiddleware'
- Para permitir os templates, precisamos criar um diretório na aplicação chamado **templates**, e dentro da linha de configuração **TEMPLATES**, na opção **DIR** devemos especificar o diretório **DIR['templates']**.
- Devemos também informar o diretório dos nosso arquivos estáticos como visto nas configurações acima. 
```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')=
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
- Para configurar o **dj-static** no lugar do whitenoise, precisamos alterar o arquivo **wsgi.py**.

```python
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = Cling(MediaCling(get_wsgi_application()))
```
- Nos arquivos **.html** precismos informar que os mesmos irão trabalhar com arquivos estáticos. Para isso, bastamos usar a sintaxe abaixo

```Django
{% load static %}
<link rel="stylesheet" href="{% static 'css/estilos.css' %}">
```
- O comando abaixo é responsável por coletar todos os arquivos estáticos ao longo das aplicações e a reúnem de forma central dentro da aplicação. 

```python
python manage.py collectstatic
```
- Para usar o B4 dentro da aplicação, precisamos usar a seguinte sintaxe. 

```Django
{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>página web</title>
    <!--Carrega o css do B4-->
    {% bootstrap_css %}
  </head>
  <body>
    <div class="container">    
    <h1>Página WEB</h1>
    <!--Local onde serão exibidas as mensagens-->
    {% bootstrap_messages %}
    <!--Carrega o JS e jquery do B4 Deve ser a última coisa do arquivo. -->
    {% bootstrap_javascript jquery='full' %}
    </div>
  </body>
</html>
```

[Escrevendo sua primeira aplicação Django, parte 6 (Personalize a aparência da sua aplicação)](https://docs.djangoproject.com/en/dev/intro/tutorial06/)
### 7.1.1. Configurando o MySQL

Caso ocorra algum erro acesse: [Erro no Django com a conexão MySQL](https://pt.stackoverflow.com/questions/395744/erro-no-django-2-2-conex%C3%A3o-com-o-mysql)

```python
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'django2',
        'USER': 'root',
        'PASSWORD': 'SENHA',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 7.1.2. Configurando o PostGree 

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fusion',
        'USER': 'root',
        'PASSWORD': 'Senha',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

ou então

```python
DATABASES = {
    'default': dj_database_url.config()
}
```


### 7.1.3. Configurações de Email

Podemos usar o email apenas dentro do terminal, caso não tenha um servidor de email. 

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Caso tenha um servidor para tratar de email, configure dentro do arquivo **settings.py**:

```python
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'asd@asd.com.br'
EMAIL_PORT = 0898
EMAIL_USER_TSL = True
EMAIL_HOST_PASSWORD = 'senha'
```

**************

# 8. Modelos de banco de dados com Django - ORM (Object-Relational-Mapping)

Todos os nossos modelos devem ser guardados dentro do arquivo **models.py**, que deve ser nossa única fonte de dados.

Exemplos simples:

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

Este modelo acima, irá gerar a seguinte tabela no banco de dados:

```SQL
CREATE TABLE myapp_person (
    "id" NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(30) NOT NULL,
    "last_name" VARCHAR(30) NOT NULL
);
```

OBS: Como pode observar, o campo ID é gerado automaticamente, mas pode ser sobrescrito caso necessário. 


## 8.1. Campos de models Django

Os campos de models se assemelham muito aos campos dos formulários, e todas as possibilidades pode ser acessada em [Model field reference](https://docs.djangoproject.com/en/dev/ref/models/fields/)

- [AutoField](https://docs.djangoproject.com/en/dev/ref/models/fields/#autofield)
- [BigAutoField](https://docs.djangoproject.com/en/dev/ref/models/fields/#biguutofield)
- [BigIntegerField](https://docs.djangoproject.com/en/dev/ref/models/fields/#bigintegerfield)
- [BinaryField](https://docs.djangoproject.com/en/dev/ref/models/fields/#binaryfield)
- [BooleanField](https://docs.djangoproject.com/en/dev/ref/models/fields/#booleanfield)
- [CharField](https://docs.djangoproject.com/en/dev/ref/models/fields/#charfield)
- [DateField](https://docs.djangoproject.com/en/dev/ref/models/fields/#datefield)
- [DateTimeField](https://docs.djangoproject.com/en/dev/ref/models/fields/#datetimefield)
- [DecimalField](https://docs.djangoproject.com/en/dev/ref/models/fields/#decimalfield)
- [DurationField](https://docs.djangoproject.com/en/dev/ref/models/fields/#durationfield)
- [EmailField](https://docs.djangoproject.com/en/dev/ref/models/fields/#emailfield)
- [FileField](https://docs.djangoproject.com/en/dev/ref/models/fields/#filefield)
- [FilePathField](https://docs.djangoproject.com/en/dev/ref/models/fields/#filepathfield)
- [FloatField](https://docs.djangoproject.com/en/dev/ref/models/fields/#floatfield)
- [ImageField](https://docs.djangoproject.com/en/dev/ref/models/fields/#imagefield)
- [IntegerField](https://docs.djangoproject.com/en/dev/ref/models/fields/#integerfield)
- [GenericIPAddressField](https://docs.djangoproject.com/en/dev/ref/models/fields/#genericipaddressfield)
- [JSONField](https://docs.djangoproject.com/en/dev/ref/models/fields/#jsonfield)
- [NullBooleanField](https://docs.djangoproject.com/en/dev/ref/models/fields/#nullbooleanfield)
- [PositiveBigIntegerField](https://docs.djangoproject.com/en/dev/ref/models/fields/#positivebigIntegerfield)
- [PositiveIntegerField](https://docs.djangoproject.com/en/dev/ref/models/fields/#positiveintegerfield)
- [PositiveSmallIntegerField](https://docs.djangoproject.com/en/dev/ref/models/fields/#positivesmallintegerfield)
- [SlugField](https://docs.djangoproject.com/en/dev/ref/models/fields/#slugfield)
- [SmallAutoField](https://docs.djangoproject.com/en/dev/ref/models/fields/#smalluutofield)
- [SmallIntegerField](https://docs.djangoproject.com/en/dev/ref/models/fields/#smallintegerfield)
- [TextField](https://docs.djangoproject.com/en/dev/ref/models/fields/#textfield)
- [TimeField](https://docs.djangoproject.com/en/dev/ref/models/fields/#iimefield)
- [URLField](https://docs.djangoproject.com/en/dev/ref/models/fields/#urlfield)
- [UUIDField](https://docs.djangoproject.com/en/dev/ref/models/fields/#uuidfield)
- [ForeignKey](https://docs.djangoproject.com/en/dev/ref/models/fields/#foreignkey)
- [ManyToManyField](https://docs.djangoproject.com/en/dev/ref/models/fields/#manytomanyfield)
- [OneToOneField](https://docs.djangoproject.com/en/dev/ref/models/fields/#onetoonefield)

### 8.1.1. Os principais parâmetros dos campos

- **null** - Se **True** permite valores vazios para o campo
- **blank** - Se **True** permite valores em branco para o campo
- **choices** - Uma sequência que consiste em iteráveis ​​de exatamente dois itens (por exemplo, [(A, B), (A, B) ...]) para usar como opções para este campo, gerando para o campo uma caixa de seleção.
- **db_column** - O nome da coluna do banco de dados a ser usado para este campo. Se não for fornecido, Django usará o nome do campo.
- **db_index** - Se for **True**, um índice de banco de dados será criado para este campo.
- **default** - Define um valor padrão para o campo.
- **editable** - Se **False**, o campo não será exibido no admin ou em qualquer outro ModelForm. Eles também são ignorados durante a validação do modelo. O padrão é **True**.
- **error_messages** - O argumento error_messages permite que você substitua as mensagens padrão que o campo irá gerar. Passe um dicionário com chaves que correspondam às mensagens de erro que você deseja substituir.
- **help_text** - Texto extra de ajuda para ser mostrado com o “widget” do formulário. É útil para documentar mesmo que seu campo não seja usado em um formulário.
- **primary_key** - Se **True**, este campo será a chave-primária do seu model
- **unique** - Se ***True***, este campo deve ser único dentro da tabela
- **unique_for_date**, **unique_for_month**, **nique_for_year** - Defina como o nome de um DateField ou DateTimeField para exigir que este campo seja exclusivo para o valor do campo de data.
- **verbose_name** - Um nome legível para o campo. Se o nome detalhado não for fornecido, o Django o criará automaticamente usando o nome do atributo do campo, convertendo sublinhados em espaços.
- **validators** - Uma lista de validadores a serem executados para este campo. 

Os principais campos podem ser acessados em [Tipos de campos](https://docs.djangoproject.com/en/dev/ref/models/fields/#field-types)

## 8.2. ForeignKey - Chave Estrangeira com Django

Para inserir uma chave estrangeira, precisamos criar os modelos, e especificar o tipo do on_delete que pode ser 

- CASCADE - Exclui em cascata. Django emula o comportamento da restrição SQL ON DELETE CASCADE e também deleta o objeto que contém a ForeignKey.
- PROTECT - Evite a exclusão do objeto referenciado
- RESTRICT - Evite a exclusão do objeto referenciado levantando RestrictedError (uma subclasse de django.db.IntegrityError). Ao contrário de PROTECT, a exclusão do objeto referenciado é permitida se também fizer referência a um objeto diferente que está sendo excluído na mesma operação, mas por meio de um relacionamento CASCADE.

Exemplo: 

```python
class Artist(models.Model):
    name = models.CharField(max_length=10)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)
```

Ainda temos as opções

- SET_NULL - Defina o ForeignKey como nulo; isso só é possível se null for True.
- SET_DEFAULT - Defina a ForeignKey com seu valor padrão; um padrão para ForeignKey deve ser definido
- DO_NOTHING - Não faça nada. Se o back-end do banco de dados impõe integridade referencial, isso causará um IntegrityError, a menos que você adicione manualmente uma restrição SQL ON DELETE ao campo do banco de dados.

Para ver a referência completa sobre a chave estrangeira acesse: [foreign key](https://docs.djangoproject.com/en/dev/ref/models/fields/#foreignkey)

Outro exemplo 

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```

## 8.3. Tipos de Relacionamentos em Models

### 8.3.1. Relacionamento 1:1 - OneToOne

O relacionamento 1-1 define que um item de uma entidade só poderá se relacionar com um item de outra entidade e o inverso também será verdade. Como exemplo podemos supor que na regra de negócio um determinado cliente pode ter apenas um único endereço, e o endereço pode estar atribuído a um único cliente.

```python
class Endereco(models.Model):
    # Definimos seus atributos

class Cliente(models.Model):
    # Definimos seus atributos
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
```

### 8.3.2. Relacionamento 1:N - ForeignKey

Um relacionamento 1-N define que um item de uma tabela pode se relacionar com vários itens de uma outra tabela, mas que o inverso não seja verdade. Um exemplo seria um cliente que pode fazer vários pedidos, mas cada pedido pode estar relacionado a um único cliente.

```python
class Endereco(models.Model):
    # Definimos seus atributos

class Pedido(models.Model):
    # Definimos seus atributos
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='pedidos')

class Cliente(models.Model):
    # Definimos seus atributos
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
```

### 8.3.3. Relacionamento N:N ManyToMany

O relacionamento NN define que um item de uma tabela pode se relacionar com vários itens de uma outra tabela e vice-versa. Um exemplo seria um produto que pode ser vendido em vários pedidos e consequentemente vários pedidos poderão ter o mesmo produto. 

```python
class Endereco(models.Model):
    # Definimos seus atributos

class Pedido(models.Model):
    # Definimos seus atributos
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='pedidos')
    produtos = models.ManyToManyField(Produto)

class Produto(models.Model):
    # Definimos seus atributos

class Cliente(models.Model):
    # Definimos seus atributos
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
```


-> O Exemplo completo pode ser acessado em: [Relacionamento 1-1, 1-N e N-N com Django](https://www.treinaweb.com.br/blog/relacionamento-1-1-1-n-e-n-n-com-django/)


## 8.4. Herança de modelos

Podemos herdar um modelo em outro, como se fosse uma base para evitar repetir muitos os dados que são  comuns em vários modelos. A referência completa de herança pode ser acessa em [Model inheritance](https://docs.djangoproject.com/en/dev/topics/db/models/#model-inheritance)

```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```
## 8.5. Classes e métodos para os nossos modelos

Métodos muitas vezes retornam (return) algo. Um exemplo disto é o método __str__() que irá retornar um nome significativo para o modelo, podendo ser o nome completo do usuário, ou uma combinação de colunas do modelo.

Os métodos podem assumir várias funcionalidades extras para o modelo, como calcular_desconto  ou realizar algum tratamento de dados antes de salvar no banco de dados.

 Referência completa pode ser acessada em: [Model methods](https://docs.djangoproject.com/en/dev/topics/db/models/#model-methods)

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
```
O exemplo acima pode ser visto com  mais detalhes em: [Models em views](https://tutorial.djangogirls.org/pt/django_models/)

```python
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blogpost')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
```

Também é comum sobrescrever a classe **meta** (uma classe interna em modelos Django) que funciona como contêiner de classe com algumas opções (metadados) anexadas ao modelo. 

A classe define permissões disponíveis, nome da tabela de banco de dados associada, se o modelo é abstrato ou não, versões no singular e plural do nome, etc. Para saber mais acesse: [Meta](https://docs.djangoproject.com/en/dev/topics/db/models/#meta-options) ou então [Meta Completo](https://docs.djangoproject.com/en/dev/ref/models/options/)


```python
class Cargo(models.Model):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo
```

## 8.6. Gerando os bancos de dados

Para gerar os bancos de dados precisamos executar o comando **makemigrations**. Este comando irá gerar um histórico do banco e manter a integridade entre as versões. Após os testes de integridade forem checados, devemos usar o comando **migrate** para gerar as tabelas do banco. Podemos também especificar o nome de aplicação caso necessário, ao invés de executar para todas todas. 

```python
>>python manage.py makemigrations
>>python manage.py migrate
```
## 8.7. ORM - Consultas

Podemos usar uma API para acessar os dados do nosso modelo, que contém diversas abstrações de comandos que nos permitem trabalhar com os objetos, principalmente dentro de uma view.

### 8.7.1. objects.create - Criando um objeto e salvando no banco de dados

O comando objects.create executa um comando SQL INSERT por detrás dos panos. O Django não acessa o banco de dados até que você chame explicitamente o método save(). O método save() não retorna um valor. Para criar e salvar um objeto em um único passo, use o método create(). 

[Criando Objetos](https://docs.djangoproject.com/pt-br/dev/ref/models/querysets/#create)

```python
p = Person.objects.create(first_name="Bruce", last_name="Springsteen")
```

ou [Salvando objetos](https://docs.djangoproject.com/pt-br/dev/ref/models/instances/#saving-objects)

```python
p = Person(first_name="Bruce", last_name="Springsteen")
p.save(force_insert=True)
```

Comando SQL
```SQL
INSERT INTO Person VALUES('Mano', '23', 'male')
```

Comando Django
```Python
Person.objects.create(name="Mano", age="23", gender="male")
```

### 8.7.2. objects.all() - Encontrando um ou vários objetos

A maneira mais simples de recuperar objeto de uma tabela é pegar todos eles. Para fazer isso, use o método all() na Manager:

    A Manager é a principal fonte de QuerySets para um modelo. Por exemplo, Blog.objects.all() retorna uma QuerySet que contém todos os objetos do tipo Blog do banco de dados.

    Os Managers são acessíveis somente através das classes de modelo, e não de instâncias de modelos, para reforçar a separação entre operações no “nível das tabelas” e operações no “nível dos registros”.

```python
all_entries = Person.objects.all()
```

É equivalente à algo do tipo:

```SQL
SELECT * FROM Person;
```

Exemplo: 

```python
persons = Person.objects.all()

for person in persons:
    print(person.name)
    print(person.gender)
    print(person.age)
```

### 8.7.3. objects.only() - Consultando apenas alguma colunas

Comando em SQL
```SQL
SELECT name, age FROM Person;
```
Comando em Django
```python
Person.objects.only('name', 'age')
```

### 8.7.4. objects.values().distinct() - Selecionado apenas os dados distintos
Consulta SQL
```SQL
SELECT DISTINCT name, age FROM Person;
```
Comando Django
```python
Person.objects.values('name', 'age').distinct()
```

### 8.7.5. Limit e Offset - Consultando um número específico de linhas

Entretanto podemos limitar as consultas de uma consulta, que pode ser usada para criar, por exemplo, o conceito de **PAGINAÇÃO**. Se um subconjunto da syntax de fatias de array Python para limitar seu QuerySet para um certo número de resultados. Este é o equivalente às cláusulas SQL Limit e OFFSET.

Comando SQL
```SQL
SELECT * FROM Person LIMIT 5;
SELECT * FROM Person OFFSET 5 LIMIT 5;
```

Comando Django
```python
Limit5 = Person.objects.all()[:5]
offset5_limit5 = Person.objects.all()[5:10]
```
### 8.7.6. objects.get - Recuperando um único Objeto

O filter() sempre lhe dará um QuerySet, mesmo se um único objeto combina com a consulta - neste caso, ele será uma QuerySet que contém um único elemento.Se você sabe que somente um objeto combina com sua consulta, você pode usar o método get() em uma Manager o qual retorna o objeto diretamente:

```python
one_entry = Entry.objects.get(pk=1)
```

### 8.7.7. objects.filter - Filtrando a consulta de dados

Para criar o subconjunto, você refina o QuerySet inicial, adicionando filtros de condições. As duas maneiras mais comuns de refinar um QuerySet são:

- filter(**kwargs)
    - Retorna uma nova QuerySet contendo objetos que combinem com os parâmetros de filtros dados.
- exclude(**kwargs)
    - Retornam uma nova QuerySet contendo objetos que não combinem com os parâmetros de filtros dados. 

```python
selected_entries = Entry.objects.filter(pub_date__year=2006)
no_selected_entries = Entry.objects.all().filter(pub_date__year=2006)
```
O resultado de um refinamento de uma QuerySet é ela mesma: uma QuerySet, tal que é possível encadear refinamentos. Por exemplo:

```python
selected_entries = Entry.objects.filter( headline__startswith='What').exclude(pub_date__gte=datetime.date.today()).filter(pub_date__gte=datetime.date(2005, 1, 30))
```
    QuerySets são preguiçosos (“lazy”) – o ato de criar uma QuerySet não envolve nenhuma atividade no banco de dados. Você pode empilhar filtros o dia inteiro, e o Django não irá executar a consulta realmente até que a QuerySet seja interpretada.

Comando SQL
```SQL
SELECT * FROM Person WHERE id = 1
```

Comando Django
```Django
Person.objects.filter(id=1)
```


#### 8.7.7.1. Filtrando pelos operadores de comparação

Comandos SQL
```SQL
WHERE age > 18;
WHERE age >= 18;
WHERE age < 18;
WHERE age <= 18;
WHERE age != 18;
```

Comandos Django
```Python
Person.objects.filter(age__gt=18)
Person.objects.filter(age__gte=18)
Person.objects.filter(age__lt=18)
Person.objects.filter(age__lt3=18)
Person.objects.exclude(=18)
```

#### 8.7.7.2. Filtrando com o operador Between

Comandos SQL
```SQL
SELECT * FROM Person WHERE age BETWEEN 10 AND 20;
```

Comandos Django
```Python
Person.objects.filter(age__range=(10,20))
```

#### 8.7.7.3. Filtrando com o operador LIKE

Comandos SQL
```SQL
WHERE name LIKE '%A%';
WHERE name LIKE 'A%';
WHERE name LIKE '%A';
```

Comandos Django
```Python
Person.objects.filter(name__icontains='A')
Person.objects.filter(name__istartswith='A')
Person.objects.filter(name__iendswith='A')
```

#### 8.7.7.4. Filtrando com o operador IN

Comandos SQL
```SQL
WHERE id IN (1,2);
```

Comandos Django
```Python
Person.objects.filter(id__in=[1,2])
```

#### 8.7.7.5. Filtrando com o operador AND

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE gender='male' AND age > 25;
```

Comandos Django
```Python
Person.objects.filter(gander='male', age__gt=25)
```

#### 8.7.7.6. Filtrando com o operador OR

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE gender='male' OR age > 25;
```

Comandos Django
```Python
FROM django.db.models import Q
Person.objects.filter(Q(gander='male') | Q(age__gt=25))
```

#### 8.7.7.7. Filtrando com o operador NOT

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE NOT gender='male';
```

Comandos Django
```Python
Person.objects.exclude(gander='male')
```

#### 8.7.7.8. Filtrando com o operador NULL

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE age IS NULL;
```

Comandos Django
```Python
Person.objects.filter(age__isnull=True)
# OU 
Person.objects.filter(age=None)
```

#### 8.7.7.9. Filtrando com o operador NOT NULL

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE age IS NOT NULL;
```

Comandos Django
```Python
Person.objects.filter(age__isnull=False)
# OU 
Person.objects.exclude(age=None)
```

PARA VER MAIS POSSIBILIDADES E EXEMPLOS ACESSE [Field lookups](https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups)

### 8.7.8. objects.order_by - Ordenando consultas

Podemos usar o OrderBy para ordenar nossas consultas, de forma descendente (-), ascendente(padrão), de forma aleatória (?) ou dentre outras formas. [ORDER BY](https://docs.djangoproject.com/en/dev/ref/models/querysets/#order-by) 

```python
Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')
Entry.objects.order_by('?')
```

Comando SQL
```SQL
SELECT * FROM Person ORDER BY age;
SELECT * FROM Person ORDER BY age DESC;
```

Comando Django
```python
Person.objects.order_by('age')
Person.objects.order_by('-age')
```

### 8.7.9. UPDATE

Comando SQL
```SQL
UPDATE Person SET age = 20 WHERE id = 1;
#Múltiplas Linhas
UPDATE Person SET age = age * 1.5ç
```

Comando Django
```Python
person = Person.objects.get(id=1)
person.age = 20
person.save
# Múltiplas linhas
from django.db.models import F
Person.objects.update(age=F('age')*1.5)
```


### 8.7.10. DELETE

Comando SQL
```SQL
DELETE FROM Person;
DELETE FROM Person WHERE age < 10;
```

Comando Django
```Python
Person.objects.all().delete()
Person.objects.filter(age_lt=10).delete()
```

#### 8.7.10.1. Funções SQL - MIN, MAX, AVG, SUM E COUNT

```SQL
SELECT MIN(age) FROM Person;
SELECT MAX(age) FROM Person;
SELECT AVG(age) FROM Person;
SELECT SUM(age) FROM Person;
SELECT COUNT(*) FROM Person;
```

Comando Django
```Python
from django.db.models import Min, Max, Avg, Sum

Person.objects.all().aggregate(Min('age'))
{'age__min': 0}

Person.objects.all().aggregate(Max('age'))
{'age__max': 100}

Person.objects.all().aggregate(Sum('age'))
{'age__sum': 5050}

Person.objects.all().count()
```

### 8.7.11. GROUP BY

```SQL
SELECT gender, COUNT(*) AS count FROM Person GROUP BY gender;
```

Comando Django
```Python
Person.objects.values('gender').annotate(count=Count('gender'))
```

#### 8.7.11.1. HAVING
```SQL
SELECT gender, COUNT(*) AS count FROM Person GROUP BY gender HAVING count > 1;
```

Comando Django
```Python
Person.objects.values('gender').annotate(count=Count('gender')).values('gender', 'count').filter(count_gt=1)
```

### 8.7.12. Consultas Personalizadas

O ORM ainda nos permite consultas de SQL em estado BRUTO, para podermos realizar consultas mais complexas, ou até mesmo, se quisermos evitar ter que aprender SQL de outra forma.

```Python
Person.objects.raw('SELECT * FROM myapp_person')
Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
Person.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
```

#### 8.7.12.1. Passando parâmetros para consultas personalizadas

Existem cuidados que devemos tomar, e mais opções de personalizações que podem ser acessadas em 
[Passing parameters into raw()](https://docs.djangoproject.com/en/dev/topics/db/sql/#passing-parameters-into-raw)

```python
lname = 'Doe'
>>> Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
```


#### 8.7.12.2. Referências completas de ORM Django

- [Consultas](https://docs.djangoproject.com/en/dev/topics/db/queries/)
- [QuerySet API reference](https://docs.djangoproject.com/en/dev/ref/models/querysets/)
- [Como funciona o ORM do Django](https://www.gilenofilho.com.br/como-funciona-o-orm-do-django/)
- [Performing raw SQL queries](https://docs.djangoproject.com/en/dev/topics/db/sql/)

## 8.8. Exemplo de Views e Models

- urls.py
```python
from .views import index, produto

urlpatterns = [
    path('', index),
    path('contact', contact),
    ## Iremos gerar um rota com um inteiro que que é o ID do produto como /produtos/1
    path('produtos/<int:pk>', produto, name = 'produto'),
]
```

- models.py
```python
class Produto(models.Model):
  #models.tipoDeDados CharField("label", tamanho máximo)
  nome = models.CharField('Nome', max_length=100)
  #decimal_places = quantidade de casas decimais e max_digits é a quantidade de dígitos máximo
  preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
  estoque = models.IntegerField('Quantidade em estoque')
  #Apresenta o objeto instanciado pelo nome dele no admin
  def __str__(self):
    return self.nome
```

- views.py
```python
from .models import Produto

def index(request):
  #Dados do Models
  produtos = Produto.objects.all()
  context = {
    'produtos' : produtos
  }
  return render(request, 'index.html', context)
```

- index.html
```Django
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

  <head>
    <title>Django</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <link rel="stylesheet" href="{% static 'css/estilos.css' %}">
  </head>

  <body>
    <table>
      <thead>
        <tr>
          <th>Produto</th>
          <th>Preço</th>
        </tr>
      </thead>
      <tbody>
        {% for produto  in produtos  %}
        <tr>
          <td><a href="{% url 'produto' produto.id %}">{{produto.nome}}</a></td>
          <td>{{produto.preco}}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
<button onclick="teste();">CLIQUE!</button>
<script src="{% static 'js/script.js' %}"></script>
  </body>
</html>
```

#### 8.8.0.1. Rota produto

- views.py
```python
def produto(request, pk):
  produtos = Produto.objects.get(id=pk)
  context = {
    'produto' : produtos
  }
  return render(request, 'produto.html', context)
```

- produto.html

```Django
<!DOCTYPE html>
<html lang="pt-bt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
      <table>
      <thead>
        <tr>
          <th>Produto</th>
          <th>Preco</th>
          <th>Estoque</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{produto.nome}}</td>
          <td>{{produto.preco}}</td>
          <td>{{produto.estoque}}</td>
        </tr>
      </tbody>
    </table>
</body>
</html>
```
**************
# 9. Templates com Django

Um template Django é um documento de texto ou uma string Python marcada usando a linguagem de template Django. Algumas construções são reconhecidas e interpretadas pelo mecanismo de template. Os principais são variáveis ​​e tags. Um modelo é renderizado com um contexto. A renderização substitui variáveis ​​por seus valores, que são pesquisados ​​no contexto, e executa tags. Todo o resto é produzido como está.

## 9.1. Variáveis

Uma variável produz um valor do contexto, que é um objeto do tipo dicionário que mapeia chaves para valores. As variáveis ​​são circundadas por {{ e }} (chaves duplas) assim:

```Django
My first name is {{ first_name }}. My last name is {{ last_name }}.
```

Se os valores passados pelo contexto forem {'first_name': 'John', 'last_name': 'Doe'}, então o resultado seria: 

```Django
My first name is John. My last name is Doe.
```
As pesquisas de dicionário, de atributo e de índice de lista são implementadas com uma notação de ponto:

```Django
{{ my_dict.key }}
{{ my_object.attribute }}
{{ my_list.0 }}
```

## 9.2. TAGS
As tags fornecem lógica arbitrária no processo de renderização. Esta definição é deliberadamente vaga. Por exemplo, uma tag pode produzir conteúdo, servir como uma estrutura de controle, por exemplo, uma instrução “if” ou um loop “for”, obter conteúdo de um banco de dados ou até mesmo permitir o acesso a outras tags de modelo.

As tags são circundadas por {% e %} (chave e porcentagem?) assim:

```Django
{% csrf_token %}
```

As tags aceitam parâmetros como:

```Django
{% cycle 'odd' 'even' %}
{% url 'produto/' produto.id %}
```

Algumas tags exigem tags de início e fim:

```Django
{% if user.is_authenticated %} Hello, {{ user.username }}.{% endif %}
```


### 9.2.1. comment

Ignora tudo entre as tags. Uma nota opcional pode ser inserida na primeira tag. Por exemplo, isso é útil ao comentar o código para documentar porque o código foi desativado.{% comment %}{% endcomment %}

```Django
<p>Rendered text with {{ pub_date|date:"c" }}</p>
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
```

### 9.2.2. csrf_token

Essa tag é usada para proteção contra CSRF, conforme descrito na documentação para [Cross Site Request Forgeries]([https://link](https://7xwm2drhn3gdndpwco2driejom--docs-djangoproject-com.translate.goog/en/3.1/ref/csrf/)) .

### 9.2.3. cycle

Produz um de seus argumentos cada vez que essa tag é encontrada. O primeiro argumento é produzido no primeiro encontro, o segundo argumento no segundo encontro e assim por diante. Depois que todos os argumentos são exauridos, a tag passa para o primeiro argumento e o produz novamente.

Esta tag é particularmente útil em um loop:

```django
{% for o in some_list %}
    <tr class="{% cycle 'row1' 'row2' %}">
        ...
    </tr>
{% endfor %}
```
A primeira iteração produz HTML que se refere à classe row1, a segunda a row2, a terceira a row1novamente e assim por diante para cada iteração do loop. Você também pode usar variáveis.


### 9.2.4. debug

Produz uma carga completa de informações de depuração, incluindo o contexto atual e os módulos importados.

### 9.2.5. filter

Filtra o conteúdo do bloco por meio de um ou mais filtros. Vários filtros podem ser especificados com canais e filtros podem ter argumentos, assim como na sintaxe de variável. Observe que o bloco inclui todo o texto entre as tags filter e endfilter.

```django
{% filter force_escape|lower %}
    This text will be HTML-escaped, and will appear in all lowercase.
{% endfilter %}
```

### 9.2.6. firstof

Produz a primeira variável de argumento que não é “falsa” (ou seja, existe, não está vazia, não é um valor booleano falso e não é um valor numérico zero). Não produz nada se todas as variáveis ​​passadas forem “falsas”.

```django
{% firstof var1 var2 var3 %}
```

Isso é equivalente a:
```django
{% if var1 %}
    {{ var1 }}
{% elif var2 %}
    {{ var2 }}
{% elif var3 %}
    {{ var3 }}
{% endif %}
```

### 9.2.7. for

Faz um loop em cada item em uma matriz, tornando o item disponível em uma variável de contexto. Por exemplo, para exibir uma lista de atletas fornecida em athlete_list:

```django
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```
Você pode fazer um loop em uma lista ao contrário usando .{% for obj in list reversed %}. Se você precisar fazer um loop em uma lista de listas, poderá descompactar os valores de cada sublista em variáveis ​​individuais.

```Django
{% for x, y in points %}
    There is a point at {{ x }},{{ y }}
{% endfor %}
```

### 9.2.8. for… empty

A tag for pode receber uma cláusula opcional cujo texto é exibido se a matriz fornecida estiver vazia ou não puder ser encontrada:{% empty %}

```django
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>
```

### 9.2.9. if

A tag avalia uma variável e se essa variável for "verdadeira" (ou seja, existe, não está vazia e não é um valor booleano falso), o conteúdo do bloco é gerado:{% if %}

```django
{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
```

### 9.2.10. Operadores booleanos

Os operadores booleanos aceitos são and, or, not, == (igualdade), != (disigualdade), < (meno que), > (maior que), <= (menos ou igual que),=> (maior ou igual que), in (contido dentro de), is (identidade do objeto).

```Django 
{% if athlete_list and coach_list or cheerleader_list %}
{% endif %}

{% if somevar == "x" %}
  This appears if variable somevar equals the string "x"
{% endif %}

{% if somevar != "x" %}
  This appears if variable somevar does not equal the string "x",   or if somevar is not found in the context
{% endif %}

{% if somevar < 100 %}
  This appears if variable somevar is less than 100.
{% endif %}

{% if somevar > 0 %}
  This appears if variable somevar is greater than 0.
{% endif %}

{% if somevar <= 100 %}
  This appears if variable somevar is less than 100 or equal to 100.
{% endif %}

{% if somevar >= 1 %}
  This appears if variable somevar is greater than 1 or equal to 1.
{% endif %}

{% if "bc" in "abcdef" %}
  This appears since "bc" is a substring of "abcdef"
{% endif %}

{% if somevar is True %}
  This appears if and only if somevar is True.
{% endif %}

{% if somevar is not True %}
  This appears if somevar is not True, or if somevar is not found in the
  context.
{% endif %}
```


### 9.2.11. lorem

xibe texto latino “lorem ipsum” aleatório. Isso é útil para fornecer dados de amostra em modelos a sinatxe é {% lorem [count] [method] [random] %}, onde:

- count - Um número (ou variável) contendo o número de parágrafos ou palavras a serem gerados (o padrão é 1).
- method - Quer wpor palavras, ppara HTML parágrafos ou bpara blocos de parágrafo de texto simples (o padrão é b).
- random - A palavra random, que se dada, não usa o parágrafo comum (“Lorem ipsum dolor sit amet…”) ao gerar texto.

exemplos 

- {% lorem %} produzirá o parágrafo comum “lorem ipsum”.
- {% lorem 3 p %}irá gerar o parágrafo “lorem ipsum” comum e dois parágrafos aleatórios, cada um envolvido em <p>tags HTML .
- {% lorem 2 w random %} irá produzir duas palavras latinas aleatórias.

### 9.2.12. now 

Exibe a data e / ou hora atual, usando um formato de acordo com a string fornecida. Essa string pode conter caracteres especificadores de formato, conforme descrito na seção de filtro date.

```django 
It is {% now "jS F Y H:i" %}
```

para ver mais opções acesse [now]([https://link](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#now))


### 9.2.13. regroup

Reagrupa uma lista de objetos semelhantes por um atributo comum. Você pode usar a tag para agrupar a lista de cidades por país. O seguinte snippet de código de modelo faria isso:{% regroup %}. Para ver o exemplo completo acesse: [regroup](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#regroup)

```django
{% regroup cities by country as country_list %}

<ul>
{% for country in country_list %}
    <li>{{ country.grouper }}
    <ul>
        {% for city in country.list %}
          <li>{{ city.name }}: {{ city.population }}</li>
        {% endfor %}
    </ul>
    </li>
{% endfor %}
</ul>
```

### 9.2.14. resetcycle

Reinicia um ciclo anterior para que ele reinicie de seu primeiro item em seu próximo encontro. Sem argumentos, irá redefinir o último definido no modelo.{% resetcycle %}{% cycle %}. A referência completa pode ser acessa em: [resetcycle]([https://link](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#resetcycle))


```django
{% for coach in coach_list %}
    <h1>{{ coach.name }}</h1>
    {% for athlete in coach.athlete_set.all %}
        <p class="{% cycle 'odd' 'even' %}">{{ athlete.name }}</p>
    {% endfor %}
    {% resetcycle %}
{% endfor %}
```

a saída seria algo do tipo

```html
<h1>José Mourinho</h1>
<p class="odd">Thibaut Courtois</p>
<p class="even">John Terry</p>
<p class="odd">Eden Hazard</p>

<h1>Carlo Ancelotti</h1>
<p class="odd">Manuel Neuer</p>
```

### 9.2.15. spaceless

Remove os espaços em branco entre as tags HTML. Isso inclui caracteres de tabulação e novas linhas.

```django
{% spaceless %}
    <p>
        <a href="foo/">Foo</a>
    </p>
{% endspaceless %}
```

resultaria em:

```html
<p><a href="foo/">Foo</a></p>
```

### 9.2.16. url

Retorna uma referência de caminho absoluto (um URL sem o nome de domínio) correspondendo a uma determinada visualização e parâmetros opcionais. Quaisquer caracteres especiais no caminho resultante serão codificados usando iri_to_uri().

```django
{% url 'some-url-name' v1 v2 %}
```
O primeiro argumento é um nome de padrão de URL . Pode ser um literal entre aspas ou qualquer outra variável de contexto. Argumentos adicionais são opcionais e devem ser valores separados por espaço que serão usados ​​como argumentos no URL. 


#### 9.2.16.1. url interagindo com o path

```python
path('client/<int:id>/', app_views.client, name='app-views-client')
```

```django
{% url 'app-views-client' client.id %}
```

#### 9.2.16.2. url com apelidos

Se quiser recuperar um URL sem exibi-lo, você pode usar uma chamada um pouco diferente:

```django
{% url 'some-url-name' arg arg2 as the_url %}
<a href="{{ the_url }}">I'm linking to {{ the_url }}</a>
```

Essa sintaxe não causará erro se a visualização estiver ausente. Na prática, você usará isso para vincular a visualizações que são opcionais:{% url ... as var %}

```django
{% url 'some-url-name' as the_url %}
{% if the_url %}
  <a href="{{ the_url }}">Link to optional stuff</a>
{% endif %}
```

### 9.2.17. verbatim

Impede o mecanismo de template de renderizar o conteúdo desta tag de bloco. 

```django
{% verbatim myblock %}
    Avoid template rendering via the {% verbatim %}{% endverbatim %} block.
{% endverbatim myblock %}
```

### 9.2.18. widthratio

Para criar gráficos de barras e outros, esta tag calcula a proporção de um determinado valor a um valor máximo e, em seguida, aplica essa proporção a uma constante. - Referência completa : [widthratio](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#widthratio)

### 9.2.19. width
Armazena em cache uma variável complexa com um nome mais simples. Isso é útil ao acessar um método “caro” (por exemplo, um que acessa o banco de dados) várias vezes.

```django
{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
```

A variável preenchida (no exemplo acima, total) está disponível apenas entre as tags e .{% with %}{% endwith %}. Você pode atribuir mais de uma variável de contexto:

```django
{% with alpha=1 beta=2 %}
    ...
{% endwith %}
```

### 9.2.20. load 

Carrega um conjunto de tags de modelo personalizado. Por exemplo, o modelo a seguir carregaria todas as tags e filtros registrados somelibrarye localizados no pacote package.otherlibrary:

```django
{% load somelibrary package.otherlibrary %}
```

Você também pode carregar seletivamente filtros ou tags individuais de uma biblioteca, usando o fromargumento. Neste exemplo, as tags / filtros do modelo nomeados fooe barserão carregados de somelibrary:

```django 
{% load foo bar from somelibrary %}
```

### 9.2.21. include

Carrega um modelo e o renderiza com o contexto atual. Esta é uma forma de “incluir” outros modelos em um modelo. O nome do modelo pode ser uma variável ou uma string codificada (entre aspas), entre aspas simples ou duplas. Este exemplo inclui o conteúdo do modelo "foo/bar.html":

```django
{% include "foo/bar.html" %}
```

Você pode passar contexto adicional para o modelo usando argumentos de palavra-chave:

```django
{% include "name_snippet.html" with person="Jane" greeting="Hello" %}
```

### 9.2.22. 


*******************

## 9.3. Filtros
Filtros transformam os valores de variáveis ​​e argumentos de tag. Eles se parecem com isto:

``` Django
{{ django|title }}
```

### 9.3.1. add 

Adiciona o argumento ao valor: Se value for 4, a saída será 6.

```django 
{{ value|add:"2" }}
```

### 9.3.2. addslashes

Adiciona barras antes das aspas. Útil para sequências de escape em CSV, por exemplo: Se value for "I'm using Django", a saída será ."I\'m using Django"

```django
{{ value|addslashes }}
```

### 9.3.3. capfirst

Capitaliza o primeiro caractere do valor. Se o primeiro caractere não for uma letra, este filtro não terá efeito: Se valuefor "django", a saída será "Django".

```django
{{ value|capfirst }}
```

### 9.3.4. center

Centraliza o valor em um campo de uma determinada largura: Se value for "Django", a saída será : "     Django    "

```django
"{{ value|center:"15" }}"
```

### 9.3.5. cut
Remove todos os valores de arg da string fornecida. Se value for "String with spaces", a saída será "Stringwithspaces"

```django 
{{ value|cut:" " }}
```

### 9.3.6. date

Formata uma data de acordo com o formato fornecido. Se valuefor um datetime, a saída será a string .'Wed 09 Jan 2008'. Para ver a lista completa de personalização de datas acesse [Date]([https://link](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date))

```django 
{{ value|date:"D d M Y" }}
```

### 9.3.7. Deafult

Se o valor for avaliado como False, usa o padrão fornecido. Caso contrário, usa o valor. Se value for "" (a string vazia), a saída será nothing.

```python
{{ value|default:"nothing" }}
```

### 9.3.8. default_if_none

Se (e somente se) o valor for None, usa o padrão fornecido. Caso contrário, usa o valor. Observe que, se uma string vazia for fornecida, o valor padrão não será usado. Se value for None, a saída será nothing.

```django
{{ value|default_if_none:"nothing" }}
```

### 9.3.9. dictsort

Pega uma lista de dicionários e retorna essa lista classificada pela chave fornecida no argumento.  Se value for [{'name': 'zed', 'age': 19}, {'name': 'amy', 'age': 22}, {'name': 'joe', 'age': 31},] a saída será [{'name': 'amy', 'age': 22}, {'name': 'joe', 'age': 31}, {'name': 'zed', 'age': 19},]

``` python
{{ value|dictsort:"name" }}
```

outro exemplo :

```python
{% for book in books|dictsort:"author.age" %}
    * {{ book.title }} ({{ book.author.name }})
{% endfor %}
```

Se books é:

```python
[
    {'title': '1984', 'author': {'name': 'George', 'age': 45}},
    {'title': 'Timequake', 'author': {'name': 'Kurt', 'age': 75}},
    {'title': 'Alice', 'author': {'name': 'Lewis', 'age': 33}},
]
```

então a saída seria:

* Alice (Lewis)
* 1984 (George)
* Timequake (Kurt)
  
### 9.3.10. dictsortreversed

Pega uma lista de dicionários e retorna essa lista classificada em ordem reversa pela chave fornecida no argumento. Isso funciona exatamente da mesma forma que o filtro acima, mas o valor retornado estará na ordem inversa.

### 9.3.11. divisibleby

Retorna True se o valor for divisível pelo argumento. Se value for 21, a saída seria True.

```django
{{ value|divisibleby:"3" }}
```

### 9.3.12. escape

Escapa do HTML de uma string. Especificamente, ele faz essas substituições:

- < é convertido para \&lt;
- \> é convertido para \&gt;
- ' (aspas simples) é convertido para \&#x27;
- " (aspas duplas) é convertido para \&quot;
- & é convertido para \&amp;

Aplicar escapea uma variável que normalmente teria escape automático aplicado ao resultado resultará em apenas uma rodada de escape. Portanto, é seguro usar essa função mesmo em ambientes com escape automático. Se você quiser que vários passes de escape sejam aplicados, use o filtro force_escape.

```django
{% autoescape off %}
    {{ title|escape }}
{% endautoescape %}
```

### 9.3.13. escapejs
Caracteres de escape para uso em strings JavaScript. Isso não torna a string segura para uso em literais de modelo HTML ou JavaScript, mas protege você de erros de sintaxe ao usar modelos para gerar JavaScript / JSON.

```django
{{ value|escapejs }}
```


### 9.3.14. filesizeformat

Formatos o valor como um tamanho de arquivo 'legível' (ie , , , etc.).'13 KB''4.1 MB''102 bytes'. Se valuefor 123456789, a saída seria .117.7 MB

```django 
{{ value|filesizeformat }}
```

### 9.3.15. first

Retorna o primeiro item de uma lista. Se value for a lista ['a', 'b', 'c'], a saída será 'a'.

```django 
{{ value|first }}
```

### 9.3.16. floatformat
Quando usado sem um argumento, arredonda um número de ponto flutuante para uma casa decimal - mas apenas se houver uma parte decimal a ser exibida. Por exemplo: Se value for 34.23234 a saída será 34.2, se 34.00000 será 34, se 34.26000 será 34.3.

```django
{{ value|floatformat }}
```

Se usado com um argumento de número inteiro, floatformat arredonda um número para essa quantidade de casas decimais. Por exemplo: Se value for 34.23234 a saída será 34.232, se 34.00000 será 34.000, se 34.26000 será 34.260.

```django
{{ value|floatformat:3 }}
```

- Para ver mais possibilidades de formtação, acesse [floatformat](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#floatformat)

### 9.3.17. get_digit

ado um número inteiro, retorna o dígito solicitado, onde 1 é o dígito mais à direita, 2 é o segundo dígito mais à direita, etc. Retorna o valor original para entrada inválida (se a entrada ou argumento não for um inteiro, ou se argumento é menor que 1). Caso contrário, a saída é sempre um número inteiro. 

```django
{{ value|get_digit:"2" }}
```

Se value for 123456789, a saída será 8.

### 9.3.18. iriencode

Converte um IRI (Identificador de Recurso Internacionalizado) em uma string adequada para inclusão em uma URL. Isso é necessário se você estiver tentando usar strings contendo caracteres não ASCII em um URL. É seguro usar este filtro em uma string que já passou pelo urlencodefiltro. Se value for "?test=1&me=2", a saída será "?test=1&amp;me=2".

```django
{{ value|iriencode }}
```

### 9.3.19. join

Junta uma lista com uma string.  Se valuefor a lista ['a', 'b', 'c'], a saída será a string "a // b // c".

```python
{{ value|join:" // " }}
```

### 9.3.20. json_script

Produz com segurança um objeto Python como JSON, envolvido em uma \<\script\> tag, pronto para uso com JavaScript.
[json_script](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#json-script)

### 9.3.21. last

Retorna o último item de uma lista. Se value for a lista ['a', 'b', 'c', 'd'], a saída será a string "d".

``` django
{{ value|last }}
```

### 9.3.22. length

Retorna o comprimento do valor. Isso funciona para strings e listas. Se value for ['a', 'b', 'c', 'd'] ou "abcd", a saída será 4. O filtro retorna 0para uma variável indefinida.

```django
{{ value|length }}
```


### 9.3.23. length_is

Retorna Truese o comprimento do valor for o argumento ou Falsecaso contrário. Se value for ['a', 'b', 'c', 'd'] ou "abcd", a saída será True.

```django
{{ value|length_is:"4" }}
```

### 9.3.24. linebreaks

Substitui quebras de linha em texto simples por HTML apropriado; uma única nova linha torna-se uma quebra de linha HTML ( \<br>) e uma nova linha seguida por uma linha em branco torna-se uma quebra de parágrafo ( \<p>). Se value for Joel\nis a slug, a saída será \<p>Joel\<br>is a slug\</p>.

```django
{{ value|linebreaks }}
```

### 9.3.25. linebreaksbr

Converte todas as novas linhas em um pedaço de texto simples em quebras de linha HTML (\<br>). Se value for Joel\nis a slug, a saída será Joel\<br>is a slug.

```python
{{ value|linebreaksbr }}
```

### 9.3.26. linenumbers

Exibe texto com números de linha.

```python
{{ value|linenumbers }}
```

Se value é:

one
two
three

a saída será:

1. one
2. two
3. three

### 9.3.27. force_escape

Aplica escape de HTML a uma string (consulte o filtro escape para obter detalhes). Este filtro é aplicado imediatamente e retorna uma nova string com escape. Isso é útil nos raros casos em que você precisa de vários escapes ou deseja aplicar outros filtros aos resultados de escape. Normalmente, você deseja usar o filtro escape. Por exemplo, se você deseja capturar os elementos \<p> HTML criados pelo linebreaksfiltro:

```django
{% autoescape off %}
    {{ body|linebreaks|force_escape }}
{% endautoescape %}
```

### 9.3.28. ljust

Alinha à esquerda o valor em um campo de uma determinada largura. Se value for Django, a saída será "Django    ".

```django
"{{ value|ljust:"10" }}"
```

### 9.3.29. lower

Converte uma string em letras minúsculas.Se value for Totally LOVING this Album!, a saída será totally loving this album!

```django
{{ value|lower }}
```

### 9.3.30. make_list

Retorna o valor transformado em uma lista. Para uma string, é uma lista de caracteres. Para um inteiro, o argumento é convertido em uma string antes de criar uma lista. Se valuefor a string "Joel", a saída seria a lista ['J', 'o', 'e', 'l'] . Se value for 123, a saída será a lista ['1', '2', '3'].

```django 
{{ value|make_list }}
```

### 9.3.31. phone2numeric

Converte um número de telefone (possivelmente contendo letras) em seu equivalente numérico. A entrada não precisa ser um número de telefone válido. Isso irá facilmente converter qualquer string. Se value for 800-COLLECT, a saída será 800-2655328.

```django 
{{ value|phone2numeric }}
```

### 9.3.32. pluralize

Retorna um plural sufixo se o valor não é 1, '1' ou um objeto de comprimento 1. Por padrão, este sufixo é 's'. 
Se num_messages for 1, a saída será You have 1 message. Se num_messages for 2a saída seráYou have 2 messages.

```django
You have {{ num_messages }} message{{ num_messages|pluralize }}.
```

Podemos alterar o sufixo caso necessário 

```django
You have {{ num_walruses }} walrus{{ num_walruses|pluralize:"es" }}.
```

Para palavras que não são pluralizadas por sufixo simples, você pode especificar um sufixo no singular e no plural, separados por vírgula

```django 
You have {{ num_cherries }} cherr{{ num_cherries|pluralize:"y,ies" }}.
```

### 9.3.33. random

Retorna um item aleatório da lista fornecida. Se value for a lista ['a', 'b', 'c', 'd'], a saída pode ser "b".

```django
{{ value|random }}
```

### 9.3.34. rjust

Alinha à direita o valor em um campo de uma determinada largura. Se value for Django, a saída será ."    Django"

```django
"{{ value|rjust:"10" }}"
```

### 9.3.35. safe

Marca uma string como não exigindo mais escape de HTML antes da saída. Quando o escape automático está desativado, este filtro não tem efeito. Se você estiver encadeando filtros, um filtro aplicado depois safepode tornar o conteúdo inseguro novamente. Por exemplo, o código a seguir imprime a variável como está, sem escape:

```django
{{ var|safe|escape }}
```

### 9.3.36. safeseq

Entendi nada. Desculpa! [safeseq](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#safeseq)


### 9.3.37. slice

Retorna uma parte da lista.  Se some_list for ['a', 'b', 'c'], a saída será ['a', 'b'].

```django 
{{ some_list|slice:":2" }}
```

### 9.3.38. slugify

Converte para ASCII. Converte espaços em hifens. Remove caracteres que não são alfanuméricos, sublinhados ou hifens. Converte em minúsculas. Também remove os espaços em branco à esquerda e à direita. Se value for "Joel is a slug", a saída será "joel-is-a-slug".

```django 
{{ value|slugify }}
```

### 9.3.39. stringformat

Formata a variável de acordo com o argumento, um especificador de formatação de string. Este especificador usa a sintaxe de Formatação de String no estilo printf , com a exceção de que o “%” inicial é descartado. Se value for 10, a saída será 1.000000E+01.

```django
{{ value|stringformat:"E" }}
```

### 9.3.40. striptags

Faz todos os esforços possíveis para remover todas as tags HTML. Se value for "\<b>Joel\</b> \<button>is\</button> a \<span>slug\</span>", a saída será "Joel is a slug".

```django
{{ value|striptags }}
```

### 9.3.41. time
Formata uma hora de acordo com o formato fornecido. O formato fornecido pode ser o predefinido TIME_FORMAT ou um formato personalizado, igual ao filtro date. Observe que o formato predefinido depende da localidade. Se valuef or equivalente a datetime.datetime.now(), a saída será a string "01:23".

```django
{{ value|time:"H:i" }}
```

[time](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#time)

### 9.3.42. timesince

Formata uma data como a hora desde essa data (por exemplo, “4 dias, 6 horas”). Recebe um argumento opcional que é uma variável contendo a data a ser usada como ponto de comparação (sem o argumento, o ponto de comparação é agora ). Por exemplo, se blog_date for uma instância de data representando meia-noite em 1 de junho de 2006 e comment_date for uma instância de data para 08:00 em 1 de junho de 2006, o seguinte retornaria “8 horas”:

```django 
{{ blog_date|timesince:comment_date }}
```

### 9.3.43. timeuntil 

emelhante a timesince, exceto que mede o tempo de agora até a data ou datetime fornecida. Por exemplo, se hoje é 1 de junho de 2006 e conference_dateé uma instância de data que contém 29 de junho de 2006, então retornará “4 semanas”.{{ conference_date|timeuntil }} . ecebe um argumento opcional que é uma variável contendo a data a ser usada como ponto de comparação (em vez de agora ). Se from_datecontiver 22 de junho de 2006, o seguinte retornará “1 semana”:

### 9.3.44. title

Converte uma string em caixa de título, fazendo com que as palavras comecem com um caractere maiúsculo e os caracteres restantes com minúsculas. Esta tag não faz nenhum esforço para manter “palavras triviais” em minúsculas. Se value for "my FIRST post", a saída será "My First Post".

```django
{{ value|title }}
```

### 9.3.45. truncatechars

Trunca uma string se for maior que o número especificado de caracteres. As strings truncadas terminarão com um caractere de reticências traduzível (“…”). Se value for "Joel is a slug", a saída será "Joel i…".

```django
{{ value|truncatechars:7 }}
```

### 9.3.46. truncatechars_html

Semelhante a truncatechars, exceto que reconhece tags HTML. Quaisquer tags que são abertas na string e não fechadas antes do ponto de truncamento são fechadas imediatamente após o truncamento. Se value for "\<p>Joel is a slug\</p>", a saída será "\<p>Joel i…\</p>". As novas linhas no conteúdo HTML serão preservadas.

### 9.3.47. truncatewords

Trunca uma string após um certo número de palavras. Se value for "Joel is a slug", a saída será "Joel is …".

```django 
{{ value|truncatewords:2 }}
```

### 9.3.48. truncatewords_html

emelhante a truncatewords, exceto que reconhece tags HTML. Todas as tags que são abertas na string e não fechadas antes do ponto de truncamento são fechadas imediatamente após o truncamento. Isso é menos eficiente do que truncatewords, portanto, só deve ser usado quando estiver recebendo texto HTML. Se value for "\<p>Joel is a slug\</p>", a saída será "\<p>Joel is …\</p>".

### 9.3.49. unordered_list

Pega recursivamente uma lista auto-aninhada e retorna uma lista HTML não ordenada - SEM abrir e fechar as tags \<ul>.  Para ler sobre acesse : 
[unordered_list](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#unordered-list)

### 9.3.50. upper

Converte uma string em maiúsculas. Se value for "Joel is a slug", a saída será "JOEL IS A SLUG".

```django 
{{ value|upper }}
```

### 9.3.51. urlencode

Escapa um valor para uso em um URL. Se value for "https://www.example.org/foo?a=b&c=d", a saída será "https%3A//www.example.org/foo%3Fa%3Db%26c%3Dd"

```django
{{ value|urlencode }}
```

Um argumento opcional contendo os caracteres que não devem ser escapados pode ser fornecido. Se não for fornecido, o caractere '/' será considerado seguro. Uma string vazia pode ser fornecida quando todos os caracteres devem ser escapados. Por exemplo:

```django
{{ value|urlencode:"" }}
```

Se value for "https://www.example.org/", a saída será "https%3A%2F%2Fwww.example.org%2F".

### 9.3.52. urlize

Converte URLs e endereços de e-mail em texto em links clicáveis. Os links podem ter pontuação final (pontos, vírgulas, parênteses próximos) e pontuação inicial (parênteses de abertura) e urlizeainda farão a coisa certa. Se value for "Check out www.djangoproject.com", a saída será ."Check out \<a href="http://www.djangoproject.com" rel="nofollow">www.djangoproject.com\</a>"

```django
{{ value|urlize }}
```

### 9.3.53. urlizetrunc

Converte URLs e endereços de e-mail em links clicáveis ​​assim como urlize , mas trunca URLs mais longos do que o limite de caracteres fornecido. Se value for "Check out www.djangoproject.com", a saída seria 'Check out \<a href="http://www.djangoproject.com" rel="nofollow">www.djangoproj…\</a>'

```django 
{{ value|urlizetrunc:15 }}
```

### 9.3.54. wordcount

Retorna o número de palavras. Se value for "Joel is a slug", a saída será 4.

```django 
{{ value|wordcount }}
```

### 9.3.55. wordwrap

Encapsula palavras no comprimento de linha especificado.

```django
{{ value|wordwrap:5 }}
```

Se value for Joel is a slug, a saída seria:

Joel
is a
slug

### 9.3.56. yesno

Mapas valores para True, Falsee (opcionalmente) None, para as cadeias de “sim”, “não”, “talvez”, ou um mapeamento personalizado passada como uma lista separada por vírgulas, e retorna uma dessas cadeias de acordo com o valor: Se valor for True, a saída será yeah; se for Flase, será no; se for None, será maybe... Por padrão se não por passado parâmetro, será apenas yes e no.


```django
{{ value|yesno:"yeah,no,maybe" }}
```

****************************

- Também é possível criar tags e filtros personalizados. Para isto acesse: [Writing custom template tags](https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/#howto-writing-custom-template-tags)

## 9.4. Henraça de templates

A parte mais poderosa - e portanto a mais complexa - do mecanismo de template do Django é a herança de template. A herança do modelo permite que você crie um modelo básico de “esqueleto” que contém todos os elementos comuns do seu site e define os blocos que os modelos filhos podem substituir.


Para criar o modelo base, iremos criar um esquelo que irá conter todo que é comum em todoas as páginas que a herdarem, como links de bibliotecas, menus, barras laterais, rodapé, etc. 

exemplo de um arquivo base.html

```django
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <title>{% block title %}My amazing site{% endblock %}</title>
</head>

<body>
    <div id="sidebar">
        {% block sidebar %}
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
        </ul>
        {% endblock %}
    </div>

    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

Usando as TAGS **Blocks**, podemos sobreescrever o que estiver contido dento deles usando o nome que a atribuímos no arquivo que herdar o documento base. 
Exemplo de documento que herda de base. Para herdar, usamos a tag **extends**

```django
{% extends "base.html" %}

{% block title %}My amazing blog{% endblock %}

{% block content %}
{% for entry in blog_entries %}
    <h2>{{ entry.title }}</h2>
    <p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}
```

### 9.4.1. Dicas para usar a herança
- Se você usar em um modelo, {% extends %} deve ser a primeira tag de modelo nesse modelo. A herança do modelo não funcionará, caso contrário.
-  Mais tags {% block %} em seus modelos básicos são melhores. Lembre-se de que os modelos filhos não precisam definir todos os blocos pais, portanto, você pode preencher padrões razoáveis ​​em vários blocos e, em seguida, definir apenas aqueles de que precisa mais tarde. É melhor ter mais ganchos do que menos ganchos.
-  Se você estiver duplicando conteúdo em vários modelos, provavelmente significa que você deve mover esse conteúdo para um {% block %} em um modelo pai.
-  Se você precisar obter o conteúdo do bloco do template pai, a variável {{ block.super }}{{ block.super }} fará o truque. Isso é útil se você deseja adicionar ao conteúdo de um bloco pai em vez de substituí-lo completamente. Os dados inseridos usando não serão escapados automaticamente, uma vez que já foram escapados, se necessário, no modelo pai.
-  Usando o mesmo nome de modelo do qual você está herdando, pode ser usado para herdar um modelo ao mesmo tempo em que o substitui. Combinado com {% extends %}{{ block.super }}, esta pode ser uma maneira poderosa de fazer pequenas personalizações. Consulte Estendendo um modelo substituído em Como substituir modelos para obter um exemplo completo.
-  Variáveis ​​criadas fora de usando a sintaxe da tag template não podem ser usadas dentro do bloco. Por exemplo, este modelo não renderiza nada:
```django
{% block %}as{% translate "Title" as title %}
{% block content %}{{ title }}{% endblock %}
```
Para facilitar a leitura extra, você pode opcionalmente dar um nome à sua tag. Por exemplo:{% endblock %}

```django
    {% block content %}
    ...
    {% endblock content %}
```

- Em modelos maiores, essa técnica ajuda a ver quais tags {% block %} estão sendo fechadas. Finalmente, observe que você não pode definir várias blocktags com o mesmo nome no mesmo modelo. Essa limitação existe porque uma tag de bloco funciona em “ambas” direções. Ou seja, uma tag de bloco não fornece apenas uma lacuna a ser preenchida - ela também define o conteúdo que preenche a lacuna no pai . Se houvesse duas blocktags com nomes semelhantes em um modelo, o pai desse modelo não saberia qual dos conteúdos dos blocos usar.

## 9.5. Comentários

Para criar um comentário de uma linha em um modelo, use a sintaxe de comentário: .{# #}

```django
{# greeting #}hello
```


## 9.6. Arquivos Estáticos

Para usar os arquivos estáticos dentro de um template, primeiro devemos configurar corretamente o arquivo **setting.py** espeficificando o caminhos dos arquivos estáticos. Em seguida devemos ter um diretório chamado static com os arquivos dentro da aplicação. Em seguida, em todos os templates, nas primeiras linhas devemos especificar que iremos usar arquivos estáticos, carregando ele com a tag {% load %}.

```django
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Página de testes</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

<h1>Olá, mundo</h1>

</body>
</html>
```

Configurações do arquivo settings.py: 
- STATIC_URL

**************
# 10. Formulário com Django

Primeiro precisamos criar um arquivo chamado **forms.py** que irá armazenar todos os formulários da nossa aplicação. Lembrando que estes formulários podem ser gerados automáticamente de tal forma que não precisamos criar as marcações html para os formulários.

- Exemplo de um formulário

```python
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
```

## 10.1. Campos de formulários DJango

Para criar um formulário, precisamos ver todas as possibilidades de campos possível em [Campos de formulários](https://docs.djangoproject.com/en/dev/ref/forms/fields/).

Os principais campos de um formulários são:

- [BooleanField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#booleanfield)
- [CharField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#charfield)
- [ChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#choicefield)
- [DateField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#datefield)
- [EmailField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#emailfield)
- [BooleanField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#Booleanfield)
- [CharField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#Charfield)
- [TypedChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#typedchoicefield)
- [DateField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#datefield)
- [DateTimeField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#datetimefield)
- [DecimalField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#decimalfield)
- [DurationField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#durationfield)
- [FileField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#filefield)
- [FilePathField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#filepathfield)
- [FloatField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#Ffoatfield)
- [ImageField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#imagefield)
- [IntegerField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#integerfield)
- [GenericIPAddressField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#genericipaddressfield)
- [MultipleChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#multiplechoicefield)
- [TypedMultipleChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#typedmultiplechoicefield)
- [NullBooleanField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#nullbooleanfield)
- [RegexField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#regexfield)
- [SlugField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#slugfield)
- [TimeField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#timefield)
- [URLField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#urlfield)
- [UUIDField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#uuidfield)
- [ComboField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#combofield)
- [MultiValueField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#multivaluefield)
- [SplitDateTimeField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#splitdatetimefield)
- [ModelMultipleChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#modelmultiplechoicefield)
- [ModelChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#modelchoicefield)

### 10.1.1. Os principais parâmetros dos campos

Os parâmetros mais comuns que usamos para definir os campos são:

- **label='Nome'** - Define um label para o campo que será exibido com o campo
- **help_text='texto de ajuda'** - Define um pequeno texto que descreve como devemos preencher o campo
- **initial='valor'** - Define um valor inicial para o campo
- **error_messages={'required': 'Please enter your name'}** - Define um dicionários para os possíveis erros do campo. Por exemplo: o campo deve ser obrigatório (required), ou que já existe algum usuário com aquele nome (unique). Lembrando que para muitos erros já existem mensagem padrões.
- **Required** - Define que o campo é obrigatório
- **Disabled** - Define que o campo deve estar desabilitado 

Para ver mais detalhes acesse [Campos de formulários e seus argumentos](https://docs.djangoproject.com/pt-br/dev/ref/forms/fields/#core-field-arguments)

### 10.1.2. widgets

Além dos campos, temos também os **widgets** que é a forma como o html é apresentado. Cada campo acima tem um widget padrão, mas podemos alterar como o campo é exibido na tela. Para ver a lista completa de widget e seus usos, acesse: [widgts](https://docs.djangoproject.com/en/dev/ref/forms/widgets/).

Exemplos: 

```python
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
```

```python
from django import forms

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
```

Ainda podemos especificar atributos HTML dentro de um widget.attr. [widget](https://docs.djangoproject.com/pt-br/dev/ref/forms/widgets/#widget)

```python
class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    url = forms.URLField()
    comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
```

ou então atualizar posteriormente com 

```python
class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField()

    name.widget.attrs.update({'class': 'special'})
    comment.widget.attrs.update(size='40')
```

Abaixo temos um formulário que extends de um modelo, ou seja, já tem os campos previamente definidos pelo banco de dados **models.py**

```python
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category',
                  'author', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title for post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': "", 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
```

## 10.2. Exibindo o formulário em templates

Existem diversas formas de exibir um formulário, a primeira é trabalhar 100% com HTML, enquanto no outro extremo podemos inserir o formulário usando apenas um comando Python.

### 10.2.1. Formulário com HTML puro

```Django
<p><label for="id_subject">Subject:</label>
    <input id="id_subject" type="text" name="subject" maxlength="100" required></p>
<p><label for="id_message">Message:</label>
    <textarea name="message" id="id_message" required></textarea></p>
<p><label for="id_sender">Sender:</label>
    <input type="email" name="sender" id="id_sender" required></p>
<p><label for="id_cc_myself">Cc myself:</label>
    <input type="checkbox" name="cc_myself" id="id_cc_myself"></p>
```

### 10.2.2. Formulário Python-HTML

- form.campo.id_for_label - Contém o ID do campo
- form.campo.errors - Irá exibir os errors do campo caso haja algum erro ou mensagem de erro atribuída ao erro gerado.
- form.campo - Renderiza o campo 

```Django 
{{ form.non_field_errors }}
<div class="fieldWrapper">
    {{ form.subject.errors }}
    <label for="{{ form.subject.id_for_label }}">Email subject:</label>
    {{ form.subject }}
</div>
<div class="fieldWrapper">
    {{ form.message.errors }}
    <label for="{{ form.message.id_for_label }}">Your message:</label>
    {{ form.message }}
</div>
<div class="fieldWrapper">
    {{ form.sender.errors }}
    <label for="{{ form.sender.id_for_label }}">Your email address:</label>
    {{ form.sender }}
</div>
<div class="fieldWrapper">
    {{ form.cc_myself.errors }}
    <label for="{{ form.cc_myself.id_for_label }}">CC yourself?</label>
    {{ form.cc_myself }}
</div>
```

### 10.2.3. Formulário Python com menos HTML

-{{ form.subject.label_tag }} - contém todo o elemento Label, com o atributo for e o seu nome.

```Django 
{{ form.non_field_errors }}
<div class="fieldWrapper">
    {{ form.subject.errors }}
    {{ form.subject.label_tag }}
    {{ form.subject }}
</div>
<div class="fieldWrapper">
    {{ form.message.errors }}
     {{ form.message.label_tag }}
    {{ form.message }}
</div>
<div class="fieldWrapper">
    {{ form.sender.errors }}
    {{ form.sender.label_tag }}
    {{ form.sender }}
</div>
<div class="fieldWrapper">
    {{ form.cc_myself.errors }}
    {{ form.cc_myself.label_tag }}
    {{ form.cc_myself }}
</div>
```

## 10.3. Exibindo erros

Os erros de um único campo são exibidos seguindo o código abaixo, podendo ser alterado para mudar a sua forma de exibição de forma mais personalizada.

```Django
{% if form.campo.errors %}
    <ol>
    {% for error in form.campo.errors %}
        <li><strong>{{ error|escape }}</strong></li>
    {% endfor %}
    </ol>
{% endif %}
```

## 10.4. Exibindo o texto de ajuda

Muitas vexes o texto de ajuda pode ser grande e conter muitos dados, como senhas que podem conter vários critérios. Para isso, podemos usar o código abaixo para exibir o erro de forma formatada.

```Django
    {% if form.campo.help_text %}
    <p class="help">{{ form.campo.help_text|safe }}</p>
    {% endif %}
```

## 10.5. Iterando sobre um formulário

Podemos fazer um loop para iterar sobre todos os campos de um formulário. Para saber mais, além de descrição das propriedades dos campos acesse [Looping over the form’s fields](https://7xwm2drhn3gdndpwco2driejom--docs-djangoproject-com.translate.goog/pt-br/dev/topics/forms/#looping-over-the-form-s-fields)

```Django
{% for field in form %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
        {% if field.help_text %}
        <p class="help">{{ field.help_text|safe }}</p>
        {% endif %}
    </div>
{% endfor %}
```

## 10.6. Formulário 100% Python
podemos gerar um fomulário criado, usando apenas uma linha de código.

- {{ form.as_table }} will render them as table cells wrapped in &lt;tr> tags
- {{ form.as_p }} will render them wrapped in &lt;p> tags
- {{ form.as_ul }} will render them wrapped in &lt;li> tags

```Django
<form action="" method="post">
    {% csrf_token %}
    <table>
    {{ form.as_table }}
    </table>
    <input type="submit" value="Submit">
  </form>
```

{% csrf_token %} é usado para gerar uma chave de segurança para os formulário para aumentar a integridade do sistema.

## 10.7. Trabalhando com Formulários nas Views

### 10.7.1. Views Baseadas em Funções

```python
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # se esta for uma solicitação POST, precisamos processar os dados do formulário
    if request.method == 'POST':
        # crie uma instância de formulário e preencha-a com os dados da solicitação:
        form = NameForm(request.POST)
        # verifique se é válido (confere crsf):
        if form.is_valid():
            # processar os dados em form.cleaned_data conforme necessário
            # ...
            # redirecionar para um novo URL:
            return HttpResponseRedirect('/thanks/')

    # Se for um GET (ou qualquer outro método), criaremos um formulário em branco
    else:
        form = NameForm()

    context = {
        'form': form,
    }
    return render(request, 'name.html', context)
```


### 10.7.2. Views Baseadas em Classes

Para usarmos as views baseadas em classes precisamos entender a classe genérica [FormView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/#formview).

Em resumo é uma visão que exibe um formulário. Em caso de erro, exibe novamente o formulário com erros de validação; em caso de sucesso, redireciona para um novo URL.

**FormView** deve ser usado quando você precisa de um formulário na página e deseja realizar determinada ação quando um formulário válido é enviado. Ex: Ter um formulário de contato e enviar um e-mail no envio do formulário.

```python
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm

class IndexView(FormView):
  template_name = 'index.html'
  form_class = ContatoForm
  success_url = reverse_lazy('index')

  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    #trabalha a lógica do contexto
    return context

  def form_valid(self, form, *args, **kwargs):
    form.send_mail()
    messages.success(self.request, 'E-mail enviado com sucesso')
    return super(IndexView, self).form_valid(form, *args, **kwargs)

  def form_invalid(self, form, *args, **kwargs):
    messages.error(self.request, 'Erro ao enviar o e-mail')
    return super(IndexView, self).form_invalid(form, *args, **kwargs)
```

Mais sobre a classe genérica acesse [Form handling with class-based views](https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/)


## 10.8. Validando formulários

Podemos ainda validar os formulários com a classe e os parâmetros [validators](https://docs.djangoproject.com/en/dev/ref/validators/). 

Primeiro podemos criar uma função própria e usá-la para validar um valor de um campo do formulário, ou podemos usar uma função pronta para validar o nosso formulário. 

```python
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
```

então precisamos apenas chamar o argumento **validators** dentro de um campo, que serve tanto em campos de modelo, quanto campos de formulários.

```python
from django import forms

class MyForm(forms.Form):
    even_field = forms.IntegerField(validators=[validate_even])
```

ou então podemos usar um validador pronto como:

```python
from django.core.validators import MaxValueValidator, MinValueValidator

max_discount = models.FloatField( verbose_name=u'Maximum Discount', validators = [MinValueValidator(0.0)])
```

*********************************

# 11. Criando Rotas

Como criar urls dinâmicas e com expressões regulares acesse [URL dispatcher]([https://link](https://docs.djangoproject.com/en/dev/topics/http/urls/))

- Para capturar valores de um URL devemos usar colchetes angulares (<>) .
- Os valores capturados podem incluir opcionalmente um tipo de conversor como int ou str.
- Não há necessidade de adicionar uma barra inicial, porque todo URL tem isso. 

Exemplo: 
```python
from django.urls import path
from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
```

- Uma solicitação para a url /articles/2005/03/ corresponderia à terceira entrada na lista. Django chamaria a função views.onth_archive(request, year=2005, month=3).
- Uma solicitação para a url /articles/2003/ corresponderia ao primeiro padrão da lista, não ao segundo, porque os padrões são testados em ordem, e o primeiro é o primeiro teste a ser aprovado. Aqui, o Django chamaria a função views.special_case_2003(request)
- Uma solicitação para a url  /articles/2003 não corresponderia a nenhum desses padrões, porque cada padrão requer que o URL termine com uma barra.
- Uma solicitação para a url  /articles/2003/03/building-a-django-site/ corresponderia ao padrão final. Django chamaria a função views.article_detail(request, year=2003, month=3, slug="building-a-django-site").

## 11.1. Conversores de Caminhos

Os seguintes conversores de caminho estão disponíveis por padrão:

- str - Corresponde a qualquer string não vazia, excluindo o separador de caminho '/'. Este é o padrão se um conversor não estiver incluído na expressão.
- int - Corresponde a zero ou qualquer inteiro positivo. Retorna um int.
- slug - Corresponde a qualquer string slug consistindo em letras ou números ASCII, mais o hífen e os caracteres de sublinhado. Por exemplo building-your-1st-django-site.
- uuid - Corresponde a um UUID formatado. Para evitar que vários URLs sejam mapeados para a mesma página, devem ser incluídos travessões e as letras devem ser minúsculas. Por exemplo 075194d3-6885-417e-a8a8-6c931e272f00. Retorna uma UUIDinstância.
- path - Corresponde a qualquer string não vazia, incluindo o separador de caminho '/',. Isso permite que você compare com um caminho de URL completo em vez de um segmento de um caminho de URL como com str.

[Registrando conversores de caminho personalizado](https://docs.djangoproject.com/en/3.1/topics/http/urls/#registering-custom-path-converters)

### 11.1.1. Usando Expressões regulares
Se a sintaxe de caminhos e conversores não for suficiente para definir seus padrões de URL, você também pode usar expressões regulares. Para fazer isso, use re_path () em vez de path ().

Em expressões regulares Python, a sintaxe para grupos nomeados de expressão regular é (? P <nome> padrão), onde nome é o nome do grupo e padrão é algum padrão a ser correspondido.

- ^ (Início do url)
- $ (Fim do url)
- \ (Escape para valores interpretados)
- | (Ou)
- \+ (1 ou mais ocorrências)
- ? (0 ou 1 ocorrência)
- {n} (n ocorrências)
- {n,m} (Entre n e m ocorrências)
- [] (Agrupamento de caracteres)
- (?P ___) (Capture a ocorrência que corresponde a regexp ___ e atribua-a ao nome
- . (Qualquer caractere)
- \d+(Um ou mais dígitos). Observe o escape, sem correspondências de escape 'd+'literalmente
- \D+(Um ou mais não dígitos). Note escape, sem correspondências de escape 'D+'literalmente
- [a-zA-Z0-9_]+ (Um ou mais caracteres de palavra, letra minúscula, número ou sublinhado)
- \w+(Um ou mais caracteres de palavra, equivalente a [a-zA-Z0-9_]) Nota de escape, sem correspondências de escape 'w+'literalmente
- [-@\w]+(Um ou mais caracteres de palavra, traço ou arroba). Não observe nenhum escape, \wpois está entre colchetes (ou seja, um agrupamento)

|Expressão regular de url| Descrição | URLs de exemplo |
|--|--| -- |
| re_path(r'^$',.....) | String vazia (página inicial) | http://127.0.0.1/ |
| re_path(r'^stores/',.....) | Quaisquer caracteres finais | http://127.0.0.1/stores/ ou http://127.0.0.1/stores/long+string+with+12345 |
| re_path(r'^about/contact/$',.....) | Exato, sem caracteres finais | http://127.0.0.1/about/contact/ |
| re_path(r'^stores/\d+/',.... | Número | http://127.0.0.1/stores/2/ |
| re_path(r'^drinks/\D+/',.....) | Sem dígitos | http://127.0.0.1/drinks/mocha/ |
| re_path(r'^drinks/mocha|espresso/',.....) | Opções de palavra, quaisquer caracteres finais | http://127.0.0.1/drinks/mocha/ ou http://127.0.0.1/drinks/mochaccino/ ou http://127.0.0.1/drinks/espresso/ |
| re_path(r'^drinks/mocha$|espresso/$',.....) | Opções de palavras exatas, sem caracteres finais | http://127.0.0.1/drinks/mocha/ ou http://127.0.0.1/drinks/espresso/ |
| re_path(r'^stores/\w+/',.....) | Caracteres de palavras (qualquer letra minúscula ou maiúscula, número ou sublinhado) | http://127.0.0.1/stores/sandiego/ ou http://127.0.0.1/stores/1/  |
| re_path(r'^stores/[-\w]+/',.....) | Caracteres de palavra ou traço | http://127.0.0.1/san-diego/ |
| re_path(r'^state/[A-Z]{2}/',.....)| Duas letras maiúsculas | http://127.0.0.1/CA/ |


Aqui está o URLconf de exemplo anterior, reescrito usando expressões regulares

```python
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]
```

Fontes: 

- [URL dispatcher](https://docs.djangoproject.com/en/dev/topics/http/urls/#registering-custom-path-converters)
- [Url paths and regular expressions]([https://link](https://www.webforefront.com/django/regexpdjangourls.html))


***********************

# 12. Generic Views - Visões Genéricas

As views genéricas surgem para simplificar o trabalho repetitivo de criação das views, ou seja, elas contém diversos métodos prontos que nem precisamos naos preocupar em ter que escrevé-los como validação de formuláros. 

## 12.1. Base Views

As três classes a seguir fornecem muitas das funcionalidades necessárias para criar visualizações do Django. Você pode pensar nelas como visualizações pai , que podem ser usadas por si mesmas ou herdadas. Eles podem não fornecer todos os recursos necessários para projetos; nesse caso, há Mixins e visualizações baseadas em classes genéricas.

### 12.1.1. View 

A visão de base baseada na classe mestre. Todas as outras visualizações baseadas em classe herdam desta classe base. Não é estritamente uma visualização genérica e, portanto, também pode ser importada django.views.

A lista de nomes de métodos HTTP que esta visualização aceitará por padrão são: ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

Exemplo:
```python
from django.http import HttpResponse
from django.views import View

class MyView(View):
    # Responde apenas requisições GET
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
```
```python
from django.urls import path
from myapp.views import MyView

urlpatterns = [
    path('mine/', MyView.as_view(), name='my-view'),
]
```

### 12.1.2. TemplateView

Quando você precisa apenas renderizar uma página para o usuário essa com certeza é a melhor Class Based View (CBV) para o caso. Você pode editar o contexto que o template recebe sobrescrevendo a função get_context_data(). Imporante ressaltar que o TemplateView conta com o mixim ContextMixin que irá pegar automaticamente os argumentos da URL que serviu a View.

Exemplo

```python
from django.views.generic.base import TemplateView
from articles.models import Article

class HomePageView(TemplateView):

    template_name = "article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context
```

``` python
from django.urls import path
from myapp.views import HomePageView

urlpatterns = [
    path('article/<int:value>', HomePageView.as_view(), name='article'),
]
```

- No exemplo acima, a variável context contém os latest_articles e o value armazenados. 
- Temos ainda adicionar extra_context durante a url
```python
from django.views.generic import TemplateView
TemplateView.as_view(extra_context={'title': 'Custom Title'})
```

### 12.1.3. Redirect View

Redireciona para um determinado URL.

O URL fornecido pode conter formatação de string no estilo dicionário-de-strings. Os parâmetros capturados na URL do RedirectView serão repassados para a URL que o usuário está sendo redirecionado.

Atributos
- url - O URL para o qual será redirecionado, como uma string um valor vazio para gerar um erro HTTP 410 (desaparecido).
- pattern_name - O nome do padrão de URL para o qual redirecionar. A reversão será feita usando os mesmos argumentos e kwargs que são passados ​​para esta visão.
- permanent - Se o redirecionamento deve ser permanente. A única diferença aqui é o código de status HTTP retornado. Se True, então o redirecionamento usará o código de status 301. Se False, então o redirecionamento usará o código de status 302. Por padrão, permanent é False.
- query_string - Se deve passar a string de consulta GET para o novo local. Se True, então a string de consulta é anexada ao URL. Se False, então a string de consulta é descartada. Por padrão, query_stringé False.
Métodos
- get_redirect_url( * args , ** kwargs ) -  Constrói o URL de destino para redirecionamento. Os argumentos args e kwargs são argumentos posicionais e/ou de palavra-chave capturados do padrão de URL, respectivamente.

Exemplo: 
```python
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from articles.models import Article

class ArticleCounterRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)
```

```python
from django.urls import path
from django.views.generic.base import RedirectView
from article.views import ArticleCounterRedirectView, ArticleDetail

urlpatterns = [
    path('counter/<int:pk>/', ArticleCounterRedirectView.as_view(), name='article-counter'),
    path('details/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),
]
```

## 12.2. Display Views

As duas views abaixo foram desenvolvidas para exibir informações. Tipicamente essas views são as mais usadas na maioria dos projetos.

### 12.2.1. DetailView

Esta CBV é usada para renderizar um template contendo em seu contexto um objeto obtido pelo parâmetro enviado na URL. Contextualizando seria passado algo como um produto e o seu id para ser detalhado dentro do template.

É importante notar o fluxo de execução das views genéricas. O fluxo básico de execução dessa classe quando recebe uma requisição é(LEMBRANDO que todas as funções já estão implementadas, mas caso seja necessário sobreescrever alguma, devemos entender o seu contexto):

1. dispatch()
   - verifica se a classe tem um método com o nome do verbo HTTP usado na requisição. Caso não haja, um http.HttpResponseNotAllowed é retornado
2. http_method_not_allowed()
3. get_template_names()
   - retorna uma lista de templates que devem ser usados para renderizar a resposta. Caso o primeiro template da lista não seja encontrado o Django tenta o segundo e assim por diante.. 
4. get_slug_field()
   - Esta função deve retornar o nome do campo que será usado para fazer a busca pelo objeto. Por default o Django procura pelo campo slug.
5. get_queryset()
  - retornar um queryset que será usado para buscar um objeto. get_queryset() é chamado pela implementação default do método get_object(), se o get_object() for sobrescrito a chamada ao get_queryset() pode não ser realizada.
6. get_object()
   - É o responsável por retornar o objeto que será enviado para o template. Normalmente essa função não precisa ser sobrescrita.
7. get_context_object_name()
  - Depois de obter o objeto que será enviado para o template é necessário saber qual será o nome desse objeto no contexto do template, isso é feito pela função get_context_object_name(), por default o nome do objeto no template será o nome do Model.
8. get_context_data()
    - Função que captura o contexto para os templates
9.  get()
    - Obtém o objeto e coloca no contexto,
10. render_to_response()
    -  Renderiza o template.

Exemplo

Views.py
```python 
from django.views.generic.detail import DetailView
from django.utils import timezone
from articles.models import Article

class ArticleDetailView(DetailView):
    slug_field = 'titulo'
    model = Article
    context_object_name = 'meu_artigo'
    template_name = 'detalhe_artigo.html'

    get_queryset(self):
        return self.model.filter(user=self.request.user)
```
Urls.py
```python
from django.conf.urls import url
from article.views import ArticleDetailView

urlpatterns = [
    url(r'^(?P<titulo>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
]
```

detalhe_artigo.html
```Django
<h1>{{ meu_artigo.titulo }}</h1>
<p>{{ meu_artigo.conteudo }}</p>
<p>Reporter: {{ meu_artigo.user.name }}</p>
<p>Published: {{ meu_artigo.data_publicacao|date }}</p>
```


Outro exemplo na mesma lógica

```python
from django.utils import timezone
from django.views.generic.detail import DetailView
from articles.models import Article

class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
```

```python
from django.urls import path
from article.views import ArticleDetailView

urlpatterns = [
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]
```

```Django
<h1>{{ object.headline }}</h1>
<p>{{ object.content }}</p>
<p>Reporter: {{ object.reporter }}</p>
<p>Published: {{ object.pub_date|date }}</p>
<p>Date: {{ now|date }}</p>
```

### 12.2.2. ListView

Uma página que representa uma lista de objetos. Enquanto essa view está executando a variável **self.object_list** vai conter a lista de objetos que a view está utilizando. Também possui o mesmo fluxo que as demais views.

views.py
```python
from django.views.generic.list import ListView
from django.utils import timezone
from articles.models import Artigo

class ArticleListView(ListView):

    model = Artigo
    queryset = Artigo.objects.filter(status='publicado')
    template_name = 'artigo_list.html'

    # OU ENTÃO
    #def get_queryset(self, **kwargs):
    #    return Artigo.objects.filter(status='publicado')  
```
artigo_list.html
```Django
<h1>Articles</h1>
<ul>
{% for article in object_list %}
    <li>{{ article.pub_date|date }} - {{ article.headline }}</li>
{% empty %}
    <li>No articles yet.</li>
{% endfor %}
</ul>  
```

Outro exemplo 
```python
from django.utils import timezone
from django.views.generic.list import ListView
from articles.models import Article

class ArticleListView(ListView):

    model = Article
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
```

```python
from django.urls import path
from article.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
]
```

```Django
<h1>Articles</h1>
<ul>
{% for article in object_list %}
    <li>{{ article.pub_date|date }} - {{ article.headline }}</li>
{% empty %}
    <li>No articles yet.</li>
{% endfor %}
</ul>
```

## 12.3. Editing Views

As views descritas abaixo contém o comportamento básico para edição de conteúdo. 

### 12.3.1. FormView

Uma view que mostra um formulário. Se houver erro, mostra o formulário novamente contendo os erros de validação. Em caso de sucesso redireciona o usuário para uma nova URL.

- form_valid(): Chamada quando o formulário é validado com sucesso
- form_invalid(): Chamada quando o formuĺário contém erros
- get_sucess_url(): Chamada quando o formulário é validado com sucesso e retorna a url para qual o usuário deve ser redirecionado

froms.py
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
```

views.py
```python
from myapp.forms import ContactForm
from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
```

contact.html
```Django
<form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Send message" />
</form>
```

### 12.3.2. CreateView
Uma visão que exibe um formulário para a criação de um objeto, exibindo novamente o formulário com erros de validação (se houver) e salvando o objeto. Trabalham bem com MODELOS!

- O atributo fields determina quais campos do model devem estar presentes no formulário. É obrigatório especificar o atributo fields ou então o atributo form_class, nunca os dois ao mesmo tempo, pois isso geraria uma exceção ImproperlyConfigured.

urls.py
```python
from django.urls import path
from .views import AddPostCreateView

urlpatterns = [
    path('add_post/', AddPostCreateView.as_view(), name='add_post'),
]
```

 Models.py
```python
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='title')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="coding")
    likes = models.ManyToManyField(User, related_name='blogpost')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})
```

views.py Se formos usar um formulário personalizado, devemos omitir quais campos serão usados na criação em fields.
```python
class AddPostCreateView(CreateView):
    model = Post
    #form_class = PostForm
    template_name = "add_post.html"
    fields = '__all__'
```
add_post.html
```Django
{% extends 'base.html' %}
{% block title %}ADD Post{% endblock title %}
{% block content %}
<h1>Add Post</h1>
<br />
<hr />
<br />
<div class="form-group">
  <form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.media }}
    {{ form.as_p }}
    <button type="submit" class="btn btn-secondary">Post</button>
  </form>
</div>
<script>
  var name = "{{ user.id }}";
  document.getElementById("elder").value =  name;
</script>
{% endblock content %}
```

Outro exemplo

```python
from django.views.generic.edit import CreateView
from myapp.models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = ['name']
```

```Django
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
```


### 12.3.3. UpdateView

Uma visão que exibe um formulário para editar um objeto existente, exibindo novamente o formulário com erros de validação (se houver) e salvando as alterações no objeto. Isso usa um formulário gerado automaticamente a partir da classe de modelo do objeto (a menos que uma classe de formulário seja especificada manualmente).

- template_name_suffix 
    - A UpdateView exibida para uma solicitação GET usa um template_name_suffixde '_form'. Por exemplo, alterar este atributo para '_update_form' atualizando os objetos para modelo do Author faria com que o padrão do template_name fosse 'myapp/author_update_form.html'.
- object
  - Ao usar UpdateView você tem acesso ao **self.object**, que é o objeto que está sendo atualizado.


```python
from django.views.generic.edit import UpdateView
from myapp.models import Author

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']
    template_name_suffix = '_update_form'
```

```Django 
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Update">
</form>
```

### 12.3.4. DeleteView

Uma visualização que exibe uma página de confirmação e exclui um objeto existente. O objeto fornecido só será excluído se o método de solicitação for POST. Se essa visualização for obtida por meio de GET, ela exibirá uma página de confirmação que deve conter um formulário que efetua um POST no mesmo URL.

```python
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from myapp.models import Author

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
```

```Django
<form method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    <input type="submit" value="Confirm">
</form>
```


Um exemplo mais completo
```python
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from myapp.models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = ['name']

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
```

urls.py
```python
from django.conf.urls import url
from myapp.views import AuthorCreate, AuthorUpdate, AuthorDelete

urlpatterns = [
    # ...
    url(r'author/add/$', AuthorCreate.as_view(), name='author_add'),
    url(r'author/(?P<pk>[0-9]+)/$', AuthorUpdate.as_view(), name='author_update'),
    url(r'author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author_delete'),
]
```

## 12.4. Date Views

Date-based generic views são views com a função de exibir páginas com dados filtrados por datas, por exemplo: posts em um blog, notícias, consultas ao médico, etc.

### 12.4.1. ArchiveIndexView

Uma página de índice de nível superior mostrando os objetos “mais recentes”, por data. Objetos com uma data futura não são incluídos, a menos que você defina **allow_future** como **True**.

- O nome default do context_object_name é latest.
- O sufixo _archive no nome do template.
- Além da lista de objetos o contexto também contem a variável date_list contendo todos os anos que tem objetos em ordem decrescente. Isso pode ser alterado para mês ou dia usando o atributo date_list_period. Isso se aplica a todas as Data-based generic views.
- date_list: Um objeto QuerySet que contém todos os anos que possuem objetos disponíveis de acordo com queryset, representados como datetime.datetimeobjetos, em ordem decrescente.

urls.py
```python
from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from myapp.models import Article

urlpatterns = [
    path('archive/',
         ArchiveIndexView.as_view(model=Article, date_field="pub_date"),
         name="article_archive"),
]
```

```Django
<ul>
    {% for article in latest %}
        <li>{{ article.pub_date }}: {{ article.title }}</li>
    {% endfor %}
</ul>
```

### 12.4.2. YearArchiveView

Uma página de arquivo anual mostrando todos os meses disponíveis em um determinado ano. Objetos com uma data futura não são exibidos, a menos que você defina **allow_future** como **True**.

- make_object_list
  - Um booleano que especifica se é necessário recuperar a lista completa de objetos deste ano e passá-los para o modelo. Se True, a lista de objetos será disponibilizada para o contexto. Se False, o Nonequeryset será usado como a lista de objetos. Por padrão, é False
- get_make_object_list() 
  - Determine se uma lista de objetos será retornada como parte do contexto. Retorna make_object_listpor padrão.
- date_list
  - Um QuerySetobjeto que contém todos os meses que têm objetos disponíveis de acordo com queryset, representados como datetime.datetimeobjetos, em ordem crescente.
- year
  - Um dateobjeto que representa o ano determinado.
- next_year
  - Um dateobjeto que representa o primeiro dia do próximo ano, de acordo com allow_emptye allow_future.
- previous_year
  - Um dateobjeto que representa o primeiro dia do ano anterior, de acordo com allow_emptye allow_future.
- Usa um padrão template_name_suffixde_archive_year

```python
from django.views.generic.dates import YearArchiveView
from myapp.models import Article

class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
```

```python
from django.urls import path
from myapp.views import ArticleYearArchiveView

urlpatterns = [
    path('<int:year>/',
         ArticleYearArchiveView.as_view(),
         name="article_year_archive"),
]
```

```Django
<ul>
    {% for date in date_list %}
        <li>{{ date|date }}</li>
    {% endfor %}
</ul>

<div>
    <h1>All Articles for {{ year|date:"Y" }}</h1>
    {% for obj in object_list %}
        <p>
            {{ obj.title }} - {{ obj.pub_date|date:"F j, Y" }}
        </p>
    {% endfor %}
</div>
```

### 12.4.3. Outras DateViews

Existem também outras que seguem a mesma lógica de implementação com os mesmos atributos e métodos como:
- [MonthArchiveView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/#montharchiveview)
  - Uma página de arquivo mensal mostrando todos os objetos em um determinado mês.
- [WeekArchiveView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/#weekarchiveview)
  - Uma página de arquivo semanal mostrando todos os objetos em um determinado mês.
- [DayArchiveView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/#dayarchiveview)
  - Uma página de arquivo do dia mostrando todos os objetos em um determinado dia.
- [TodayArchiveView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/#todayarchiveview)
  - Uma página de arquivo do dia mostrando todos os objetos de hoje . É exatamente igual a django.views.generic.dates.DayArchiveView, exceto que a data de hoje é usada em vez dos argumentos year/ month/ day.
- [DateDetailView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/#datedetailview)
  - Uma página que representa um objeto individual. Se o objeto tiver um valor de data no futuro, a visualização lançará um erro 404 por padrão, a menos que você defina allow_futurecomo True.

Fontes : [class-based-views-django](http://pythonclub.com.br/class-based-views-django.html)
*******************************************









