<template>
  <div>
    <h3>This is child component</h3>
    <p>{{ staticProps }}</p>
    <p>{{ myProps }}</p>
    <button @click="childToParent">클릭:</button>
    <input type="text" v-model="childInputData" @keyup.enter="childInput">
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  data: function() {
    return {
      childInputData: null,
    }
  },
  props: {
    staticProps: String,
    myProps: String,
  },
  methods: {
    childToParent: function () {
      this.$emit('child-to-parent', 'child Data')
    },
    childInput: function () {
      this.$emit('child-input', this.childInputData) // child-input이라는 이벤트 상위에 발생, this.childInputData 전달해줌
      this.childInputData = ""
    }  
  }
  
}
</script>

<style>
  
</style>
