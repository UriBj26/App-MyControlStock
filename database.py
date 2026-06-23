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

    def vender_producto(self, nombre, cantidad):

        self.cursor.execute(
            "SELECT cantidad FROM productos WHERE nombre=?",
            (nombre,)
        )

        fila = self.cursor.fetchone()

        if fila and fila[0] >= cantidad:

            nueva_cantidad = fila[0] - cantidad

            self.cursor.execute(
                """
                UPDATE productos
                SET cantidad=?
                WHERE nombre=?
                """,
                (nueva_cantidad, nombre)
            )

            self.conexion.commit()

            return True

        return False