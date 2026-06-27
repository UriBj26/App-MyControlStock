import wx
from fpdf import FPDF # type: ignore

def generar_pdf_stock(frame):
    """Función para crear el PDF usando los datos directos del inventario"""
    dialogo = wx.FileDialog(
        frame, 
        message="Guardar reporte de stock", 
        defaultFile="reporte_stock.pdf",
        wildcard="Archivos PDF (*.pdf)|*.pdf", 
        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
    )
    
    if dialogo.ShowModal() == wx.ID_CANCEL:
        return
        
    ruta_guardado = dialogo.GetPath()
    
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        
        # Título del reporte
        pdf.cell(0, 10, "MY STOCK CONTROL - REPORTE DE STOCK", ln=True, align="C")
        pdf.ln(10)
        
        # Encabezados
        pdf.set_font("Arial", "B", 12)
        pdf.cell(50, 10, "Nombre", border=1, align="C")
        pdf.cell(40, 10, "Categoria", border=1, align="C")
        pdf.cell(40, 10, "Precio", border=1, align="C")
        pdf.cell(40, 10, "Stock Disp.", border=1, align="C")
        pdf.ln()
        
        # Datos (Filtrando solo los productos con cantidad mayor a 0)
        pdf.set_font("Arial", "", 11)
        for p in frame.inv.obtener_todo():
            if p.cantidad > 0:
                pdf.cell(50, 8, str(p.nombre), border=1)
                pdf.cell(40, 8, str(p.categoria), border=1)
                pdf.cell(40, 8, f"$ {p.precio}", border=1, align="R")
                pdf.cell(40, 8, str(p.cantidad), border=1, align="C")
                pdf.ln()
                
        pdf.output(ruta_guardado)
        wx.MessageBox("El reporte en PDF se generó correctamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
        
    except Exception as error:
        wx.MessageBox(f"No se pudo generar el PDF: {error}", "Error", wx.OK | wx.ICON_ERROR)


def al_eliminar(frame, tabla, event):
    
    indice_seleccionado = tabla.GetFirstSelected()

    if indice_seleccionado == -1:
        wx.MessageBox("Por favor, seleccione un producto de la lista para eliminar.", "Aviso", wx.OK | wx.ICON_WARNING)
        return

    
    nombre_producto = tabla.GetItemText(indice_seleccionado, 0)

    
    confirmacion = wx.MessageBox(
        f"¿Está seguro de que desea eliminar por completo el producto '{nombre_producto}'?",
        "Confirmar eliminación",
        wx.YES_NO | wx.ICON_QUESTION
    )

    if confirmacion == wx.YES:
        
        frame.inv.eliminar(nombre_producto)
        wx.MessageBox(f"Producto '{nombre_producto}' eliminado con éxito.", "Éxito", wx.OK | wx.ICON_INFORMATION)
        
        
        mostrar_stock(frame)


def mostrar_stock(frame):
    frame.limpiar()

    sizer_interno = wx.BoxSizer(wx.VERTICAL)

    
    tabla = wx.ListCtrl(
        frame.contenido_panel,
        style=wx.LC_REPORT | wx.BORDER_SUNKEN
    )

    columnas = ["Nombre", "Categoría", "Precio", "Cantidad"]
    for i, columna in enumerate(columnas):
        tabla.InsertColumn(i, columna, width=150)

    for p in frame.inv.obtener_todo():
        fila = tabla.InsertItem(tabla.GetItemCount(), p.nombre)
        tabla.SetItem(fila, 1, p.categoria)
        tabla.SetItem(fila, 2, str(p.precio))
        tabla.SetItem(fila, 3, str(p.cantidad))

    
    
    sizer_botones = wx.BoxSizer(wx.HORIZONTAL)

    boton_eliminar = wx.Button(frame.contenido_panel, label="Eliminar Producto Seleccionado", size=(220, 30))
    boton_eliminar.SetBackgroundColour(wx.Colour(255, 200, 200)) 
    boton_eliminar.Bind(wx.EVT_BUTTON, lambda event: al_eliminar(frame, tabla, event))
    
    # NUEVO BOTÓN: Exportar PDF
    boton_pdf = wx.Button(frame.contenido_panel, label="Descargar (PDF)", size=(180, 30))
    boton_pdf.SetBackgroundColour(wx.Colour(212, 237, 218)) 
    boton_pdf.Bind(wx.EVT_BUTTON, lambda event: generar_pdf_stock(frame))

    # Añadimos los botones al sizer horizontal con una separación
    sizer_botones.Add(boton_pdf, 0, wx.RIGHT, 10)
    sizer_botones.Add(boton_eliminar, 0)
    # -----------------------------------------------------------

    sizer_interno.Add(tabla, 1, wx.EXPAND | wx.ALL, 5)
    
    # Cambiamos boton_eliminar por el contenedor con ambos botones alineado a la derecha
    sizer_interno.Add(sizer_botones, 0, wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM, 10)

    
    frame.contenido_sizer.Add(sizer_interno, 1, wx.EXPAND | wx.ALL, 10)
    frame.contenido_panel.Layout()