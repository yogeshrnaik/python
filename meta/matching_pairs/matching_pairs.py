import math


# Add any extra import statements you may need here


# Add any helper functions you may need here
def matching_pairs(s, t):
    total_matches = 0
    non_matches = {}
    char_match_counts = {}
    swappable_without_reducing_match_count = False
    for i in range(0, len(s)):
        if s[i] == t[i]:
            total_matches += 1
            count = char_match_counts.get(s[i], 0)
            char_match_counts[s[i]] = count + 1
            if char_match_counts[s[i]] > 1:
                swappable_without_reducing_match_count = True
        else:
            non_matched_chars = non_matches.get(s[i], [])
            non_matched_chars.append(t[i])
            non_matches[s[i]] = non_matched_chars

    if not non_matches:
        if swappable_without_reducing_match_count:
            return total_matches
        else:
            return total_matches - 2

    swappable_without_reducing_match_count = False
    for char, non_matched_chars in non_matches.items():
        for non_match_char in non_matched_chars:
            if char in non_matches.get(non_match_char, []):
                return total_matches + 2

    return total_matches - 1


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here
    s_2, t_2 = "abc", "abd"
    expected_2 = 1
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    s_2, t_2 = "abcd", "abdc"
    expected_2 = 4
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    s_2, t_2 = "abcda", "abdca"
    expected_2 = 5
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

