import { mapActions, mapMutations } from "vuex";

export default {
    created() {
        // Get user from local storage
        const storedUser = localStorage.getItem('user');

        if (!this.user) {
            if (storedUser) this.setUser(JSON.parse(storedUser));
            else {
                console.log("[DEBUG]: User Unavailable.");
                this.logout();
            }
        }

        this.sync();
    },
    methods: {
        ...mapMutations('Auth', ['setUser']),
        ...mapActions('Auth', ['logout', 'sync'])
    }
}