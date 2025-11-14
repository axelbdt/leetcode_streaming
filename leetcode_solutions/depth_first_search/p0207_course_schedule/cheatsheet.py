from collections import deque


def prerequisites_to_adjacency_list(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    return graph


def can_finish(num_courses, prerequisites):
    return can_finish_copy(num_courses, prerequisites)


def can_finish_copy(num_courses, prerequisites):
    prerequisites = prerequisites_to_adjacency_list(num_courses, prerequisites)

    def has_cycle(course, path):
        if course in path:
            return True
        new_path = set(path)
        new_path.add(course)
        for prereq in prerequisites[course]:
            if has_cycle(prereq, new_path):
                return True
        return False

    for course in range(num_courses):
        if has_cycle(course, set()):
            return False
    return True


def can_finish_slow(num_courses, prerequisites):
    prerequisites = prerequisites_to_adjacency_list(num_courses, prerequisites)

    def has_cycle(course, path):
        if course in path:
            return True
        path.add(course)
        for prereq in prerequisites[course]:
            if has_cycle(prereq, path):
                return True
        path.remove(course)
        return False

    for course in range(num_courses):
        if has_cycle(course, set()):
            return False
    return True


def can_finish_memo(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    def has_cycle(course, path, checked):
        if course in path:
            return True
        if course in checked:
            return False
        path.add(course)
        for prereq in graph[course]:
            if has_cycle(prereq, path, checked):
                return True
        path.remove(course)
        checked.add(course)
        return False

    checked = set()
    for course in range(num_courses):
        if has_cycle(course, set(), checked):
            return False
        else:
            checked.add(course)
    return True


def can_finish_imp(num_courses, prerequisites):
    prerequisites = prerequisites_to_adjacency_list(num_courses, prerequisites)

    def has_cycle(start):
        stack = [start]
        path = set()

        while stack:
            course = stack[-1]

            if course not in path:
                path.add(course)
                for prereq in prerequisites[course]:
                    if prereq in path:
                        return True
                    stack.append(prereq)
            else:
                stack.pop()
                path.remove(course)

        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False
    return True


def can_finish_imp_memo(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    visited = set()

    def has_cycle(start):
        if start in visited:
            return False

        stack = [start]
        path = set()

        while stack:
            course = stack[-1]

            if course not in path:
                path.add(course)
                for prereq in graph[course]:
                    if prereq in path:
                        return True
                    if prereq not in visited:
                        stack.append(prereq)
            else:
                stack.pop()
                path.remove(course)
                visited.add(course)

        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False
    return True
