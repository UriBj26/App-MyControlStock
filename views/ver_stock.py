import wx


def al_eliminar(frame, tabla, event):
    # Obtener el índice de la fila seleccionada por el usuario en la tabla
    indice_seleccionado = tabla.GetFirstSelected()

    if indice_seleccionado == -1:
        wx.MessageBox("Por favor, seleccione un producto de la lista para eliminar.", "Aviso", wx.OK | wx.ICON_WARNING)
        return

    # Obtener el nombre del producto (columna 0) de la fila seleccionada
    nombre_producto = tabla.GetItemText(indice_seleccionado, 0)

    # Ventana de confirmación para evitar borrados por error
    confirmacion = wx.MessageBox(
        f"¿Está seguro de que desea eliminar por completo el producto '{nombre_producto}'?",
        "Confirmar eliminación",
        wx.YES_NO | wx.ICON_QUESTION
    )

    if confirmacion == wx.YES:
        # Llamamos al método eliminar de la capa de datos
        frame.inv.eliminar(nombre_producto)
        wx.MessageBox(f"Producto '{nombre_producto}' eliminado con éxito.", "Éxito", wx.OK | wx.ICON_INFORMATION)
        
        # Refrescar la pantalla de stock para actualizar los cambios visualmente
        mostrar_stock(frame)


def mostrar_stock(frame):
    frame.limpiar()

    sizer_interno = wx.BoxSizer(wx.VERTICAL)

    # Creamos la tabla de visualización
    tabla = wx.ListCtrl(
        frame.contenido_panel,
        style=wx.LC_REPORT | wx.BORDER_SUNKEN
    )

    columnas = ["Nombre", "Categoría", "Precio", "Cantidad"]
    for i, columna in enumerate(columnas):
        tabla.InsertColumn(i, columna, width=150)

    for p in frame.inv.obtener_todo():
        fila = tabla.InsertItem(tabla.GetItemCount(), p.nombre)
        tabla.SetItem(fila, 1, p.categoria)
        tabla.SetItem(fila, 2, str(p.precio))
        tabla.SetItem(fila, 3, str(p.cantidad))

    # Creamos el botón de eliminar abajo de la tabla
    boton_eliminar = wx.Button(frame.contenido_panel, label="Eliminar Producto Seleccionado", size=(220, 30))
    boton_eliminar.SetBackgroundColour(wx.Colour(255, 200, 200)) # Color rojizo suave de advertencia
    
    # Vinculamos el evento del botón pasando la tabla como argumento
    boton_eliminar.Bind(wx.EVT_BUTTON, lambda event: al_eliminar(frame, tabla, event))

    # Agregamos la tabla (ocupa el espacio expandido vertical con proporción 1)
    sizer_interno.Add(tabla, 1, wx.EXPAND | wx.ALL, 5)
    
    # Agregamos el botón abajo a la derecha
    sizer_interno.Add(boton_eliminar, 0, wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM, 10)

    # Añadir al sizer maestro y refrescar el Layout
    frame.contenido_sizer.Add(sizer_interno, 1, wx.EXPAND | wx.ALL, 10)
    frame.contenido_panel.Layout()