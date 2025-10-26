# [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/description/?envType=problem-list-v2&envId=dynamic-programming)

You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return <code>0</code>.

You may assume that you have an infinite number of each kind of coin.

The answer is **guaranteed** to fit into a signed **32-bit** integer.

**Example 1:**

```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2:**

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3:**

```
Input: amount = 10, coins = [10]
Output: 1
```

**Constraints:**

- <code>1 <= coins.length <= 300</code>
- <code>1 <= coins[i] <= 5000</code>
- All the values of <code>coins</code> are **unique** .
- <code>0 <= amount <= 5000</code>
