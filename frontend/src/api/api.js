import axios from './axios.js';

export const getInfo = () => {
    return axios.get('/get-info');
}