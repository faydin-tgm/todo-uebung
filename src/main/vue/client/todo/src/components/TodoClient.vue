<template>
  <div>
    <h1>Todo App</h1>
    <input type="text" placeholder="Task" id="taskInput" v-model="task">
    <input type="text" placeholder="Task Description" id="taskDescrInput" v-model="taskDescription">
    <input type="text" placeholder="Status" id="statusInput" v-model="status">
    <br>
    <br>
    <button v-on:click="getTodos">Get Todos</button>
    <button v-on:click="createTodo">Create Todos</button>
    <button v-on:click="deleteTodo">Delete Todos</button>
    <button v-on:click="updateTodo">Update Todos</button>
    <br><br><br><br>
    <div style="border-bottom: solid" v-for="todo in todos">
      Task:             {{ todo.task }} <br>
      TaskDescription:  {{ todo.taskDescription }} <br>
      Status:           {{ todo.status }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'TodoClient',
  data () {
    return {
      todos: {},
      input: {
        task:"",
        taskDescription:"",
        status:''
      }
    }
  },
  methods: {
    getTodos: function () {
      axios.get('http://localhost:5000/todos').then((response) => {
        console.log(response);

        this.todos = response.data;
      }).catch((error) => {
        console.log(error);
      });
    },
    createTodo: function () {
      axios.post('http://localhost:5000/todos/' + this.task, {

        task: this.task,
        taskDescription: this.taskDescription,
        status: this.status
      }).then(response => {
        console.log(response);

        this.getTodos();
      }).catch((error) => {
        console.log(error);
      });
    },
    deleteTodo: function () {
      axios.delete('http://localhost:5000/todos/' + this.task)
        .then(response => {
          this.getTodos()
      })
    },
    updateTodo: function () {
      axios.put('http://localhost:5000/todos/' + this.task, {

        task: this.task,
        taskDescription: this.taskDescription,
        status: this.status
      }).then(response => {
        this.getTodos()
      }).catch((error) => {
        console.log(error);
      });
    },
  },
  created(){
    this.getTodos()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
