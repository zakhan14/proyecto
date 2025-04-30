# # Guía rápida para poner en marcha el proyecto web

Después de descargar el archivo del proyecto y abrirlo en **Visual Studio Code**, lo primero que debes hacer es abrir una terminal integrada dentro del editor.

En esa terminal, ejecuta los siguientes comandos, uno por uno:

```bash
.venv/Scripts/activate
cd nuevo_proyecto
python manage.py runserver --nostatic
```

- `activate`: activa el **entorno virtual** del proyecto, esencial para trabajar con las dependencias de Python sin afectar tu sistema.
- `cd`: te mueve a la carpeta principal del proyecto Django.
- `runserver`: inicia el **servidor de desarrollo** de Django.

Si todo está correcto, verás un mensaje como este:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 29, 2025 - 17:40:28
Django version 5.1.7, using settings 'nuevo_proyecto.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Una vez aparezca este mensaje, mantén pulsada la tecla **Ctrl** y haz clic en el enlace:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Primer vistazo a la página

Al abrir la web, verás un botón para **iniciar sesión** y una frase en rojo.

- Si ya tienes una cuenta, simplemente inicia sesión.
- Si no, regístrate desde allí mismo.

---

## Navegación principal

Una vez dentro, verás tres secciones en la parte superior del navegador:

- `HTML`
- `JAVASCRIPT`
- `POST`

### 🔹 ¿Quieres jugar?

- Entra en la sección **JAVASCRIPT** para jugar a **Piedra, Papel o Tijera**.
- Las reglas son las de siempre, ¡así que no necesitas instrucciones!

### 🔹 ¿Prefieres crear o leer contenido?

- Dirígete a la sección **POST**, donde puedes:
  - Ver todos los posts existentes.
  - Crear un post nuevo.
  - Consultar la lista de **tags** (temas o categorías).

Los primeros botones grises permiten acceder a estas funciones.

---

## Explora los posts

En la parte inferior verás una lista de publicaciones. Cada post tiene:

- Título y contenido resumido.
- Botón **"Leer el post"** para ver el contenido completo.
- Sección de comentarios.

Además, cada post tiene una serie de **tags**. Si haces clic en alguno de ellos, se abrirá una nueva página con todos los posts relacionados con ese mismo tag.

---

## Cerrar sesión

En todo momento, en la esquina superior derecha, tendrás acceso al botón **"Cerrar sesión"**.
