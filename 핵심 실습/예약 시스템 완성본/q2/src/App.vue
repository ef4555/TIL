<template>
  <div id="app">
    <h1>SSAFY 상담 예약 시스템</h1>
    <SelectTime/>
  </div>
</template>

<script>
import SelectTime from './components/SelectTime.vue';

export default {
  name: 'App',
  components: {
    SelectTime,
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
