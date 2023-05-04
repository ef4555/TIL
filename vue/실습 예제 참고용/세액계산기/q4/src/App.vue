<template>
  <div id="app">
    <div class="border-botton">
      <img alt="Vue logo" src="./assets/logo.png">

      <h1>소득세 계산기</h1>
      <InCome/>
    </div>


    
  </div>
</template>

<script>
import InCome from './components/InCome.vue';

export default {
  name: 'App',
  components: {
    InCome,
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
