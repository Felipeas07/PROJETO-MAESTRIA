import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_secreta_dificil_de_adivinhar'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///maestria.db'  # Caminho para o banco de dados SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Evita um aviso desnecessário no console
    
    # Configurações de e-mail (caso precise enviar e-mails da página de contato)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')  # Coloque o email em uma variável de ambiente
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')  # Coloque a senha em uma variável de ambiente

# Você pode adicionar outras classes de configuração, por exemplo, para desenvolvimento, produção e teste

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
