import wx
from fpdf import FPDF # type: ignore

class VerStock:
    def __init__(self, frame):
        self.frame = frame
        self.tabla = None

    def generar_pdf_stock(self, event):
        dialogo = wx.FileDialog(
            self.frame,
            message="Guardar reporte de stock",
            defaultFile="reporte_stock.pdf",
            wildcard="Archivos PDF (*.pdf)|*.pdf",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        )
        if dialogo.ShowModal() == wx.ID_CANCEL:
            return
        ruta = dialogo.GetPath()
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "MY STOCK CONTROL - REPORTE DE STOCK", ln=True, align="C")
            pdf.ln(10)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(50, 10, "Nombre", border=1, align="C")
            pdf.cell(40, 10, "Categoria", border=1, align="C")
            pdf.cell(40, 10, "Precio", border=1, align="C")
            pdf.cell(40, 10, "Stock Disp.", border=1, align="C")
            pdf.ln()
            pdf.set_font("Arial", "", 11)
            for p in self.frame.inv.obtener_todo():
                pdf.cell(50, 10, str(p.nombre), border=1)
                pdf.cell(40, 10, str(p.categoria), border=1)
                pdf.cell(40, 10, str(p.precio), border=1)
                pdf.cell(40, 10, str(p.cantidad), border=1)
                pdf.ln()
            pdf.output(ruta)
            wx.MessageBox("PDF generado correctamente", "Éxito", wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            wx.MessageBox(f"Error al generar PDF: {e}", "Error", wx.OK | wx.ICON_ERROR)

    def eliminar_producto(self, event):
        indice = self.tabla.GetFirstSelected()
        if indice == -1:
            wx.MessageBox("Seleccione un producto de la lista.", "Aviso")
            return
        nombre = self.tabla.GetItemText(indice)
        if wx.MessageBox(f"¿Eliminar {nombre}?", "Confirmar", wx.YES_NO) == wx.YES:
            self.frame.inv.eliminar(nombre)
            mostrar_stock(self.frame)

def mostrar_stock(frame):
    frame.limpiar()
    controlador = VerStock(frame)
    sizer_interno = wx.BoxSizer(wx.VERTICAL)
    
 
    tabla = wx.ListCtrl(
        frame.contenido_panel,
        style=wx.LC_REPORT | wx.BORDER_SUNKEN
    )
    controlador.tabla = tabla
    
   
    columnas = ["Nombre", "Categoría", "Precio", "Cantidad"]
    for i, columna in enumerate(columnas):
        tabla.InsertColumn(i, columna, width=150)
        
   
    for p in frame.inv.obtener_todo():
        fila = tabla.InsertItem(tabla.GetItemCount(), p.nombre)
        tabla.SetItem(fila, 1, p.categoria)
        tabla.SetItem(fila, 2, str(p.precio))
        tabla.SetItem(fila, 3, str(p.cantidad))
        
    
    sizer_botones = wx.BoxSizer(wx.HORIZONTAL)
    
    boton_pdf = wx.Button(frame.contenido_panel, label="Descargar (PDF)", size=(180, 30))
    boton_pdf.SetBackgroundColour(wx.Colour(212, 237, 218))
    boton_pdf.Bind(wx.EVT_BUTTON, controlador.generar_pdf_stock)
    
    boton_eliminar = wx.Button(frame.contenido_panel, label="Eliminar Producto Seleccionado", size=(220, 30))
    boton_eliminar.SetBackgroundColour(wx.Colour(255, 200, 200))
    boton_eliminar.Bind(wx.EVT_BUTTON, controlador.eliminar_producto)
    
    sizer_botones.Add(boton_pdf, 0, wx.RIGHT, 10)
    sizer_botones.Add(boton_eliminar, 0)
    
    
    sizer_interno.Add(tabla, 1, wx.EXPAND | wx.ALL, 5)
    sizer_interno.Add(sizer_botones, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
    
    frame.contenido_sizer.Add(sizer_interno, 1, wx.EXPAND | wx.ALL, 10)
    frame.contenido_panel.Layout()
