<template>
  <div>
    <h1>전체 할 일</h1>
    <div style="display: flex;" class="m-4">
      <button style="font-size;" class="btn col-1 border" @click="createTodo">+</button>
      <input style="display: flex;" class="col-11 tedo" type="text" @keypress.enter="createTodo" placeholder="할 일을 작성해주세요" v-model="inputTodo">
    </div>
    
    <hr>
    <div class="container">
      <div class='tedo m-2 row' v-for="(con, index) in list" :key="index">
        <input class="col-1 m-3" type="radio">
        <span class="col-9 m-3 text-start">할 일: {{ con.content }} 중요한가? : {{ con.isImportant  }} 완료 여부 :  {{ con.isCompleted }}</span>
      </div>
    </div>
    

  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {
      inputTodo : '',
    }
  },
  computed: {
    ...mapState({
      list: state => state.todo.list
    }),
  },
  methods: {
    createTodo() {
      if (this.inputTodo == '') {
        alert('내용을 입력해주세요')
      }
      else {
        this.$store.dispatch('todo/createTodo', this.inputTodo)
        this.inputTodo = ''
      }
    }

  }
}
</script>

<style>
.tedo {
    border-style:solid;
    border-width: 1px;
    border-radius: 7px;
 }
</style>