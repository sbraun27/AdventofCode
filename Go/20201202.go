package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func readLines(filePath string) []string {
	f, err := os.Open(filePath)

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	passwords := []string{}

	for scanner.Scan() {
		passwords = append(passwords, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return passwords
}

func part1(passwordList []string) int {
	validPasswords := 0

	for _, passwordFull := range passwordList {
		policySlice := strings.Split(passwordFull, " ")

		policy := policySlice[0]
		policies := strings.Split(policy, "-")
		lower, _ := strconv.Atoi(policies[0])
		upper, _ := strconv.Atoi(policies[1])

		letter := strings.Split(policySlice[1], "")[0]

		password := policySlice[2]

		letterCount := strings.Count(password, letter)

		if lower <= letterCount && letterCount <= upper {
			validPasswords++
		}
	}
	return validPasswords
}

func part2(passwordList []string) int {
	validPasswords := 0

	for _, passwordFull := range passwordList {
		policySlice := strings.Split(passwordFull, " ")
		policy := policySlice[0]
		policies := strings.Split(policy, "-")
		first, _ := strconv.Atoi(policies[0])
		second, _ := strconv.Atoi(policies[1])

		letter := strings.Split(policySlice[1], "")[0]
		password := strings.Split(policySlice[2], "")

		firstCheck := password[first-1] == letter
		secondCheck := password[second-1] == letter

		if firstCheck {
			if !secondCheck {
				validPasswords++
			}
		}
		if secondCheck {
			if !firstCheck {
				validPasswords++
			}
		}
	}
	return validPasswords
}

func main() {
	passwords := readLines("../input/day2.txt")
	part1Count := part1(passwords)
	fmt.Println("Part 1: ", part1Count)

	part2Count := part2(passwords)
	fmt.Println("Part 2: ", part2Count)
}
