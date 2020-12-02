from numpy import loadtxt


def parse_pass_policy(password_line):
    policy, password = password_line.split(":")
    policy_num, policy_letter = policy.split()
    policy_low, policy_high = policy_num.split("-")

    password = password.strip()

    policy_low = int(policy_low)
    policy_high = int(policy_high)

    return policy_low, policy_high, policy_letter, password


def check_valid_password(password_line):
    low, high, letter, password = parse_pass_policy(password_line)

    letter_count = password.count(letter)

    if (letter_count >= low) and (letter_count <= high):
        return 1
    else:
        return 0


def check_pass_part_2(password_line):
    first, second, letter, password = parse_pass_policy(password_line)

    if password[first-1] == letter:
        if password[second-1] == letter:
            return 0
        else:
            return 1
    else:
        if password[second-1] == letter:
            return 1
        else:
            return 0


if __name__ == "__main__":
    lines = open("../input/day2.txt", "r")
    lines = lines.readlines()

    valid_passwords = 0
    valid_passwords_2 = 0

    for password in lines:
        valid_passwords += check_valid_password(password.rstrip())
        valid_passwords_2 += check_pass_part_2(password.rstrip())

    print(valid_passwords)
    print(valid_passwords_2)
