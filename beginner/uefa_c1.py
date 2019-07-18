# Problem: https://www.codechef.com/problems/UCL
def find_leaders(table):
    result = sorted(table.items(), key = lambda x: (x[1][0], x[1][1]), reverse = True)
    return result[0], result[1]

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        matches = []
        teams = []
        for k in range(12):
            match = input()
            matches.append(match)
            arr = match.split(' ')
            teams.append(arr[0])
            teams.append(arr[-1])
        teams = list(set(teams))
        table = {}
        for team in teams:
            table.update({team: [0, 0]})
        for match in matches:
            arr = match.split(' ')
            score1 = int(arr[1])
            score2 = int(arr[3])
            if score1 > score2:
                table[arr[0]][0] += 3
            elif score1 == score2:
                table[arr[0]][0] += 1
                table[arr[-1]][0] += 1
            else:
                table[arr[-1]][0] += 3
            table[arr[0]][1] += score1 - score2
            table[arr[-1]][1] += score2 - score1
        top1, top2 = find_leaders(table)
        print(top1[0], top2[0])
