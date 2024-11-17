# Portal F1


O Portal F1 é uma aplicação Full Stack que combina análise de dados avançada e visualizações dinâmicas para explorar a história da Fórmula 1. Utilizando dados reais e uma interface interativa, o projeto permite aos usuários mergulhar em estatísticas, gráficos e curiosidades da principal categoria do automobilismo mundial.

Este projeto abrange desde a coleta e processamento de dados até o desenvolvimento completo de uma interface amigável para explorar estatísticas históricas. É uma solução que integra **tecnologias de back-end robustas** e **design responsivo**, oferecendo insights detalhados sobre corridas, pilotos e circuitos.

---
## Índice
1. [Introdução](#introdução)
2. [Etapas Realizadas](#etapas-realizadas)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Galeria de Demonstrações](#galeria-de-demonstrações)
5. [Credenciais e Configuração](#credenciais-e-configuração)
6. [Próximos Passos e Backlog](#próximos-passos-e-backlog)
7. [Agradecimentos e Créditos](#agradecimentos-e-créditos)

## Etapas Realizadas

### 1. Análise de Dados e Criação do Banco de Dados
A base de dados utilizada se encontra no [Kaggle](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)
e possui as seguintes informações:
- circuits - Todos os circuitos onde ocorreram um grande prêmio
- constructor_results - Resultados de todos os construtores registrados
- constructor_standings - Pontuação final do campeonato de construtores
- constructors - Todas as equipes que ja foram registradas
- driver_standings - Pontuação final do campeonato de pilotos
- drivers - Todos os pilotos que correram na categoria
- lap_times - Tempos de voltas registrados
- pit_stops - Registro das paradas no pit stop
- qualifying - Registro das sessões de qualificação
- races - Informaçoes de todas as corridas registradas
- results - Resultado geral das corridas
- seasons - Registro de todos os anos que houveram campeonato
- sprint_results - Resultado geral das corridas sprint
- status - Status final da corrida



1. Analisamos os dados do Kaggle e identificamos registros nulos.
2. Implementamos as seguintes estratégias para tratar esses dados:
   - **Dados faltantes** foram preenchidos com valores padrão (`0` para números e espaço em branco para strings).
   - **Dados inexistentes** foram reorganizados em tabelas auxiliares para evitar inconsistências. Por exemplo:
     - Dividimos os tempos de qualificação (`q1`, `q2`, `q3`) em tabelas específicas, com uma relação direta com a tabela principal. 
      
        | qualifyingid | ... | q1  | q2 | q3  |
        |--------------|-----|-----|----|-----|
        | 40           | ... | 1:36.388 | \N  | \N |
        | 14           | ... | 1:26.891| 1:26.413| \N |
        | 9            | ... | 1:26.919 | 1:26.164 | 1:29.593 |
    - Então foram criadas três tabelas nomeadas q1, q2 e q3 possuindo os campos ID, tempo de classificação, e a chave estrangeira que aponta para  tabela qualifying.
         - Tabela q1 
        
        | id | time | qualifying_id |
        |----|------|---------------|
        | 1  | 1:36.388 | 40            |
        | 2  | 1:26.891 | 14            |
        | 3  | 1:26.919 | 9             |

         - Tabela q2
    
        | id | time | qualifying_id |
        |----|------|---------------|
        | 1  | 1:26.413 | 14            |
        | 2  | 1:26.164 | 9             |

         - Tabela q3

        | id | time | qualifying_id |
        |----|------|---------------|
        | 1  | 1:29.593 | 9             |

  



Para todas as tabelas foi configurada uma chave primária única denominada id.


### 2. Criação da Aplicação com Django
#### Banco de Dados
- Modelagem de todas as tabelas com **chaves primárias e estrangeiras**.
- Scripts para importar os dados do CSV para o PostgreSQL.

#### Backend
- Implementamos as principais views para:
  - Exibir listas (pilotos, circuitos).
  - Mostrar dashboards detalhados de estatísticas.
- APIs configuradas para fornecer dados para gráficos.

#### Frontend
- Utilizamos templates HTML com CSS customizado para criar:
  - Home Page com carrossel e estatísticas.
  - Páginas detalhadas de pilotos e circuitos.
  - Seções dinâmicas, como dashboards interativos.
  
- Template para a sessão de blog: [CARSERV FREE CSS TEMPLATE](https://www.free-css.com/free-css-templates/page291/carserv)
- Template para a sessão de dashboards: [Gradiente Able](https://django-gradient-pro.onrender.com/#)

## Galeria de Demonstrações

### Home Page
![Home Page com estatísticas e carrossel](upload_images_project%2Fblog%20f1%20site.png)

### Página Analytics
#### Página Inicial
![Página inicial do Analytics](upload_images_project%2FAnalytics%20home%20page.png)

#### Listagem de Pilotos
![Tabela de pilotos](upload_images_project%2FDriver%20List.png)

#### Dashboard de Piloto
![Dashboard de um piloto](upload_images_project%2FDriver%20Detail.png)

#### Gráficos
- **Resultados por Temporada**
  ![Gráfico 1](upload_images_project%2FGr%C3%A1fico%201.png)

- **Pontos por Temporada**
  ![Gráfico 2](upload_images_project%2FGr%C3%A1fico%202.png)

#### Listagem de Circuitos
![Tabela de circuitos](upload_images_project%2FCircuit%20List.png)

#### Dashboard de Circuito
![Dashboard de circuito](upload_images_project%2FCircuit%20Dashboard.png)

## Credenciais e Configuração

1. **Criação do Arquivo `.env`:**  
- Certifique-se de criar um arquivo `.env` na raiz do projeto. Inclua as variáveis necessárias, como:
  ```
    DEBUG=True
    SECRET_KEY=sua-chave-secreta-aqui
    SERVER=localhost
    SERVER_2=127.0.0.1
    SERVER_3=localhost
    TZ=America/Sao_Paulo
    NAME_DB=nome_do_banco
    USER_DB=user_do_banco
    PASSWORD_DB=sua_senha_do_user_do_banco
    HOST_DB=localhost
    PORT_DB=_escolha_sua_porta
    SCHEMA_DB=public
     ```
2. **Instalação das Dependências:**  
   - Rode o comando `pip install -r requirements.txt` para instalar as bibliotecas necessárias.

3. **Migrações do Banco:**  
   - Execute as migrações com `python manage.py migrate`.

4. **Carga Inicial de Dados:**  
   - Use os scripts disponíveis na pasta `upload_data` para popular o banco de dados.

## Próximos Passos e Backlog

- Finalizar a seção **Photo Gallery** e **Circuits**, adicionando imagens de carros históricos, informações das pistas e traçados.
- Expandir os gráficos do **dashboard de pilotos** para incluir métricas adicionais, como:
  - Desempenho em qualificações.
- Melhorar a seção de circuitos com:
  - Gráficos de desempenho por equipe em cada circuito.
- Criar uma funcionalidade de **comparação direta** entre dois pilotos ou equipes.
- Criar listagem de corridas mostrando os resultados e informações gerais

## Agradecimentos e Créditos

- **Base de Dados:**  
  [Fórmula 1 World Championship Dataset no Kaggle](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020).

- **Templates Utilizados:**  
  - [CARSERV FREE CSS TEMPLATE](https://www.free-css.com/free-css-templates/page291/carserv)
  - [Gradiente Able](https://django-gradient-pro.onrender.com/#).

- **Ferramentas:**  
  - Python e Django para o back-end.
  - PostgreSQL para o banco de dados.
  - HTML/CSS/JavaScript para o front-end.
> Diretório

A estrutura do código segue

```
bash
< PROJECT ROOT >
   |
   |-- portal_f1/                           # Raiz do projeto
   |    |-- applications/                   # Dentro dessa pasta estão as aplicações Analytics e Blog do Django
   |        |-- analytics/                  # Aplicação Analytics, com models, views , APIs e templates individuais
                |-- filters                 # Filtros de pilotos e circuitos
                |-- migrations              # Arquivos de alteração do banco de dados
                |-- models                  # Pasta da definição dos bancos de dados                     
                |-- static                  # Arquivos JavaScript das APIs dos gráficos
                |-- templates               # Interfaces Django do Analytics
                |-- views                   # Pasta onde define as lógicas das páginas analytics
   |        |-- blog/                       # Aplicação da página do blog, com templates e views referentes
                |-- templates               # Interfaces Django do Blog
                |-- views                   # Pasta onde define as lógicas das páginas do blog
   |    |-- core/
   |        |-- wsgi.py                     # Starta a aplicação em produção
   |        |-- urls.py                     # Define as urls permitidas
            |-- settings.py                 # Configurações do Projeto
   |    |-- core_access                     # Aplicação de controle de usuarios
   |    |-- core_log                        # Aplicação para salvar o log de alterações do sistema
   |    |-- core_pages                      # Aplicação que contem páginas que são comuns para o projeto
   |    |-- core_registration               # Aplicação que contem os cadastros gerais do sistema
   |    |-- gunicor n                       # Controle para start da aplicação
   |    |-- static                          # Arquivos estaticos
   |    |-- staticfiles                     # Pasta onde o django coloca todos os arquivos estáticos através do comando python manage.py collectstatic
   |    |-- .env                            # Inject Configuration via Environment
   |    |-- manage.py                       # Start the app - Django default start script
   |    |-- README.md                       # Arquivo de descrição
   |    |-- requirements.txt                # Bibliotecas necessárias
   |-- upload_data                          # Scripts que geram os arquivos csv para serem importados no postgreSQL
   |-- upload_images_project                # Pasta de prints do site em funcionamento para o README
   |-- ************************************************************************
```
<br />