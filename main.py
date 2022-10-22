from typing import List
from itertools import permutations


def get_1024(nums: List[int], signs: List[str]):
    if len(nums) < 4 or len(signs) < 3:
        print("卡片不足")
        return
    cnt = 0
    for num in permutations(nums, 4):
        for sign in permutations(signs, 3):
            stk = []
            num_list = list(num)
            sign_list = list(sign)
            stk.append(num_list.pop())
            ans = 0
            while sign_list:
                a = str(stk.pop())
                b = str(num_list.pop())
                s = sign_list.pop()
                ans = eval(a + s + b)
                stk.append(ans)
            if ans == 1024:
                cnt += 1
                print(f"方案{cnt}:")
                print(num[::-1])
                print(sign[::-1])
    if cnt == 0:
        print("没有可行的方案")


def main():
    get_1024(nums=[6, 9, 2, 2, 1337, 30, 2, 29, 7, 32, 1024],
             signs=["*", "+", ">>", "^"])


if __name__ == '__main__':
    main()
