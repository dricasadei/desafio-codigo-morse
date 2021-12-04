# Introdução
Esse projeto foi realizado como parte do Processo Seletivo do CESAR.

# Desafio
O desafio proposto foi criar um repositório no github ou gitlab e o projeto é criar uma tradução de código morse. Por exemplo: o cliente irá enviar o código morse ".-" o servidor vai receber estas informações e traduzir para a letra correspondente, no caso, "A".
Nesse momento não é necessário se preocupar com gramática, concordância ou frases complexas.
O objetivo do desafio é ser definida uma arquitetura que resolva a solução, utilizando o código morse como protocolo de comunicação e pensando em como esta solução poderia ser criada de forma que fosse o mais escalável possível.

# Como executar:
No *terminal*, é necessário executar os comandos abaixo:
1. Para ativar o ambiente virtual, nesse momento, para conferir se ocorreu tudo certo, obeserve que seu terminal terá um prefixo *venv*.
   ```
   source venv/bin/activate
   ```
2. Use o pip, que é o gerenciador de pacotes do Python, para instalar o micro framework Flask.
   ```
   pip install flask
   ``` 
3. Comando python para configurar o banco de dados sqlite3. Assim que terminar a execução, um novo arquivo arquivo chamado *database.db* aparecerá no diretório *desafio-codigo-morse*
   ```
   python init_db.py
   ```
4. Comando para informar ao Flask onde encontrar o aplicativo (nesse caso o arquivo app.py).
   ```
   export FLASK_APP=app
   ```
5. Comando para executar o modo de desenvolvimento.
   ```
   export FLASK_VENV=development
   ```
6. Comando para executar o aplicativo. Assim que estiver em execução no terminal, aparecerá algumas informações, inclusive o endereço e porta localhost: <http://127.0.0.1:5000>, através da qual no *navegador* será possível acessar a aplicação.
   ```
   flask run
   ```

# Detalhes dos arquivos:

### app.py
Nesse arquivo Python tem os imports necessários, como o banco de dados (**sqlite3**), Flask entre outros. 
A função *get_db_connection()* conecta o banco de dados.
No arquivo contém também o algoritmo do tradutor de código morse.
Em seguida, a função *def home()* que cuida da interface: dados do cliente/banco de dados.
Por último, o método *render_template* que renderiza os arquivos html indicados.

### init_db.py
Nesse arquivo Python ocorre a importação do módulo de banco de dados, o *sqlite3*. Em seguida, é aberto uma conexão no arquivo *database.db*. Por fim, o método *executescript()* irá executar algumas instruções SQL, criando as tabelas necessárias.

### schema.sql
Nesse arquivo SQL é definida a tabela *morseCodes*, que é composta pelas colunas:
* **id** - chave primária, preenchida automaticamente pelo método: AUTOINCREMENT.
* **code** - que armazena o código morse digitado pelo cliente.
* **translation** - que armazena a tradução do código morse retornada pelo algoritmo.

### base.html
Nesse arquivo HTML tem a base da página WEB, com algumas tags como: 
* *meta* -  essa tag fornece informações para o navegador WEB.
* *link* - vincula os arquivos CSS do Bootstrap.
* *script* - são links para o código JavaScript que permitem algumas funcionalidades adicionais.
* *cógigos do modelo Jinja* (mecanismo de templates da WEB, padrão no Flask) - como:
    - {% block title %} {% endblock %}​​​: substituto para não precisar reescrever a seção <head> inteira, esse bloco reserva um espaço reservado para um título.
    - {% block content %} {% endblock %}​​​: bloco que posteriormente será substituído pelo conteúdo, podendo ser herdado desse arquivo, base.html.
    - {% for message in get_flashed_messages() %} - bloco que exibe as mensagens de erro, por exemplo, quando o cliente aperta o botão Traduzir (submit), com o form vazio.

### home.html
Nesse arquivo HTML é definido através do bloco de código do modelo Jinja algumas heranças do arquivo base.html, como as definições da tag meta.
Em seguida é definido a aparência da página, sendo usado uma *textarea* e suas definições. E um botão, traduzir.

### translation.html
Nesse arquivo HTML é definido a forma e as definições de exibição da página e exibição do resultado da tradução do código morse. Foram usados alguns recursos do Booststrap como o *breadcrumb*. Também foi adicionado um botão, *Traduzir outro código*, que ao pressionado, retorna a página home(raiz) para o cliente poder digitar outro código morse para ser traduzido.

### script.js
Nesse arquivo JS é definido a função *submitOnEnter(event)* e a condição *if* que verifica se o cliente digitou algum código para ser traduzido, e ao ser pressionado a tecla *Enter* o código digitado é traduzido. Dessa forma, o código será traduzido se o cliente apertar o *botão Traduzir* ou a *tecla Enter*.

# Arquitetura utilizada:
Para esse projeto foi utilizado por base a arquitetura Model-View-Controller (MVC). Onde a camada *Model* corresponde ao banco de dados, no caso, optei pelo sqlite. O projeto poderia ser implementado sem a utilização de um banco de dados, porém para que a arquitetura estivesse completa, criei e implementei o arquivo *schema.sql*.
A camada *Controller*  implementada através do arquivo *app.py* gerencia as requisições, fazendo a mediação entre as camadas *Model* e *View*.
A camada *View* implementada através dos arquivos *html*, no diretório *templates*, cuida da interface com o cliente, e exibe as saídas fornecidas pelo Controller.

# Testes de uso:
O código morse utiliza somente os caracteres **.** (ponto) e **-** (traço), utilizando **/** (barra) como separador entre letras.

Abaixo alguns códigos que podem ser testados:

| Código Morse                                   	| Tradução       	|
|------------------------------------------------	|----------------	|
| ---/.-../.-                                    	| OLA            	|
| .-/-../.-./../.-/-./.-                         	| ADRIANA        	|
| ...././.-../.-../---/.--/---/.-./.-../-..      	| HELLOWORLD     	|
| -----/.----/..---/...--/....-/.....            	| 012345         	|
| .-/-../.-./../.-/-./.-/-.-./.-/.../.-/-.././.. 	| ADRIANACASADEI 	|
| -----/---../-.././-.././--.././--/-.../.-./--- 	| 08DEDEZEMBRO   	|

![Vocabulário do Código Morse: ](/static/img/morse-vocabulario.png)
# Imagens de tela:

![Página incial](/static/img/img1.png)
![Página incial](/static/img/img2.png)
![Página incial](/static/img/img3.png)