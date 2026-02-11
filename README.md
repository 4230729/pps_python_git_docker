# pps_python_git_docker
Aplicacion estilo galleta de la fortuna (realmente es una servilleta pero bueno)

Lo primero es instalarse python si no lo tienes lo cual es dificl que no lo tengas

Mira las dependencia de tu entorno virtual, deberias tener solo pip version 24.0
Sino ejecuta este comando en un nuevo entorno virtual:
- python -m pip install --upgrade pip==24.0

Docker Desktop instalado en Windows, macOS o Linux
En la carpeta del proyecto ejecuta los siguientes comandos

- docker network create bayeta_net
- docker run -d --name mongo_bayeta --network bayeta_net mongo
- docker build -t bayeta .
- docker run -d --name bayeta_app --network bayeta_net -p 5000:5000 bayeta

Una vez hecho todo esto te puedes meter en http://localhost:5000 y funcionara.
