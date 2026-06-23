import wx
from data import Producto


def guardar(frame, event):

    producto = Producto(
        frame.n.GetValue(),
        frame.c.GetValue(),
        frame.p.GetValue(),
        frame.a.GetValue()
    )

    frame.inv.agregar(producto)

    wx.MessageBox("Producto guardado correctamente")


def mostrar_agregar(frame):

    frame.limpiar()

    sizer = wx.BoxSizer(wx.VERTICAL)

    frame.n = wx.TextCtrl(
        frame.contenido_panel,
        size=(300, 25)
    )

    frame.c = wx.ComboBox(
        frame.contenido_panel,
        choices=["Bebidas", "Alimentos", "Limpieza"],
        size=(300, 25)
    )

    frame.p = wx.TextCtrl(
        frame.contenido_panel,
        size=(300, 25)
    )

    frame.a = wx.TextCtrl(
        frame.contenido_panel,
        size=(300, 25)
    )

    boton = wx.Button(
        frame.contenido_panel,
        label="Guardar Producto"
    )

    boton.Bind(
        wx.EVT_BUTTON,
        lambda event: guardar(frame, event)
    )

    controles = [
        wx.StaticText(frame.contenido_panel, label="Nombre:"),
        frame.n,

        wx.StaticText(frame.contenido_panel, label="Categoría:"),
        frame.c,

        wx.StaticText(frame.contenido_panel, label="Precio:"),
        frame.p,

        wx.StaticText(frame.contenido_panel, label="Cantidad:"),
        frame.a,

        boton
    ]

    for c in controles:
        sizer.Add(c, 0, wx.ALL, 5)

    frame.contenido_panel.SetSizer(sizer)
    frame.contenido_panel.Layout()