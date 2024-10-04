# Vehicle Plate Recognition API
- Esta API em Python utiliza a inteligência artificial do Gemini para detectar e reconhecer placas de veículos a partir de fotos. A API verifica se a placa já está cadastrada no sistema e oferece funcionalidades para gerenciamento de veículos e usuários. O projeto foi desenvolvido com Flask, SQLAlchemy, Google Generative AI e JWT.
- Deploy do front que testa a aplicação: https://vehicle-consultation.vercel.app 

## Funcionalidades
- Reconhecimento de Placas: Detecta e identifica placas de veículos em imagens utilizando a API Gemini.
- Verificação no Sistema: Verifica se a placa detectada está cadastrada no sistema.
- Gerenciamento de Veículos: Adiciona novos veículos ao banco de dados e retorna informações sobre veículos já cadastrados.
- Gerenciamento de Administrador: login de usuários administradores, com autenticação baseada em JWT.
- Endpoint de status da API: Verifica o estado da API e se está pronta para atender requisições.
  
## Estrutura do Projeto
- A estrutura do projeto é organizada da seguinte forma:
````
  ├── app/
  │   ├── __init__.py            # Inicializa o aplicativo Flask
  │   ├── routes/                # Define as rotas da API
  │   ├── models/                # Modelos de banco de dados (Vehicle, User)
  │   ├── db/                    # Scripts relacionados ao banco de dados
  │   ├── token/                 # Manipulação de autenticação com JWT
  │   ├── vision/                # Integração com a API Gemini para reconhecimento de placas
  ├── config/
  │   ├── config.py              # Arquivos de configuração principais
  ├── run.py                     # Arquivo principal para execução da API
````

## Tabelas do Banco de Dados
- 1 - Vehicle (Tabela de Veículos)
````
class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(10), unique=True, nullable=False)
    model = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.String(100), nullable=False)

````
- 2 - User (Tabela de Usuários)
````
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # A senha é criptografada
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

````

## Rotas da API
- POST /buscar_veiculo: Busca um veículo no sistema pelo número da placa.
- POST /adicionar_veiculo: Adiciona um novo veículo ao sistema.
- GET /loadingAPI: Verifica o status da API.
- POST /usuarios: Cadastrar usuários adm.
- POST /login: Realiza login de usuários e gera um token JWT.

## Como Executar o Projeto
- Clone o repositório:
````
git clone https://github.com/albertverso/API_Gemini_IA_Recognition.git
cd /API_Gemini_IA_Recognition
````
- Instale as dependências:
````
pip install -r requirements.txt
````
- Configure as variáveis de ambiente: Crie um arquivo .env na raiz do projeto e configure as chaves necessárias, como a chave da API do Gemini e o secret para o JWT.
  
- Execute as migrações do banco de dados:
````
flask db upgrade
````
- Execute a API:
````
python run.py
````

- Acesse a API: A API estará disponível em http://localhost:5000.

## Autenticação
- Para acessar as rotas protegidas, o usuário deve realizar login na rota /login, que retornará um token JWT. Esse token deve ser incluído nos headers das requisições subsequentes.
- Exemplo de header:
````
Authorization: Bearer <seu_token_jwt>
````

## Contribuição
- Sinta-se à vontade para contribuir com o projeto. Abra issues ou envie pull requests com melhorias ou correções.
