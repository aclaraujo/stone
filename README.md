# Dados Abertos

Insights sobre os arquivos Empresas e Socios do [Portal de Dados Abertos ](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj)

## Visão Geral

### Arquitetura Geral

![image](https://github.com/aclaraujo/stone/assets/45980136/98a50ad1-4dcc-43ad-9933-72e27861b10b)

O projeto foi desenvolvido utilizando os seguintes componentes ou soluções:

1. Python - para a escrita dos jobs de extração, carga e tratamento dos dados
2. MongoDB - para o armazenamento dos dados
3. MongoDB-Express para visualização dos dados

Todos os componentes são executados por meio de container Docker. Um projeto em docker-compose orquestra a criação e execução dos containers

### Arquitetura de dados
* O projeto foi desenvolvido utilizando o padrão "Arquitetura de Medalhões". Dessa forma, o armazenamento e disponibilização de dados está organizado da seguinte maneira:

#### Bronze
* Banco de dados responsável por armazenar os dados brutos (raw). Os dados são extraídos das fontes e inseridos no armazenamento da forma mais original possível, evitando assim perda de dados ou introdução de inconssistência. Outra função para esse banco é armazenar dados históricos.
* Possui as tabelas: empresas e socios

#### Silver
* Banco de dados responsável por armazenar os dados em uma forma mais estruturada, porém ainda próxima do dado origem. Nesse modelo são realizadas as primeiras validações de qualidade e adequações nos modelos de dados, tornando-os mais próximos dos requisitos analíticos.
* Possui as tabelas: empresas e socios

#### Gold
* Nesse banco de dados, as tabelas refletem as necessidades analíticas da organização, frequetemente apresentando uma modelagem multidimensinal.
* Antes de sua ingestão, todas as validações e verificações de qualidade devem ser realizadas.
* Outra tarefa que pode ser executada nesse banco é o enriquecimento de dados a apartir de outra fontes, sejam internas ou externas a organização.
* Possui a tabela: fato_socios

### Requisitos para execução
1. Possuir o [Docker](https://docs.docker.com/desktop/install/linux-install/) instalado
2. Mínimo disponível: 10Gb RAM

## Executando
1. Clonar este repositório
2. Entrar na pasta stone/docker e digitar
   ```docker-compose up```
4. Aguardar os serviços serem iniciados e a execução do pipeline de ingestão dos dados
5. Após o serviço ser exectado a seguinte mensagem deverá aparecer no console
   ```jobs-1 exited with code 0```
7. No navegador acesse [http://localhost8081](http://localhost8081) para acessar as tabelas criadas
8. Faça login com o usuário e senha admin:pass
9. Para visualizar o resultado final da execução, acessa o banco gold e coleção fato_socios
