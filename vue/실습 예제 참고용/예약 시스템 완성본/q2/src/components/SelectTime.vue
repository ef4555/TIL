<template>
  <div class="container">
    <div class="row">
      <span class="col-6 border shadow-sm" >
        <br>
        <h2>예약 페이지</h2>
        <br>
        <p class="bold">선생님 선택</p> 
        <div class="">
          <span id="Eric" class="border p-2 m-4" v-on:click="clickName">Eric</span>
          <span id="Tony" class="border p-2 m-4" v-on:click="clickName">Tony</span>
        </div>
        <br>
        <div class="border-top border-primary" id="TimeSchedule" >
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
          <p>선택 시간:<span v-for="time in ericTimeList" v-bind:key="time">
              {{ time }}
            </span>
          </p>
          <p>선택 시간:<span v-for="time in tonyTimeList" v-bind:key="time">
              {{ time }}
            </span>
          </p>
          </span>
          <br>
      </span>
      <span class="col-6 border shadow-sm">
        <YeYak :doctor-name="doctorSelected" :eric-list="ericTimeList" :tony-list="tonyTimeList"/>
      </span>
    </div>
    
  </div>
  
  
</template>

<script>
import YeYak from './YeYak.vue'

export default {
  name: 'SelectTime',
  components : {
    YeYak,
  },
  data: function() { 
    return { 
      times: [
      "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30",  
      "13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30",  
      "17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30",     
      "21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      ericTimeList: [],
      tonyTimeList: [],
      doctorSelected: null,
      // isSelected : false // isSelected를 여러 개가 함께 공유한다.
    }
  },
  methods : {
    clickName(event) {
      const E = document.querySelector('#Eric')
      const T = document.querySelector('#Tony')
      const btntags = document.querySelectorAll('#btn')
      btntags.forEach(function(btn) {
          btn.classList.remove('selected')
        })
        
      if (event.target.innerText == 'Eric') {     
        E.classList.toggle('selected')
        T.classList.remove('selected')
        this.doctorSelected = 'Eric'
        for (let time of this.ericTimeList) {
          btntags.forEach(function(btn) {
            if (btn.innerText == time) {
              btn.classList.toggle('selected')
            }
          })
        }
        
      } else if (event.target.innerText == 'Tony') {     
        T.classList.toggle('selected')
        E.classList.remove('selected')
        this.doctorSelected = 'Tony'
        for (let time of this.tonyTimeList) {
          btntags.forEach(function(btn) {
            if (btn.innerText == time) {
              btn.classList.toggle('selected')
            }
          })
        }
      }
    },


    clickTime(event) {
      if (this.doctorSelected == null) {
        alert('예약할 선생님을 선택해주세요')
        this.tonyTimeList.pop()
        event.target.classList.toggle('selected')
      }

      event.target.classList.toggle('selected')
      if (this.doctorSelected == 'Eric') {
        if (this.ericTimeList.includes(event.target.innerText)) {
        const time_idx = this.ericTimeList.indexOf(event.target.innerText)
        this.ericTimeList.splice(time_idx, 1)

        }
        else {
          this.ericTimeList.push(event.target.innerText)
        }
        if (this.ericTimeList.length > 5) {
        alert('5타임까지만 신청할 수 있습니다.')
        this.ericTimeList.pop()
        event.target.classList.toggle('selected')
      }
      } else if (this.doctorSelected == 'Tony') {
        if (this.tonyTimeList.includes(event.target.innerText)) {
        const time_idx = this.tonyTimeList.indexOf(event.target.innerText)
        this.tonyTimeList.splice(time_idx, 1)

        }
        else {
          this.tonyTimeList.push(event.target.innerText)
        }
        if (this.tonyTimeList.length > 5) {
        alert('5타임까지만 신청할 수 있습니다.')
        this.tonyTimeList.pop()
        event.target.classList.toggle('selected')
      }
    }

    }
  }

  }
</script>

<style scoped>
.selected {
  background-color: rgb(63, 121, 121);
  color: azure;
  font-weight: bolder;
}

.selected-timebtn {
  background-color: #658dc63d;
  color: #0f4c81
}
</style>

