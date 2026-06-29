import wx
from data import Producto

class AgregarProducto:
    def __init__(self, frame):
        self.frame = frame

    def guardar(self, event):
        if not self.frame.n.GetValue().strip() or not self.frame.p.GetValue().strip() or not self.frame.a.GetValue().strip():
            wx.MessageBox("Por favor, complete todos los campos.", "Error", wx.OK | wx.ICON_ERROR)
            return

        try:
            producto = Producto(self.frame.n.GetValue(), self.frame.c.GetValue(), self.frame.p.GetValue(), self.frame.a.GetValue())
            self.frame.inv.agregar(producto)
            wx.MessageBox("Producto guardado correctamente", "Éxito", wx.OK | wx.ICON_INFORMATION)
            self.frame.n.SetValue("")
            self.frame.p.SetValue("")
            self.frame.a.SetValue("")
        except Exception as e:
            wx.MessageBox(f"Error al guardar: {e}", "Error", wx.OK | wx.ICON_ERROR)

def mostrar_agregar(frame):
    frame.limpiar()
    controlador = AgregarProducto(frame)
    sizer_interno = wx.BoxSizer(wx.VERTICAL)

    frame.n = wx.TextCtrl(frame.contenido_panel, size=(300, 25))
    frame.c = wx.ComboBox(frame.contenido_panel, choices=["Bebidas", "Alimentos", "Limpieza"], size=(300, 25), style=wx.CB_READONLY)
    frame.c.SetSelection(0)
    frame.p = wx.TextCtrl(frame.contenido_panel, size=(300, 25))
    frame.a = wx.TextCtrl(frame.contenido_panel, size=(300, 25))

    boton = wx.Button(frame.contenido_panel, label="Guardar Producto", size=(150, 30))
    boton.Bind(wx.EVT_BUTTON, controlador.guardar)

    controles = [("Nombre del Producto:", frame.n), ("Categoría:", frame.c), ("Precio:", frame.p), ("Cantidad Inicial:", frame.a)]

    for texto, control in controles:
        sizer_interno.Add(wx.StaticText(frame.contenido_panel, label=texto), 0, wx.TOP, 10)
        sizer_interno.Add(control, 0, wx.TOP, 3)

    sizer_interno.Add(boton, 0, wx.TOP, 20)
    frame.contenido_sizer.Add(sizer_interno, 1, wx.EXPAND | wx.ALL, 10)
    frame.contenido_panel.Layout()