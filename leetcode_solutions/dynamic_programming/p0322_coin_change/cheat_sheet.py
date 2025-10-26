def coin_change_rec(coins, amount):
    if amount == 0:
        return 0
    elif coins == []:
        return -1
    elif coins[0] > amount:
        return coin_change_rec(coins[1:], amount)
    else:
        take_coin = coin_change_rec(coins, amount - coins[0])
        leave_coin = coin_change_rec(coins[1:], amount)
        if take_coin == -1 and leave_coin == -1:
            return -1
        elif take_coin == -1:
            return leave_coin
        elif leave_coin == -1:
            return 1 + take_coin
        else:
            return min(1 + take_coin, leave_coin)


def coin_change_dp(coins, amount):
    # T[i][j] : min coins needed to make amount j with coins[0:i]
    T = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
    for i in range(len(coins) + 1):
        for j in range(amount + 1):
            if j == 0:
                T[i][j] = 0
            elif i == 0:
                T[i][j] = -1
            elif coins[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                take_coin = T[i][j - coins[i - 1]]
                leave_coin = T[i - 1][j]
                if take_coin == -1 and leave_coin == -1:
                    T[i][j] = -1
                elif take_coin == -1:
                    T[i][j] = leave_coin
                elif leave_coin == -1:
                    T[i][j] = 1 + take_coin
                else:
                    T[i][j] = min(1 + take_coin, leave_coin)
    return T[len(coins)][amount]


def coin_change_dp2(coins, amount):
    # T[i][j] : min coins needed to make amount j with coins[0:i]
    T = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
    # T[i][0] = 0 for all i, already initialized
    for j in range(1, amount + 1):
        T[0][j] = -1
    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                take_coin = T[i][j - coins[i - 1]]
                leave_coin = T[i - 1][j]
                if take_coin == -1 and leave_coin == -1:
                    T[i][j] = -1
                elif take_coin == -1:
                    T[i][j] = leave_coin
                elif leave_coin == -1:
                    T[i][j] = 1 + take_coin
                else:
                    T[i][j] = min(1 + take_coin, leave_coin)
    return T[len(coins)][amount]


# Fill only one row left to right
# because T[i][j - c] and T[i - 1][j] are already filled
def coin_change_dp3(coins, amount):
    # T[i][j] : min coins needed to make amount j with coins[0:i]
    T = [0 for _ in range(amount + 1)]
    for j in range(1, amount + 1):
        T[j] = -1
    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] > j:
                continue
            else:
                take_coin = T[j - coins[i - 1]]
                leave_coin = T[j]
                if take_coin == -1 and leave_coin == -1:
                    T[j] = -1
                elif take_coin == -1:
                    T[j] = leave_coin
                elif leave_coin == -1:
                    T[j] = 1 + take_coin
                else:
                    T[j] = min(1 + take_coin, leave_coin)
    return T[amount]
