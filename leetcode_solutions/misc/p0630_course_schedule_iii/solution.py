import heapq


def schedule_course(courses):
    # sort courses by increasing deadline
    sorted_courses = sorted(courses, key=lambda course: course[1])
    count = 0
    last_day = 0
    max_heap = [0]
    for duration, deadline in sorted_courses:
        if last_day + duration <= deadline:
            last_day += duration
            count += 1
            heapq.heappush(max_heap, -duration)
        elif duration < -max_heap[0]:
            longest = -heapq.heappop(max_heap)
            last_day += duration - longest
            heapq.heappush(max_heap, -duration)
    return count
