# Problem: https://www.codechef.com/problems/CSUM

def check_exist(arr, k):
    arr = set(arr)
    for i in arr:
        if (k - i) in arr:
            return 'Yes'
    return 'No'

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(check_exist(arr, K))
