import wx


def mostrar_agotados(frame):

    frame.limpiar()

    agotados = [

        p.nombre

        for p in frame.inv.obtener_todo()

        if p.cantidad <= 0

    ]

    lista = wx.ListBox(
        frame.contenido_panel,
        choices=agotados
    )

    sizer = wx.BoxSizer(wx.VERTICAL)

    sizer.Add(
        lista,
        1,
        wx.EXPAND
    )

    frame.contenido_panel.SetSizer(sizer)
    frame.contenido_panel.Layout()