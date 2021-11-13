package main

import (
	"fmt"
)

var N int
var hs []int
var memo map[int]int

func main() {
	fmt.Scan(&N)
	hs = make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&hs[i])
	}
	memo = make(map[int]int)
	fmt.Println(solve(0))
}

func solve(pos int) (cost int) {
	if pos >= N-1 {
		return 0
	}

	if v, ok := memo[pos]; ok {
		return v
	}

	if pos == N-2 {
		return solve(pos+1) + Abs(hs[pos+1]-hs[pos])
	}

	a := solve(pos+1) + Abs(hs[pos+1]-hs[pos])
	b := solve(pos+2) + Abs(hs[pos+2]-hs[pos])
	memo[pos] = Min(a, b)
	return memo[pos]
}

func Abs(a int) int {
	if a >= 0 {
		return a
	} else {
		return -a
	}
}

func Min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
