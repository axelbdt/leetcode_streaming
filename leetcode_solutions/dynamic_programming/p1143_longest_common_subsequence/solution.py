def longest_common_subsequence_rec(text1, text2):
    if len(text1) == 0 or len(text2) == 0:
        return 0
    elif text1[0] == text2[0]:
        return 1 + longest_common_subsequence_rec(text1[1:], text2[1:])
    else:
        return max(
            longest_common_subsequence_rec(text1[1:], text2),
            longest_common_subsequence_rec(text1, text2[1:]),
        )


def longest_common_subsequence_dp(text1, text2):
    n = len(text1)
    m = len(text2)
    # T[i][j] : longest common subsequence of text1[i:] and text2[j:]
    T = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            if i == n or j == m:
                T[i][j] = 0
            elif text1[i] == text2[j]:
                T[i][j] = 1 + T[i + 1][j + 1]
            else:
                T[i][j] = max(T[i + 1][j], T[i][j + 1])
    return T[0][0]


def longest_common_subsequence_dp2(text1, text2):
    n = len(text1)
    m = len(text2)
    # T[i][j] : longest common subsequence of text1[i:] and text2[j:]
    T = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if text1[i] == text2[j]:
                T[i][j] = 1 + T[i + 1][j + 1]
            else:
                T[i][j] = max(T[i + 1][j], T[i][j + 1])
    return T[0][0]


def longest_common_subsequence_dp_slim(text1, text2):
    n = len(text1)
    m = len(text2)
    T = [[0 for _ in range(m + 1)] for _ in range(2)]
    # T[0][j] : longest common subsequence of text1[i:] and text2[j:]
    # T[1][j] : longest common subsequence of text1[i - 1:] and text2[j:
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if text1[i] == text2[j]:
                T[1][j] = 1 + T[0][j + 1]
            else:
                T[1][j] = max(T[0][j], T[1][j + 1])
        T[0] = T[1]
        T[1] = [0 for _ in range(m + 1)]
    return T[0][0]


def longest_common_subsequence(text1, text2):
    return longest_common_subsequence_dp(text1, text2)
