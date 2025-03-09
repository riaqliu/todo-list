<script>
import TodosPageTaskItem from '@/components/TodosPageTaskItem.vue';
import SignedInMixin from '@/mixins/SignedInMixin';
import { mapState, mapActions, mapMutations } from 'vuex';

export default {
    name: 'TodosPage',
    components: {
        TodosPageTaskItem
    },

    mixins:[SignedInMixin],

    data() {
        return {
            searchString: '',
            taskItems: []
        }
    },

    async created() {
        await this.fetchInitialTodos();
    },

    computed: {
        ...mapState('Auth', ['user']),

        filteredTaskItems() {
            return this.taskItems.filter(task => {
                return task.title.trim()
                    .toLowerCase()
                    .includes(this.searchString.trim().toLowerCase());
            });
        },

        emptyMessage() {
            return this.searchString ? `There are no tasks matching "${this.searchString}"` : "You have no tasks";
        }
    },
    methods: {
        ...mapActions('Todo', ['fetchTodos', 'createTodo', 'deleteTodo', 'updateTodo']),
        ...mapMutations('Auth', ['setUser']),

        async fetchInitialTodos() {
            const fetchedTodos = await this.fetchTodos();

            fetchedTodos.forEach(todo => {
                const newTodo = {
                    id: todo.id,
                    title: todo.title,
                    hovered: false,
                    isBeingEdited: false,
                    isDone: todo.is_done
                };
                this.taskItems.push(newTodo);
            });
        },

        showButtons(taskID) {
            this.getTask(taskID).hovered = true;
        },

        hideButtons(taskID) {
            this.getTask(taskID).hovered = false;
        },

        async createNewTask() {
            const newTodo = await this.createTodo();

            if (!newTodo) return;

            const newTask = {
                id: newTodo.id,
                title: newTodo.title,
                hovered: false,
                isBeingEdited: false,
                isDone: newTodo.isDone
            }
            this.taskItems.push(newTask);
        },

        deleteTask({taskID, idx}) {
            this.taskItems.splice(idx, 1);
            this.deleteTodo(taskID);
        },

        editTask(taskID) {
            const task = this.getTask(taskID);
            task.isBeingEdited = !task.isBeingEdited;
        },

        updateTaskTitle({taskID, editedTitle}) {
            const task = this.getTask(taskID);
            if (!editedTitle) {
                task.isBeingEdited = false;
                return;
            }

            const args = {
                todoID: taskID,
                updatedTitle: editedTitle
            };
            this.updateTodo(args);

            task.title = editedTitle;
            task.isBeingEdited = false;
        },

        markedAsDone({taskID, isDone}){
            const task = this.getTask(taskID);
            task.isBeingEdited = false;

            const args = {
                todoID: taskID,
                isDone: isDone
            }
            this.updateTodo(args);

            task.isDone = isDone;
        },

        /**
         * Gets specific task from saved list of tasks
         * @param String taskID
         * @returns task
         */
        getTask(taskID) {
            return this.taskItems.find(task => task.id === taskID);
        }
    }
}
</script>
<template>
    <div>
        <RouterLink to="/">Home</RouterLink>
        <div class="content-body">
            <h1>TODO LIST</h1>
            <div>
                <div class="search-container">
                    <input type="text" v-model="searchString">
                </div>
            </div>
            <div>
                <ul v-if="filteredTaskItems.length" class="task-list">
                    <TodosPageTaskItem
                        v-for=" (task, idx) in filteredTaskItems"
                        :key="task.id"
                        :task="task"
                        :idx="idx"
                        @delete-task="deleteTask($event)"
                        @task-title-clicked="editTask($event)"
                        @edited-task-title="updateTaskTitle($event)"
                        @marked-as-done="markedAsDone($event)"
                        @mouseenter="showButtons(task.id)"
                        @mouseleave="hideButtons(task.id)"
                    ></TodosPageTaskItem>
                </ul>
                <span class="empty-message" v-else>{{emptyMessage}}</span>
            </div>

            <div class="footer">
                <button class="button-4" @click="createNewTask()">Add new Todo</button>
            </div>
        </div>
    </div>

</template>
<style lang="scss" scoped>
    h1 {
        text-align: center;
        font-size: 40px;
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    }

    .content-body {
        background-color: white;
        width:70svw;
        max-width: 705px;
        min-width: 360px;
        height:80svh;
        border-radius: 2px;
        border-width: 8px;
        display: grid;
        grid-template-rows: 120px 8% 60% auto;
        grid-template-columns: 1fr;
    }

    .search-container {
        background-color: rgb(233, 233, 233);
        margin: 0px 20px 0px 20px;
        border-bottom: 2px solid black;
        input[type=text]{
            background-color: rgb(233, 233, 233);
            width: 100%;
            margin-left: 8%;
            height: 40px;
            outline: none;
            border: none;
            font-size: 20px;
            margin: 0;
        }
    }
    .empty-message {
        display:block;
        text-align: center;
        width: 100%;
        height: 100%;
    }

    .footer {
        display: inline-grid;
    }

    .task-list {
        list-style-type: none;
        padding: 0 20px 0 20px;
        height: 100%;
        overflow:auto;

        .todo-item {
            background-color: rgb(233, 233, 233);
        }

        .todo-item:nth-child(odd) {
            background-color: #d1e4bd;
        }
    }


</style>
