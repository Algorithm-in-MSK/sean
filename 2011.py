MAX_STR_LEN = 5000
DIVIDE_BY = 1000000


def is_start_with_non_zero(c):
    return not c.startswith("0")


def is_valid_code(c):
    return is_start_with_non_zero(c) and 1 <= int(c) <= 26


def recursion(ipt, idx):
    if idx >= len(ipt) - 1:
        return 1
    elif idx + 2 <= len(ipt) and is_valid_code(ipt[idx:idx + 2]):
        return recursion(ipt, idx + 1) + recursion(ipt, idx + 2)
    else:
        return recursion(ipt, idx + 1)


def dynamic_programming(ipt):
    length = len(ipt)
    mem = [0 for _ in range(length)]
    for idx in range(length):
        if idx == 0:
            mem[0] = int(is_valid_code(ipt[0]))
        else:
            if is_start_with_non_zero(ipt[idx]):
                mem[idx] += mem[idx - 1]

            # Trick: int(True) => 1, int(False) => 0
            if idx == 1:
                mem[idx] += int(is_valid_code(ipt[:2])) * 1
            else:
                mem[idx] += int(is_valid_code(ipt[idx - 1:idx + 1])) * mem[idx - 2]

    return mem[length - 1]


def validate_input(ipt):
    assert ipt.isdigit() and len(ipt) <= MAX_STR_LEN


def main(question):
    validate_input(question)
    # return recursion(question, 0) % DIVIDE_BY
    return dynamic_programming(question) % DIVIDE_BY


if __name__ == "__main__":
    question = input()
    answer = main(question)
    print(answer)
