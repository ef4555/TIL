<template>
  <div id="app">
    <h1 class="text-primary">SSAFY TUBE</h1>
    <input @keypress.enter="con" type="text" v-model="aaa">
    <button @click="con">검색!</button>
    <br>
    <iframe :src="searchURL" frameborder="0" width="420" height="315" ></iframe>
    <br>
    <p>{{ searchTitle }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      searchURL: '',
      searchTitle: '',
      aaa: '',
      }
    },
    methods: {
      con() {
        const youTubeURL = 'https://www.googleapis.com/youtube/v3/search?'
        const params = {
          part: 'snippet',
          q: this.aaa,
          type: 'video',
          key: process.env.VUE_APP_YOUTUBE_API,
        }
        axios({
          methods: 'get',
          params : params,
          url: youTubeURL
        })

        .then((response) => {
          console.log(response.data)
          const title = response.data.items[0].snippet.title
          this.searchTitle = title
          const URL = `https://www.youtube.com/embed/${response.data.items[0].id.videoId}`
          this.searchURL = URL
          console.log(this.searchURL)
        })
        }
    },
    created() {
      // const URL = `https://www.youtube.com/embed/${this.result.items[0].id.videoId}`
      // this.searchURL = URL
      //  const youTubeURL = 'https://www.googleapis.com/youtube/v3/search?'
      //  const params = {
      //    part: 'snippet',
      //    q: this.aaa,
      //    type: 'video',
      //    key: process.env.VUE_APP_YOUTUBE_API,
      //  }
      //  axios({
      //    methods: 'get',
      //    params : params,
      //    url: youTubeURL
      //  })
      //  .then((response) => {
      //    console.log(response.data)
      //    const title = response.data.items[0].snippet.title
      //    this.searchTitle = title
      //    const URL = `https://www.youtube.com/embed/${response.data.items[0].id.videoId}`
      //    this.searchURL = URL
      //    console.log(this.searchURL)
      //  })
      //  }
    
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
