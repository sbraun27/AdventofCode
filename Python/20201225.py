import time


def find_loop_size(public_key, subject_num=7):
    loop_size = 0
    value = 1
    while (value - public_key):
        loop_size += 1
        value = value * subject_num
        value = value % 20201227

    return loop_size


def find_encryption_key(subject_number, loop_size):
    value = 1
    for loop in range(loop_size):
        value = value * subject_number
        value = value % 20201227

    return value


if __name__ == "__main__":
    card_public_key = 8184785
    door_public_key = 5293040

    card_loop_size = find_loop_size(card_public_key)
    door_loop_size = find_loop_size(door_public_key)

    part1 = find_encryption_key(card_public_key, door_loop_size)

    import ipdb
    ipdb.set_trace()
