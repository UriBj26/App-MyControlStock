import sqlite3


class BaseDatos:

    def __init__(self):
        self.conexion = sqlite3.connect("inventario.db")
        self.cursor = self.conexion.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos(
            nombre TEXT PRIMARY KEY,
            categoria TEXT,
            precio REAL,
            cantidad INTEGER
        )
        """)

        self.conexion.commit()

    def agregar_producto(self, producto):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO productos
            VALUES (?, ?, ?, ?)
            """,
            (
                producto.nombre,
                producto.categoria,
                producto.precio,
                producto.cantidad
            )
        )

        self.conexion.commit()

    def obtener_productos(self):

        self.cursor.execute("SELECT * FROM productos")

        return self.cursor.fetchall()

    def obtener_cantidad(self, nombre):
        """Busca y retorna la fila con la cantidad actual del producto."""
        self.cursor.execute(
            "SELECT cantidad FROM productos WHERE nombre=?",
            (nombre,)
        )
        return self.cursor.fetchone()

    def actualizar_cantidad(self, nombre, nueva_cantidad):
        """Guarda el nuevo valor de stock en la base de datos."""
        self.cursor.execute(
            """
            UPDATE productos
            SET cantidad=?
            WHERE nombre=?
            """,
            (nueva_cantidad, nombre)
        )
        self.conexion.commit()

    def eliminar_producto(self, nombre):
        """Elimina un producto por completo de la base de datos usando su nombre."""
        self.cursor.execute(
            "DELETE FROM productos WHERE nombre=?",
            (nombre,)
        )
        self.conexion.commit()