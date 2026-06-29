import wx

def mostrar_agotados(frame):
    frame.limpiar()

    sizer_interno = wx.BoxSizer(wx.VERTICAL)
    agotados = [p for p in frame.inv.obtener_todo() if p.cantidad <= 0]

    if not agotados:
        texto = wx.StaticText(frame.contenido_panel, label="No hay productos agotados.")
        texto.SetForegroundColour(wx.Colour(0, 128, 0))
        sizer_interno.Add(texto, 0, wx.ALL, 10)
    else:
        titulo = wx.StaticText(frame.contenido_panel, label="¡ALERTA: PRODUCTOS AGOTADOS!")
        titulo.SetForegroundColour(wx.Colour(255, 0, 0))
        sizer_interno.Add(titulo, 0, wx.BOTTOM, 5)

        lista = wx.ListBox(frame.contenido_panel, choices=[p.nombre for p in agotados])
        sizer_interno.Add(lista, 1, wx.EXPAND | wx.ALL, 5)

    frame.contenido_sizer.Add(sizer_interno, 1, wx.EXPAND | wx.ALL, 10)
    frame.contenido_panel.Layout()