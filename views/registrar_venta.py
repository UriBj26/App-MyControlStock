import wx

class RegistrarVenta:
    def __init__(self, frame):
        self.frame = frame

    def ejecutar_venta(self, event):
        if not self.frame.cv.GetValue():
            wx.MessageBox("No hay productos seleccionados para vender.", "Aviso", wx.OK | wx.ICON_WARNING)
            return
        if self.frame.inv.vender(self.frame.cv.GetValue(), self.frame.registrar_venta.GetValue()):
            wx.MessageBox("Venta realizada correctamente", "Éxito", wx.OK | wx.ICON_INFORMATION)
            mostrar_venta(self.frame)
        else:
            wx.MessageBox("Stock insuficiente para realizar la venta.", "Error", wx.OK | wx.ICON_ERROR)

def mostrar_venta(frame):
    frame.limpiar()
    controlador = RegistrarVenta(frame)
    sizer_interno = wx.BoxSizer(wx.VERTICAL)
    nombres = [p.nombre for p in frame.inv.obtener_todo()]

    frame.cv = wx.ComboBox(frame.contenido_panel, choices=nombres, style=wx.CB_READONLY, size=(300, 25))
    if nombres:
        frame.cv.SetSelection(0)

    frame.registrar_venta = wx.SpinCtrl(frame.contenido_panel, min=1, max=9999, size=(300, 25))
    boton = wx.Button(frame.contenido_panel, label="Hacer Venta", size=(150, 30))
    boton.Bind(wx.EVT_BUTTON, controlador.ejecutar_venta)

    sizer_interno.Add(wx.StaticText(frame.contenido_panel, label="Seleccione Producto:"), 0, wx.TOP, 10)
    sizer_interno.Add(frame.cv, 0, wx.TOP, 3)
    sizer_interno.Add(wx.StaticText(frame.contenido_panel, label="Cantidad a vender:"), 0, wx.TOP, 10)
    sizer_interno.Add(frame.registrar_venta, 0, wx.TOP, 3)
    sizer_interno.Add(boton, 0, wx.TOP, 20)

    frame.contenido_sizer.Add(sizer_interno, 1, wx.EXPAND | wx.ALL, 10)
    frame.contenido_panel.Layout()