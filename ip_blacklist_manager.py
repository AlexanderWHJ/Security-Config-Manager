import json
import os
import re

# Constantes de configuración
DB_PATH = "blacklist-01.json"
ANALISTA = "AlexanderWHJ"

def validar_ip(ip):
    """Usa expresiones regulares para asegurar que el formato sea una IP válida."""
    patron = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(patron, ip) is not None

def gestionar_blacklist():
    print(f"--- 🛡️ Firewall Manager | Analista: {ANALISTA} ---")
    
    # Datos iniciales si el archivo no existe
    if not os.path.exists(DB_PATH):
        seed_data = ["192.168.1.5", "10.0.0.7"]
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(seed_data, f, indent = 4, ensure_ascii = False)
        print(f"[*] Base de datos inicializada en {DB_PATH}")

    # Entrada de usuario con limpieza
    ip_usuario = input("\n[?] Ingrese IP para verificar/bloquear: ").strip()

    if not validar_ip(ip_usuario):
        print("❌ Error: Formato de IP inválido. Use el estándar (ej: 192.168.1.1)")
        return

    # Procesamiento de la lista
    with open(DB_PATH, "r", encoding="utf-8") as f:
        lista_negra = json.load(f)

    if ip_usuario in lista_negra:
        print(f"⚠️ Alerta: La IP {ip_usuario} ya se encuentra BLOQUEADA.")
    else:
        lista_negra.append(ip_usuario)
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(lista_negra, f, indent = 4, ensure_ascii = False)
        print(f"✅ Éxito: IP {ip_usuario} añadida a la lista de denegación.")

if __name__ == "__main__":
    gestionar_blacklist()