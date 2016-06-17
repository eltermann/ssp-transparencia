[![DOI](https://zenodo.org/badge/20978/eltermann/ssp-transparencia.svg)](https://zenodo.org/badge/latestdoi/20978/eltermann/ssp-transparencia)

A Secretaria de Segurança Pública do estado de São Paulo disponibiliza dados sob a forma de tabelas em páginas web.

O presente software realiza a chamada "raspagem" desse conteúdo. Seu objetivo é automatizar a navegação nas páginas e gerar arquivos em um formato acessível para análise.


## Baixando o conteúdo extraído

Para facilitar o acesso aos dados, o conteúdo extraído é disponibilizado para download no link abaixo:

* https://github.com/eltermann/ssp-transparencia/releases/latest

## Campos disponíveis

### Tabela de BOs (bos.csv)

* id: identificador do BO (referenciado nas outras tabelas)
* nav_natureza: natureza da ocorrência na navegação (ex: homicidio-doloso, latrocinio, etc.)
* nav_ano: ano na navegação das páginas
* nav_mes: mês na navegação
* nav_menu_adicional: em alguns casos (ex: morte-suspeita), indica o conteúdo do menu adicional
* tabela_numero_bo: número do BO conforme aparece na tabela
* tabela_tipo_bo: tipo do BO conforme aparece na tabela
* tabela_cidade: cidade conforme aparece na tabela
* tabela_delegacia_elaboracao: delegacia de elaboração conforme aparece na tabela
* tabela_data_fato: data do fato conforme aparece na tabela
* tabela_data_registro: data do registro conforme aparece na tabela
* tabela_endereco_fato: endereço do fato conforme aparece na tabela
* bo_dependencia: dependência conforme aparece na página do BO
* bo_numero: número do BO conforme aparece na página do BO
* bo_iniciado: horário em que foi iniciado, conforme aparece na página do BO
* bo_emitido: horário em que foi emitido, conforme aparece na página do BO
* bo_autoria: autoria do BO, conforme aparece na página do BO
* bo_complementar_ao_rdo: informação sobre o BO ser complementar, conforme aparece na página do BO
* bo_desdobramentos: desdobramentos, conforme aparece na página do BO
* bo_local_linha1: primeira linha de informações do local da ocorrência, conforme aparece na página do BO
* bo_local_linha2: segunda linha de informações do local da ocorrência, conforme aparece na página do BO
* bo_tipo_local: tipo do local, conforme aparece na página do BO
* bo_circunscricao: circunscrição, conforme aparece na página do BO
* bo_ocorrencia: indicação do momento da ocorrência, conforme aparece na página do BO
* bo_comunicacao: data e hora da comunicação da ocorrência, conforme aparece na página do BO
* bo_elaboracao: data e hora da elaboração do boletim, conforme aparece na página do BO
* bo_flagrante: indicador se houve flagrante, conforme aparece na página do BO
* bo_exames_requisitados: exames requisitados, conforme aparece na página do BO
* bo_solucao: solução, conforme aparece na página do BO
* bo_numero_naturezas: quantidade de naturezas envolvidas (detalhadas na tabela "naturezas-envolvidas.csv")
* bo_numero_vitimas: quantidade de vítimas (detalhadas na tabela "vitimas.csv")

### Tabela de Vítimas (vitimas.csv)

* bo_id: identificador do BO
* nome: Nome da vítima
* autor_vitima: Indicador se pessoa é "Vítima" ou "Autor e Vítima"
* tipo: ex: Vítima Fatal
* rg: número do RG
* natural_de: cidade de origem da vítima
* nacionalidade: nacionalidade da vítima
* sexo: sexo da vítima
* nascimento: data de nascimento da vítima
* idade: idade de vítima
* estado_civil: estado civil da vítima
* profissao: profissão da vítima
* instrucao: nível de instrução da vítima
* cutis: informação sobre a pele da vítima
* naturezas_envolvidas: naturezas envolvidas relacionadas à vítima


### Tabela de Naturezas envolvidas (naturezas-envolvidas.csv)

* bo_id: identificador do BO
* especie: espécie da natureza envolvida (ex: "Título II - Patrimônio (arts. 155 a 183)")
* linha1: primeira linha de informações da natureza (ex: "Roubo (art. 157)")
* linha2: segunda linha de informações da natureza (ex: "Consumado")


## Executando o programa

### Requerimentos

* python
* scrapy 1.1.0

### Comandos

No Linux, depois de clonar o projeto, os passos são:

#### Executando o scrapy diretamente
* $ cd ssptransparencia
* $ scrapy crawl ssptransparencia -a target_dir=/caminho/para/destino


## Autores

* Felipe Eltermann Braga - FEEC/UNICAMP - http://lattes.cnpq.br/9016415024825203
* Silas Nogueira de Melo - IG/UNICAMP - http://lattes.cnpq.br/9875457749739729


## Dúvidas e contato

* felipe.eltermann@gmail.com
