<template>
  <div class="about">
    <h1>로또</h1>
    <button @click="pickLotto" >Get Lucky Numbers</button>
    <p>{{ lottoPick }}</p>
  </div>
</template>

<script>
  export default {
  name: 'TheLottoView',
  components: {
  },
  data() {
    return {
      lottoPick: null,
      count : this.$route.params.count
    }
  },
  methods: {
    pickLotto() {
    var i = this.count
    this.lottoPick = []
    while(i) {
      var pick = Math.floor(Math.random()*45)+1
      if(!this.lottoPick.find(el => el === pick)) {
        this.lottoPick.push(pick)
        i--
      }
    }
  }
}
  }
</script>
