# File Encryption API --- DES-based Encryption Service

Este proyecto implementa un sistema funcional para **encriptar y
desencriptar archivos** utilizando el algoritmo **DES (Data Encryption
Standard)**.\
El servicio está desarrollado con **Flask** y expone endpoints REST que
permiten cargar un archivo y una clave personalizada. Dicha clave es
procesada mediante una función hash para derivar los **64 bits** usados
por el algoritmo DES.

## Características principales

-   API REST construida con **Flask**
-   Encriptación y desencriptación mediante **DES**
-   Derivación de claves usando **hash**
-   Procesamiento y retorno del archivo de forma automática
-   Separación clara en **rutas**, **controladores** y **servicios**
-   Archivos almacenados temporalmente en `uploads/`

## 📁 Estructura del proyecto

    📦 project
    │
    ├── app.py
    ├── controllers/
    │   └── file_controller.py
    ├── routes/
    │   └── file_routes.py
    ├── services/
    │   ├── des_service.py
    │   └── key_derivation_service.py
    ├── uploads/
    │   ├── encrypted/
    │   └── decrypted/
    └── README.md

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

``` bash
git clone https://github.com/SamuelVar05/DES_Cipher
cd DES_CIPHER
```

### 2. Crear entorno virtual (opcional)

``` bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

``` bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor

``` bash
python app.py
```

El servicio estará disponible en:

    http://localhost:5000/api

## 🔧 Endpoints

### 🔐 1. Encriptar archivo

**POST** `/api/encrypt`

Parámetros:\
- `file`\
- `key`

### 🔓 2. Desencriptar archivo

**POST** `/api/decrypt`

Parámetros:\
- `file`\
- `key`

## 🧠 Funcionamiento interno

1.  El usuario envía un archivo y una clave.\
2.  La clave es hasheada y truncada a 64 bits.\
3.  El archivo se guarda temporalmente.\
4.  El servicio DES procesa el archivo.\
5.  Se devuelve el archivo resultante.

## 📚 Tecnologías utilizadas

-   Python 3\
-   Flask\
-   Hashlib\
-   PyCryptodome o pyDES

## 📝 Licencia

Proyecto académico. Uso libre con fines educativos.
