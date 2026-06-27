import sys
import os

# Agregamos la carpeta 'librerias' al buscador de Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'librerias'))

import wx
from data import Inventario
from ventana_principal import MyStockControl
from views.splash_screen import SplashScreen

def terminar_espera(event):
    """Esta función se ejecuta automáticamente cuando el reloj llega a 3 segundos."""
    global splash, timer
    
    timer.Stop()    
    splash.Close() 

    
    mi_inventario = Inventario()
    ventana = MyStockControl(mi_inventario)
    ventana.Show()

if __name__ == "__main__":
    app = wx.App()

  
    splash = SplashScreen()
    splash.Show()

   
    timer = wx.Timer()
    timer.Bind(wx.EVT_TIMER, terminar_espera)
    timer.Start(3000)

    app.MainLoop()