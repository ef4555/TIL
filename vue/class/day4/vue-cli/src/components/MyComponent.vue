<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild static-props="component에서 child로" 
    :my-props="dynamicProps"
    @child-to-parent="parentGetEvent"
    @child-input="getDynamicData"
    />
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  },
  data: function () {
    return {
      dynamicProps: "It is dataasdsad"
    }
  },
  methods: {
    parentGetEvent(inputData) {
      console.log('자식 컴포넌트에서 발생한 이벤트')
      console.log(`child에서 보낸 ${inputData}를 받음!`)
    },
    getDynamicData(a) {
      console.log(`child에서 입력한 ${a}을 출력`)
    }
  }
}

</script>

<style>
  .border {
    border: solid;
  }
</style>
