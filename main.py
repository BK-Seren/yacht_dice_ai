from y_model import Ymodel
from y_view import Yview
from y_controller import Ycontroller
import numpy as np
import matplotlib.pyplot as plt


# 게임 반복 횟수 설정
NUM_GAMES = 1000

# 플레이어별 결과 저장용
player_scores = {}  # {플레이어 이름: [게임1 점수, 게임2 점수, ...]}
rank_counts = {}    # {플레이어 이름: [1등 횟수, 2등 횟수, ...]}

# 초기화: 플레이어 이름 가져오기
m = Ymodel()
player_names = [player.name for player in m.players]
for name in player_names:
    player_scores[name] = []  # 각 플레이어 점수 저장
    rank_counts[name] = [0] * len(player_names)  # 1등, 2등, 3등 횟수

# 게임 반복
for _ in range(NUM_GAMES):
    # 새로운 게임 초기화
    m = Ymodel()
    v = Yview(m)
    Ycontroller(m, v)

    # 각 게임의 점수 기록 (음수 값 제외)
    game_result = {
        player.name: sum(score for score in player.board.score if score >= 0)
        for player in m.players
    }

    # 점수를 내림차순으로 정렬하여 순위 계산
    sorted_result = sorted(
        game_result.items(), key=lambda x: (-x[1], x[0])
    )  # 점수 내림차순, 이름 오름차순 정렬
    for rank, (player_name, score) in enumerate(sorted_result):
        player_scores[player_name].append(score)  # 플레이어별 점수 저장
        rank_counts[player_name][rank] += 1       # 순위 횟수 증가

# 플레이어별 점수 분석
print("Final Analysis:")
player_stats = {}
for player_name, scores in player_scores.items():
    scores = np.array(scores)
    player_stats[player_name] = {
        "min": scores.min(),
        "max": scores.max(),
        "avg": scores.mean(),
    }
    print(f"{player_name}:")
    print(f"  Minimum Score: {scores.min()}")
    print(f"  Maximum Score: {scores.max()}")
    print(f"  Average Score: {scores.mean():.2f}")

# 순위 분석 출력
print("\nRankings:")
for player_name, ranks in rank_counts.items():
    print(f"{player_name}:")
    for rank, count in enumerate(ranks):
        print(f"  Rank {rank + 1}: {count} times")

# 시각화
# 점수 분포
plt.figure(figsize=(12, 6))
for player_name, scores in player_scores.items():
    plt.hist(
        scores,
        bins=20,
        alpha=0.5,
        label=f"{player_name} (avg: {player_stats[player_name]['avg']:.2f})",
    )
plt.title("Player Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.legend(loc="upper right")
plt.show()

# 순위 분포
plt.figure(figsize=(12, 6))
x = np.arange(1, len(player_names) + 1)
bar_width = 0.2
for idx, player_name in enumerate(player_names):
    plt.bar(
        x + idx * bar_width - bar_width / 2,
        rank_counts[player_name],
        width=bar_width,
        label=player_name,
    )
plt.title("Player Rank Distribution")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.xticks(x, [f"Rank {i}" for i in range(1, len(player_names) + 1)])
plt.legend(loc="upper right")
plt.show()


'''
m = Ymodel()
v = Yview(m)
Ycontroller(m,v)
'''