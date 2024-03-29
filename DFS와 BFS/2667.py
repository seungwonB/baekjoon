from collections import deque

def solution():
    map_size = int(input()) # 지도의 크기
    graph = [] # 그래프 배열
    answer = [] # 총 아파트 수 담은 배열
    for i in range(map_size):
        graph.append(list(map(int, input())))

    visited = [[False for j in range(map_size)] for i in range(map_size)]

    for i in range(map_size):
        for j in range(map_size):
            if graph[i][j] == 1:
                answer.append(BFS(map_size, graph, i, j, visited))

    # 배열의 크기 먼저 출력
    print(len(answer))
    answer.sort()
    for i in answer:
        print(i)

def BFS(N, graph, i, j, visited):
    # 큐 생성
    queue = deque()
    # 동 서 남 북
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 시작 노드 큐에 삽입
    queue.append((i, j))
    cnt_apart = 1
    # 큐가 빌 떄 까지
    while queue:
        # 현재 y, x 큐에서 꺼냄
        cur_y, cur_x = queue.popleft()
        # 방문 처리
        visited[i][j] = True

        for k in range(4):
            # 동 서 남 북 으로 이동
            next_y = cur_y + dy[k]
            next_x = cur_x + dx[k]

            # 밖으로 나가지 않고 N,M보다 크지 않을 때
            if next_y >= 0 and next_x >= 0 and next_y < N and next_x < N:
                # 해당 값이 0이 아니고 방문하지 않았을 때
                if graph[next_y][next_x] != 0 and visited[next_y][next_x] == 0:
                    # 방문 처리
                    visited[next_y][next_x] = True
                    # 인접한 노드는 가중치 증가
                    graph[next_y][next_x] = 0
                    queue.append((next_y, next_x))
                    cnt_apart += 1

    return cnt_apart

solution()
