MAX_STR_LEN = 5000
DIVIDE_BY = 1000000


def is_valid_code(c):
    return 1 <= c <= 26


def count_interpretation(ipt, idx):
    if idx == len(ipt) - 1:
        return 1
    elif idx + 2 <= len(ipt) and is_valid_code(int(ipt[idx:idx+2])):
        return count_interpretation(ipt, idx + 1) + count_interpretation(ipt, idx + 2)
    else:
        if idx >= len(ipt) - 1:
            return 1
        return count_interpretation(ipt, idx + 1)


def get_answer(q):
    return count_interpretation(q, 0) % DIVIDE_BY


if __name__ == "__main__":
    question = input()
    print(get_answer(question))
