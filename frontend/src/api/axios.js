import axios from 'axios';

const API_URL = '/api';
//SE CREA UNA INSTANCIA DE AXIOS CON LA URL BASE
const axiosInstance = axios.create({
    baseURL: API_URL,
    withCredentials: true, // Habilita el envío de cookies
})

export default axiosInstance;