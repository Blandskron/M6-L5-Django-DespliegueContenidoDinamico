# EduDashboard

Este proyecto es una aplicación educativa desarrollada en Django que sirve como base para un **dashboard dinámico**. En esta primera parte, nos enfocamos en establecer el diseño principal, incluyendo un **header**, un **sidebar**, un área de contenido principal y un **footer**, usando **Bootstrap 4** para estilizar.

## Requisitos Previos

1. Python 3.8 o superior instalado.
2. pip para la gestión de paquetes de Python.
3. Entorno virtual configurado (opcional pero recomendado).

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd edu_dashboard
   ```

2. **Crea un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos**:
   Asegúrate de que el archivo `settings.py` apunte a la base de datos por defecto (SQLite). Para iniciar la base de datos, ejecuta:
   ```bash
   python manage.py migrate
   ```

5. **Crea un superusuario** (opcional):
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicia el servidor**:
   ```bash
   python manage.py runserver
   ```

   Accede a la aplicación en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Estructura del Proyecto

- `edu_project/settings.py`:
  Contiene configuraciones clave como directorios estáticos y plantillas.
- `edu_project/urls.py`:
  Define las rutas principales, incluyendo la vista `index`.
- `edu_app/views.py`:
  Contiene la lógica de las vistas, como la función `index`.
- `templates/base.html`:
  La plantilla base que define la estructura del **dashboard** (header, sidebar, footer).
- `static/`:
  Carpeta para archivos estáticos como CSS, JavaScript o imágenes.

---

## Estructura del Dashboard

### Diseño Base (`base.html`)

- **Header**: Barra superior fija con el título del proyecto.
- **Sidebar**: Navegación lateral para acceder a secciones como Inicio, Estudiantes, Cursos y Reportes.
- **Footer**: Pie de página fijo con información de derechos de autor.
- **Main Content**: Área central para contenido dinámico.

---

## Agregar Nuevas Funcionalidades

1. **Agregar Secciones al Sidebar**:
   En `base.html`, puedes añadir más enlaces al menú de navegación lateral:
   ```html
   <li class="nav-item">
       <a class="nav-link" href="#">Nueva Sección</a>
   </li>
   ```

2. **Crear Vistas para las Secciones**:
   Añade nuevas funciones en `views.py`:
   ```python
   def nueva_seccion(request):
       return render(request, 'nueva_seccion.html', {})
   ```

   Luego, agrégalas en `urls.py`:
   ```python
   path('nueva_seccion/', views.nueva_seccion, name='nueva_seccion'),
   ```

3. **Estilizar con Bootstrap**:
   Aprovecha los componentes de Bootstrap para darle un diseño moderno a cada sección.

---

## Tecnologías Utilizadas

- **Django 5.1.3**: Framework principal para el backend.
- **Bootstrap 4**: Librería para estilos y diseño responsive.
- **SQLite**: Base de datos por defecto para almacenamiento de datos.

---
