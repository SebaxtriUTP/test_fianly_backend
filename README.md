```markdown
# 🧠 API REST Backend - Autenticación y Gestión de Usuarios

## 🎯 Objetivo

Este proyecto backend fue desarrollado como parte de una prueba técnica para evaluar habilidades en el desarrollo de APIs RESTful utilizando Django y Django REST Framework, haciendo énfasis en:

- Validación de datos con **Cerberus**
- Tipado estático con **typing**
- Autenticación con **JWT (SimpleJWT)**
- Base de datos desacoplable (**SQLite por defecto**)
- Buenas prácticas de código, seguridad y organización

---

## ⚙️ Tecnologías Usadas

| Tecnología               | Propósito                                   |
|--------------------------|---------------------------------------------|
| Django 5.2               | Framework principal                         |
| Django REST Framework    | Desarrollo de APIs RESTful                  |
| Cerberus                 | Validación de datos de entrada              |
| SimpleJWT                | Autenticación basada en tokens JWT         |
| SQLite                   | Base de datos local (puede migrarse a PostgreSQL fácilmente) |
| Typing                   | Tipado estático (`Dict`, `List`, etc.)      |

---

## 🗃️ Estructura del Proyecto

```
📁 fianly_backend/           # Proyecto Django
│   ├── settings.py          # Configuración del proyecto
│   ├── urls.py              # Enrutamiento global
│   ├── wsgi.py / asgi.py    # Deploy WSGI/ASGI
│
📁 users/                   # Aplicación de autenticación
│   ├── views/              # Vistas (Register, Auth, UserList)
│   ├── validators/         # Esquemas Cerberus
│   ├── urls.py             # Rutas locales
│   ├── tests.py            # Pruebas automatizadas
│
📄 manage.py                # Ejecutable principal
📄 db.sqlite3               # Base de datos por defecto
📄 requirements.txt         # Dependencias del proyecto
```

---

## 🚀 Instalación del Proyecto

### 🔧 Requisitos Previos

- Python 3.10 o superior
- pip
- virtualenv (recomendado)

### 🛠️ Pasos para levantar el entorno local

```bash
# 1. Clona el repositorio
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

# 2. Crea y activa un entorno virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Aplica las migraciones
python manage.py migrate

# 5. Inicia el servidor de desarrollo
python manage.py runserver
```

---

## 🔐 Endpoints Disponibles

| Método | Ruta       | Descripción                                 | Autenticación |
|--------|------------|---------------------------------------------|---------------|
| POST   | /register  | Crear nuevo usuario                         | ❌ No         |
| POST   | /auth      | Autenticar usuario y obtener token JWT      | ❌ No         |
| GET    | /user      | Obtener lista de usuarios registrados       | ✅ Sí         |

> ⚠️ Todos los datos de entrada se validan previamente usando esquemas Cerberus.

---

## 🧪 Validaciones con Cerberus

Ubicación: `users/validators/user_validators.py`

### ✅ Esquema de Registro

```python
register_schema = {
    "username": {"type": "string", "required": True},
    "password": {"type": "string", "required": True},
    "first_name": {"type": "string", "required": True},
    "last_name": {"type": "string", "required": True}
}
```

### ✅ Esquema de Autenticación

```python
auth_schema = {
    "user": {"type": "string", "required": True},
    "password": {"type": "string", "required": True}
}
```

---

## 🧪 Pruebas Automatizadas

Archivo: `users/tests.py`

Para ejecutar los tests:

```bash
python manage.py test
```

Pruebas incluidas:

- Registro exitoso de usuario
- Autenticación con credenciales válidas
- Acceso a usuarios autenticado con JWT

---

## 🧠 Tipado Estático

Se utilizó `typing` en todas las vistas para mejorar legibilidad y robustez:

```python
from typing import List, Dict, Optional, Union
```

Ejemplo:

```python
def post(self, request) -> Response:
    data: Dict = request.data
```

---

## 🗃️ Base de Datos

Se usa SQLite por defecto para facilitar la instalación local. Puedes migrar fácilmente a PostgreSQL modificando el archivo `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mi_db',
        'USER': 'usuario',
        'PASSWORD': 'clave',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

Para instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🧪 Ejemplos de Peticiones JSON (Postman / curl)

### 1. 📌 Registro de Usuario (`/register`)

**Método:** POST  
**URL:** `http://localhost:8000/register`

```json
{
  "username": "testuser",
  "password": "TestPass123",
  "first_name": "Test",
  "last_name": "User"
}
```

**Respuesta esperada (201):**

```json
{
  "message": "Usuario creado exitosamente"
}
```

---

### 2. 🔐 Autenticación (`/auth`)

**Método:** POST  
**URL:** `http://localhost:8000/auth`

```json
{
  "user": "testuser",
  "password": "TestPass123"
}
```

**Respuesta esperada (201):**

```json
{
  "token": "<jwt_token_aquí>",
  "user_name": "Test"
}
```

> Guarda el token para autorizar las siguientes peticiones usando JWT.

---

### 3. 👥 Obtener Usuarios (`/user`)

**Método:** GET  
**URL:** `http://localhost:8000/user`  
**Encabezado (Headers):**

```
Authorization: Bearer <jwt_token_aquí>
```

**Respuesta esperada (200):**

```json
[
  {
    "user_name": "Test",
    "user_lastname": "User"
  }
]
```

---

## 🔁 Flujo Sugerido de Pruebas

1. Registra un nuevo usuario (`/register`)
2. Autentícate con ese usuario (`/auth`) y copia el token
3. Usa el token para acceder al listado de usuarios (`/user`)

---

## ✅ Consejos para Postman

- En la pestaña **Authorization**, selecciona tipo `Bearer Token` y pega el JWT.
- En **Headers**, asegúrate de incluir `Content-Type: application/json`.
- Usa el entorno `localhost:8000` al levantar tu servidor local con `runserver`.

---
## 🧑 Autor

**Juan Sebastián Gómez Díaz**  
📧 [tu.email@dominio.com]  
🌐 GitHub: [https://github.com/tu_usuario](https://github.com/tu_usuario)

---

## ✅ Consideraciones Finales

- El proyecto sigue buenas prácticas de seguridad (JWT, validación robusta).
- Estructura modular y desacoplada para facilitar escalabilidad.
- La base de datos y lógica están listas para ambientes de staging o producción.

---
```
