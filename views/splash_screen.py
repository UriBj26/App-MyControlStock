import wx
import os

class SplashScreen(wx.Frame):
    
    def __init__(self):
        super().__init__(
            parent=None,
            title="MyStockControl",
            style=wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP | wx.BORDER_NONE
        )

        panel = wx.Panel(self)
        
        
        panel.SetBackgroundColour(wx.Colour(253, 253, 230))

        
        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_imagen = os.path.join(ruta_base, "logo.png")

        print(f"[Splash] Buscando imagen en: {ruta_imagen}")

        
        if not os.path.exists(ruta_imagen):
            mensaje_error = wx.StaticText(panel, label="No se encontró el archivo logo.png")
            sizer_error = wx.BoxSizer(wx.VERTICAL)
            sizer_error.AddStretchSpacer()
            sizer_error.Add(mensaje_error, 0, wx.ALIGN_CENTER)
            sizer_error.AddStretchSpacer()
            panel.SetSizer(sizer_error)
            self.SetClientSize((500, 400))
            self.Centre()
            return

        
        imagen = wx.Image(ruta_imagen, wx.BITMAP_TYPE_PNG)
        ancho = imagen.GetWidth()
        alto = imagen.GetHeight()

        ancho_maximo = 500
        alto_maximo = 500
        factor = min(ancho_maximo / ancho, alto_maximo / alto)

        nuevo_ancho = int(ancho * factor)
        nuevo_alto = int(alto * factor)

        imagen = imagen.Scale(nuevo_ancho, nuevo_alto, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap(imagen))

        
        texto_carga = wx.StaticText(panel, label="CARGANDO...")
        fuente = wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        texto_carga.SetFont(fuente)
        texto_carga.SetForegroundColour(wx.Colour(60, 60, 60)) # Gris oscuro

        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(bitmap, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        sizer.Add(texto_carga, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 15)

        panel.SetSizer(sizer)
        sizer.Fit(self)
        self.Centre()