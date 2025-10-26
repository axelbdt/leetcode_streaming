# Step 0 : Recursive
def min_cost_climbing_stairs_rec(cost):
    def helper(current_floor):
        if current_floor == len(cost):
            return 0
        elif current_floor == len(cost) - 1:
            return cost[current_floor]
        else:
            return min(
                helper(current_floor + 1) + cost[current_floor],
                helper(current_floor + 2) + cost[current_floor],
            )

    return min(helper(0), helper(1))


# Note : overlap because several ways to reach the same floor, but min cost from this floor is unchanged


# Aside : recursive with tail call optimization (accumlated cost as a parameter)
def min_cost_climbing_stairs_rec2(cost):
    def helper(current_floor, current_cost):
        if current_floor == len(cost):
            return current_cost
        elif current_floor == len(cost) - 1:
            return cost[current_floor] + current_cost
        else:
            current_floor_cost = 0 if current_floor == -1 else cost[current_floor]
            return min(
                helper(current_floor + 1, current_cost + current_floor_cost),
                helper(current_floor + 2, current_cost + current_floor_cost),
            )

    return min(helper(0, 0), helper(1, 0))


# Step 1 : Dynamic Programming from recursion
def min_cost_climbing_stairs_dp1(cost):
    T = [0 for _ in range(len(cost) + 1)]
    i = len(cost)
    while i >= 0:
        if i == len(cost):
            T[i] = 0
        elif i == len(cost) - 1:
            T[i] = cost[i]
        else:
            T[i] = min(
                T[i + 1] + cost[i],
                T[i + 2] + cost[i],
            )
        i -= 1
    return min(T[0], T[1])


# Step 2 : Dynamic Programming with initial value
def min_cost_climbing_stairs_dp2(cost):
    T = [0 for _ in range(len(cost) + 1)]
    T[len(cost)] = 0
    T[len(cost) - 1] = cost[len(cost) - 1]
    i = len(cost) - 2
    while i >= 0:
        T[i] = min(
            T[i + 1] + cost[i],
            T[i + 2] + cost[i],
        )
        i -= 1
    return min(T[0], T[1])


# Step 3 : Dynamic Programming with only two cells
def min_cost_climbing_stairs_dp3(cost):
    T = [0, cost[len(cost) - 1]]
    i = len(cost) - 2
    # invariants :
    # T[0] is cost from step i + 1,
    # T[1] is cost from step i + 2
    while i >= 0:
        new_cost = min(
            T[0] + cost[i],
            T[1] + cost[i],
        )
        T[0] = T[1]
        T[1] = new_cost
        i -= 1
    return min(T[0], T[1])


# Note : loop invariant : T[0] is cost from step i + 1, T[1] is cost from step i + 2


# Step 4 : Using only two variables
def min_cost_climbing_stairs_final(cost):
    prev, curr = 0, cost[len(cost) - 1]
    for i in range(len(cost) - 2, -1, -1):
        prev, curr = curr, min(
            prev + cost[i],
            curr + cost[i],
        )
    return min(prev, curr)
