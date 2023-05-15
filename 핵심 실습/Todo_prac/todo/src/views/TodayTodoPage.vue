<template>
  <div>
    <h1>오늘 할 일</h1>
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
        const todaylist = this.$store.state.todo.list
        const today = new Date()
        const year = today.getFullYear();
        const month = String(today.getMonth() + 1).padStart(2, '0');
        const day = String(today.getDate()).padStart(2, '0');
        const hours = String(today.getHours()).padStart(2, '0');
        const minutes = String(today.getMinutes()).padStart(2, '0');
        const bbb = `${year}-${month}-${day}T${hours}:${minutes}`;
        
        return todaylist.filter(item => item.dueDateTime == bbb)       
      } 
  },
}
</script>

<style>

</style>