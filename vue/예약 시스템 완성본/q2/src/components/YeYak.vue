<template>
  <div>
    <br>
    <h2>상담 신청 현황</h2>
    <br>
    <p>상담 선생님</p>
    <span>성함 : <span class="bold">{{doctorName}}</span></span>
    <div class="border-top border-bottom border-primary m-1" >
    <br>
    <p>예약 현황</p>
    <p v-if="doctorName == 'Eric'">
        <span v-for="time in ericList" v-bind:key="time">
            {{ time }}
        </span>
    </p>
    <p v-else>
        <span v-for="time in tonyList" v-bind:key="time">
        {{ time }}
        </span>
    </p>
    </div>
    <br>
    <br>
    <br>
    <img src = "@/assets/ssafy-logo.png" />
  </div>
</template>

<script>
export default {
    props: {
        ericList : Array,
        tonyList : Array,
        doctorName : String,
    }
}
</script>

<style scoped>
.bold {
  font-weight: bolder;
}
</style>