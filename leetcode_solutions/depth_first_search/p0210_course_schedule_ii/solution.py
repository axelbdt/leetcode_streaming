def find_order(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    visited = set()  # permanent mark
    path = set()  # temporary mark
    order = []

    def visit(course):
        if course in visited:
            return True
        if course in path:
            return False  # cycle detected

        path.add(course)
        for next_course in graph[course]:
            if not visit(next_course):
                return False
        path.remove(course)

        visited.add(course)
        order.append(course)
        return True

    for course in range(num_courses):
        if course not in visited:
            if not visit(course):
                return []

    return order[::-1]


def find_order_iter(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    visited = set()
    path = set()
    order = []

    for start in range(numCourses):
        if start in visited:
            continue

        stack = [start]

        while stack:
            course = stack[-1]

            if course in visited:
                stack.pop()
                continue

            if course in path:
                # Back edge - already processing this node
                path.remove(course)
                visited.add(course)
                order.append(course)
                stack.pop()
                continue

            # Check for cycle
            if any(neighbor in path for neighbor in graph[course]):
                return []

            path.add(course)

            # Add unvisited neighbors
            added = False
            for neighbor in graph[course]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    added = True

            # If no neighbors added, mark as done
            if not added:
                path.remove(course)
                visited.add(course)
                order.append(course)
                stack.pop()

    return order[::-1]
