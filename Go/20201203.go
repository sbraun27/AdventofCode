package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"time"
)

func readFile(fileName string) []string {
	f, _ := os.Open(fileName)

	defer f.Close()

	scanner := bufio.NewScanner(f)

	lines := []string{}

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

func calcTrees(slopeMap []string, steps [2]int) int {
	column := 0
	targetCol := 0
	rowLength := len(slopeMap[0])

	treeNum := 0

	for row := 0; row < len(slopeMap); row += steps[0] {
		if column >= rowLength {
			targetCol = column % rowLength
		} else {
			targetCol = column
		}

		currentRow := strings.Split(slopeMap[row], "")
		if currentRow[targetCol] == "#" {
			treeNum++
		}

		column += steps[1]
	}
	return treeNum
}

func main() {
	slopeMap := readFile("../input/day3.txt")
	steps := [2]int{1, 3}

	start := time.Now()
	part1Result := calcTrees(slopeMap, steps)
	fmt.Println("Part 1 result: ", part1Result, "Took: ", time.Since(start))

	part2Results := 1

	part2Steps := [5][2]int{
		{1, 1},
		{1, 3},
		{1, 5},
		{1, 7},
		{2, 1},
	}

	start = time.Now()
	for _, steps := range part2Steps {
		part2Results = part2Results * calcTrees(slopeMap, steps)
	}
	fmt.Println("Part 2 result: ", part2Results, "Took: ", time.Since(start))
}
