from collections import deque
from typing import List


class BuildOrder:
    def find_order(self, projects: List[str], dependencies: List[List[str]]) -> List[str]:
        ans = []
        from_project_to_in_out = {}
        visited = set()

        for project in projects:
            from_project_to_in_out[project] = {"in": 0, "out": set()}
        
        for pre, target in dependencies:
            from_project_to_in_out[target]["in"] += 1
            from_project_to_in_out[pre]["out"].add(target)
        
        current_courses = deque()
        for project, in_out in from_project_to_in_out.items():
            if in_out["in"] == 0:
                current_courses.append(project)
                visited.add(project)
                ans.append(project)
        
        while current_courses:
            current_course = current_courses.popleft()
            for _next in from_project_to_in_out[current_course]["out"]:
                from_project_to_in_out[_next]["in"] -= 1
                if from_project_to_in_out[_next]["in"] == 0:
                    current_courses.append(_next)
                    visited.add(_next)
                    ans.append(_next)

        return ans


if __name__ == "__main__":
    ans = BuildOrder().find_order(
        ["a", "b", "c", "d", "e", "f"], 
        [
            ["a", "d"],
            ["f", "b"],
            ["b", "d"],
            ["f", "a"],
            ["d", "c"],
        ]
    )
    print(ans)
