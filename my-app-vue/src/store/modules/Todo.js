import axios from "@/lib/axios";

const actions = {
    async fetchTodos({ rootGetters }) {
        try {
            const data = {
                userID: rootGetters['Auth/user'].id
            }

            const response = await axios.get(`/todos/`, { params: data });
            return response;
        } catch(e) {
            console.error(`[Error]:`, e);
        }
    },

    async createTodo({ rootGetters }) {
        try {
            const data = {
                userID: rootGetters['Auth/user'].id,
                title: 'New Task'
            }

            const response = await axios.post(`/todos/`, { data: data });
            return response["created_todo"];
        } catch(e) {
            console.error(`[Error]:`, e);
        }
    },

    async deleteTodo(_, idx) {
        try {
            const data = {
                todoID: idx
            }
            const response = await axios.delete(`/todos/`, { data: data });
        } catch(e) {
            console.error(`[Error]:`, e);
        }
    },

    async updateTodo(_, args) {
        try {
            const response = await axios.put(`/todos/`, { data: {...args} });
        } catch(e) {
            console.error(`[Error]:`, e);
        }

    }
}


export default {
    namespaced: true,
    actions
}