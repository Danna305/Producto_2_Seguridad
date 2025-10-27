# Servidor Web con Cifrado y Hash

Aplicación Flask para demostración de cifrado simétrico y generación de hash.

## Requisitos Previos

- Python 3.7 o superior instalado en tu sistema
- pip (gestor de paquetes de Python)

## Instalación

### Opción 1: Instalación individual de paquetes

Abre una terminal en el directorio del proyecto y ejecuta:

```bash
pip install flask
pip install cryptography
```

### Opción 2: Instalación desde requirements.txt (Recomendado)

```bash
pip install -r requirements.txt
```

**Nota para Windows:** Si `pip` no funciona, prueba con:
```bash
python -m pip install -r requirements.txt
```
O si tienes el Python Launcher:
```bash
py -m pip install -r requirements.txt
```

## Ejecución del Servidor

Una vez instaladas las dependencias, ejecuta el servidor con:

```bash
python server.py
```

O en Windows:
```bash
py server.py
```

El servidor se iniciará en modo debug en `http://127.0.0.1:5000/`

## Estructura del Proyecto

- `server.py` - Servidor Flask con rutas de login
- `seguridad.py` - Funciones de cifrado simétrico y generación de hash
- `templates/login.html` - Interfaz de usuario
- `requirements.txt` - Lista de dependencias del proyecto

## Uso

1. Accede a `http://127.0.0.1:5000/` en tu navegador
2. Ingresa un usuario y contraseña
3. Los datos se cifrarán y se generará un hash que se mostrará en la consola
