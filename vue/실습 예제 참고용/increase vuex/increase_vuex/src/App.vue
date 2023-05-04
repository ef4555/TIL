// App.vue
<template>
  <div id="app">
    <p>Counter: {{ number }}</p>
    <p>Counter x2: {{ double }}</p>
    <p></p>
    <button @click="changeNumber">increase +</button>
    <button @click="minusNumber">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  methods: {
    changeNumber() {
      const newNumber = this.$store.state.counter + 1
      this.$store.dispatch('changeNumber', newNumber)
    },
    minusNumber() {
      const newNumber = this.$store.state.counter - 1
      this.$store.dispatch('changeNumber', newNumber)
    }

  },
  computed: {
    number() {
      return this.$store.state.counter
    },
    double() {
      return this.$store.state.counter * 2
    },

  },
}
</script>

<style>
</style>