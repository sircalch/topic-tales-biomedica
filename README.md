# TopicTales Biomédica - Sistema Médico Profesional

## 🏥 Descripción

Sistema médico modular profesional desarrollado con Django y plantilla Datta Able Pro. Diseñado para clínicas y consultorios que requieren una solución escalable y profesional.

## ✨ Características Actuales

- ✅ **Login Premium**: Interfaz de autenticación profesional con Datta Able Pro
- ✅ **Sidebar Modular**: Navegación limpia y organizada
- ✅ **Dashboard Base**: Panel principal funcional
- ✅ **Estructura Limpia**: Código organizado y documentado
- ✅ **Diseño Responsivo**: Compatible con dispositivos móviles

## 🔧 Tecnologías

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Datta Able Pro
- **Base de Datos**: SQLite (desarrollo)
- **Iconos**: Feather Icons
- **Estilos**: Bootstrap 5 + CSS personalizado

## 📋 Módulos Planificados

### Plan Básico
- [ ] **Gestión de Pacientes** - Registro y seguimiento
- [ ] **Agenda y Citas** - Programación de consultas  
- [ ] **Historia Clínica** - Expedientes médicos digitales
- [ ] **Recetas Electrónicas** - Generación de prescripciones

### Plan Medio
- [ ] **Inventario de Insumos** - Control de medicamentos y materiales
- [ ] **Facturación Simple** - Gestión de cobros y pagos
- [ ] **Laboratorio** - Gestión de estudios y resultados
- [ ] **Módulos Especializados** - Odontología, Nutrición, etc.

### Plan Avanzado
- [ ] **Gestión de Equipos** - Control de mantenimiento
- [ ] **Sistema de Usuarios** - Roles y permisos avanzados
- [ ] **Reportes Avanzados** - Analytics con gráficos
- [ ] **Especialidades Múltiples** - Configuraciones personalizadas

## 🚀 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone [URL_DEL_REPO]
   cd TopicTalesBiomedica
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instalar dependencias**
   ```bash
   pip install django
   ```

4. **Configurar base de datos**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Ejecutar servidor**
   ```bash
   python manage.py runserver
   ```

6. **Acceder al sistema**
   - URL: http://localhost:8000
   - Admin: http://localhost:8000/admin

## 👤 Credenciales de Prueba

- **Usuario**: admin
- **Contraseña**: admin

## 📁 Estructura del Proyecto

```
TopicTalesBiomedica/
├── core/                    # App principal
├── accounts/               # Gestión de usuarios
├── static/                # Archivos estáticos
│   └── assets/           # Datta Able Pro assets
├── templates/             # Plantillas HTML
│   ├── layouts/          # Layouts base
│   ├── includes/         # Componentes reutilizables
│   └── registration/     # Templates de autenticación
├── topic_tales/          # Configuración Django
└── manage.py            # Comando principal Django
```

## 🎨 Diseño

El sistema utiliza la plantilla **Datta Able Pro** con:
- Colores médicos profesionales
- Navegación intuitiva
- Componentes responsivos
- Iconografía médica
- Animaciones suaves

## 🔒 Seguridad

- Autenticación requerida para todas las vistas
- Protección CSRF
- Validación de formularios
- Gestión segura de sesiones

## 📝 Notas de Desarrollo

- **Estado**: Base limpia lista para desarrollo
- **Login y Sidebar**: Completamente funcionales
- **Próximo paso**: Implementar módulo de Pacientes
- **Arquitectura**: Modular y escalable

## 🤝 Contribución

1. Fork el proyecto
2. Crear rama para nueva funcionalidad
3. Hacer commit de los cambios
4. Push a la rama
5. Crear Pull Request

## 📄 Licencia

Proyecto propietario - TopicTales Biomédica © 2024

---

**Desarrollado con ❤️ para profesionales de la salud**