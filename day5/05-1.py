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


def check_update(page_ordering_rules: dict, update: List[int]) -> int:
    # get a copy of the update line to verify it
    update_copy = update.copy()
    for i in range(len(update_copy)):
        # check rule for last number of update line
        page_ordering_rule = page_ordering_rules.get(update_copy[-1]) or []
        # if numbers in rule are found in the update line, update is wrong
        # the numbers in the rule should be after last number in update line
        if any(number in update_copy for number in page_ordering_rule):
            return 0
        # remove last number in update line
        update_copy.pop(-1)

    # if all update line numbers' rule was verified, return the middle number in update line
    return int(update[len(update) // 2])


if __name__ == "__main__":
    page_ordering_rules, updates = parse_input("day5/05-input.txt")
    valid_updates_middle_number_sum = sum(check_update(page_ordering_rules, update) for update in updates)
    print(valid_updates_middle_number_sum)
