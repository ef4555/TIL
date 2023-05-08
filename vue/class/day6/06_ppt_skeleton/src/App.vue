<template>
  <div id="app">
    <h1>길이 {{ messageLength }}의 메시지 {{ message }}를 입력받음</h1>
    
    <h3>x2 : {{ doubleLength }}</h3>
    <h3>{{ age }}</h3>
    <input type="text" @keyup.enter="onSubmit ()" v-model="inputData">
    <h1>{{ level }}</h1>
    <button @click="uplevel">level up!</button>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters} from 'vuex'

export default {
  name: 'App',
  components: {
  },
  created() {
    // this.$store.dispatch('loadMessage')
  },
  computed: {
    ...mapState(['age']),
    ...mapState({
      message: state => state.message,
      level: state => state.myModule.level
    }),
    message() {
      return this.$store.state.message
    },
    // messageLength() {
    //     return this.$store.getters.messageLength
    // },
    ...mapGetters(['messageLength', 'doubleLength']),
    // doubleLength() {
    //     return this.$store.getters.doubleLength
    // },
  },
  data() {
    return {
      inputData: '',
    }
  },
  methods: {
    // ...mapActions(['changeMessage']),
    ...mapActions({
      actionChangeMessage: 'changeMessage'
    }),
    onSubmit () {
      const newMessage = this.inputData
      this.actionChangeMessage(newMessage)
      this.inputData = ''
    },
    uplevel() {
      this.$store.dispatch('increment_level')
    }
  },
    // changeMessage() {
    //   const newMessage = this.inputData
    //   this.$store.dispatch('changeMessage', newMessage)
    //   this.inputData = null
    // },

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
