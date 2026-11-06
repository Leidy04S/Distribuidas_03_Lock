import time
import threading

# Variable compartida por los hilos (recurso crítico)
saldo = 100

# Objeto Lock para controlar el acceso a la variable compartida
lock = threading.Lock()

def retirar(nombre):
    global saldo
    print(f"▶ {nombre} se acerca al cajero automático...")
    
    # El bloqueo con 'with lock' asegura que solo un hilo modifique el saldo a la vez
    with lock:
        print(f"   -> {nombre} consulta el saldo actual: ${saldo}")
        if saldo >= 80:
            print(f"   -> {nombre} procesa el retiro de $80...")
            saldo_actual = saldo
            time.sleep(1)  # Simula el tiempo que tarda la máquina en entregar el dinero
            saldo = saldo_actual - 80
            print(f"✔ {nombre} retiró $80 con éxito. Saldo restante: ${saldo}\n")
        else:
            print(f"❌ {nombre} no pudo retirar. Saldo insuficiente (Saldo actual: ${saldo})\n")

def main():
    print("=" * 65)
    print("   EJERCICIO 3: PREVENCIÓN DE CONDICIONES DE CARRERA CON LOCK")
    print("=" * 65)
    print("Gracias al uso del Lock, el segundo hilo debe esperar a que el")
    print("primer hilo complete la operación antes de consultar o retirar.\n")

    # Creación de dos hilos concurrentes
    hilo1 = threading.Thread(target=retirar, args=("Juan",))
    hilo2 = threading.Thread(target=retirar, args=("Maria",))

    # Iniciar la ejecución de los hilos
    hilo1.start()
    hilo2.start()

    # Esperar a que ambos hilos terminen
    hilo1.join()
    hilo2.join()

    print("=" * 65)
    print(f"PROCESO FINALIZADO - Saldo final en la cuenta: ${saldo}")
    print("=" * 65)

if __name__ == "__main__":
    main()