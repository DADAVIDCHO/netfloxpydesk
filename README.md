### Historia de Usuario
Como usuario,  
quiero poder buscar películas por su título en el listado de películas,  
para filtrar rápidamente la información mostrada y encontrar la película que deseo ver, utilizando una barra de búsqueda integrada en la interfaz.

![Image](https://github.com/user-attachments/assets/8bf6847b-26e2-4107-94f8-dad11bab3eca)

### 🎯 Estimación:
🕒 **Esfuerzo estimado:** 4 puntos de historia  
👕 **Tamaño:** Pequeño (S)

### 🔗 Dependencias:
- Acceso al repositorio en GitHub.
- Configuración de Python 3.12 en el entorno de desarrollo.
- Integración de PyQt6 y módulos del template **uixcore**.
- Disponibilidad del ícono de búsqueda ("search.png") en la ruta de íconos.

### 📅 Fecha Límite:
⏳ **Fecha estimada de finalización:** 25 de marzo de 2025  
👤 **Responsable:** @DADAVIDCHO 

### 🏆 Sprint / Milestone:
📌 **Sprint:** Sprint 4 - Funcionalidades de Búsqueda  
🏁 **Milestone:** Versión 0.4 - Listado de Películas v1

### ✅ Definición de Hecho:
- [x] Se ha añadido una barra de búsqueda en la parte superior del listado.
- [x] La barra de búsqueda incluye un QLineEdit para ingresar el título y un botón "Search" con el ícono search.png.
- [ ] Al presionar el botón "Search", se filtran las películas por título (búsqueda básica, case-insensitive).
- [ ] Se siguen usando los datos hardcode en memoria para la lista de películas.
- [x] La grilla continúa sin permitir edición ni ordenamiento, manteniendo el estilo dark.
- [x] El módulo puede ejecutarse de forma independiente para pruebas.

### 📌 Tareas:
- [x] Agregar una Search Bar (QFrame) con QLineEdit y QPushButton (con ícono search.png).
- [x] Respetar el estilo y el aspecto del ejemplo.
- [ ] Implementar la función de filtrado que busca el texto ingresado en el QLineEdit.
- [x] Integrar la búsqueda en el método onSearchBasic.
- [ ] Validar que, al vaciar el campo de búsqueda, se recarguen todos los datos.
- [ ] Agregar la correspondiente documentación en el README.md.
- [ ] Realizar pruebas de integración e independientes.

### 🔗 Referencias:
🔹 **Commit:** [Listado de Películas v1 - Búsqueda Básica por Título #6](https://github.com/dadavidcho/netfloxpydesk/commit/hash)  
🔹 **Repositorio:** [GitHub - NetfloxPyDesk](https://github.com/dadavidcho/netfloxpydesk)

**Paso 6: Subir el Proyecto a GitHub**

Configura Git y sube el proyecto:

```bash
git remote add origin https://github.com/dadavidcho/netfloxpydesk.git
git add .
git commit -m "Listado de Películas v1 - Búsqueda Básica por Título #6"
git branch -M main
git push -u origin main