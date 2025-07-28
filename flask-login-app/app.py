from flask import Flask
from src.routes import main

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto a una clave secreta más segura

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)