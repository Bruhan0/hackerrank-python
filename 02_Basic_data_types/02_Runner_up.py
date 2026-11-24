def runner_up(n , arr):
    return sorted(set(arr))[-2]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(runner_up(n , arr))