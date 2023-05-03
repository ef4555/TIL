<template>
  <div class="w-50" style="box-shadow: -1px 5px 10px; display:flex; flex-direction:column; align-items:center;">
    <br>
    <h2>예약 페이지</h2>
    <br>
    <p class="bold">선생님 선택</p> 
    <div class="row">
      <span id="Eric" style="height:45px; width:100px;" class="col-3 border p-2 m-3" v-on:click="clickName">Eric</span>
      <span id="Tony" style="height:45px; width:100px;" class="col-3 border p-2 m-3" v-on:click="clickName">Tony</span>
    </div>
    
    
    <div class="border-top border-primary" id="TimeSchedule" style="margin:auto; display:flex; flex-direction:column; align-items:center;">
      <br>
      <p>시간 선택</p>
      <div class="">
        <span v-for="(time, index) in times" v-bind:key="time">
          <br v-if="index % 8 == 0" >     
          <span id="btn" v-on:click="clickTime" class="m-1">{{ time }}</span>
        </span >
        <br>
      </div>
    </div>
    <br>
    <span>
      <p>선택 시간:<span v-for="time in TimeList" v-bind:key="time">
          {{ time }}
        </span></p>
      </span>
      <br>
  </div>
  
</template>

<script>


export default {
  name: 'SelectTime',
  data: function() { 
    return { 
      times: [
      "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30",  
      "13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30",  
      "17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30",     
      "21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      count: 0,
      TimeList: [],
      // isSelected : false // isSelected를 여러 개가 함께 공유한다.
    }
  },
  methods : {

    // 버튼이 클릭 되었을 때 class를 동적으로 부여하기 위해 boolean 값을 리턴한다.
    isSelected(time) {
      console.log(time)
      if(this.Timelist.includes(time)) {
        return true
      }
      return false

    },
    clickName(event) {
      // const Eric = document.querySelector('#Eric')
      // const Tony = document.querySelector('#Tony')
      // Eric.classList.toggle('selected')
      // Tony.classList.toggle('selected')
      event.target.classList.toggle('selected')
    },
    clickTime(event) {
      console.log(event.target.innerText)
      event.target.classList.toggle('selected')
      const btns = document.querySelectorAll('#btn')
      if (this.TimeList.includes(event.target.innerText)) {
        const time_idx = this.TimeList.indexOf(event.target.innerText)
        this.TimeList.splice(time_idx, 1)
        //const NewTimeList = this.TimeList.filter(function(data) {
        //  return data !== event.target.innerText 
        // })
        // this.TimeList= NewTimeList 
        
      }
      else {
        this.TimeList.push(event.target.innerText)
        console.log(this.TimeList)
      }



      // this.count = 0
      // btns.forEach((btn) => {
      //   if (btn.classList.contains('selected')) {
      //     this.count += 1
      //   }
      // })

      if (this.TimeList.length > 5) {
        alert('5타임까지만 신청할 수 있습니다.')
        this.TimeList = []
        btns.forEach((btn) => {
          btn.setAttribute('class', 'm-1')
        })
        // this.count = 0
      }

    }
  }

  }
</script>

<style scoped>
.selected {
  background-color: #658dc63d;
  color: #0f4c81
}

.selected-timebtn {
  background-color: #658dc63d;
  color: #0f4c81
}
</style>

