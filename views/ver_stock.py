import wx


def mostrar_stock(frame):

    frame.limpiar()

    tabla = wx.ListCtrl(
        frame.contenido_panel,
        style=wx.LC_REPORT
    )

    columnas = [
        "Nombre",
        "Categoría",
        "Precio",
        "Cantidad"
    ]

    for i, columna in enumerate(columnas):

        tabla.InsertColumn(
            i,
            columna,
            width=150
        )

    for p in frame.inv.obtener_todo():

        fila = tabla.InsertItem(
            tabla.GetItemCount(),
            p.nombre
        )

        tabla.SetItem(fila, 1, p.categoria)
        tabla.SetItem(fila, 2, str(p.precio))
        tabla.SetItem(fila, 3, str(p.cantidad))

    sizer = wx.BoxSizer(wx.VERTICAL)

    sizer.Add(
        tabla,
        1,
        wx.EXPAND
    )

    frame.contenido_panel.SetSizer(sizer)
    frame.contenido_panel.Layout()