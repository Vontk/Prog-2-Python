from typing import List


def recursive_index_of(arr: List[str], value: str) -> int:
    return recursive_index_of_by_index(arr, value, 0)


def recursive_index_of_by_index(arr: List[str], value: str, index: int) -> int:
    if len(arr) == index:
        return -1
    elif arr[index] == value:
        return index
    else:
        return recursive_index_of_by_index(arr, value, index + 1)


def recursive_index_of_empty(arr: List[str]) -> int:
    return recursive_index_of_empty_helper(arr, 0)


def recursive_index_of_empty_helper(arr: List[str], index: int) -> int:
    if len(arr) == index:
        return -1
    elif arr[index] == "":
        return index
    else:
        return recursive_index_of_empty_helper(arr, index + 1)


def recursive_put(value: str, arr: List[str]) -> int:
    index = recursive_index_of_empty(arr)
    if index == -1:
        return -1
    arr[index] = value
    return index


def recursive_remove(arr: List[str], value: str) -> int:
    return recursive_remove_helper(arr, value, 0)


def recursive_remove_helper(arr: List[str], value: str, count: int) -> int:
    index = recursive_index_of(arr, value)
    if index != -1:
        arr.pop(index)
        return recursive_remove_helper(arr, value, count + 1)
    else:
        return count


def recursive_sum(arr: List[int]) -> int:
    return recursive_sum_helper(arr, 0, 0)


def recursive_sum_helper(arr: List[int], index: int, sum: int) -> int:
    if len(arr) == index:
        return sum
    else:
        return recursive_sum_helper(arr, index + 1, sum + arr[index])


def recursive_factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * recursive_factorial(n - 1)
    else:
        return n


def recursive_pow(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * recursive_pow(base, exponent - 1)
    else:
        return 1


def recursive_fibonacci(n: int) -> int:
    if n > 1:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
    elif n == 1:
        return 1
    else:
        return 0


def recursive_palindrome(s: str) -> bool:
    return recursive_palindrome_helper(s, 0)


def recursive_palindrome_helper(s: str, index: int) -> bool:
    currentIndexMatchesPalindrome = s[index] == s[len(s) - index - 1]
    reachedHalfOfWord = index >= len(s) // 2
    if currentIndexMatchesPalindrome and not reachedHalfOfWord:
        return recursive_palindrome_helper(s, index + 1)
    elif currentIndexMatchesPalindrome and reachedHalfOfWord:
        return True
    return False
