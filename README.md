# pps_python_git_docker
Aplicacion estilo galleta de la fortuna (realmente es una servilleta pero bueno).

Lo primero es instalarse python si no lo tienes lo cual es dificl que no lo tengas.

Mira las dependencia de tu entorno virtual, deberias tener solo pip version 24.0.
Sino ejecuta este comando en un nuevo entorno virtual:
- python -m pip install --upgrade pip==24.0

Docker Desktop instalado en Windows, macOS o Linux y MongoDB.
En la carpeta del proyecto ejecuta los siguientes comandos

- docker compose up -d

Y para quitarlo:

- docker compose down

Una vez hecho todo esto te puedes meter en http://localhost:5000 y funcionara.

!!! Si no te salen las frases ejecuta este comando:

- docker compose exec bayeta python -c "from mongo_frases import inicializar; inicializar()"


