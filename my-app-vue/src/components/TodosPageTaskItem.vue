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
            if (this.task.isDone) return;
            this.$emit('taskTitleClicked', this.task.id);
        },

        deleteTask() {
            const args = {
                taskID: this.task.id,
                idx: this.idx
            }
            this.$emit('deleteTask', args);
        },

        markAsDone() {
            const args = {
                taskID: this.task.id,
                isDone: !this.task.isDone
            }
            this.$emit('markedAsDone', args);
        }
    }
}
</script>
<template>
    <li class="todo-item">
        <input type="checkbox" v-model="task.isDone" @click="markAsDone()">
        <input
            type="text"
            v-if="task.isBeingEdited"
            v-model="newTaskTitle"
            @keydown.enter="editTaskTitle()"
        >
        <span
            v-else @click="editTaskContents($event)"
            :class="{ isDone: task.isDone }"
        >
            {{ task.title }}
        </span>
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

    .isDone {
        text-decoration: line-through;
    }
</style>
