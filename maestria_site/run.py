from app import create_app  # Importe a função create_app

app = create_app()  # Crie a aplicação Flask

if __name__ == '__main__':
    app.run(debug=True)
