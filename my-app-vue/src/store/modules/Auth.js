import axios from "@/lib/axios";
import router from '@/router';

const state = {
    user: null,
    authError: null
};

const getters = {
    user: (state) => state.user
};

const mutations = {
    setUser(state, user) {
        state.user = user
    },

    setError(state, string) {
        state.authError = string
    },

    signOutUser(state) {
        state.user = null
    }
};

const actions = {
    async login({ commit }, data) {
        let response;
        try {
            response = await axios.post(`/auth/sign-in`, data);
            commit('setUser', response.user);
            localStorage.setItem('user', JSON.stringify(response.user));
            console.log('[Debug]: ', response.message);
            router.push({ name: 'home' });

        } catch (e) {
            console.error(`[Error]:`, e);
            commit('setError', e.response.data.error)
        }
    },

    async logout({ commit }) {
        commit('signOutUser');
        localStorage.removeItem('user');
        console.log('[Debug]: Logging out. Redirecting to Sign-in Page');
        router.push({ name: 'sign-in' });
    }
};

export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
}