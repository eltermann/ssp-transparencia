![screenshot](https://cloud.githubusercontent.com/assets/569111/15650275/bd1b5a26-264d-11e6-8feb-88fcb752d4c6.png)

A Secretaria de Segurança Pública do estado de São Paulo disponibiliza dados sob a forma de tabelas em páginas web.

O presente software realiza a chamada "raspagem" desse conteúdo. Seu objetivo é automatizar a navegação nas páginas e gerar arquivos em um formato acessível para análise.


## Baixando o conteúdo extraído

Para facilitar o acesso aos dados, o conteúdo extraído é disponibilizado para download no link abaixo:

* https://github.com/eltermann/ssp-transparencia/releases/latest

## Campos disponíveis

### Campos iniciados em "nav_"

![nav](https://cloud.githubusercontent.com/assets/569111/15796923/accfbf1a-29de-11e6-8f98-881d9076157b.png)

Representam o ano e mês.

### Campos iniciados em "tabela_"

![tabela](https://cloud.githubusercontent.com/assets/569111/15796924/acecdd34-29de-11e6-9976-3077238fa967.png)

Representam os campos da tabela.

### Campos iniciados em "bo_"

![bo](https://cloud.githubusercontent.com/assets/569111/15796938/eab5b62c-29de-11e6-82fe-4bccd4e4430e.png)

Representam informações contidas no BO.

### Campos iniciados em "bo_primeira_natureza_"

![bo_primeiranatureza](https://cloud.githubusercontent.com/assets/569111/15796909/64477184-29de-11e6-84e0-f344d39a4f8e.png)

Representam informações **apenas** da primeira natureza do BO.

### Campos iniciados em "bo_primeira_vitima_"

![bo_primeiravitima](https://cloud.githubusercontent.com/assets/569111/15796910/6463a264-29de-11e6-8faf-c52832dd9dcf.png)

Representam as informações **apenas** da primeira vítima do BO.


## Executando o programa

### Requerimentos

* python 2.7
* scrapy 1.1.0

### Comandos

No Linux, depois de clonar o projeto, os passos são:

* $ cd ssptransparencia
* $ scrapy crawl homicidio-doloso -t csv -o homicidio-doloso.csv
* $ scrapy crawl latrocinio -t csv -o latrocinio.csv
* $ scrapy crawl lesao-morte -t csv -o lesao-seguida-de-morte.csv



## Dúvidas e contato

* felipe.eltermann@gmail.com
