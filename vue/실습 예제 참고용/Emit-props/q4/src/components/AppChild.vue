<template>
  <div>
    <h1>AppChild</h1>
    <input type="number" v-model.number="appChildInputData" @change="appChildInput" >
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ appChildInputData }}</p>


  </div>
</template>

<script>
export default {
  props: {
    appData : Number, 
    parentData : Number,
  },
  data: function () {
    return {
      appChildInputData: null,
    }
  },

  methods: {
    appChildInput: function() {
      this.$emit('app-child-input', this.appChildInputData)
    }
  }
}
</script>

<style>

</style>