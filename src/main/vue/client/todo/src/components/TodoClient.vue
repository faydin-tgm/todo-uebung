<template>
  <div class="hello">
    <h1>Todo App</h1>
    <h3> Todos: </h3>
    <ol>
      <li v-for="todo in todos">
        {{ todo.task }}
        {{ todo.taskDescribtion }}
        {{ todo.status }}
      </li>
    </ol>

    <button v-on:click="getTodos">Get Todos</button>
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
        taskDescribtion:"",
        status:'false'
      }
  }
  },
  methods: {
    getTodos: function () {
      axios.get('http://localhost:5000/todos').then((response) => {
        this.todos = response.data;

        console.log(response);
      }).catch((error) => {
        console.log(error);
      });
    }
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
