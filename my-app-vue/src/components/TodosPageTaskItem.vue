<script>
export default {
    name: 'TodosPageTaskItem',
    props: {
        task: {
            type: Object,
            required: true
        },
        idx: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            newTaskTitle: this.task.title,
            isDone: false
        }
    },
    methods: {
        editTaskTitle() {
            const args = {
                taskID: this.task.id,
                editedTitle: this.newTaskTitle,
            }
            this.$emit('editedTaskTitle', args);
        },

        editTaskContents() {
            this.$emit('taskTitleClicked', this.task.id);
        },

        deleteTask() {
            this.$emit('deleteTask', this.idx);
        },

        markAsDone() {
            const args = {
                taskID: this.task.id,
                isDone: !this.isDone
            }
            this.$emit('markedAsDone', args);
        }
    }
}
</script>
<template>
    <li class="todo-item">
        <input type="checkbox" v-model="isDone" @click="markAsDone()">
        <input
            type="text"
            v-if="task.isBeingEdited"
            v-model="newTaskTitle"
            @keydown.enter="editTaskTitle()"
        >
        <span v-else @click="editTaskContents($event)">{{ task.title }}</span>
        <button v-if="task.hovered" class="delete-button" @click="deleteTask()">delete</button>
    </li>
</template>
<style lang="scss" scoped>
    .todo-item {
        padding: 10px 0 10px 10px;
    }

    .delete-button {
        float: right;
    }
</style>
