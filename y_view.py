from y_model import Ymodel

class Yview:
    ym:Ymodel
    
    def __init__(self, y_model:Ymodel):
        self.ym = y_model

    def show_round(self, round:int):
        #print("Round: "+str(round)+"/13")
        pass
    
    def show_board(self):

        p_l_len = len(self.ym.players)
        print("             ",end='')
        for i in range(p_l_len):
            print("\tp"+str(i+1),end='')
        print("")
        print("aces\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[1] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[1]),end='')
        print("")
        print("twos\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[2] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[2]),end='')
        print("")
        print("threes\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[3] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[3]),end='')
        print("")
        print("fours\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[4] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[4]),end='')
        print("")
        print("fives\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[5] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[5]),end='')
        print("")
        print("sixes\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[6] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[6]),end='')
        print("")
        print("bonus\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[0] == -1:
                print("\t0",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[0]),end='')
        print("")
        print("3 kind\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[7] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[7]),end='')
        print("")
        print("4 kind\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[8] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[8]),end='')
        print("")
        print("f house\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[9] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[9]),end='')
        print("")
        print("s straight\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[10] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[10]),end='')
        print("")
        print("l straight\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[11] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[11]),end='')
        print("")
        print("yacht\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[12] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[12]),end='')
        print("")
        print("choice\t\t:",end='')
        for i in range(p_l_len):
            if self.ym.players[i].board.score[13] == -1:
                print("\t-",end='')
            else:
                print("\t"+str(self.ym.players[i].board.score[13]),end='')
        print("")
        print("total\t\t:",end='')
        for i in range(p_l_len):
            print("\t"+str(sum(self.ym.players[i].board.score)+self.ym.players[i].board.score.count(-1)),end='')
        print("")

    
    def show_dices(self):
        pass
        #print(self.ym.dices)

    def ask_cmd(self)->str:
        while True:
            print("Submit or Roll again?(submit:s, roll:r):",end=' ')
            cmd:int = input()
            if cmd == 's' or cmd == 'r':
                break
        return cmd


    def ask_dice_keep(self)->list:
        keep_list = [False]*5
        flag:bool = False
        while True:
            print("Type in dice index to keep (ex. 1 3 5, none: enter):", end=' ')
            idx_list = input().split()
        
            # 아무것도 입력하지 않으면 기본값을 반환
            if not idx_list:
                return keep_list
        
            # 입력된 인덱스가 유효한지 검사
            valid_input = True
            for i in range(len(idx_list)):
                if 1 <= int(idx_list[i]) <= 5:
                    keep_list[int(idx_list[i]) - 1] = True
                else:
                    valid_input = False
                    break
        
            # 모든 입력이 유효하면 keep_list 반환
            if valid_input:
                return keep_list
            else:
                print("Invalid input. Please enter numbers between 1 and 5.")



    def ask_submit_idx(self,p_num:int,expt_s:list)->int:
        if 1 not in self.ym.players[p_num].history:
            print("1: aces("+str(expt_s[0])+")")
        if 2 not in self.ym.players[p_num].history:
            print("2: twos("+str(expt_s[1])+")")
        if 3 not in self.ym.players[p_num].history:
            print("3: threes("+str(expt_s[2])+")")
        if 4 not in self.ym.players[p_num].history:
            print("4: fours("+str(expt_s[3])+")")
        if 5 not in self.ym.players[p_num].history:
            print("5: fives("+str(expt_s[4])+")")
        if 6 not in self.ym.players[p_num].history:
            print("6: sixes("+str(expt_s[5])+")")
        if 7 not in self.ym.players[p_num].history:
            print("7: 3 of kind("+str(expt_s[6])+")")
        if 8 not in self.ym.players[p_num].history:
            print("8: 4 of kind("+str(expt_s[7])+")")
        if 9 not in self.ym.players[p_num].history:
            print("9: full house("+str(expt_s[8])+")")
        if 10 not in self.ym.players[p_num].history:
            print("10: small straight("+str(expt_s[9])+")")
        if 11 not in self.ym.players[p_num].history:
            print("11: large straight("+str(expt_s[10])+")")
        if 12 not in self.ym.players[p_num].history:
            print("12: yacht("+str(expt_s[11])+")")
        if 13 not in self.ym.players[p_num].history:
            print("13: choice("+str(expt_s[12])+")")
        while True:
            print("Type in submit index (1~13):",end=' ')
            idx:int = int(input())
            if 1<=idx and idx<=13 and (idx not in self.ym.players[p_num].history):
                break
        return idx

    def show_final_results(self, players):
        print("Game End! Final Score:")
        self.show_board()   # 최종 항목당 점수 보드 안보이게 하고 싶으면 여기를 주석처리 하세요!

        # 순위 정렬 후 출력
        players.sort(key=lambda x: sum(x.board.score), reverse=True)
        print("  rank  |  player name  |  total_score  ")
        print("=" * 36)
        for rank, player in enumerate(players, start=1):
            total_score = sum(player.board.score) + player.board.score.count(-1)
            print(f"   {rank}   |    {player.name}    |   {total_score}   ")

