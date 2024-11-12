from itertools import combinations_with_replacement, product
from collections import Counter
import random
from y_model import Ymodel
from y_view import Yview


class Ycontroller:
    ym: Ymodel
    yv: Yview

    def __init__(self, y_model: Ymodel, y_view: Yview):
        self.ym, self.yv = y_model, y_view

        for round in range(13):
            self.yv.show_round(round + 1)
            for i in range(len(self.ym.players)):
                if self.ym.players[i].is_ai:  # AI 플레이어는 자동으로 행동
                    self.play_ai_round(i)
                else:
                    self.play_round(i)
        
        self.show_final_board()
    
    def show_final_board(self):
        print("Final Scores")
        self.yv.show_board()

    def play_round(self, p_num: int):
        self.yv.show_board()
        roll_count: int = 0
        while roll_count < 3:
            if roll_count == 0:
                keep_list = [False] * 5
                self.roll_dices(keep_list)
                roll_count += 1
                self.yv.show_dices()
                cmd: str = self.yv.ask_cmd()
            if cmd == 's':  # submit
                break
            else:  # roll again
                keep_list = self.yv.ask_dice_keep()
                self.roll_dices(keep_list)
                roll_count += 1
                self.yv.show_dices()
                if roll_count < 3:
                    cmd = self.yv.ask_cmd()
        s_idx: int = self.yv.ask_submit_idx(p_num, [self.cal_dices(self.ym.dices, i) for i in range(1, 14)])
        self.ym.players[p_num].history.append(s_idx)
        self.ym.players[p_num].board.score[s_idx] = self.cal_dices(self.ym.dices, s_idx)
        self.ym.players[p_num].board.score[0] = self.cal_bonus(p_num)

    def play_ai_round(self, p_num: int):
        self.yv.show_board()
        roll_count: int = 0
        while roll_count < 3:
            if roll_count == 0:
                # AI가 최적의 주사위 선택
                keep_list = [False] * 5
                self.roll_dices(keep_list)
                roll_count += 1
                self.yv.show_dices()
                print(f"AI{p_num+1}가 선택한 주사위 유지: {keep_list}")
                print(f"현재 주사위: {self.ym.dices}")
            else:
                keep_list = self.get_best_dice_keep()  # 자동으로 선택된 주사위를 유지
                self.roll_dices(keep_list)
                roll_count += 1
                self.yv.show_dices()
                print(f"AI{p_num+1}가 선택한 주사위 유지: {keep_list}")
                print(f"현재 주사위: {self.ym.dices}")

        # 최적의 선택을 자동으로 하고, 점수도 자동으로 매기게 합니다.
        s_idx: int = self.get_best_score_idx(p_num)
        print(f"AI{p_num+1}가 선택한 점수 항목: {s_idx} ({self.cal_dices(self.ym.dices, s_idx)}점)")

        self.ym.players[p_num].history.append(s_idx)
        self.ym.players[p_num].board.score[s_idx] = self.cal_dices(self.ym.dices, s_idx)
        self.ym.players[p_num].board.score[0] = self.cal_bonus(p_num)


    def get_best_dice_keep(self) -> list:
        # AI가 주사위 굴린 후 최적의 선택을 하기 위해 가능한 높은 기댓값을 가지는 주사위를 유지
        keep_list = [False] * 5
        best_outcome = None
        best_expected_value = float('-inf')

        # 현재 주사위 상태에서 남길 주사위 결정
        for outcome in combinations_with_replacement(range(1, 7), 5):
            expected_value = self.expected_value(outcome)
            if expected_value > best_expected_value:
                best_expected_value = expected_value
                best_outcome = outcome

        # AI가 선택할 주사위 유지 리스트 결정
        for i in range(5):
            if self.ym.dices[i] in best_outcome:  # 최적의 경우에 있는 값을 True로
                keep_list[i] = True
        return keep_list

    def cal_bonus(self, p_num:int) -> int:
        sum:int = 0
        for i in range(1,7):
            sum += self.ym.players[p_num].board.score[i]
        if sum >= 63:
            return 35
        else:
            return 0
        

    def get_best_score_idx(self, p_num: int) -> int:
        # 각 점수 항목에 대해 계산한 점수의 기댓값을 비교하여 가장 높은 점수를 선택
        best_idx = -1
        best_score = -1
        
        # 이미 선택한 항목을 가져와 제외할 항목을 확인
        used_indices = self.ym.players[p_num].history

        for i in range(1, 14):
            # 이미 사용한 항목은 건너뜁니다
            if i in used_indices:
                continue

            score = self.cal_dices(self.ym.dices, i)
            if score > best_score:
                best_score = score
                best_idx = i

        return best_idx

    def roll_dices(self, keep_list: list):
        for i in range(5):
            if not keep_list[i]:
                self.ym.dices[i] = random.randint(1, 6)


    def expected_value(self, dice_list: list) -> float:
        # 고정된 주사위 값과 남은 주사위 개수 구하기
        fixed_dice = [d for d in dice_list if d != 0]  # 고정된 주사위 (0은 던질 주사위)
        remaining_dice_count = dice_list.count(0)  # 던져야 할 주사위 개수
        
        # 가능한 모든 주사위 던지기 결과 생성
        all_outcomes = product(range(1, 7), repeat=remaining_dice_count)
        
        total_score = 0
        best_score = -float('inf')

        # 가능한 모든 주사위 결과에 대해 기댓값 계산
        for outcome in all_outcomes:
            # outcome은 남은 주사위에 대한 결과 (fixed_dice는 고정)
            full_outcome = fixed_dice + list(outcome)  # 전체 주사위 결과 -> 고정된 주사위 + 모든 가능한 경우의 수 
            
            outcome_score = self.cal_dices(full_outcome, 13)  # 주사위 조합에 대한 점수 계산
            
            total_score += outcome_score

        # 기댓값 계산 (기댓값 = 확률 * 점수의 합)
        expected_value = total_score  # 이미 확률을 반영한 총합

        return expected_value


    def cal_dices(self, dice_list: list, row_num: int) -> int:
        score = 0
        if 1 <= row_num <= 6:
            return dice_list.count(row_num) * row_num
        elif row_num == 7:
            counts = [dice_list.count(dice_list[i]) for i in range(5)]
            if 3 in counts or 4 in counts or 5 in counts:
                return sum(dice_list)
            else:
                return 0
        elif row_num == 8:
            counts = [dice_list.count(dice_list[i]) for i in range(5)]
            if 4 in counts or 5 in counts:
                return sum(dice_list)
            else:
                return 0
        elif row_num == 9:
            counts = [dice_list.count(dice_list[i]) for i in range(5)]
            if 2 in counts and 3 in counts:
                return 25
            else:
                return 0
        elif row_num == 10:
            temp_set = set(dice_list)
            if temp_set.issuperset(set([1, 2, 3, 4])) or temp_set.issuperset(set([2, 3, 4, 5])) or temp_set.issuperset(set([3, 4, 5, 6])):
                return 30
            else:
                return 0
        elif row_num == 11:
            temp_set = set(dice_list)
            if temp_set.issuperset(set([1, 2, 3, 4, 5])) or temp_set.issuperset(set([2, 3, 4, 5, 6])):
                return 40
            else:
                return 0
        elif row_num == 12:
            if len(set(dice_list)) == 1:
                return 50
            else:
                return 0
        elif row_num == 13:
            return sum(dice_list)

