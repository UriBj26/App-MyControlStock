import sys
import os

# Agregamos la carpeta 'librerias' al buscador de Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "librerias"))

import wx

from data import Inventario
from ventana_principal import MyStockControl
from views.splash_screen import SplashScreen


class Aplicacion:

    def __init__(self):
        self.app = wx.App()

        self.splash = SplashScreen()
        self.splash.Show()

        self.timer = wx.Timer()

        self.timer.Bind(wx.EVT_TIMER, self.terminar_espera)

        self.timer.Start(3000)

    def terminar_espera(self, event):

        self.timer.Stop()

        self.splash.Close()

        inventario = Inventario()

        ventana = MyStockControl(inventario)

        ventana.Show()

    def ejecutar(self):
        self.app.MainLoop()


if __name__ == "__main__":

    programa = Aplicacion()

    programa.ejecutar()