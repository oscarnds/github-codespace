# Flask Login App

Este proyecto es una aplicación web simple construida con Flask que incluye un sistema de inicio de sesión básico. Utiliza formularios HTML para la autenticación de usuarios y proporciona rutas para la página de inicio de sesión y la página principal.

## Estructura del Proyecto

```
flask-login-app
├── app.py               # Punto de entrada de la aplicación Flask
├── src
│   ├── routes.py       # Definición de rutas para la aplicación
│   ├── forms.py        # Definición de formularios utilizando Flask-WTF
│   └── templates
│       ├── login.html  # Plantilla HTML para la página de inicio de sesión
│       └── home.html   # Plantilla HTML para la página principal
├── requirements.txt     # Dependencias necesarias para el proyecto
└── README.md            # Documentación del proyecto
```

## Requisitos

Asegúrate de tener Python y pip instalados en tu sistema. Luego, instala las dependencias necesarias ejecutando:

```
pip install -r requirements.txt
```

## Ejecución de la Aplicación

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Uso

1. Accede a la página de inicio de sesión en `http://127.0.0.1:5000/login`.
2. Ingresa tus credenciales (usuario y contraseña).
3. Si las credenciales son correctas, serás redirigido a la página principal.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, siéntete libre de hacer un fork y enviar un pull request.