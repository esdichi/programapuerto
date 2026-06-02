import psutil

def buscar_programa_por_puerto(puerto):
    encontrado = False
    # Iteramos sobre todas las conexiones de red activas
    for conexion in psutil.net_connections():
        # Verificamos si el puerto local coincide y si hay un proceso asociado (pid)
        if conexion.laddr.port == puerto and conexion.pid:
            try:
                proceso = psutil.Process(conexion.pid)
                print(f"--- Puerto {puerto} en uso ---")
                print(f"Programa: {proceso.name()}")
                print(f"PID (ID del Proceso): {conexion.pid}")
                print(f"Ruta ejecutable: {proceso.exe()}")
                encontrado = True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Por si el proceso se cerró justo en el momento o requiere permisos de administrador
                print(f"Se encontró el PID {conexion.pid} pero no se pudo acceder a sus detalles.")
    
    if not encontrado:
        print(f"No se encontró ningún programa usando el puerto {puerto}.")

# Creamos la lista combinando el rango del 1 al 25, el 80 y el 3306
puertos_a_revisar = list(range(1, 26)) + [80, 3306]

# Recorremos la lista y llamamos a tu función original para cada puerto
for p in puertos_a_revisar:
    buscar_programa_por_puerto(p)
