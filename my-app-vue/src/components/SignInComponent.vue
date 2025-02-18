<script>
    import { mapActions, mapMutations, mapState } from 'vuex';

    export default {
        name: "SignInComponent",
        data() {
            return {
                username: '',
                password: '',
                isAuthenticating: false,
            }
        },
        computed: {
            ...mapState('Auth', ['user', 'authError']),
        },
        methods: {
            ...mapActions('Auth', ['login']),
            ...mapMutations('Auth', ['setError']),

            async onSubmit() {
                this.setError(null);
                this.isAuthenticating = true;

                const data = {
                    username: this.username,
                    password: this.password
                }
                await this.login(data);
                this.clearForm();
                this.isAuthenticating = false;
            },

            clearForm() {
                this.username = '';
                this.password = '';
            }
        }
    }
</script>
<template>
    <div class="form-body">
        <h1>Sign In</h1>
        <form @submit.prevent="onSubmit()">
            <p>
                Username:
                <input
                    type="text" v-model="username" :disabled="isAuthenticating" required
                >
            </p>
            <p>Password:
                <input
                    type="password" v-model="password" :disabled="isAuthenticating" required
                >
            </p>
            <button type="submit" :disabled="isAuthenticating">Sign In</button>
            <div v-if="authError" class="error-message">{{authError}}</div>
        </form>
    </div>
</template>
<style scoped>
    h1 {
        text-align: center;
    }

    button {
        display: flex;
        justify-content: center;
        align-items: center;
        width:100%;
        height: 30px;
        border-radius: 10px;
    }

    .form-body {
        background-color: white;
        padding: 20px 40px 20px 40px;
        margin: 5px;
        border-radius: 10px;
        border-color: black;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .error-message {
        color: red;
        font-size: 14px;
        text-align: center;
    }

</style>