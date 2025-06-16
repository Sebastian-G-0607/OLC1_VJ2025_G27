import './mainPage.css';
import { useRef, useState, useEffect } from 'react';
import Swal from 'sweetalert2';
import { getParse, getAST } from '../api/api.js'; // Asegúrate de que la ruta sea correcta

const MainPage = () => {
    const fileInputRef = useRef(null);
    const textareaRef = useRef(null);
    const resultadoRef = useRef(null); // Nuevo ref para el textarea de salida
    const [svgUrl, setSvgUrl] = useState(null);

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
                text: 'SeleccioneP un archivo con extensión .objc',
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
            console.error('Error al interpretar:', error);
        }
    };

    const handleASTClick = async () => {
        try {
            const codigo = textareaRef.current ? textareaRef.current.value : '';
            const data = { code: codigo };
            const svgBlob = await getAST(data);

            // Crear URL temporal para el blob
            const url = window.URL.createObjectURL(svgBlob);
            setSvgUrl(url);
        } catch (error) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'No se pudo generar el AST.',
            });
        }
    };

    // Limpieza de la URL temporal cuando cambia
    useEffect(() => {
        return () => {
            if (svgUrl) window.URL.revokeObjectURL(svgUrl);
        };
    }, [svgUrl]);

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
                        <button className='editor-buttons'>Reporte de Errores</button>
                        <button className='editor-buttons'>Tabla de Símbolos</button>
                        <button className='editor-buttons'  onClick={handleASTClick} >AST</button>
                    </div>

                    <textarea id="resultado" readOnly ref={resultadoRef} spellCheck={false}></textarea>
                    {/* Mostrar el SVG si existe */}
                    {svgUrl && (
                        <div style={{ marginTop: 20 }}>
                            <h3>Árbol de Sintaxis Abstracta (AST)</h3>
                            <img src={svgUrl} alt="AST" style={{ width: '100%', maxHeight: 500 }} />
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default MainPage;
