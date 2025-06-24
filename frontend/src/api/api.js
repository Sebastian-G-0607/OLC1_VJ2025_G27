import axios from './axios.js';

export const getParse = async (input) => {
    try {
        const response = await axios.post('/parse', { input });
        return response.data;        
    } catch (error) {
        if (error.response.data) throw new Error(error.response.data.error)
        throw new Error(`Error al obtener el parse: ${error}`);
    }
}

export const getAST = async(input) =>{
    const response = await axios.post('/ast',{input}, { responseType: 'blob'});
    return response.data;
}

export const getMemoria = async(input) =>{
    const response = await axios.post('/reporte/memoria',{input}, { responseType: 'text/html'});
    return response.data;
}

export const getVectores = async() => {
    const response = await axios.get('/reporte/vectores');
    return response.data;
}

export const getAdvertencia = async(input) => {
    const response = await axios.post('/reporte/advertencias', { input }, { responseType: 'text/html' });
    return response.data;
}