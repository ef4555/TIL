const key = 'country'
const value = ['한국', '일본', '중국']

const myObj = {
  [key] : value,
}

console.log(myObj)
console.log(myObj.country)

const userInformation = {
  name : 'aaa',
  userId: 'bbbb'
}

const {userId} = userInformation
console.log(userId)