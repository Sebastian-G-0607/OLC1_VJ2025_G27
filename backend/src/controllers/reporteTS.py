from backend.src.Interprete.simbol.InstanciaTabla import st

def generar_reporteTS():
    """
    Crear reporte html de la tabla de simbolos
    """
    with open('backend/src/controllers/reporteTS.html', 'w') as file:
        file.write('<html><head><title>Reporte de Tabla de Símbolos</title>')
        file.write('<link rel="stylesheet" type="text/css" href="frontend/src/pages/mainPage.css">')
        file.write('</head><body>')

        file.write('<h1>Reporte de Tabla de Símbolos</h1>')
        file.write('<table border="1"><tr><th>Nombre</th><th>Tipo de Entidad</th><th>Tipo de Dato</th><th>Valor</th><th>Alcance</th><th>Fila</th><th>Columna</th></tr>')

        # Valida si hay simbolos antes de generar el reporte
        if not st.symbols():
            file.write('<tr><td colspan="7">No hay símbolos en la tabla.</td></tr>')
            file.write('</table></body></html>')
            return
        
        # Si hay símbolos, se procede a generar el reporte
        # Itera sobre los símbolos y los agrega a la tabla
        for simbolo in st.symbols():
            file.write(f'<tr><td>{simbolo.name}</td><td>{simbolo.entity_type}</td><td>{simbolo.data_type}</td>')
            file.write(f'<td>{simbolo.value}</td><td>{simbolo.scope}</td><td>{simbolo.line}</td><td>{simbolo.column}</td></tr>')

        file.write('</table></body></html>')