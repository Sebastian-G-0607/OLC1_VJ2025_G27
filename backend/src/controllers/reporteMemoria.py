import os

from backend.src.Interprete.nodes.instrucciones.Execute import Execute
from backend.src.Interprete.nodes.instrucciones.Procedimiento import Procedimiento
from backend.src.Interprete.simbol.RaizArbol import Arbol

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
memoria_html_path = os.path.join(PROJECT_ROOT, 'public', 'memoria', 'reporteMemoria.html')

from flask import Blueprint, jsonify, request, send_file
from backend.src.Interprete.simbol.InstanciaTabla import st
from backend.src.Interprete.parser import parse
from backend.src.Interprete.simbol.ListaErrores import errores
from backend.src.Interprete.visitor_object.visitor_output import Visitor_Output

BlueprintMemoria = Blueprint('reporte_memoria', __name__)

@BlueprintMemoria.route('/api/reporte/memoria', methods=['POST'])
def generar_reporteMemoria():

    #Limpiar la lista de errores antes de cada petición
    errores.clear()
    #Limpia la tabla de simbolos antes de cada petición
    global st
    st.clear()

    ast = None
    data = None
    instrucciones = None

    # Accede al contenido JSON enviado por el frontend
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'No hay contenido para interpretar'}), 400

    input = data['input']

    # SE OBTIENE EL AST CREADO POR EL PARSER
    try:
        instrucciones = parse(input['code'])
        ast = Arbol(instrucciones)
    except Exception as e:
        print(f"Error al crear el árbol")
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al crear el AST durante el reporte de memoria'}), 500

    if ast is None: 
        print("Hubo un error al parsear la expresión durante el reporte de memoria.")
        return jsonify({'error': 'Error al parsear la expresión durante el reporte de memoria.'}), 500

    print("AST generado correctamente.")
    visitor = Visitor_Output(ast)

    # SE IMPRIME EL AST
    if ast.getInstrucciones() is None:
        print("El AST no contiene instrucciones.")
        return jsonify({'error': 'El AST no contiene instrucciones para el reporte de memoria.'}), 500
    try:
        for nodo in ast.getInstrucciones():
            try:
                nodo.accept(visitor)
            except TypeError as e:
                if "NoneType" in str(e):
                    continue  # Ignora y sigue con el siguiente nodo
                else:
                    raise  # Si es otro TypeError, relanza la excepción
    except Exception as e:
        print(f"Error al visitar el AST: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al visitar el AST'}), 500

    try:
        # CSS PARA EL REPORTE HTML
        css = """
<style>
    body {
        font-family: 'Arial', sans-serif;
        max-width: 1000px; /* Aumentado para acomodar tabla más ancha */
        margin: 0 auto;
        padding: 20px;
        background-color: #FFFCF8;
        color: #5A4A3A;
        line-height: 1.6;
    }
    h1 {
        text-align: center;
        margin-bottom: 30px;
        color: #D47D36;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    table {
        width: 105%; /* Tabla más ancha que el contenedor */
        margin-left: -2.5%; /* Compensa el aumento de ancho */
        border-collapse: collapse;
        margin-bottom: 30px;
        border: 1px solid #F0E6DC;
    }
    th, td {
        border: 1px solid #F0E6DC;
        padding: 12px 15px;
        text-align: left;
    }
    th {
        background-color: #FDF2E5;
        color: #D47D36;
        font-weight: 500;
    }
    tr:nth-child(even) {
        background-color: #FFF9F3;
    }
    tr:hover {
        background-color: #FDF2E5;
    }
    .execution-container {
        margin-top: 30px;
    }
    .execution-title {
        text-align: left;
        margin-bottom: 20px;
        color: #D47D36;
        font-weight: 400;
    }
    .content-row {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        padding: 0 20px;
        margin-bottom: 25px;
        position: relative; /* Para posicionar la flecha */
    }
    .stack-container {
        width: 240px;
        margin-right: 20px;
    }
    .stack-title {
        font-weight: 500;
        margin-bottom: 15px;
        font-size: 1em;
        color: #D47D36;
        padding-left: 2px;
        letter-spacing: 0.3px;
    }
    .stack {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .stack-item {
        border: 1px solid #F0D9C5;
        padding: 12px 15px;
        background-color: #FFF9F3;
        text-align: center;
        border-radius: 3px;
        color: #5A4A3A;
        font-size: 0.95em;
        transition: all 0.15s ease;
    }
    .stack-item:hover {
        background-color: #FDF2E5;
        border-color: #E8C7A8;
    }
    .symbols-container {
        width: 380px;
        margin-left: 20px;
    }
    .symbols-title {
        font-weight: 500;
        margin-bottom: 15px;
        font-size: 1em;
        color: #D47D36;
        padding-left: 2px;
        visibility: hidden;
    }
    .symbols-table {
        width: 100%;
        border: 1px solid #F0E6DC;
    }
    .symbols-table th {
        background-color: #FDF2E5;
        color: #D47D36;
        font-weight: 500;
    }
    h2 {
        color: #D47D36;
        border-bottom: 1px solid #F0D9C5;
        padding-bottom: 5px;
        font-weight: 400;
        margin-top: 40px;
    }
    
    /* Flecha entre la pila y la tabla */
    .arrow-connector {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        color: #D47D36;
        font-size: 90px;
        width: 200px;
    }
</style>
            """
        with open(memoria_html_path, 'w') as file:
            file.write('<html><head><title>Reporte de memoria</title>')
            file.write(css)
            file.write('</head><body>')
            file.write('<h1>Reporte de memoria</h1>')
            file.write('<h1>Procedimientos</h1>')

            #FOR PRINCIPAL QUE RECORRE CADA PROCEDIMIENTO EN EL AST
            for idx, nodo in enumerate(ast.getInstrucciones()):
                if not isinstance(nodo, Procedimiento):
                    continue  # Ignora nodos que no son Procedimiento o Execute
                if isinstance(nodo, Procedimiento):
                    try:
                        file.write('<table><thead><tr><th>Nombre</th><th>Atributos</th><th>No. de llamadas</th><th>Líneas de llamada</th></tr></thead>')
                        #TABLA QUE DEFINE EL PROCEDIMIENTO
                        tabla = f'''<tbody>
                                <tr>
                                    <td>{nodo.id}</td>
                                    <td>{', '.join([f"{param.id}: {param.tipo}" for param in nodo.parametros])}</td>
                                    
                                    <td>{str(len(nodo.lineas_llamada))}</td>
                                    <td>{', '.join([str(linea) for linea in nodo.lineas_llamada])}</td>
                                </tr>
                            </tbody>
                        </table>'''
                        file.write(tabla)
                        #EJECUCIONES DEL PROCEDIMIENTO
                        ejecuciones = f'''<div class="execution-container">
                                <h2 class="execution-title">Ejecuciones</h2>'''
                        file.write(ejecuciones)
                        
                        #LISTA PARA SABER DONDE RETORNA EL PROCEDIMIENTO
                        retornos = []
                        for idx_exec, instruccion in enumerate(ast.getInstrucciones()):
                            if isinstance(instruccion, Execute) and instruccion.identificador == nodo.id:
                                retornos.append(idx_exec)

                        # SE RECORRE CADA EXECUTE DEL PROCEDIMIENTO
                        for i, linea in enumerate(nodo.lineas_llamada):
                            #SE CREA LA PILA
                            ejecucion = f'<div class="content-row"><div class="stack-container"><div class="stack-title">Línea {linea}</div>'
                            # Obtener los ids de las declaraciones dentro del procedimiento
                            declaracion_ids = [
                                instr.id for instr in getattr(nodo, 'instrucciones', [])
                                if instr.__class__.__name__ == 'Declaracion'
                            ]
                            ejecucion += f'''<div class="stack">
                                    <div class="stack-item"><b style="font-size:1.2em;">Parámetros</b><br><br>{', '.join([f"{param.id}" for param in nodo.parametros])}</div>'''
                            if declaracion_ids:
                                ejecucion += f'''<div class="stack-item"><b style="font-size:1.1em;">Variables locales</b><br><br>{', '.join(declaracion_ids)}</div>'''
                            ejecucion += f'''<div class="stack-item">{nodo.id}()</div>'''
                            # Validar que el índice no esté fuera de rango
                            idx_retorno = retornos[i] + 1 if i < len(retornos) and retornos[i] + 1 < len(ast.getInstrucciones()) else None
                            if idx_retorno is not None:
                                linea_retorno = getattr(ast.getInstrucciones()[idx_retorno], 'linea', 'N/A')
                                classname = ast.getInstrucciones()[idx_retorno].__class__.__name__
                                ejecucion += f'<div class="stack-item">Retorno en linea {linea_retorno} {classname}</div>'
                            else:
                                ejecucion += f'<div class="stack-item">Retorno fin de programa</div>'
                            ejecucion += '</div></div>'
                            file.write(ejecucion)
                            # Obtener todas las instrucciones de tipo Execute para este procedimiento
                            executes = [
                                instr for instr in ast.getInstrucciones()
                                if isinstance(instr, Execute) and instr.identificador == nodo.id
                            ]
                            # Para la ejecución actual (índice i), obtener el ID correspondiente
                            if i < len(executes):
                                execute_actual = executes[i]
                                id_ejecucion = execute_actual.id
                                
                                # Obtener todos los símbolos del procedimiento
                                simbolos_proc = st.get_scope_proc(nodo.id)

                                # Filtrar símbolos cuyo scope termine con el ID de la ejecución actual
                                simbolos_filtrados = [
                                    s for s in simbolos_proc 
                                    if s.scope.endswith(f"_{id_ejecucion}")
                                ]
                            else:
                                simbolos_filtrados = []
                            
                            # Construir la tabla de símbolos
                            tabla_simbolos = f'''<div class="arrow-connector">→</div><div class="symbols-container">
                                <div class="symbols-title">Tabla de Símbolos</div>
                                    <table class="symbols-table">
                                        <thead>
                                            <tr>
                                                <th>Variable</th>
                                                <th>Valor</th>
                                                <th>Tipo</th>
                                            </tr>
                                        </thead>
                                        <tbody>'''
                            
                            # Agregar cada símbolo a la tabla
                            for simbolo in simbolos_filtrados:
                                tabla_simbolos += f'''
                                            <tr>
                                                <td>{simbolo.name}</td>
                                                <td>{simbolo.value}</td>
                                                <td>{simbolo.data_type}</td>
                                            </tr>'''
                            
                            # Si no hay símbolos, mostrar un mensaje o dejar vacío
                            if not simbolos_filtrados:
                                tabla_simbolos += f'''
                                            <tr>
                                                <td colspan="3">No hay símbolos para esta ejecución</td>
                                            </tr>'''
                            
                            # Cerrar la tabla
                            tabla_simbolos += '''
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            </div>'''
                            
                            file.write(tabla_simbolos)
                    except Exception as e:
                        print(f"Error al procesar el nodo {nodo}: {str(e)}")
                continue
            file.write('''</body></html>''')
        return send_file(memoria_html_path, mimetype='text/html')

    except Exception as e:
        print(f"Error al generar el reporte de memoria: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al generar el reporte de memoria.'}), 500

    # Devuelve el archivo html



    # for simbolo in st.symbols:
    #     print(f"Procesando símbolo")

    # with open(memoria_html_path, 'w') as file:
    #     file.write('<html><head><title>Reporte de memoria</title>')
    #     file.write(css)
    #     file.write('</head><body>')

    #     file.write('<h1>Reporte de memoria</h1>')
    #     file.write('<h1>Procedimientos</h1>')


    #     # Valida si hay simbolos antes de generar el reporte
    #     if not st.symbols:
    #         file.write('<tr><td colspan="7">No hay símbolos en la tabla.</td></tr>')
    #         file.write('</table></body></html>')
        
    #     else:
    #         # Si hay símbolos, se procede a generar el reporte
    #         for simbolo in st.symbols:
    #             file.write(f'<tr><td>{simbolo.name}</td><td>{simbolo.entity_type}</td><td>{simbolo.data_type}</td>')
    #             file.write(f'<td>{simbolo.value}</td><td>{simbolo.scope}</td><td>{simbolo.line}</td><td>{simbolo.column}</td></tr>')

    #     file.write('</table></body></html>')
    # return send_file(memoria_html_path, mimetype='text/html')