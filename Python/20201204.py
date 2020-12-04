import time
import re


def convert_lines_to_dict(batch_file):
    all_results = []
    current_results = {}

    for line in batch_file:
        if line == "":
            all_results.append(current_results)
            current_results = {}
            continue

        key_value = line.split(" ")
        for kv_pair in key_value:
            key, value = kv_pair.split(":")
            current_results[key] = value

    return all_results


def validate_passport(passport_list, required_keys=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
    valid_passports = 0
    passports = passport_list.copy()

    for passport in passport_list:
        if all(keys in passport for keys in required_keys):
            valid_passports += 1
        else:
            passports.remove(passport)

    return valid_passports, passports


def strict_validate_passport():
    def validate_byr(byr):
        digits = len(byr) == 4
        return digits and (1920 <= int(byr) <= 2002)

    def validate_iyr(iyr):
        digits = len(iyr) == 4
        return digits and (2010 <= int(iyr) <= 2020)

    def validate_eyr(eyr):
        digits = len(eyr) == 4
        return digits and (2020 <= int(eyr) <= 2030)

    def validate_hgt(hgt):
        if hgt[-2:] == "in":
            return 59 <= int(hgt[:-2]) <= 76
        elif hgt[-2:] == "cm":
            return 150 <= int(hgt[:-2]) <= 193

    def validate_hcl(hcl):
        hcl_re = re.compile(r"^#[0-9a-f]{6}$")
        return re.match(hcl_re, hcl)

    def validate_ecl(ecl):
        return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def validate_pid(pid):
        pid_re = re.compile(r'^[0-9]{9}$')
        return re.match(pid_re, pid)

    conditions = {
        "byr": validate_byr,
        "iyr": validate_iyr,
        "eyr": validate_eyr,
        "hgt": validate_hgt,
        "hcl": validate_hcl,
        "ecl": validate_ecl,
        "pid": validate_pid
    }
    return conditions


def validate_strict_passports(passport_list):
    conditions = strict_validate_passport()
    results = 0

    for passport in passport_list:
        validation = all([
            conditions["byr"](passport["byr"]),
            conditions["iyr"](passport["iyr"]),
            conditions["eyr"](passport["eyr"]),
            conditions["hgt"](passport["hgt"]),
            conditions["hcl"](passport["hcl"]),
            conditions["ecl"](passport["ecl"]),
            conditions["pid"](passport["pid"]),
        ])

        if validation:
            results += 1

    return results


if __name__ == "__main__":
    with open("../input/day4.txt", "r") as f:
        batch_file = f.read().splitlines()

    passports = convert_lines_to_dict(batch_file)
    start = time.time()
    count, valid_passports = validate_passport(passports)
    print(f"Part 1: {count}. Took: {time.time() - start}")

    start = time.time()
    strict_count = validate_strict_passports(valid_passports)
    print(f"Part 2: {strict_count}. Took: {time.time() - start}")
