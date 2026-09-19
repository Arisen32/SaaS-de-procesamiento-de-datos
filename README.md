# 🚀 SaaS Backend - Sistema Asíncrono de Procesamiento de Datos

Plataforma backend escalable diseñada para la gestión de archivos pesados y procesamiento asíncrono en segundo plano, evitando bloqueos en el servidor web principal.

## 🛠️ Tecnologías y Stack
* **Lenguaje:** Python
* **Framework Principal:** Django & Django REST Framework (DRF)
* **Procesamiento Asíncrono:** Celery[cite: 1]
* **Broker de Mensajes / Cache:** Redis
* **Base de Datos:** PostgreSQL / SQLite[cite: 1]
* **Contenedorización:** Docker & Docker Compose[cite: 1]

## 🏗️ Arquitectura del Sistema
1. **Recepción:** El usuario envía un archivo mediante una API REST (`POST /api/upload/`).
2. **Persistencia inicial:** El archivo se almacena y se registra en la base de datos con un estado `pending`.
3. **Delegación:** La vista dispara una tarea asíncrona en **Celery** pasando el ID del registro, liberando al hilo principal de Django de inmediato.
4. **Procesamiento:** Un *Worker* de Celery toma la tarea de forma concurrente, procesa el archivo por bloques (chunks) simulando tareas pesadas y actualiza el progreso en tiempo real.

## ⚙️ Instalación y Ejecución Local (con Docker)

La forma más rápida de levantar todo el entorno (Django, Celery y Redis) es utilizando Docker Compose:

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
   cd tu-repositorio