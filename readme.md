# **API de Concesionaria**

Esta es una aplicación creada para gestionar la información de una concesionaria. Permite manejar datos de autos, sedes, proveedores, usuarios y comentarios asociados a los autos.

## **Instalación**

1. Clona el repositorio:
   ```bash
   git clone https://github.com/ramiroquiro17/Quiroga-EFI-p.1-Ingenier-a-de-Software.git 
   ```
2. Accede al directorio del proyecto:
   ```bash
   cd Quiroga-EFI-p.1-Ingenier-a-de-Software
   ```
3. Ejecutar el comando
  ```bash
   python3 -m venv env 
   ```
4. Activar el entorno virtual
  ```bash
   source env/bin/activate 
   ```
5. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
6. Ingresa a efiP1:
   ```bash
   cd efiP1
   ```
7. Realiza las migraciones:
   ```bash
   python3 manage.py migrate
   ```
8. Inicia el servidor de desarrollo:
   ```bash
   python3 manage.py runserver
   ```
9. Acceder a la url http://127.0.0.1:8000/

## **Endpoints**

### **1. Autos**
- **URL Base:** `/api_v1/autos/`
- **Descripción:** Gestión de los autos disponibles en la concesionaria.
- **Operaciones:**
  - `GET /`: Listar todos los autos.
  - `POST /`: Crear un auto nuevo.
  - `GET /<id>/`: Obtener detalles de un auto específico.
  - `PUT /<id>/`: Actualizar información de un auto.
  - `DELETE /<id>/`: Eliminar un auto.

- **Comentarios por auto:**
  - **URL:** `/api_v1/autos/<int:auto_id>/comentarios/`
  - **Descripción:** Permite listar comentarios asociados a un auto.

---

### **2. Sedes**
- **URL Base:** `/api_v1/sedes/`
- **Descripción:** Gestión de las sedes de la concesionaria.
- **Operaciones:**
  - `GET /`: Listar todas las sedes.
  - `GET /<id>/`: Obtener detalles de una sede específica.
  - `DELETE /<id>/`: Eliminar una sede.

---

### **3. Proveedores**
- **URL Base:** `/api_v1/proveedores/`
- **Descripción:** Gestión de proveedores que suministran autos o servicios a la concesionaria.
- **Operaciones:**
  - `GET /`: Listar todos los proveedores.
  - `POST /`: Crear un proveedor nuevo.
  - `GET /<id>/`: Obtener detalles de un proveedor específico.
  - `PUT /<id>/`: Actualizar información de un proveedor.
  - `DELETE /<id>/`: Eliminar un proveedor.

---

### **4. Usuarios**
- **URL Base:** `/api_v1/users/`
- **Descripción:** Gestión de usuarios de la API.
- **Operaciones:**
  - `GET /`: Listar todos los usuarios.
  - `POST /`: Crear un usuario nuevo.
  - `GET /<id>/`: Obtener detalles de un usuario específico.
  - `PUT /<id>/`: Actualizar información de un usuario.
  - `DELETE /<id>/`: Eliminar un usuario.

---

## **Ejemplo de Uso**

### **1. Autos**
#### **Listar todos los autos**
- **GET** `/api_v1/autos/`
  
##### Respuesta:
```json
[
  {
    "pk": 1,
    "marca": {
      "nombre": "Toyota"
    },
    "modelo": {
      "nombre": "Civic"
    },
    "categoria": {
      "nombre": "Sedan"
    },
    "color": {
      "nombre": "Negro"
    },
    "pais": {
      "nombre": "Argentina"
    },
    "numero_de_puertas": 4,
    "cilindrada": "2.00",
    "tipo_de_combustible": "Electric",
    "precio": "56246.00"
  },
  {
    "pk": 2,
    "marca": {
      "nombre": "Nissan"
    },
    "modelo": {
      "nombre": "Corolla"
    },
    "categoria": {
      "nombre": "Pick-up"
    },
    "color": {
      "nombre": "Azul"
    },
    "pais": {
      "nombre": "Alemania"
    },
    "numero_de_puertas": 4,
    "cilindrada": "1.40",
    "tipo_de_combustible": "Electric",
    "precio": "26706.00"
  },
  ...
]
```

#### **Obtener detalles de un auto**
- **GET** `/api_v1/autos/1/`

##### Respuesta:
```json
{
  "marca": {"nombre": "Toyota"},
  "modelo": {"nombre": "Corolla"},
  "categoria": {"nombre": "Sedán"},
  "color": {"nombre": "Rojo"},
  "pais": {"nombre": "Japón"},
  "numero_de_puertas": 4,
  "cilindrada": 1.8,
  "tipo_de_combustible": "Gasolina",
  "precio": 25000.00
}
```

#### **Crear un nuevo auto**
- **POST** `/api_v1/autos/`

##### Cuerpo:
```json
{
  "marca": "Nissan",
  "modelo": "Sentra",
  "precio": 18000,
  "color": "Negro",
  "sede": "Sede Sur"
}
```

