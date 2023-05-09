<template>
  <div class="home">
    <h1>점심메뉴</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <p>{{ pick }}</p>
    <br>
    <br>
    <h2>로또를 뽑아보자</h2>
    <button @click="goToLotto">Pick Lotto</button>
  </div>
</template>

<script 
src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js">
</script>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>

export default {
  name: 'TheLunchView',
  components: {
  },
  data() {
    return {
      menu: ['국밥', '피자', '굶어', '서브웨이', '김밥'],
      pick: ''
    }
  },
  methods: {
    goToLotto() {
      this.$router.push({ name: 'lotto', params: {count: 6} })
    },
    pickLunch() {
      const pickIndex = Math.floor(Math.random() * this.menu.length)
      this.pick = this.menu[pickIndex]
    }
  }
}
</script>
