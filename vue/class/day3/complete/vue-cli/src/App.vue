<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 사용한다. -->
    <MyComponent /> 
    <MyComponent /> 
    <MyComponent /> 
    <HelloWorld msg="반가워 vue.... 잘해보자 만반잘부"/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyComponent from '@/components/MyComponent' // 1. 불러온다

export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComponent, // 2. 등록한다.
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
