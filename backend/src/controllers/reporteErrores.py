from backend.src.Interprete.simbol.ListaErrores import errores


def generar_reporteErrores():
    """
    Crear reporte html de errores
    """
    with open('backend/src/controllers/reporteErrores.html', 'w') as file:
        file.write('<html><head><title>Reporte de Errores</title>')
        file.write('<link rel="stylesheet" type="text/css" href="frontend/src/pages/mainPage.css">')
        file.write('</head><body>')

        file.write('<h1>Reporte de Errores</h1>')
        file.write('<table border="1"><tr><th>Tipo</th><th>Descripción</th><th>Fila</th><th>Columna</th></tr>')
        
        # Valida si hay errores antes de generar el reporte
        if not errores:
            file.write('<tr><td colspan="4">No hay errores registrados.</td></tr>')
            file.write('</table></body></html>')
            return

        for error in errores:
            file.write(f'<tr><td>{error.tipo}</td><td>{error.descripcion}</td><td>{error.linea}</td><td>{error.columna}</td></tr>')
        
        file.write('</table></body></html>')

