<div align="center">

# Event Project

### Sistema de Gerenciamento de Eventos

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16.1-red.svg)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Uma plataforma web robusta e escalável para gerenciamento de eventos, desenvolvida com Django. Permite que usuários se registrem, autentiquem e gerenciem eventos.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow.svg)

</div>

## 📑 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Screenshots](#-screenshots)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#tecnologias)
- [Arquitetura](#-arquitetura)
- [API Endpoints](#-api-endpoints)
- [Instalação](#-instalação)
- [Testes](#-testes)
- [Configuração Avançada](#-configuração-avançada)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Deploy](#-deploy)
- [Modelos de Dados](#modelos-de-dados)
- [Comandos Úteis](#-comandos-úteis-do-django)
- [Estrutura de Código](#-estrutura-de-código)
- [FAQ](#-faq-perguntas-frequentes)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)
- [Suporte](#-suporte)

---

## 📖 Sobre o Projeto

O **Event Project** é uma aplicação web voltada para o gerenciamento de eventos. Os usuários podem se cadastrar, criar, organizar e participar de eventos.

**IMPORTANTE**: Este projeto não utiliza práticas de Inteligência Artificial. Ele foi criado com o propósito de aprimorar meus conhecimentos em Python e Django, utilizando apenas pesquisas na web, incluindo sites oficiais do próprio framework Django.

### 🎯 Objetivos do Projeto

- Aprender e praticar desenvolvimento web com Django
- Implementar um sistema de autenticação customizado
- Trabalhar com relacionamentos de banco de dados (ForeignKey, ManyToMany)
- Criar uma API RESTful profissional
- Aplicar boas práticas de desenvolvimento Python/Django

## 📸 Screenshots

*Em desenvolvimento - Screenshots serão adicionados em breve*

<!-- 
Planeje adicionar:
- Página inicial
- Dashboard de eventos
- Tela de criação de evento
- Perfil de usuário
- Painel administrativo
-->

## ✨ Funcionalidades

### Implementadas
- ✅ Modelo de usuário customizado com autenticação via email
- ✅ Sistema de gerenciamento de eventos
- ✅ Sistema de participantes em eventos
- ✅ Validação de números de telefone internacionais
- ✅ Painel administrativo Django
- ✅ Relacionamento entre usuários e eventos

### Em Desenvolvimento
- 🔄 API RESTful completa para eventos
- 🔄 Sistema de autenticação JWT
- 🔄 Interface web frontend
- 🔄 Upload de imagens para eventos
- 🔄 Sistema de notificações

### Planejadas
- 📋 Busca e filtros avançados de eventos
- 📋 Sistema de categorias de eventos
- 📋 Dashboard de estatísticas
- 📋 Exportação de dados em PDF/CSV
- 📋 Integração com calendários (Google Calendar, iCal)

## Tecnologias

### Core
- **[Python 3.13](https://www.python.org/)** - Linguagem de programação
- **[Django 5.2.7](https://www.djangoproject.com/)** - Framework web
- **[Django REST Framework 3.16.1](https://www.django-rest-framework.org/)** - API RESTful

### Banco de Dados
- **SQLite3**
- **PostgreSQL** 

### Bibliotecas Adicionais
- **phonenumbers 9.0.16** - Validação de números de telefone
- **django-phonenumber-field 8.3.0** - Integração Django para phonenumbers
- **django-cors-headers 4.9.0** - Gerenciamento de CORS
- **Pillow 12.0.0** - Processamento de imagens

## 📁 Arquitetura

```
event_project/
│
├── event_project/          # Configurações principais do projeto
│   ├── settings.py        # Configurações do Django
│   ├── urls.py            # Roteamento principal
│   ├── wsgi.py            # Configuração WSGI
│   └── asgi.py            # Configuração ASGI
│
├── users/                 # Aplicação de usuários
│   ├── models.py         # Modelo de usuário customizado
│   ├── views.py          # Views de autenticação
│   ├── urls.py           # Rotas de usuários
│   ├── admin.py          # Configuração do admin
│   └── migrations/       # Migrações do banco de dados
│
├── events/               # Aplicação de eventos
│   ├── models.py        # Modelos de eventos e participantes
│   ├── views.py         # Views de eventos
│   ├── urls.py          # Rotas de eventos
│   ├── admin.py         # Configuração do admin
│   └── migrations/      # Migrações do banco de dados
│
├── venv/                # Ambiente virtual Python
├── db.sqlite3           # Banco de dados SQLite
├── manage.py            # CLI do Django
├── requirements.txt     # Dependências do projeto (nota: arquivo atual: requeriments.txt)
└── README.md            # Este arquivo
```

## 📡 API Endpoints

### Usuários
*Em desenvolvimento - Endpoints planejados:*

| Método | Endpoint | Descrição | Status |
|--------|----------|-----------|--------|
| POST | `/api/users/register/` | Registro de novo usuário | 🔄 |
| POST | `/api/users/login/` | Login de usuário | 🔄 |
| GET | `/api/users/profile/` | Perfil do usuário autenticado | 🔄 |
| PUT | `/api/users/profile/` | Atualizar perfil | 🔄 |

### Eventos
*Em desenvolvimento - Endpoints planejados:*

| Método | Endpoint | Descrição | Status |
|--------|----------|-----------|--------|
| GET | `/api/events/` | Listar todos os eventos | 🔄 |
| POST | `/api/events/` | Criar novo evento | 🔄 |
| GET | `/api/events/{id}/` | Detalhes de um evento | 🔄 |
| PUT | `/api/events/{id}/` | Atualizar evento | 🔄 |
| DELETE | `/api/events/{id}/` | Deletar evento | 🔄 |
| POST | `/api/events/{id}/participate/` | Participar de evento | 🔄 |
| DELETE | `/api/events/{id}/participate/` | Cancelar participação | 🔄 |
| GET | `/api/events/{id}/participants/` | Listar participantes | 🔄 |

### Exemplo de Requisição (Planejado)

```json
POST /api/events/
Content-Type: application/json
Authorization: Bearer {token}

{
  "title": "Workshop Django",
  "description": "Aprenda Django do zero",
  "date": "2025-11-01T14:00:00Z",
  "location": "São Paulo, SP"
}
```

### Exemplo de Resposta (Planejado)

```json
{
  "id": 1,
  "title": "Workshop Django",
  "description": "Aprenda Django do zero",
  "date": "2025-11-01T14:00:00Z",
  "location": "São Paulo, SP",
  "organizer": {
    "id": 1,
    "email": "organizador@exemplo.com",
    "first_name": "João"
  },
  "participants_count": 0,
  "created_at": "2025-10-21T10:00:00Z",
  "updated_at": "2025-10-21T10:00:00Z"
}
```

## 🔧 Instalação

### Pré-requisitos

- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a Passo

1. **Clone o repositório**

```bash
git clone https://github.com/MarceloTIFavaro/event_project.git
cd event_project
```

2. **Crie e ative o ambiente virtual**

```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

> **Nota**: O arquivo atual está nomeado como `requeriments.txt`. Você pode renomeá-lo para `requirements.txt` ou usar:
> ```bash
> pip install -r requeriments.txt
> ```

4. **Configure as variáveis de ambiente** (opcional)

```bash
# Crie um arquivo .env na raiz do projeto
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. **Execute as migrações do banco de dados**

```bash
python manage.py migrate
```

6. **Crie um superusuário**

```bash
python manage.py createsuperuser
```

### Desenvolvimento

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse a aplicação em: **http://127.0.0.1:8000/**

### Painel Administrativo

Acesse o painel admin em: **http://127.0.0.1:8000/admin/**

Use as credenciais do superusuário criado anteriormente.

## 🧪 Testes

### Executar Todos os Testes

```bash
python manage.py test
```

### Executar Testes de um App Específico

```bash
# Testar apenas o app de usuários
python manage.py test users

# Testar apenas o app de eventos
python manage.py test events
```

### Executar Testes com Verbosidade

```bash
python manage.py test --verbosity=2
```

### Cobertura de Testes

Para verificar a cobertura de código dos testes:

```bash
# Instale o coverage
pip install coverage

# Execute os testes com coverage
coverage run --source='.' manage.py test

# Gere o relatório
coverage report

# Gere relatório HTML (mais detalhado)
coverage html
# Abra htmlcov/index.html no navegador
```

### Criar Novas Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

## ⚙️ Configuração Avançada

### Variáveis de Ambiente

Para ambientes de produção, é recomendado usar variáveis de ambiente. Crie um arquivo `.env` na raiz do projeto:

```env
# Django Settings
SECRET_KEY=sua-chave-secreta-aqui-gere-uma-nova
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,seudominio.com

# Database (PostgreSQL)
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=event_project_db
DATABASE_USER=seu_usuario
DATABASE_PASSWORD=sua_senha
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Email (Opcional - para envio de emails)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=sua-senha-de-app

# Security (Produção)
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

**Para gerar uma nova SECRET_KEY:**
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Configuração do PostgreSQL

1. **Instale o PostgreSQL** (se ainda não tiver)

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# macOS (via Homebrew)
brew install postgresql
```

2. **Crie o banco de dados**

```bash
# Acesse o PostgreSQL
sudo -u postgres psql

# Crie o banco e usuário
CREATE DATABASE event_project_db;
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
ALTER ROLE seu_usuario SET client_encoding TO 'utf8';
ALTER ROLE seu_usuario SET default_transaction_isolation TO 'read committed';
ALTER ROLE seu_usuario SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE event_project_db TO seu_usuario;

# Saia do PostgreSQL
\q
```

3. **Instale o adapter Python**

```bash
pip install psycopg2-binary
```

4. **Atualize o settings.py**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'event_project_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. **Execute as migrações**

```bash
python manage.py migrate
```

## 🔧 Troubleshooting

### Problemas Comuns

**1. Erro: `No module named 'phonenumber_field'`**
```bash
# Solução: Instale as dependências
pip install -r requirements.txt
```

**2. Erro: `django.db.utils.OperationalError: no such table`**
```bash
# Solução: Execute as migrações
python manage.py migrate
```

**3. Erro: `ModuleNotFoundError: No module named 'users'`**
```bash
# Solução: Verifique se está no diretório correto e se o app está no INSTALLED_APPS
cd /home/marcelo/event_project
python manage.py runserver
```

**4. Erro ao criar superusuário: `email já existe`**
```bash
# Solução: Use outro email ou delete o usuário existente via shell
python manage.py shell
>>> from users.models import User
>>> User.objects.filter(email='seu-email@exemplo.com').delete()
>>> exit()
```

**5. Porta 8000 já em uso**
```bash
# Solução: Use outra porta
python manage.py runserver 8001

# Ou mate o processo na porta 8000
sudo lsof -t -i tcp:8000 | xargs kill -9
```

**6. Problemas com migrações**
```bash
# Solução: Resete as migrações (CUIDADO: apaga dados!)
python manage.py migrate --fake events zero
python manage.py migrate --fake users zero
python manage.py migrate
```

## 🗺️ Roadmap

### Versão 0.1.0 (Atual - Em Desenvolvimento)
- [x] Modelo de dados básico
- [x] Sistema de autenticação
- [ ] API REST completa
- [ ] Documentação da API (Swagger/OpenAPI)

### Versão 0.2.0 (Próximo)
- [ ] Interface web frontend (React/Vue.js)
- [ ] Sistema de upload de imagens
- [ ] Busca e filtros de eventos
- [ ] Testes unitários e de integração
- [ ] Autenticação JWT

### Versão 0.3.0 (Futuro)
- [ ] Sistema de notificações por email
- [ ] Dashboard com estatísticas
- [ ] Categorias de eventos
- [ ] Sistema de comentários em eventos
- [ ] Geolocalização de eventos

### Versão 1.0.0 (Release)
- [ ] Deploy em produção
- [ ] Documentação completa
- [ ] Testes de carga e performance
- [ ] CI/CD automatizado
- [ ] Monitoramento e logs

## 🚀 Deploy

### Preparação para Produção

1. **Atualize as configurações de segurança**
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['seudominio.com', 'www.seudominio.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

2. **Colete arquivos estáticos**
```bash
python manage.py collectstatic
```

3. **Use um servidor WSGI (Gunicorn)**
```bash
pip install gunicorn
gunicorn event_project.wsgi:application --bind 0.0.0.0:8000
```

### Deploy no Heroku

```bash
# Instale o Heroku CLI e faça login
heroku login

# Crie um novo app
heroku create seu-app-eventos

# Adicione PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Configure as variáveis de ambiente
heroku config:set SECRET_KEY=sua-chave-secreta
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Execute as migrações
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Deploy na AWS/DigitalOcean

*Documentação detalhada em desenvolvimento*

## Modelos de Dados

### User (Usuário Customizado)
- `email` - Email único (usado para login)
- `first_name` - Nome
- `last_name` - Sobrenome
- `phone_number` - Número de telefone validado
- `is_active` - Status do usuário
- `is_staff` - Acesso ao admin
- `date_joined` - Data de cadastro

### Event (Evento)
- `title` - Título do evento
- `description` - Descrição detalhada
- `date` - Data e hora do evento
- `location` - Local do evento
- `organizer` - Organizador (ForeignKey para User)
- `created_at` - Data de criação
- `updated_at` - Data de atualização

### Participant (Participante)
- `event` - Evento (ForeignKey)
- `user` - Usuário participante (ForeignKey)
- `registered_at` - Data de inscrição

## 💡 Comandos Úteis do Django

### Gerenciamento de Banco de Dados

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Visualizar SQL de uma migração
python manage.py sqlmigrate events 0001

# Listar migrações
python manage.py showmigrations

# Reverter migração
python manage.py migrate events 0002  # volta para a migração 0002
```

### Shell Interativo

```bash
# Shell padrão do Django
python manage.py shell

# Shell aprimorado (se tiver ipython instalado)
pip install ipython
python manage.py shell
```

### Gerenciamento de Usuários

```bash
# Criar superusuário
python manage.py createsuperuser

# Alterar senha de usuário
python manage.py changepassword nome_usuario
```

### Banco de Dados

```bash
# Fazer backup do banco SQLite
cp db.sqlite3 db.sqlite3.backup

# Exportar dados (fixture)
python manage.py dumpdata > backup.json
python manage.py dumpdata events > events_backup.json

# Importar dados (fixture)
python manage.py loaddata backup.json
```

### Arquivos Estáticos

```bash
# Coletar arquivos estáticos para produção
python manage.py collectstatic

# Limpar arquivos estáticos
python manage.py collectstatic --clear --noinput
```

### Outros Comandos Úteis

```bash
# Verificar problemas no projeto
python manage.py check

# Limpar sessões expiradas
python manage.py clearsessions

# Criar app novo
python manage.py startapp nome_do_app
```

## 📚 Estrutura de Código

### Boas Práticas Implementadas

- ✅ Model customizado de usuário (evita problemas futuros)
- ✅ Separação de apps por funcionalidade
- ✅ Uso de ForeignKey para relacionamentos
- ✅ Validação de dados no modelo (PhoneNumberField)
- ✅ Timestamps automáticos (created_at, updated_at)
- ✅ Organização clara de URLs por app

### Padrões de Projeto

- **MTV (Model-Template-View)**: Arquitetura padrão do Django
- **DRY (Don't Repeat Yourself)**: Reutilização de código
- **Fat Models, Thin Views**: Lógica de negócio nos models
- **RESTful API**: Seguindo princípios REST

## ❓ FAQ (Perguntas Frequentes)

### Por que usar email em vez de username para autenticação?

O uso de email como identificador único é mais intuitivo para usuários modernos e evita problemas com nomes de usuário já existentes. É uma prática comum em aplicações web atuais.

### Como funciona o sistema de participantes?

O modelo `Participant` cria uma relação many-to-many entre `User` e `Event`, permitindo que um usuário participe de vários eventos e um evento tenha vários participantes. O campo `registered_at` registra quando o usuário se inscreveu.

### Por que há duas migrações iniciais (0001 e 0002)?

Isso acontece quando você tem relacionamentos entre apps que precisam ser criados em ordem específica. O Django gerencia essas dependências automaticamente.

### Posso usar SQLite em produção?

SQLite é excelente para desenvolvimento, mas para produção com múltiplos usuários simultâneos, é recomendado usar PostgreSQL ou MySQL para melhor performance e concorrência.

### Como adicionar novos campos ao modelo User?

Como estamos usando um modelo customizado, você pode simplesmente adicionar campos ao modelo `User` em `users/models.py` e criar uma nova migração:
```python
# users/models.py
class User(AbstractUser):
    # ... campos existentes ...
    bio = models.TextField(blank=True)  # novo campo
```
Depois execute: `python manage.py makemigrations` e `python manage.py migrate`

### O projeto está pronto para produção?

Atualmente o projeto está em desenvolvimento. Para produção, você precisará:
- Implementar todas as views da API
- Adicionar autenticação JWT
- Configurar variáveis de ambiente
- Usar PostgreSQL
- Implementar testes completos
- Configurar HTTPS e outras medidas de segurança

## 🤝 Contribuindo

Contribuições são bem-vindas! Este projeto foi criado para fins educacionais, mas sinta-se à vontade para:

1. **Fork o projeto**
2. **Crie uma branch para sua feature** (`git checkout -b feature/AmazingFeature`)
3. **Commit suas mudanças** (`git commit -m 'Add: nova funcionalidade incrível'`)
4. **Push para a branch** (`git push origin feature/AmazingFeature`)
5. **Abra um Pull Request**

### Convenções de Commit

- `Add:` Nova funcionalidade
- `Fix:` Correção de bug
- `Update:` Atualização de funcionalidade
- `Docs:` Documentação
- `Style:` Formatação, ponto e vírgula, etc
- `Refactor:` Refatoração de código
- `Test:` Adição ou modificação de testes

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Marcelo Henrique Favaro**

- GitHub: [@MarceloTIFavaro](https://github.com/MarceloTIFavaro)
- LinkedIn: [Marcelo Favaro](https://linkedin.com/in/seu-perfil)

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas:

1. Verifique a seção [Troubleshooting](#-troubleshooting)
2. Consulte a [documentação oficial do Django](https://docs.djangoproject.com/)
3. Abra uma [Issue](https://github.com/MarceloTIFavaro/event_project/issues)

## 🌟 Agradecimentos

- [Django Documentation](https://docs.djangoproject.com/) - Documentação oficial do Django
- [Django REST Framework](https://www.django-rest-framework.org/) - Framework para APIs REST
- [Real Python](https://realpython.com/) - Tutoriais e artigos Python
- [Django Best Practices](https://django-best-practices.readthedocs.io/) - Guia de boas práticas
- Comunidade Python/Django no Stack Overflow

## 📚 Recursos Úteis

### Documentação Oficial
- [Django 5.2 Documentation](https://docs.djangoproject.com/en/5.2/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Python 3.13 Documentation](https://docs.python.org/3.13/)

### Tutoriais e Guias
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [Mozilla Django Tutorial](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django)
- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - Livro de boas práticas

### Ferramentas
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)
- [Django Extensions](https://django-extensions.readthedocs.io/)
- [Black](https://black.readthedocs.io/) - Formatador de código Python
- [Flake8](https://flake8.pycqa.org/) - Linter Python

---

<div align="center">

Desenvolvido com ❤️ e Django por [Marcelo Favaro](https://github.com/MarceloTIFavaro)

**[⬆ Voltar ao topo](#event-project)**

</div>
