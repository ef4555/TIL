const words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    if (word === word.split('').reverse().join('')) {
      return true
    }
    else {
      return false
    }
  }
  
for (const word of words) {
  console.log(palindrome(word))
}