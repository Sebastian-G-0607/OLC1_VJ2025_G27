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