##### Respuesta:
```json
{
  "pk": 103,
  "marca": {
    "nombre": "Toyota"
  },
  "modelo": {
    "nombre": "Corolla"
  },
  "categoria": {
    "nombre": "Sedán"
  },
  "color": {
    "nombre": "Rojo"
  },
  "pais": {
    "nombre": "Japón"
  },
  "numero_de_puertas": 4,
  "cilindrada": "1.80",
  "tipo_de_combustible": "Gasolina",
  "precio": "25000.00"
}
```

#### **Actualizar información de un auto**
- **PUT** `/api_v1/autos/1/`

##### Cuerpo:
```json
{
    "marca": {
        "nombre": "Toyota"
    },
    "modelo": {
        "nombre": "Civic"
    },
    "categoria": {
        "nombre": "Sedan"
    },
    "color": {
        "nombre": "Gris"
    },
    "pais": {
        "nombre": "Argentina"
    },
    "numero_de_puertas": 4,
    "cilindrada": "2.00",
    "tipo_de_combustible": "Electric",
    "precio": "56246.00"
}
```

##### Respuesta:
```json
{
  "pk": 1,
  "marca": {
    "nombre": "Toyota"
  },
  "modelo": {
    "nombre": "Civic"
  },
  "categoria": {
    "nombre": "Sedan"
  },
  "color": {
    "nombre": "Gris"
  },
  "pais": {
    "nombre": "Argentina"
  },
  "numero_de_puertas": 4,
  "cilindrada": "2.00",
  "tipo_de_combustible": "Electric",
  "precio": "56246.00"
}
```

#### **Eliminar un auto**
- **DELETE** `/api_v1/autos/1/`

##### Respuesta:

***Código: 204 No Content***

#### **Listar comentarios por auto**
- **GET** `/api_v1/autos/1/comentarios/`

##### Respuesta:
```json
[
  {
    "auto": 1,
    "author": 2,
    "text": "Muy bueno pero algo caro",
    "date": "2024-08-11",
    "rating": 5
  },
  {
    "auto": 1,
    "author": 2,
    "text": "Exelente rendimiento",
    "date": "2024-08-11",
    "rating": 5
  },
]
```

---

### **2. Sedes**
#### **Listar todas las sedes**
- **GET** `/api_v1/sedes/`

##### Respuesta:
```json
[
  {
    "nombre": "Sede Norte",
    "ciudad_id": {
      "nombre": "12 de Octubre",
      "provincia": {
        "nombre": "Buenos Aires"
      }
    },
    "gerente": "Mario Santos",
    "direccion": "rivadavia 200",
    "telefono": "456436356"
  },
  {
    "nombre": "Sede central",
    "ciudad_id": {
      "nombre": "12 de Octubre",
      "provincia": {
        "nombre": "Buenos Aires"
      }
    },
    "gerente": "mario perez",
    "direccion": "Brasil 546",
    "telefono": "462344234"
  }
]
```

#### **Obtener detalles de una sede**
- **GET** `/api_v1/sedes/2/`

##### Respuesta:
```json
{
    "nombre": "Sede Norte",
    "ciudad_id": {
      "nombre": "12 de Octubre",
      "provincia": {
        "nombre": "Buenos Aires"
      }
    },
    "gerente": "Mario Santos",
    "direccion": "rivadavia 200",
    "telefono": "456436356"
  }
```


---

### **3. Proveedores**
#### **Listar todos los proveedores**
- **GET** `/api_v1/proveedores/`

##### Respuesta:
```json
[
  {
    "pk": 1,
    "nombre": "proveedor1",
    "direccion": "lskdfjl 123",
    "telefono": "12434456"
  },
  {
    "pk": 2,
    "nombre": "Proveedor C",
    "direccion": "Rivadavio 545",
    "telefono": "+1 777 888 999"
  }
]
```

#### **Obtener detalles de un proveedor**
- **GET** `/api_v1/proveedores/1/`

##### Respuesta:
```json
{
    "pk": 1,
    "nombre": "proveedor1",
    "direccion": "lskdfjl 123",
    "telefono": "12434456"
  }
```

#### **Crear un nuevo proveedor**
- **POST** `/api_v1/proveedores/`

##### Cuerpo:
```json
{
  "nombre": "Proveedor C",
  "telefono": "Rivadavia 545",
  "telefono": "+1 777 888 999"
}
```

##### Respuesta:
```json
{
    "pk": 2,
    "nombre": "Proveedor C",
    "direccion": "Rivadavio 545",
    "telefono": "+1 777 888 999"
  }
```

---

### **4. Usuarios**
#### **Listar todos los usuarios**
- **GET** `/api_v1/users/`

##### Respuesta:
```json
[
  {
    "id": 1,
    "username": "admin",
    "email": "admin@example.com"
  },
  {
    "id": 2,
    "username": "usuario1",
    "email": "usuario1@example.com"
  }
]
```

#### **Obtener detalles de un usuario**
- **GET** `/api_v1/users/1/`

##### Respuesta:
```json
{
  "id": 1,
  "username": "admin",
  "email": "admin@example.com"
}
```

#### **Crear un nuevo usuario**
- **POST** `/api_v1/users/`

##### Cuerpo:
```json
{
  "username": "usuario_nuevo",
  "password": "password_segura",
  "email": "nuevo@example.com"
}
```

##### Respuesta:
```json
{
  "id": 3,
  "username": "usuario_nuevo",
  "email": "nuevo@example.com"
}
```

---

