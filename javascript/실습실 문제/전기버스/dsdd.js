const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]


function solution(K, N, M, chargers) {
  // solution 함수 완성

  // 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
  // 종점인 N번 정류장
  // 충전기가 설치된 M개의 정류장 번호
  // 설치된 정류장 chargers
  
  let start = ans = 0

  chargers.unshift(0)
  chargers.push(N)


  if (chargers[0] > K) return console.log('#0')

  for (let i = 1; i < M + 3; i++) {
    if (chargers[i] - chargers[i - 1] > K) {
      ans = 0
      break

      
    } else if (chargers[i] - start > K) {
      start = chargers[i - 1]
      ans += 1
    }
  }
  console.log('#' + ans)
}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}