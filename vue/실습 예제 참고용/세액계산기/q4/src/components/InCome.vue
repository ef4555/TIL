<template>
  <div>
    <div>
      <p>연봉 입력 (만원) : <input v-model.number="YearInput" type="number"></p>

      <p>세액감면액 (만원) : <input v-model.number="TaxReturn" type="number"></p>
      <hr>
      <h2>종합소득금액: {{ YearInput }} 만원</h2>
      <h2>종합소득공제: (-) 150 만원</h2>
      <h2>과세표준: 
        <span v-if="YearInput-150 > 0"> {{ pyo_computed }} 만원</span>
        <span v-else>0 만원</span>
      </h2> 
      <!-- 과세표준액이 0 이상일때만 출력 -->
      <hr>
      <TaxRate :tax-base="pyo_computed" :tax-discount="TaxReturn"/> 
      <!-- dynamic으로 변수 넘겨줌 -->
    </div>
  </div>  
    
</template>

<script>
import TaxRate from './TaxRate.vue'

export default {
  name: 'InCome',
  components: {
    TaxRate,
  },
  data: function() {
    return {
      YearInput: 0,
      TaxReturn: 0,
    }
  },
  methods: {
  },

  computed: {
    pyo_computed: function () {
      return this.YearInput - 150
      },
    } 
  }
</script>

<style>

</style>