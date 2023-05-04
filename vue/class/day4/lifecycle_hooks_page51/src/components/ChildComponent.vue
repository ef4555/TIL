<template>
  <div>
    value : {{ value }}
    <button @click="changeValue">change value</button><br>
  </div>
</template>

<script>
export default {
  name:'ChildComponent',
  data() {
    return {
      value: 0,
    }
  },
  methods: {
    changeValue() {
      this.value = this.value + 1
    }
  },
  beforeCreate() {
    console.log('Child beforeCreate')
  },
  created() {
    console.log('Child created')
  },
  beforeMount() {
    console.log('Child beforeMount')
  },
  mounted() {
    console.log('Child mounted')
  },
  beforeUpdate() {
    console.log('Child beforeUpdate')
  },
  updated() {
    console.log('Child updated')
  },
  beforeDestroy() {
    console.log('Child beforeDestroy')
  },
  destroyed() {
    console.log('Child destroyed')
  }
}
</script>

<style>

</style>
