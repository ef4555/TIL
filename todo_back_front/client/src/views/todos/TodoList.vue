<template>
  <div>
    <CreateTodo @get-list="getTodos" />
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <span
          @click="updateTodoStatus(todo)" 
          :class="{ 'is-completed': todo.is_completed }"
        >
        {{ todo.title }}
        </span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from 'axios'
import CreateTodo from './CreateTodo.vue'

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  created() {
    this.getTodos()
  },
  components: {
    CreateTodo,
  },
  methods: {
    updateTodoStatus: function(todo) {
      todo.is_completed = !todo.is_completed
      axios({
        method:'put',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        data: todo
      })
      .then(res => {
        console.log(res)
      })
    },
    getTodos: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
      })
        .then(res => {
          console.log(res)
          this.todos = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      // 3번 문제
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
      })
        .then(res => {
          console.log(res)
          //console.log(this.todos)
          //console.log(todo.id)
          let lst = []
          for (let i of this.todos) {
            if (i.id == todo.id ) {
              console.log('제거됨!')   
            } else {
              lst.push(i) 
              console.log(lst) 
            }       
          }
          this.todos = lst

      })

    },
    // updateTodoStatus: function (todo) {
    //   // 4번 문제
    //   pass
    // },
  },
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }

</style>
