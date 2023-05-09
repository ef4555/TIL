<template>
  <div id="app">
    <div class="container">
      <nav class="row">
        <div class="col-2 te">
          <SideBar/>
        </div>
        <div class="te col-10">
          <p class=" m-3">
            <router-view/>
          </p>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import SideBar from '@/components/SideBar.vue'

export default {
  name: 'HomePage',
  components: {
    SideBar,
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
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.te {
    border-style:solid;
    border-width: 2px;
    border-radius: 7px;
 }
</style>
