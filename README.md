# Bolivia Figurinhas

Bem-vindo ao **Bolivia Figurinhas**! Este é um projeto focado em coleções de figurinhas, onde os usuários podem navegar, colecionar e interagir com figurinhas da Bolívia e de outros temas.

## Tecnologias Utilizadas

### Backend
- **FastAPI**: Framework de alto desempenho para desenvolvimento de APIs em Python.
- **Poetry**: Gerenciador de dependências para Python, facilitando a instalação e organização dos pacotes.

### Frontend
- **React**: Biblioteca JavaScript para a construção de interfaces de usuário dinâmicas e interativas.

## Estrutura do Projeto

- **Backend**: Diretório onde estão localizados os arquivos da API construída com FastAPI. Inclui os endpoints para manipulação de figurinhas, autenticação de usuários e gerenciamento dos dados das coleções.
- **Frontend**: Diretório com o código do React, responsável pela interface do usuário e pela interação com a API.

## Instalação e Configuração

### Pré-requisitos

- Python 3.8+
- Node.js 14+
- Poetry
- npm ou yarn (para gerenciar os pacotes do React)

### Backend (FastAPI + Poetry)

1. Clone o repositório:
   	```bash
   	git clone https://github.com/seu-usuario/boliviafigurinhas.git
      cd bolivia-figurinhas/backend
  
2.	Instale as dependências do projeto usando o Poetry:
  	```bash
  	poetry install

3.	Execute o servidor:
  	```bash
  	poetry run uvicorn main:app --reload

Frontend (React)

1.	Navegue até a pasta do frontend:
  	```bash
  	cd ../frontend
   
2.	Instale as dependências do projeto:
  	```bash
  	npm install
  
  ou, se estiver usando yarn:
  	```bash
  	yarn install
   
3.	Execute o frontend:
  	```bash
  	npm start

Estrutura de Diretórios

•	backend/: Contém a API desenvolvida com FastAPI.
•	frontend/: Contém o projeto React.
•	README.md: Arquivo de documentação do projeto.

Contribuição

1.	Faça um fork do projeto.
2.	Crie uma branch para sua feature (git checkout -b minha-feature).
3.	Faça o commit das suas mudanças (git commit -am 'Adiciona nova feature').
4.	Envie para a branch (git push origin minha-feature).
5.	Abra um Pull Request.

Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Sinta-se à vontade para contribuir, relatar problemas ou sugerir melhorias! :sparkles:

Esse `README` inclui instruções para instalação, execução e contribuição no projeto, e descreve a estrutura geral das tecnologias usadas. Personalize conforme necessário para refletir o estado atual do projeto ou outros detalhes que queira destacar.
