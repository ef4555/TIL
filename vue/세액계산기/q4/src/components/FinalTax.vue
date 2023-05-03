<template>
  <div>
    <h2>결정세액 : {{ finalTax }}</h2>
  </div>
</template>

<script>
export default {
  props: {
    finalTax : Number, //결정세액
  },
}
</script>

<style>

</style>