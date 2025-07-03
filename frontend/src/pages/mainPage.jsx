import './mainPage.css';
import { useRef } from 'react';
import Swal from 'sweetalert2';
import { getParse, getAST, getMemoria, getAdvertencia } from '../api/api.js'; // Asegúrate de que la ruta sea correcta

const MainPage = () => {
    const fileInputRef = useRef(null);
    const textareaRef = useRef(null);
    const resultadoRef = useRef(null); // Nuevo ref para el textarea de salida

    const handleTabInTextarea = (e) => {
        if (e.key === 'Tab') {
            e.preventDefault();
            const textarea = textareaRef.current;
            const start = textarea.selectionStart;
            const end = textarea.selectionEnd;
            // Inserta el tabulador en la posición del cursor
            textarea.value = textarea.value.substring(0, start) + '\t' + textarea.value.substring(end);
            // Mueve el cursor después del tabulador
            textarea.selectionStart = textarea.selectionEnd = start + 1;
        }
    };

    const handleFileButtonClick = () => {
        fileInputRef.current.value = ''; // Permite cargar el mismo archivo varias veces
        fileInputRef.current.click();
    };

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (!file) return;

        if (!file.name.endsWith('.objc')) {
            Swal.fire({
                icon: 'error',
                title: 'Archivo incorrecto',
                text: 'Seleccione un archivo con extensión .objc',
            });
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            if (textareaRef.current) {
                textareaRef.current.value = e.target.result;
            }
        };
        reader.readAsText(file);
    };

    const handleInterpretarClick = async () => {
        try {
            if (resultadoRef.current) {
                resultadoRef.current.value = '';
            }
            const codigo = textareaRef.current ? textareaRef.current.value : '';
            const data = {
                code: codigo,
            }
            const response = await getParse(data); // Envía el código al backend
            if (resultadoRef.current) {
                resultadoRef.current.value = response.consola; // Muestra la respuesta en el textarea de salida
            }
            console.log(response);
        } catch (error) {
            console.error('Error al interpretar el código:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Ocurrió un error al interpretar el código. Por favor, revisa tu código y vuelve a intentarlo.',
                footer: 'Consulta el reporte de errores para más detalles',
            });
        }
    };

    const handleASTClick = async () => {
        try {
            const codigo = textareaRef.current ? textareaRef.current.value : '';
            const data = { code: codigo };
            const svgBlob = await getAST(data);

            // Crear URL temporal para el blob
            const url = window.URL.createObjectURL(svgBlob);

            // Abrir el SVG en una nueva pestaña
            window.open(url, '_blank', 'noopener,noreferrer');
        } catch (error) {
            console.error('Error al generar el AST:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Ocurrió un error al crear el AST. Por favor, revisa tu código y vuelve a intentarlo.',
                footer: 'Consulta el reporte de errores para más detalles',
            });
        }
    };

    const handleGenerarReporteErrores = () => {
        window.open('http://localhost:4000/reporte/errores', '_blank');
    };

    const handleGenerarReporteTS = () => {
        window.open('http://localhost:4000/reporte/simbolos', '_blank');
    };

    const handleGenerarReporteVectores = () => {
        window.open('http://localhost:4000/reporte/vectores', '_blank');
    };

    const handleGenerarReporteMemoria = async () => {
        try {
            const codigo = textareaRef.current ? textareaRef.current.value : '';
            const data = { code: codigo };
            const html = await getMemoria(data);

            // Abrir una nueva ventana y escribir el HTML recibido
            const newWindow = window.open('', '_blank');
            if (newWindow) {
                newWindow.document.open();
                newWindow.document.write(html);
                newWindow.document.close();
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'No se pudo abrir una nueva ventana para mostrar el reporte de memoria.',
                });
            }
        } catch (error) {
            console.error('Error al generar el reporte de memoria:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Ocurrió un error al generar el reporte de memoria. Por favor, revisa tu código y vuelve a intentarlo.',
                footer: 'Consulta el reporte de errores para más detalles',
            });
        }
    };

    const handleGenerarReporteAdvertencias = async () => {
        try {
            const codigo = textareaRef.current ? textareaRef.current.value : '';
            const data = { code: codigo };
            const html = await getAdvertencia(data);

            // Abrir una nueva ventana y escribir el HTML recibido
            const newWindow = window.open('', '_blank');
            if (newWindow) {
                newWindow.document.open();
                newWindow.document.write(html);
                newWindow.document.close();
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'No se pudo abrir una nueva ventana para mostrar el reporte de advertencias.',
                });
            }
        } catch (error) {
            console.error('Error al generar el reporte de advertencias:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Ocurrió un error al generar el reporte de advertencias. Por favor, revisa tu código y vuelve a intentarlo.',
                footer: 'Consulta el reporte de errores para más detalles',
            });
        }
    };

    return (
        <div>
            <h1>OBJ - C</h1>

            <div className="container">
                <div className="input-area">
                    <h2>Entrada</h2>
                    <div className="controls_input">
                        {/* Oculta el input de archivo */}
                        <input
                            type="file"
                            id="fileInput"
                            accept=".objc"
                            ref={fileInputRef}
                            style={{ display: 'none' }}
                            onChange={handleFileChange}
                        />
                        <button type="button" className='editor-buttons' onClick={handleFileButtonClick}>
                            Cargar Archivo
                        </button>
                        <button
                            className='editor-buttons'
                            onClick={handleInterpretarClick}
                        >
                            Interpretar
                        </button>
                    </div>

                    <textarea
                        id="editor"
                        placeholder="Escribe o carga tu código aquí..."
                        ref={textareaRef}
                        spellCheck={false}
                        autoCorrect="off"
                        onKeyDown={handleTabInTextarea}
                    ></textarea>
                </div>
                <div className="output-area">
                    <h2>Salida</h2>
                    <div className="controls_output">
                        <button className='editor-buttons' onClick={handleGenerarReporteErrores}>Reporte de Errores</button>
                        <button className='editor-buttons' onClick={handleGenerarReporteTS}>Tabla de Símbolos</button>
                        <button className='editor-buttons' onClick={handleASTClick} >AST</button>
                        <button className='editor-buttons' onClick={handleGenerarReporteVectores} >Vectores</button>
                        <button className='editor-buttons' onClick={handleGenerarReporteMemoria} >Memoria</button>
                        <button className='editor-buttons' onClick={handleGenerarReporteAdvertencias} >Advertencias</button>
                    </div>

                    <textarea id="resultado" readOnly ref={resultadoRef} spellCheck={false}></textarea>
                </div>
            </div>
        </div>
    );
};

export default MainPage;
