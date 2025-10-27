# Servidor Web con Cifrado y Hash

Aplicación Flask para demostración de algoritmos criptográficos: cifrado simétrico, cifrado asimétrico y generación de hash.

## Autores

**Elaborado por:**
  - Danna Michelle Cruz Vázquez
  - Alexia Sanchez Vazquez

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
- `seguridad.py` - Funciones de cifrado simétrico, asimétrico y generación de hash
- `templates/login.html` - Interfaz de usuario
- `requirements.txt` - Lista de dependencias del proyecto

## Uso

1. Accede a `http://127.0.0.1:5001/` en tu navegador
2. Ingresa un usuario y contraseña
3. Los datos se procesarán con los 3 algoritmos de seguridad:
   - **Cifrado Simétrico (AES/Fernet)**: Usa la misma clave para cifrar y descifrar
   - **Cifrado Asimétrico (RSA-2048)**: Usa clave pública para cifrar y clave privada para descifrar
   - **Hash (SHA-256)**: Función unidireccional que no se puede descifrar
4. Los resultados se mostrarán tanto en la interfaz web como en la consola del servidor

## Características

- ✅ Implementación de cifrado simétrico con AES (Fernet)
- ✅ Implementación de cifrado asimétrico con RSA-2048
- ✅ Generación de hash con SHA-256
- ✅ Interfaz web amigable con visualización de resultados
- ✅ Explicaciones de cada algoritmo criptográfico
