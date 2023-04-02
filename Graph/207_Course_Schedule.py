from collections import deque
from typing import List


class Scheduler:
    def can_finish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node = {}
        visited = set()
        for course in range(numCourses):
            node[course] = {'in': 0, 'out': set()}
        for first, second in prerequisites:
            node[first]['in'] += 1
            node[second]['out'].add(first)
        
        get_course = deque()
        for course in range(numCourses):
            if node[course]['in'] == 0:
                get_course.append(course)
                visited.add(course)

        while get_course:
            current = get_course.popleft()
            for _next in node[current]['out']:
                node[_next]['in'] -= 1
                if node[_next]['in'] == 0:
                    visited.add(_next)
                    get_course.append(_next)
        
        return len(visited) == numCourses


if __name__ == "__main__":
    print(Scheduler().can_finish(2, [[1, 0], [0,1]]))