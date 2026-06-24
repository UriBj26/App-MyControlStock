from database import BaseDatos


class Producto:

    def __init__(self, nombre, categoria, precio, cantidad):

        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.cantidad = int(cantidad)


class Inventario:

    def __init__(self):

        self.bd = BaseDatos()

    def agregar(self, producto):

        self.bd.agregar_producto(producto)

    def obtener_todo(self):

        datos = self.bd.obtener_productos()

        productos = []

        for nombre, categoria, precio, cantidad in datos:

            productos.append(
                Producto(
                    nombre,
                    categoria,
                    precio,
                    cantidad
                )
            )

        return productos

    def vender(self, nombre, cantidad):
        # Obtenemos la cantidad directamente desde la base de datos
        fila = self.bd.obtener_cantidad(nombre)

        # La lógica de negocio y la resta se ejecutan en esta capa de objetos
        if fila and fila[0] >= cantidad:
            nueva_cantidad = fila[0] - cantidad

            # Le ordenamos a la base de datos que guarde el nuevo valor calculado
            self.bd.actualizar_cantidad(nombre, nueva_cantidad)
            return True

        return False

    def eliminar(self, nombre):
        """Ordena a la base de datos eliminar el producto especificado."""
        self.bd.eliminar_producto(nombre)