def coin_change_rec(coins, amount):
    if amount == 0:
        return 1
    elif coins == []:
        return 0
    elif amount < coins[0]:
        return coin_change_rec(coins[1:], amount)
    else:
        return coin_change_rec(coins[1:], amount) + coin_change_rec(
            coins, amount - coins[0]
        )


def coin_change_dp(coins, amount):
    T = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
    for i in range(len(coins) + 1):
        for j in range(amount + 1):
            if j == 0:
                T[i][j] = 1
            elif i == 0:
                T[i][j] = 0
            elif j < coins[i - 1]:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] + T[i][j - coins[i - 1]]
    return T[len(coins)][amount]


def coin_change_dp2(coins, amount):
    T = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
    for i in range(len(coins) + 1):
        T[i][0] = 1
    # T[0][j] = 0 for j > 0, already initialized
    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if j < coins[i - 1]:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] + T[i][j - coins[i - 1]]
    return T[len(coins)][amount]


def coin_change_dp3(coins, amount):
    T = [0 for _ in range(amount + 1)]
    T[0] = 1
    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if j < coins[i - 1]:
                T[j] = T[j]
            else:
                T[j] = T[j] + T[j - coins[i - 1]]
    return T[amount]
