<template>
  <div id="wraper">
    <header>
      <h1>버튼 박스 제작</h1>
    </header>
    <section class="inner-wrapper">
      <div class="time-wrap">
        <h2>예약 페이지</h2>
        <h3>시간 선택</h3>
        <div class="timebox">
          <span class="timebtn" 
              v-for="(time, index) in times" 
              :key="index" 
              @click="selectTime(time)"
              :class="{'selected-timebtn': isSelected(time)}"
            >
          {{ time }}
          </span>
        </div>
        <hr>
        <p>선택 시간 : {{ selectedTimes }}</p>
      </div>
    </section>
   
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data(){
    return{
      times: ["09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
              "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
              "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
              ],
      selectedTimes: [],
      // isSelected : false, //  isSelected를 여러개의 요소가 함께 공유한다

    }
  },
  methods:{
    // 버튼이 선택됐을 때 class를 동적으로 부여하기 위해 boolean값을 리턴한다. 
    isSelected(time){
      if(this.selectedTimes.includes(time)){
        return true
      }

      return false
 

    },
    selectTime(time){
      // console.log('is Selected', this.selectedTimes.includes(time)) // true
      if(this.selectedTimes.includes(time)){
        console.log('selectTime clicked', time)
        // 지울 녀석의 인덱스 
        const time_idx = this.selectedTimes.indexOf(time)
        console.log('time_idx', time_idx)
        this.selectedTimes.splice(time_idx, 1)
      }else{ // 선택 안한 시간 -> 추가하자 
      if(this.selectedTimes.length === 5){
        alert('5 타임만 선택 가능합니다!')
        return
      }
      this.selectedTimes.push(time)
      }
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.time-wrap{
  display: flex;
  flex-direction: column;
  align-content: center;

}

.timebox{
display: flex;
flex-wrap: wrap;

}
  .timebtn {
    background-color: transparent;
    border: transparent;
    color: #84898C;
    font-size: 16px;
    margin-top: 2px;
    margin-bottom: 2px;
    width: 65px;
    text-align: center;
    cursor: pointer;
  }

  .selected-timebtn{
    background-color: rgb(63, 121, 121);
    color: azure;
    font-weight: bolder;

  }

</style>