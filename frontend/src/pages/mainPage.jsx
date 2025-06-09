import './mainPage.css';
import { useRef } from 'react';
import Swal from 'sweetalert2';
import { getInfo } from '../api/api.js'; // Asegúrate de que la ruta sea correcta

const MainPage = () => {
    const fileInputRef = useRef(null);
    const textareaRef = useRef(null);

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
            const response = await getInfo();
            console.log(response);
        } catch (error) {
            console.error('Error al interpretar:', error);
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
                    ></textarea>
                </div>
                <div className="output-area">
                    <h2>Salida</h2>
                    <div className="controls_output">
                        <button className='editor-buttons'>Reporte de Errores</button>
                        <button className='editor-buttons'>Tabla de Símbolos</button>
                        <button className='editor-buttons'>AST</button>
                    </div>

                    <textarea id="resultado" readOnly></textarea>
                </div>
            </div>
        </div>
    );
};

export default MainPage;
