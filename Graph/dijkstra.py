import heapq
from typing import List


class MinDistanceFinder:
    def find_min(self, data: List[List[str]], node_num: int) -> int:
        edges = [[] for i in range(node_num)]
        for start, end, cost in data:
            edges[ord(start) - ord("a")].append([end, cost])
            if end == "s":
                edges[-1].append([start, cost])
            else: 
                edges[ord(end) - ord("a")].append([start, cost])

        node = [-1] * node_num
        node[-1] = 0
        visited = set(["s"])
        next_queue = [] # heap

        for _next, cost in edges[-1]:
            heapq.heappush(next_queue, [cost, _next])
        
        while len(visited) != node_num:
            cur_cost, _cur = heapq.heappop(next_queue)
            if _cur not in visited:
                node[ord(_cur) - ord("a")] = cur_cost
                visited.add(_cur)
                for _next, cost in edges[ord(_cur) - ord("a")]:
                    if _next not in visited:
                        heapq.heappush(next_queue, [cost + cur_cost, _next])
        
        return node


if __name__ == "__main__":
    data = [
        ["a", "s", 2],
        ["a", "d", 3],
        ["b", "s", 1],
        ["b", "d", 8],
        ["b", "e", 2],
        ["c", "s", 2],
        ["c", "e", 5],
        ["c", "f", 1],
        ["d", "e", 6],
        ["d", "g", 1],
        ["e", "f", 5],
        ["e", "i", 4],
        ["e", "g", 4],
        ["f", "i", 5],
        ["g", "h", 1],
        ["h", "i", 5],
    ]
    node_num = 10
    print(MinDistanceFinder().find_min(data, node_num))
