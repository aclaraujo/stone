# Dados Abertos

Insights sobre os arquivos Empresas e Socios do portal de dados abertos

## Visão Geral

### Arquitetura

![image](https://github.com/aclaraujo/stone/assets/45980136/98a50ad1-4dcc-43ad-9933-72e27861b10b)

### Arquitetura de dados
O projeto foi desenvolvido utilizando o padrão "Arquitetura de Medalhões". Dessa forma, o armazenamento e disponibilização de dados está organizado da seguinte maneira:

#### Bronze
Banco de dados responsável por armazenar os dados brutos (raw). Os dados são extraídos das fontes e inseridos no armazenamento da forma mais original possível, evitando assim perda de dados ou introdução de inconssitência. Outra função para esse banco é armazenar dados históricos.

#### Silver
Banco dados responsável por armazenar os dados em uma forma mais estruturada, porém ainda próxima do dado origem. Nesse modelo são realizadas as primeiras validações de qualidade e adequações nos modelos de dados, tornandoo-os mais próximos dos requisitos analíticos.

#### Gold
Nesse banco de dados, as tabelas refletem as necessidades analíticas da organização, frequetemente apresentando uma modelagem multidimensinal. Antes de sua ingestão, todas as validações e verificações de qualidade devem ser realizadas. Outra tarefa que pode ser executada nesse banco é o enriquecimento dados a apartir de outra fontes, sekam internas ou externas.


### Requisitos para execução
1. Possuir o [Docker](https://docs.docker.com/desktop/install/linux-install/) instalado
2. Mínimo disponível: 10Gb RAM

## Executando
1. Clonar este repositório
2. Entrar na pasta stone/docker e digitar docker-compose up
3. Aguardar os serviços serem iniciados e a execução do pipeline de ingestão dos dados
4. Após o serviço ser exectado uma mensagem como jobs-1 exited with code 0 deverá ser exibido no console
5. No navegador acesse [http://localhost8081](http://localhost8081) para acessar as tabelas criadas
6. Faça login com o usuário e senha admin:pass
7. Para visualizar o resultado final da execução, acessa o banco gold e coleção fato_socios
