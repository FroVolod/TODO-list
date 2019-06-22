<template>
    <div>
        <h1>TODO-list</h1>
        <b-container>
            <b-row class='head text-center'>
                <b-col cols='7'>Title</b-col>
                <b-col cols='4'>Create date</b-col>
                <b-col cols='1'>Status</b-col>
            </b-row>
            <draggable :list="tasksList" @end="onEnd" >
                <b-row class="task" v-for="task in tasksList" :key="task.id">
                    <b-col cols='7'>{{ task.title }}</b-col>
                    <b-col cols='4'>{{ task.date_creation }}</b-col>
                    <b-col cols='1'>
                        <b-form-checkbox
                            :key="task.id"
                            :checked="task.is_done"
                            @change='changeTaskStatus(task.id, !task.is_done)'
                        >
                        </b-form-checkbox>
                    </b-col>
                </b-row>
            </draggable>
        </b-container> 
        <b-button @click="showCreate" v-if="!visible">Add new task</b-button>
        <br/>
        <div v-if="visible">
            <input v-model="title" placeholder="Enter title of task" />
            <b-button @click="createTask">Create</b-button>
            <b-button @click="showCreate">Cancel</b-button>
        </div>
        
    </div>
</template>

<script>
import draggable from 'vuedraggable';

export default {
    name: 'task-list',
    components: {
        draggable,
    },
    data() {
        return {
            tasksList: [],
            title: '',
            dateDue: null,
            visible: false,
        };
    },
    beforeMount() {
        this.getTasksList()
    },
    methods: {
        onEnd(evt) {
            if (evt.oldIndex===evt.newIndex) return
            const formData = new FormData();
            formData.append('oldIndex', evt.oldIndex);
            formData.append('newIndex', evt.newIndex);
            fetch(`http://127.0.0.1:8000/api/tasks/`, {
                method: 'PUT',
                body: formData
            })
            .then(JSON)  
            .then((data) => {                
                console.log('Request succeeded with JSON response', data);
                this.getTasksList();
            })
            .catch((error) => {  
                console.log('Request failed', error);  
            });
        },
        getTasksList() {
            fetch(`http://127.0.0.1:8000/api/tasks/`)
                .then((response) => response.json())
                .then((data) => {
                    console.log('Request succeeded with JSON response', data);
                    this.tasksList = data;
                })
                .catch((error) => {  
                console.log('Request failed', error);  
            });
        },
        createTask() {
            const formData = new FormData();
            formData.append('title', this.title);
            fetch(`http://127.0.0.1:8000/api/tasks/`, {
                method: 'POST',
                body: formData
            })
            .then(JSON)  
            .then((data) => {                
                console.log('Request succeeded with JSON response', data);
                this.getTasksList();
                this.title = '';
                this.dateDue = null;
                this.visible = false;
            })
            .catch((error) => {  
                console.log('Request failed', error);  
            });
        },
        changeTaskStatus(id, status) {
            const isDone = status ? 'True' : 'False'
            const formData = new FormData();
            formData.append('isDone', isDone);
            fetch(`http://127.0.0.1:8000/api/tasks/${id}/`, {
                method: 'PUT',
                body: formData
            })
            .then(JSON)  
            .then((data) => {                
                console.log('Request succeeded with JSON response', data);
                this.getTasksList();
            })
            .catch((error) => {  
                console.log('Request failed', error);  
            });
        },
        taskStatus() {

        },
        showCreate() {
            this.visible = !this.visible;
        },
    },
}
</script>

<style>
.head {
  font-weight: bold;
}
.task {
    cursor: pointer;
}
</style>
