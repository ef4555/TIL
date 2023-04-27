const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {

  
  let i = 0
  let c = 0
  let a = 1
  while (i < N) {
    i+=K
    c += 1
    if (i >= N) {
      break
    }
    const fil = chargers.filter((j) => {
            return j <= i
          })
    const fil2 = chargers.filter((jj) => {
      return jj > i
    })

    if (i+K < fil2[0]) {
      a = 0
      break
    }
    // console.log(fil)
    // console.log(fil2)

    if (fil.length === 0) {
      break
    }

    if (fil2.length === 0) {
      break
    }
    i = fil[fil.length-1]
    // console.log(i)
  }
    // console.log(fil)
    // console.log(fil2)


}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}