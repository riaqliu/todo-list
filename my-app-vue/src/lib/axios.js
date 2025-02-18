import axios from 'axios';

const BASE_URL = "http://localhost:8000"

const instance = axios.create({
    baseURL: BASE_URL,
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
    headers: {
        'X-Requested-With': 'XMLHttpRequest'
    }
});

instance.interceptors.response.use(
    (response) => Promise.resolve(response.data),
    (error) => Promise.reject(error)
);

export default instance;
