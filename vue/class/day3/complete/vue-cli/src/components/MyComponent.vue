<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild />
    <MyChild />
    <MyChild />
    <MyChild />
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components : {
    MyChild,
  }
}
</script>

<style>
.border {
  border: solid;
}
</style>
