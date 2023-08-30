from collections import deque


def solution(maps):
    answer = 0
    q = deque()
    n = len(maps)
    m = len(maps[0])
    q.append([0, 0])
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    for i in range(m):
        for j in range(n):
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or ny < 0:
                        continue
                    if ny >= m or nx >= n:
                        continue
                    if maps[nx][ny] == 0:
                        continue
                    if visited[nx][ny] != 0:
                        continue
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

    if visited[n - 1][m - 1] == 0:
        answer = -1
    else:
        answer = visited[n - 1][m - 1]
    return answer
