<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <div>
      <h1>APP</h1>
      <input type="number" v-model.number="AppNumber" >
      <p>parentData: {{ p }} </p>
      <p>childData: {{ c }}</p>
    </div>
    <div>
      <AppParent :child-data="c" :app-data="AppNumber" @app-parent-input="getAppParentData" />
    </div>
    <hr>
    <div>
      <AppChild :parent-data="p" :app-data="AppNumber" @app-child-input="getChildData" />
    </div>

  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'
import AppChild from './components/AppChild.vue';

export default {
  name: 'App',
  components: {
    AppParent,
    AppChild,
  },
  data: function() {
    return {
      AppNumber: 0,
      p: 0,
      c: 0,
    }
  },
  methods: {
    getAppParentData: function(ParentData) {
      this.p = ParentData
    },
    getChildData: function(childData) {
      this.c = childData
    }
    
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
