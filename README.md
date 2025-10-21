<div align="center">

# 🎉 Event Project

### Sistema de Gerenciamento de Eventos

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Uma plataforma web robusta e escalável para gerenciamento de eventos, desenvolvida com Django. Permite que usuários se registrem, autentiquem e gerenciem eventos de forma intuitiva e segura.

[Características](#-características) •
[Tecnologias](#-tecnologias) •
[Instalação](#-instalação) •
[Uso](#-uso) •
[Arquitetura](#-arquitetura) •
[Contribuindo](#-contribuindo)

</div>

---

## 📋 Sobre o Projeto

O **Event Project** é uma aplicação web completa para gerenciamento de eventos, construída com as melhores práticas de desenvolvimento Django. O sistema oferece autenticação personalizada, gerenciamento de perfis de usuários e funcionalidades abrangentes para criação e administração de eventos.

### ✨ Características

- 🔐 **Autenticação Segura**
  - Sistema de registro e login personalizado
  - Validação robusta de dados do usuário
  - Gerenciamento de sessões seguro

- 👥 **Gestão de Usuários**
  - Modelo de usuário customizado com campos estendidos
  - Validação internacional de números de telefone
  - Perfis de usuário completos

- 📅 **Gerenciamento de Eventos**
  - Criação, edição e exclusão de eventos
  - Sistema de participantes
  - Listagem e visualização detalhada de eventos

- 🛡️ **Painel Administrativo**
  - Interface admin do Django totalmente configurada
  - Gerenciamento completo de usuários e eventos
  - Filtros e buscas avançadas

## 🚀 Tecnologias

### Core
- **[Python 3.13](https://www.python.org/)** - Linguagem de programação
- **[Django 5.2.7](https://www.djangoproject.com/)** - Framework web
- **[Django REST Framework 3.16.1](https://www.django-rest-framework.org/)** - API RESTful

### Banco de Dados
- **SQLite3** - Desenvolvimento (padrão)
- **PostgreSQL** - Produção (suportado via psycopg2)

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
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
```

## 🔧 Instalação

### Pré-requisitos

- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a Passo

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/event_project.git
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

7. **Colete arquivos estáticos** (para produção)

```bash
python manage.py collectstatic
```

## 💻 Uso

### Desenvolvimento

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse a aplicação em: **http://127.0.0.1:8000/**

### Painel Administrativo

Acesse o painel admin em: **http://127.0.0.1:8000/admin/**

Use as credenciais do superusuário criado anteriormente.

### Executar Testes

```bash
python manage.py test
```

### Criar Novas Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🗄️ Modelos de Dados

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

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Para contribuir:

1. Faça um **fork** do projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça **push** para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um **Pull Request**

### Diretrizes de Contribuição

- Siga o [PEP 8](https://pep8.org/) para estilo de código Python
- Escreva testes para novas funcionalidades
- Atualize a documentação conforme necessário
- Mantenha as mensagens de commit claras e descritivas

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Marcelo**

- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- Email: seu-email@exemplo.com

## 📞 Suporte

Se você tiver alguma dúvida ou problema, por favor:

1. Verifique a [documentação](docs/)
2. Abra uma [issue](https://github.com/seu-usuario/event_project/issues)
3. Entre em contato pelo email de suporte

---

<div align="center">

Desenvolvido com ❤️ usando Django

**[⬆ Voltar ao topo](#-event-project)**

</div>
