# Step 1: Recursive
def climb_stairs_rec(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return climb_stairs_rec(n - 1) + climb_stairs_rec(n - 2)


# Step 2: Dynamic Programming with recursion reuse
def climb_stairs_dp0(n: int) -> int:
    T = [0 for _ in range(n + 1)]
    for i in range(len(T)):
        if i == 0:
            T[i] = 1
        elif i == 1:
            T[i] = 1
        else:
            T[i] = T[i - 1] + T[i - 2]
    return T[n]


# Step 3: Dynamic Programming with initial values
def climb_stairs_dp1(n: int) -> int:
    T = [0 for _ in range(n + 1)]
    T[0] = 1
    T[1] = 1
    for i in range(2, len(T)):
        T[i] = T[i - 1] + T[i - 2]
    return T[n]


# Step 4: Dynamic Programming with only two cells
def climb_stairs_dp2(n: int) -> int:
    T = [1, 1]
    i = 1
    while i < n:
        # invariants :
        # T[0] is answer for i - 1,
        # T[1] is answer for i
        next = T[0] + T[1]
        T[0] = T[1]
        T[1] = next
        i += 1
    return T[1]


# Step 5: Two variables
def climb_stairs_final(n: int) -> int:
    prev, curr = 1, 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


# Note: loop invariant : T[1] = answer for i
