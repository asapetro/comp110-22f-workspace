# """COde trace # 14"""

# a: int = 3
# b: int = 0
# c: float


# def main() -> None:
#     """Entry"""
#     global a 
#     global b
#     print(fun(a, b))


# def fun(a: int, b: int) -> list[int]:
#     """Sample."""
#     global c
#     nums: list[int] = []
#     if b == 0:
#         while len(nums) < 4:
#             c = a + b / 2
#             print(f"a {a}")
#             print(f"b {b}")
#             print(f"c {c}")
#             if c % 2 == 0:
#                 a += 1
#                 b += 1
#             else:
#                 nums.append(a)
#                 a += 3
#     return nums


# if __name__ == "__main__":
#     main()

# def odd_and_even(a_list: list[int]) -> list[int]:
#     result: list[int] = list()
#     i = 0
#     while i < len(a_list):
#         if a_list[i] % 2 == 1:
#             result.append(a_list[i])
#         i += 2
#     print(result)
#     return result

# def vowels_and_threes(string: str) -> str:
#     i = 0
#     result: str = ""
#     vowels: list[str] = ["a", "e", "i", "o", "u"]
#     is_vowel: bool = False
#     while i < len(string):
#         if string[i] == "a" or "e" or "i" or "o" or "u" and i % 3 == 0:
#              i +=1
#         elif string[i] == "a" or "e" or "i" or "o" or "u":
#             result += string[i]
#             i += 1
#         else:
#             if i % 3 == 0:
#                 result += string[i]
#     return result
a = 'a'

vowels: list[str] = ['a', 'e', 'i', 'o', 'u']

i = 3

if a in vowels and len(vowels) % i != 2:
    print('ifr')