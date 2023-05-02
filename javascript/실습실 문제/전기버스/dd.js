const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  // initiate
  let ptr1 = M
  chargers.push(N)
  // result storing variable
  let rlt = 0
  // remove first case where bus can't move to the 0 index station
  if (chargers[0] > K) return console.log('#0')
  
  while (ptr1 > 0) {
    let ptr2 = ptr1
    // 탐색 절
    while (chargers[ptr1] - chargers[ptr2] <= K && ptr2 >= 0) ptr2--
    ptr2++
    // 검사절
    if (ptr1 === ptr2) return console.log('#0') // 못 감
    else if (ptr2 === 0) { // 끝까지 도달
      if (chargers[ptr1] <= K) return console.log(`#${rlt}`) // 현재 버스 위치가 한번에 갈수 있음
      return console.log(`#${++rlt}`)  // 현재 위치에 버스가 0에서부터 한번에 도달할수 없으므로 1이 위치한 지점에서 충전 한번해야함
    }
    // 업데이트
    ptr1 = ptr2 // 버스 위치 재 업데이트
    rlt++ // 충전횟수 1회 추가
  }
}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}