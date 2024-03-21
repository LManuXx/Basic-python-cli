CLI Básico en Python
Descripción
Este es un ejemplo de una aplicación CLI (Interfaz de Línea de Comandos) básica escrita en Python. Un CLI es una interfaz de usuario en la que el usuario interactúa con la aplicación a través de comandos de texto introducidos en una línea de comandos, terminal o consola.

Funcionalidades
Crear Usuario: Permite crear un nuevo usuario especificando su nombre y apellido.
Listar Usuarios: Muestra una lista de todos los usuarios existentes en el sistema.
Eliminar Usuario: Elimina un usuario existente del sistema mediante su ID.
Buscar Usuario: Busca un usuario por su ID o nombre en el sistema y muestra su información si se encuentra.
Requisitos
Python 3.x instalado en el sistema.
Uso
Clona o descarga este repositorio en tu máquina local.
Abre una terminal o línea de comandos.
Navega hasta el directorio donde se encuentra el archivo cli.py.
Ejecuta el archivo cli.py usando Python.

python cli.py [comando] [opciones]

Comandos y Opciones
new: Crea un nuevo usuario.
--name: Nombre del usuario (obligatorio).
--lastname: Apellido del usuario (obligatorio).
users: Muestra la lista de usuarios.
--order_by: Ordena la lista de usuarios por ID o nombre (opcional).
delete: Elimina un usuario existente.
--id: ID del usuario a eliminar (obligatorio).
search: Busca un usuario por su ID o nombre.
--search: ID o nombre del usuario a buscar (obligatorio).
Ejemplos de Uso
Crear un nuevo usuario:

python cli.py new --name Juan --lastname Perez

Listar usuarios ordenados por nombre:
python cli.py users --order_by name

Eliminar un usuario por ID:
python cli.py delete --id 3

Buscar un usuario por nombre:
python cli.py search --search Juan

Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, no dudes en enviar un pull request.