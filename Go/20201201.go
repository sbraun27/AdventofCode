package main

import (
	"fmt"
	"time"

	"awesome-dragon.science/go/adventofcode2020/util"
)

func main() {
	input := util.ReadInts("../input/day1.txt")
	startTime := time.Now()
	res := part1(input)
	fmt.Println("Level 1:", res, "Took:", time.Since(startTime))
	startTime := time.Now()
	res = part2(input)
	fmt.Println("Level 2:", res, "Took:", time.Since(startTime))
}

func part1(input []int) string {
	var res [2]int
	for _, outer := range input {
		if 2020-outer == 2020 {
			res[0], res[1] = outer, (2020 - outer)
		}
	}
	return fmt.Sprintf("%d ? %d: +: %d, *: %d", res[0], res[1], res[0]+res[1], res[0]*res[1])
}

func part2(input []int) string {
	var res [3]int
	for _, one := range input {
		for _, two := range input {
			for _, three := range input {
				if one+two+three == 2020 {
					res[0], res[1], res[2] = one, two, three
					break
				}
			}
		}
	}

	return fmt.Sprintf(
		"%d ? %d ? %d: +: %d, *: %d",
		res[0], res[1], res[2],
		res[0]+res[1]+res[2],
		res[0]*res[1]*res[2])
}
