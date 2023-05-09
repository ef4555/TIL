<template>
  <div>
    <TodoListItem v-for="(todo, index) in todos" :key="index" :todoitem="todo" />
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todos
    }
  }
}
</script>

<style>

</style>
