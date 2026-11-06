# Ejercicio 3: Ejecución con Hilos y Lock (Condiciones de Carrera)

## ¿De qué trata este ejercicio?
Este programa ilustra el uso de **hilos (threads)** y un **bloqueo o cerrojo (`Lock`)** para prevenir **condiciones de carrera** en un ejemplo práctico: el retiro de dinero en un cajero automático compartido.

Una condición de carrera ocurre cuando dos o más hilos intentan modificar el mismo dato al mismo tiempo. Al usar `Lock`, garantizamos que **solo un hilo pueda modificar el saldo a la vez**:
1. Juan consulta el saldo ($100) y bloquea el acceso a la cuenta.
2. Mientras Juan procesa el retiro, María no puede alterar la cuenta.
3. Al terminar Juan, la cuenta queda con $20 y el bloqueo se libera.
4. María intenta retirar $80, pero el sistema detecta que el saldo es insuficiente y bloquea la operación.

---

## Estructura de archivos

```text
Distribuidas_03_Lock/
├── 03_con_lock.py       # Script en Python usando threading y Lock
├── docker-compose.yml   # Archivo de configuración para Docker
└── README.md            # Documentación completa del proyecto
```

---

## Requisitos previos

Necesitas tener instalados los siguientes programas en tu computadora:

- **Git:** [Descargar Git](https://git-scm.com/)
- **Docker Desktop:** [Descargar Docker Desktop](https://www.docker.com/products/docker-desktop/) *(debe estar abierto antes de ejecutar los comandos)*

---

## Comprobar que Docker está listo (Opcional)

Si deseas verificar el funcionamiento de Docker en tu sistema, abre la terminal y ejecuta:

```bash
docker --version
docker compose version
```

---

## Cómo ejecutar el programa paso a paso

### 1. Clonar el repositorio
Abre la terminal y descarga el proyecto desde GitHub:

```bash
git clone [https://github.com/Leidy04S/Distribuidas_03_Lock.git](https://github.com/Leidy04S/Distribuidas_03_Lock.git)
```

### 2. Entrar a la carpeta del proyecto
```bash
cd Distribuidas_03_Lock
```

### 3. Iniciar el programa con Docker Compose
Ejecuta el siguiente comando para arrancar el contenedor y ver la ejecución:

```bash
docker compose up
```

---

## Lo que verás en pantalla

En la consola observarás cómo el uso del Lock protege la cuenta compartida y evita que ambos retiren $80 a la vez:

```text
=================================================================
   EJERCICIO 3: PREVENCIÓN DE CONDICIONES DE CARRERA CON LOCK
=================================================================
Gracias al uso del Lock, el segundo hilo debe esperar a que el
primer hilo complete la operación antes de consultar o retirar.

▶ Juan se acerca al cajero automático...
   -> Juan consulta el saldo actual: $100
   -> Juan procesa el retiro de $80...
▶ Maria se acerca al cajero automático...
✔ Juan retiró $80 con éxito. Saldo restante: $20

   -> Maria consulta el saldo actual: $20
❌ Maria no pudo retirar. Saldo insuficiente (Saldo actual: $20)

=================================================================
PROCESO FINALIZADO - Saldo final en la cuenta: $20
=================================================================
```

---

## Cómo detener y cerrar el programa

Una vez finalizada la revisión, detén y elimina el contenedor ejecutando:

```bash
docker compose down
```