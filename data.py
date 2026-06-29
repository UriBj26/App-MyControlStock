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
        
        fila = self.bd.obtener_cantidad(nombre)

       
        if fila and fila[0] >= cantidad:
            nueva_cantidad = fila[0] - cantidad

            
            self.bd.actualizar_cantidad(nombre, nueva_cantidad)
            return True

        return False

    def eliminar(self, nombre):
        
        self.bd.eliminar_producto(nombre)