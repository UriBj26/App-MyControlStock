import wx
from data import Inventario
from ventana_principal import MyStockControl

if __name__ == "__main__":
    app = wx.App()

    mi_inventario = Inventario()

    ventana = MyStockControl(mi_inventario)
    ventana.Show()

    app.MainLoop()