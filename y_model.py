class Board:
    score:list  #0:bonus, 1:aces, ... 6:sixes, 7:choice, 8:4_kind, 9:f_house, 10:ss, 11:ls, 12:yacht

    def __init__(self):
        self.score = [-1]*14
        

class Player:
    def __init__(self, name: str, is_ai: bool = False, ai_type : str = "greedy"):
        self.name = name
        self.is_ai = is_ai  # AI 여부를 나타내는 속성 추가
        self.ai_type = ai_type  # AI type
        self.history = []
        self.board = Board()

class Ymodel:
    players: list
    dices: list
    
    def __init__(self):
        self.players = []
        self.dices = []
        p_len: int = 3  # 플레이어 수
        
        # 플레이어 리스트 초기화 (AI 플레이어 포함)
        # 플레이어 리스트 초기화 (모두 AI 플레이어로 설정)
        for i in range(p_len):
            if i == 0:
                # 첫 번째 플레이어는 일반 플레이어
                self.players.append(Player(name="Greedy AI", is_ai=True, ai_type="greedy"))
            elif i == 1:
                # 두 번째 플레이어는 AI 플레이어
                self.players.append(Player(name="HighNum AI", is_ai=True, ai_type="strategic"))
            elif i == 2:
                self.players.append(Player(name="Yacht AI", is_ai=True, ai_type="yacht"))
            else:
                self.players.append(Player(name="Human Player", is_ai=False))
        

        # 주사위 초기화 (5개의 주사위)
        for i in range(5):
            self.dices.append(0)
