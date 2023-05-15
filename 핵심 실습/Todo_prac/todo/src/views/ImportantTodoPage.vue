<template>
  <div>
    <h1>중요 할 일</h1>
    <div class="container">
      <div class='tedo m-2 row' v-for="(con, index) in list" :key="index">
        <input class="col-1 m-3" type="radio">
        <span class="col-9 m-3 text-start">할 일: {{ con.content }} 중요한가? : {{ con.isImportant  }} 완료 여부 :  {{ con.isCompleted }}</span>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  computed: {
      list() {
        const imlist = this.$store.state.todo.list
        return imlist.filter(item => item.isImportant == true)       
      } 
  },
}
</script>

<style>

</style>