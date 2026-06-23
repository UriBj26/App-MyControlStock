import wx


def ejecutar_venta(frame, event):

    if frame.inv.vender(
            frame.cv.GetValue(),
            frame.sv.GetValue()):

        wx.MessageBox("Venta realizada")

    else:

        wx.MessageBox("Stock insuficiente")


def mostrar_venta(frame):

    frame.limpiar()

    nombres = [
        p.nombre
        for p in frame.inv.obtener_todo()
    ]

    frame.cv = wx.ComboBox(
        frame.contenido_panel,
        choices=nombres
    )

    frame.sv = wx.SpinCtrl(
        frame.contenido_panel,
        min=1
    )

    boton = wx.Button(
        frame.contenido_panel,
        label="Hacer Venta"
    )

    boton.Bind(
        wx.EVT_BUTTON,
        lambda event: ejecutar_venta(frame, event)
    )

    sizer = wx.BoxSizer(wx.VERTICAL)

    controles = [

        wx.StaticText(
            frame.contenido_panel,
            label="Producto:"
        ),

        frame.cv,

        wx.StaticText(
            frame.contenido_panel,
            label="Cantidad:"
        ),

        frame.sv,

        boton

    ]

    for c in controles:
        sizer.Add(c, 0, wx.ALL, 5)

    frame.contenido_panel.SetSizer(sizer)
    frame.contenido_panel.Layout()