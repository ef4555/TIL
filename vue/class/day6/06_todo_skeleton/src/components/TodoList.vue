<template>
  <div>
    <p>TodoList</p>
    <TodoListItemVue v-for="(todo, index) in TodoList" :key="index" :todo=todo />
  </div>
</template>

<script>
import TodoListItemVue from './TodoListItem.vue'

export default {
  name: 'TodoList',
  components: {
    TodoListItemVue
  },
  computed: {
    TodoList() {
      return this.$store.state.todos
    }
  }
}
</script>

<style>

</style>