# Security-Config-Manager
Módulo de gestión de listas negras (Blacklist) con validación avanzada de direcciones IPv4 mediante expresiones regulares (RegEx) y persistencia en JSON.
# 🛡️ Network IP Blocker - AlexanderWHJ

## 📝 Descripción
Este script de Python funciona como un controlador básico de firewall para gestionar el acceso a una red. Permite verificar si una dirección IP está bloqueada y añadir nuevas IPs a una lista negra persistente, garantizando que los datos ingresados sean técnicamente correctos.

## ✨ Funcionalidades Clave
* **Validación Robusta:** Implementación de Expresiones Regulares (RegEx) para asegurar que solo se procesen formatos de IPv4 válidos (0.0.0.0 a 255.255.255.255).
* **Persistencia de Datos:** Los registros se mantienen en un archivo `blacklist-01.json`, permitiendo que la configuración no se pierda al cerrar el programa.
* **Seguridad de Entrada:** Limpieza de datos con `.strip()` y normalización para evitar duplicados por errores de escritura.

## 🛠️ Tecnologías utilizadas
* **Python 3.x**
* **Módulo `re`**: Para el motor de validación de patrones.
* **Módulo `json`**: Para el almacenamiento de la base de datos.

## 🚀 Instalación y Uso
1. Clona este repositorio o descarga el archivo `main.py`.
2. Ejecuta el script: `python main.py`.
3. Ingresa la IP que deseas consultar o bloquear.
4. El sistema te informará si la IP ya existe o si ha sido añadida exitosamente.
