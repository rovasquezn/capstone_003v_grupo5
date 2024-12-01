# Sistema de Gestión de Ópticas (SGO)

Sistema de Gestión de Ópticas (SGO) es un sistema de gestión para una óptica, que permite la administración de usuarios, clientes, recetas y órdenes de trabajo. Este proyecto está desarrollado para Óptica Cruz.

## Características

- Gestión de usuarios (administradores, atendedores, técnicos)
- Gestión de clientes
- Gestión de recetas
- Gestión de órdenes de trabajo
- Cambio de contraseña para usuarios
- Panel de administración de Django

## Requisitos

- Python 3.10 o superior
- Django 4.2.15
- Otros paquetes listados en `requirements.txt`

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/optica-cruz.git
    cd optica-cruz
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

5. Crea un superusuario para acceder al panel de administración:

    ```bash
    python manage.py createsuperuser
    ```

6. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

7. Accede al sistema en tu navegador:

    ```text
    http://127.0.0.1:8000/
    ```

## Uso

### Panel de Administración

El panel de administración de Django está disponible en:

```text
http://127.0.0.1:8000/admin/
```

### Cambio de Contraseña
Los usuarios pueden cambiar su contraseña desde su perfil.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactar a de.needham@duocuc.cl o ro.vasquezn@duocuc.cl

