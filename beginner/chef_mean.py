# Problem: https://www.codechef.com/problems/CHFM

def find_coin(arr):
    mean = sum(arr) / len(arr)
    if mean in arr:
        return arr.index(mean) + 1
    return 'Impossible'

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        li = list(map(int, input().split()))
        result = find_coin(li)
        print(result)
