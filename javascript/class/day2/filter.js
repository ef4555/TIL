const products = [
    { name: 'cucumber', type: 'vegetable' }, // product
    { name: 'banana', type: 'fruit' },
    { name: 'carrot', type: 'vegetable' },
    { name: 'apple', type: 'fruit' },
  ]
  
const fruitFilter = function (product) {
  return product.type === 'fruit' // true 애들만 뽑아서 배열로 만들기
}

const fruits = products.filter(fruitFilter)
console.log(fruits)

  