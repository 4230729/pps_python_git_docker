# pps_python_git_docker
Aplicacion estilo galleta de la fortuna (realmente es una servilleta pero bueno)

Mira las dependencia de tu entorno virtual, deberias tener solo pip version 24.0
Sino ejecuta este comando en un nuevo entorno virtual:
- python -m pip install --upgrade pip==24.0

Docker Desktop instalado en Windows, macOS o Linux
En la carpeta del proyecto ejecuta los siguientes comandos
- docker build -t mi-app:latest
- docker run -d -p 5000:5000 mi-app:latest

Una vez hecho todo esto te puedes meter en http://localhost:5000 y funcionara.
