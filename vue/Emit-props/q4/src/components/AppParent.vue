<template>
  <div>
    <h1>AppParent</h1>
    <input type="number" v-model.number="appParentInputData" @change="appParentInput" >
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
  </div>
  
</template>

<script>

export default {
  props: {
    appData : Number, 
    childData : Number,

  },
  data: function () {
    return {
      appParentInputData : null,
  
    }
  },
  methods: {
    appParentInput: function() {
      this.$emit('app-parent-input', this.appParentInputData)
    }
  }
}
</script>

<style>

</style>