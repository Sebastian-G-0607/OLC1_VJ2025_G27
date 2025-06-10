import axios from './axios.js';

export const getParse = async (input) => {
    try {
        // If your backend expects raw text instead of { input }, send input directly:
        // const response = await axios.post('/parse', input, { headers: { 'Content-Type': 'text/plain' } });

        // Otherwise, if your backend expects { input }, keep as is:
        const response = await axios.post('/parse', { input });
        return response.data;        
    } catch (error) {
        throw new Error(`Error al obtener el parse: ${error}`);
    }
}