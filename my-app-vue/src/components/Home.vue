<script>
import SignedInMixin from '@/mixins/SignedInMixin';
import { mapState } from 'vuex';

export default {
    name: 'Home',

    mixins: [SignedInMixin],

    computed: {
        ...mapState('Auth', ['user']),
        username() {
            return this.user?.username ?? 'Anonymous';
        }
    }
}
</script>
<template>
    <div>
        <h1>Welcome {{username}}!</h1>
        <span><a href="javascript:void(0);" @click="logout()">Log out</a> | <RouterLink to="/todos">Todolist</RouterLink></span>
    </div>
</template>
<style scoped>

</style>
