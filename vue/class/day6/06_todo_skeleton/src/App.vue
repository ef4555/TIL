<template>
  <div id="app">
    <h1>Todo</h1>
    <h1>총 할일 {{ allTodoCount }}</h1>
    <h2>완료된 할 일</h2>
    <h2>남은 할 일</h2>
    <TodoForm/>
    <TodoList />
    <button @click="loadTodos">Todo 불러오기</button>
  </div>
</template>

<script>
import TodoForm from './components/TodoForm.vue'
import TodoList from './components/TodoList.vue'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  methods: {
    loadTodos() {
      this.$store.dispatch('loadTodos')
    },
  },
  computed: {
    allTodoCount() {
      return this.$store.getters.allTodoCount
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
