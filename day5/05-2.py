from typing import List


def parse_input(filename: str) -> tuple[dict, List[List[int]]]:
    with open(filename, "r") as f:
        data = f.read().split("\n\n")

        page_ordering_rules_raw = data[0].splitlines()
        page_ordering_rules = {}
        for line in page_ordering_rules_raw:
            rule = line.split("|")
            if page_ordering_rules.get(rule[0]) is None:
                page_ordering_rules.update({ rule[0]: [rule[1]] })
            else:
                page_ordering_rules[rule[0]].append(rule[1])
        
        updates_raw = data[1].splitlines()
        updates = list()
        for line in updates_raw:
            updates.append(line.split(","))

        return page_ordering_rules, updates

def correct_update(page_ordering_rules: dict, update: List[int]) -> int:
    # get a copy of the update line to verify it
    update_copy = update.copy()
    update_length = len(update)
    index = 0
    wrong_update = False
    while index < update_length:
        # check rule for current number of update line
        page_ordering_rule = page_ordering_rules.get(update_copy[update_length - 1 - index]) or []
        # if numbers in rule are found in numbers to the left in update line, update is wrong
        # the numbers in the rule should be after current number in update line
        if any(number in update_copy[:update_length - 1 - index] for number in page_ordering_rule):
            wrong_update = True
            # put current number in first place in the update line
            update_copy.insert(0, update_copy.pop(update_length - 1 - index))
            # check again
            continue

        # check is valid for current number, next number
        index += 1

    return int(update_copy[len(update_copy) // 2]) if wrong_update else 0


if __name__ == "__main__":
    page_ordering_rules, updates = parse_input("day5/05-input.txt")
    corrected_updates_middle_number_sum = sum(correct_update(page_ordering_rules, update) for update in updates)
    print(corrected_updates_middle_number_sum)
