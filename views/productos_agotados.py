import wx


def mostrar_agotados(frame):
    frame.limpiar()

    sizer_interno = wx.BoxSizer(wx.VERTICAL)

    agotados = [
        p.nombre
        for p in frame.inv.obtener_todo()
        if p.cantidad <= 0
    ]

    lista = wx.ListBox(
        frame.contenido_panel,
        choices=agotados
    )

   
    sizer_interno.Add(lista, 1, wx.EXPAND | wx.ALL, 5)

    
    frame.contenido_sizer.Add(sizer_interno, 1, wx.EXPAND | wx.ALL, 10)
    frame.contenido_panel.Layout()