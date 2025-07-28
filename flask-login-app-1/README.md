# Flask Login App

Este es un proyecto de ejemplo que utiliza Flask para crear una aplicación web con un sistema de inicio de sesión básico.

## Estructura del Proyecto

```
flask-login-app
├── app.py               # Punto de entrada de la aplicación Flask
├── templates            # Carpeta que contiene las plantillas HTML
│   ├── login.html      # Formulario de inicio de sesión
│   └── home.html       # Página principal después del inicio de sesión
├── static              # Carpeta que contiene archivos estáticos
│   └── style.css       # Estilos CSS para la aplicación
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

1. Abre tu navegador y ve a `http://127.0.0.1:5000/login` para acceder a la página de inicio de sesión.
2. Ingresa un nombre de usuario y contraseña válidos para iniciar sesión.
3. Después de un inicio de sesión exitoso, serás redirigido a la página principal.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, siéntete libre de hacer un fork y enviar un pull request.