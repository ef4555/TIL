<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>이 곳은 고양이의 고향이다</h1>
    <button @click="makeCat">야옹</button>
    <br>
    <img :src="catURL" alt="">
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
  },
  data() {
    return {
      catURL: null,
    }
  },
  methods: {
    makeCat() {
      axios({
          methods: 'get',
          url: 'https://api.thecatapi.com/v1/images/search'
      })
      .then((response) => {
        console.log(response.data[0].url)
        this.catURL = response.data[0].url
      })
    } 
  }
}
</script>
