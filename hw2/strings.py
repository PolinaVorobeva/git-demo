from typing import List


def filter_lines_of_length_five(lines: List[str]) -> List[str]:
    list_of_fives = []
    for i in range(len(lines)):
        if len(lines[i]) == 5:
            list_of_fives.append(lines[i])
    return list_of_fives


if __name__ == '__main__':
    print(filter_lines_of_length_five(['aaa', 'ab', 'abaab', 'ccccc']))