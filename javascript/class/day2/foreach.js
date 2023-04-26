// 1. 일단 사용해보기
const numbers = [1, 2, 3]

// 힘수 정의 (표현식)
const doubleFunc = function (number) { 
  return number * 2
}

// 함수를 다른 함수의 인자로 넣기(콜백 함수)
// const doubleNumbers = numbers.map(doubleFunc)
// console.log(doubleNumbers) // [ 2, 4, 6 ]

const doubleNumbers = numbers.map(function (number) {
  return number * 2
})
console.log(doubleNumbers)
