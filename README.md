# TuPrimeraPagina+Leonardis

Proyecto final individual desarrollado en **Django**, con patrón **MVT**, que implementa una aplicación web estilo **blog** con autenticación, perfiles de usuario y mensajería interna.

---

## 📌 Descripción general

La aplicación permite a los usuarios registrarse, iniciar sesión y gestionar contenido tipo páginas/posts.  
Incluye sistema de perfiles, subida de imágenes, texto enriquecido, y mensajería privada entre usuarios.

---

## 🧱 Tecnologías utilizadas

- Python 3
- Django
- SQLite (solo para desarrollo)
- HTML + Django Templates
- CKEditor
- Pillow

---

## 📂 Funcionalidades principales

### 🔹 Navegación
- **Home**
- **About** (`/about/`)
- **Pages** (`/pages/`)
- **Login / Signup / Logout**
- **Profile**
- **Messages**

---

### 🔹 Pages (Blog)
- Listado de páginas (`/pages/`)
- Mensaje *“No hay páginas aún”* si no existen registros
- Vista de detalle con botón **Leer más**
- Crear / Editar / Borrar páginas (solo usuarios logueados)
- Cada página incluye:
  - Título
  - Subtítulo
  - Texto enriquecido (CKEditor)
  - Imagen
  - Fecha
  - Autor

---

### 🔹 Autenticación
- Registro de usuarios (username, email, password)
- Login
- Logout

---

### 🔹 Perfil de usuario
- Vista de perfil (`/profile/`)
- Datos mostrados:
  - Nombre
  - Apellido
  - Email
  - Avatar
  - Biografía
  - Fecha de nacimiento
- Edición de perfil
- Cambio de contraseña

---

### 🔹 About
- Ruta `/about/`
- Vista “Acerca de mí”
- Acceso visible desde el navbar
- Uso de decorador `@login_required`

---

### 🔹 Mensajería
- Inbox (`/messages/`)
- Envío de mensajes entre usuarios
- Lectura de mensajes
- Marcar mensajes como leídos

---

## 🛠️ Instalación y ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd TuPrimeraPagina+Leonardis
2️⃣ Crear entorno virtual
bash
Copiar código
py -m venv .venv
3️⃣ Activar entorno virtual
bash
Copiar código
.\.venv\Scripts\activate
4️⃣ Instalar dependencias
bash
Copiar código
pip install -r requirements.txt
5️⃣ Ejecutar migraciones
bash
Copiar código
py manage.py migrate
6️⃣ Crear superusuario
bash
Copiar código
py manage.py createsuperuser
7️⃣ Ejecutar servidor
bash
Copiar código
py manage.py runserver

🌐 Rutas principales

Home → /

Pages → /pages/

About → /about/

Login → /login/

Signup → /signup/

Profile → /profile/

Messages → /messages/

Admin → /admin/

📁 Estructura del proyecto

blog/ → páginas/posts (modelo principal)

accounts/ → autenticación y perfiles

messenger/ → mensajería interna

templates/ → herencia de templates

static/ → archivos estáticos

media/ → imágenes (ignorado en git)

⚠️ Consideraciones importantes

El archivo db.sqlite3 no se incluye en el repositorio.

La carpeta media/ está excluida mediante .gitignore.

El proyecto utiliza herencia de templates con un base.html.

🎥 Video demostrativo

Se incluye un video (https://drive.google.com/file/d/1PQZiDWgoeUGRIlr5-CgKs_xlNa-gL-J0/view?usp=sharing)

Registro y login

Gestión de pages

Perfil de usuario

Mensajería

Panel admin

👤 Autor

Santiago Leonardis
Proyecto final – Curso Python 