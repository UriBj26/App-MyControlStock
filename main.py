import wx
from data import Inventario
from ventana_principal import MyStockControl
from views.splash_screen import SplashScreen

def terminar_espera(event):
    """Esta función se ejecuta automáticamente cuando el reloj llega a 3 segundos."""
    global splash, timer
    
    timer.Stop()    # Frenamos el temporizador
    splash.Close()  # Destruimos la ventana de presentación

    # Inicializamos la base de datos y la ventana principal en el momento justo
    mi_inventario = Inventario()
    ventana = MyStockControl(mi_inventario)
    ventana.Show()

if __name__ == "__main__":
    app = wx.App()

    # 1. Creamos e iniciamos la visualización de la pantalla de bienvenida estilo Frame
    splash = SplashScreen()
    splash.Show()

    # 2. Configuramos un temporizador de 3000 ms (3 segundos) en segundo plano
    timer = wx.Timer()
    timer.Bind(wx.EVT_TIMER, terminar_espera)
    timer.Start(3000)

    app.MainLoop()