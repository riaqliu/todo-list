<script>
    import { mapMutations, mapState } from 'vuex';

    export default {
        name: 'Home',
        created() {
            // Get user from local storage
            const storedUser = localStorage.getItem('user');
            if (storedUser && !this.user) this.setUser(JSON.parse(storedUser));


            if (!this.user) {
                console.log("[DEBUG] User Unavailable. Redirecting to Sign-in Page");
                this.$router.push('/sign-in');
            }
        },
        computed: {
            ...mapState('Auth', ['user']),
            username() {
                return this.user?.username ?? 'Anonymous';
            }
        },
        methods: {
            ...mapMutations('Auth', ['setUser'])
        }
    }
</script>
<template>
    <div>
        <h1>Welcome {{username}}!</h1>
    </div>
</template>
<style scoped>

</style>
