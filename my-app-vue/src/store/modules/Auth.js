import axios from "@/lib/axios";
import router from '@/router';

const state = {
    user: null,
    authError: null
};

const mutations = {
    setUser(state, user) {
        state.user = user
    },
    setError(state, string) {
        state.authError = string
    },
}

const actions = {
    async login({ commit }, data) {
        let response;
        try {
            response = await axios.post(`/auth/sign-in`, data);
            commit('setUser', response.user);
            localStorage.setItem('user', JSON.stringify(response.user));
            console.log('[Debug]:', response.message);
            router.push({ name: 'home' });

        } catch (e) {
            console.error(`[Error]:`, e);
            commit('setError', e.response.data.error)
        }
    }
};

export default {
    namespaced: true,
    state,
    mutations,
    actions
}