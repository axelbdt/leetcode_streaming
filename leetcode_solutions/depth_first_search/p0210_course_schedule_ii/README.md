# [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)

There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you **must**  take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.

- For example, the pair <code>[0, 1]</code>, indicates that to take course <code>0</code> you have to first take course <code>1</code>.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return **any**  of them. If it is impossible to finish all courses, return **an empty array** .

**Example 1:** 

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

**Example 2:** 

```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

**Example 3:** 

```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

**Constraints:** 

- <code>1 <= numCourses <= 2000</code>
- <code>0 <= prerequisites.length <= numCourses * (numCourses - 1)</code>
- <code>prerequisites[i].length == 2</code>
- <code>0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses</code>
- <code>a<sub>i</sub> != b<sub>i</sub></code>
- All the pairs <code>[a<sub>i</sub>, b<sub>i</sub>]</code> are **distinct** .
