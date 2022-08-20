import sys
from heapq import heappush, heappop
import math
# 다익스트라 구현

def dijkstra(start,*end):
    dist = [math.inf for _ in range(n+1)]
    dist[start] = 0
    h = [(start,dist[start])]
    while h:
        node = heappop(h)[0]
        for u,w in g[node].items():
            if dist[u] > dist[node] + w :
                    dist[u] = dist[node] + w
                    heappush(h,(u,dist[u]))
    return (dist[i] for i in end)

# 입력 받기

input = sys.stdin.readline

n,e = map(int,input().split())

g = [{} for _ in range(n+1)]

for _ in range(e):
    start,end,weight = map(int,input().split())

    if end in g[start]:
        g[start][end] = min(g[start][end],weight)
        g[end][start] = min(g[end][start],weight)
    
    g[start][end] = weight
    g[end][start] = g[start][end]

waypoint1,waypoint2 = map(int,input().split())

# path1 = dijkstra(1,waypoint1) + dijkstra(waypoint1,waypoint2) + dijkstra(waypoint2,n)
# path2 = dijkstra(1,waypoint2) + dijkstra(waypoint2,waypoint1) + dijkstra(waypoint1,n)

# ans = min(path1,path2)

# start_waypoint1 = dijkstra(1,waypoint1)
# start_waypoint2 = dijkstra(1,waypoint2)
# way1_2 = dijkstra(waypoint1,waypoint2)
# way1_end = dijkstra(waypoint1,n)
# way2_end = dijkstra(waypoint2,n)

# ans = min(start_waypoint1+way1_2+way2_end,start_waypoint2 + way1_2 + way1_end)

way1_start,way1_way2,way1_end=dijkstra(waypoint1,1,waypoint2,n)
way2_start,way2_end=dijkstra(waypoint2,1,n)

ans = min(way1_start+way1_way2+way2_end, way2_start+way1_end+way1_way2)
if ans == float('inf'):
    ans = -1

print(ans)