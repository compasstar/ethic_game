# 4인 카드 게임
# 카드 뭉치는 두개 - 사상가 뭉치 / 주제(직업 자연관 죽음) 뭉치
# 사상가 뭉치에서 시작한다.

# 사상가 한 명당 4가지 색깔 (하나의 카드 뭉치에 공자만 4장, 주제도 같은 주제가 다른 색깔로 4장)


# 한장씩 뽑으면서 각자 자기 앞에 카드를 쌓아간다


# 같은 색이 나온다면 대답을 한다. 아니면 넘어간다.
# 대답하는 사람은 선착순 1명 (컴퓨터 상에서는 랜덤으로 처리)

# 심판을 한 명 두는데 판단기준은 랜덤이 되겠지 (랜덤 비율 9[o]:1[x])

# 대답을 제대로 하면 사상가/주제 총 두장을 가져온다. point+2

# 카드 뭉치가 전부 다 소모되면 END


# 사상가 이름 카드 8장 x 4 [공자 파랑 / 공자 초록 / 공자 핑크 / 공자 노랑]
# 주제 하나의 카드에 주제가 2개가 써있다. 주제는 4개. 카드 종류는 6개 x4 24장 [자연 직업 죽음 효] 4C2 x 4 = 24개


import random
import time


class ethic_game():

    def __init__(self):
        self.theorist = [['공자', '파랑'], ['공자', '초록'],['공자', '핑크'],['공자', '노랑'], ['맹자', '파랑'],['맹자', '초록'],['맹자', '핑크'],['맹자', '노랑'], ['순자', '파랑'],['순자', '초록'],['순자', '핑크'],['순자', '노랑'], ['주희', '파랑'],['주희', '초록'],['주희', '핑크'],['주희', '노랑'], ['이황', '파랑'],['이황', '초록'],['이황', '핑크'],['이황', '노랑'], ['이이', '파랑'],['이이', '초록'],['이이', '핑크'],['이이', '노랑'], ['왕수인', '파랑'],['왕수인', '초록'],['왕수인', '핑크'],['왕수인', '노랑'], ['정약용', '파랑'],['정약용', '초록'],['정약용', '핑크'],['정약용', '노랑']]

        self.subject = [['자연', '직업', '파랑'],['자연', '직업', '초록'],['자연', '직업', '핑크'],['자연', '직업', '노랑'], ['자연', '죽음', '파랑'],['자연', '죽음', '초록'],['자연', '죽음', '핑크'],['자연', '죽음', '노랑'], ['자연', '효', '파랑'],['자연', '효', '초록'],['자연', '효', '핑크'],['자연', '효', '노랑'], ['직업', '죽음', '파랑'],['직업', '죽음', '초록'],['직업', '죽음', '핑크'],['직업', '죽음', '노랑'], ['직업', '효', '파랑'],['직업', '효', '초록'],['직업', '효', '핑크'],['직업', '효', '노랑'], ['죽음', '효', '파랑'],['죽음', '효', '초록'],['죽음', '효', '핑크'],['죽음', '효', '노랑']]

        self.player = ['A','B','C','D']

        self.deck_A = []
        self.deck_B = []
        self.deck_C = []
        self.deck_D = []

        self.player_point = {'A':0, 'B':0, 'C':0, 'D':0}

        # 사상가, 주제 카드 셔플
        random.shuffle(self.theorist)
        random.shuffle(self.subject)

    # 전체 총괄 함수
    def game(self):

        self.turn_number = 1

        # 돌아가면서 turn을 진행한다
        # subject 가 전부 소모되면 게임 종료
        while (len(self.subject) > 0) and (self.turn_number <= 48):
            self.present_player = ((self.turn_number - 1) % 4 )+ 1
            print()

            print(self.turn_number, "번째 턴 \n플레이어 ", self.player[self.present_player-1])
            print()

            self.turn(self.present_player)

            self.question = input("\n다음 턴을 계속하시겠습니까? (y/n) ")
            print("------------------------------------------------------------\n")
            if self.question == 'n':
                break

            self.turn_number += 1

        print()
        print("플레이어 점수: ", self.player_point)

        time.sleep(5)

        print("\n게임 종료\n")
        return True
       
    # 카드가 같은 색인지 확인
    def is_same(self):
        if len(self.deck_A)>0 and len(self.deck_B)>0:
            if self.deck_A[-1][-1] == self.deck_B[-1][-1]:
                return 'A', 'B'

        if len(self.deck_A)>0 and len(self.deck_D)>0:
            if self.deck_A[-1][-1] == self.deck_D[-1][-1]:
                return 'A', 'D'

        if len(self.deck_B)>0 and len(self.deck_C)>0:
            if self.deck_B[-1][-1] == self.deck_C[-1][-1]:
                return 'B', 'C'

        if len(self.deck_C)>0 and len(self.deck_D)>0:
            if self.deck_C[-1][-1] == self.deck_D[-1][-1]:
                return 'C', 'D'
            
        return False
        
    # 대답한 질문이 맞았는지 확인 (90% 확률로 맞는다)
    def answer_right(self):
        self.answer = [0,1,2,3,4,5,6,7,8,9]
        random.shuffle(self.answer)
        if self.answer.pop()<9:
            print("정답입니다!")
            return True
        else:
            print("애석하게도 틀렸습니다!\n")
            return False


    def turn(self, present_player):

        # present_player 는 1 2 3 4
        # 1. 카드를 뽑는다.
        if present_player == 1 or present_player == 3:
            self.this_card = self.theorist.pop()
        else:
            self.this_card = self.subject.pop()

        print("뽑은 카드는 ", self.this_card)
        print()

        
        if present_player == 1:
            self.deck_A.append(self.this_card)
        elif present_player == 2:
            self.deck_B.append(self.this_card)
        elif present_player == 3:
            self.deck_C.append(self.this_card)
        elif present_player == 4:
            self.deck_D.append(self.this_card)
        else:
            print("에러")
            return False

        
        print("현재 각 플레이어의 최상단 카드")
        if len(self.deck_A)>0:
            print("A: ", self.deck_A[-1])
        
        if len(self.deck_B)>0:
            print("B: ", self.deck_B[-1])
        
        if len(self.deck_C)>0:
            print("C: ", self.deck_C[-1])
        
        if len(self.deck_D)>0:
            print("D: ", self.deck_D[-1])

        print()

        # 2. 같은 색이 있는 지 확인

        # 3-1. 만약 같은 색이라면 랜덤으로 4명 중에 한 명이 대답한다
        # 3-2. 맞게 대답했는지 90% 확률로 맞는다. 그러면 그 플레이어는 +1 point 틀리면 다시 랜덤으로 돌린다 (그 사람 제외)
        # 3-3. 맞추면 카드 두장 제거
        # 3-4. 만약 전부다 틀렸으면, point는 없다 return End

        # 3-4. 만일 카드를 제거 했는데 같은 색이 있는 지 다시 확인 해서 있다고 하면 3-1부터 다시 시작

        self.answer_player_okay = ['A','B','C','D']

        if self.is_same() != False:
            for i in range(4):
                
                random.shuffle(self.answer_player_okay)
                self.answer_player = self.answer_player_okay[0]
                print("정답을 외치는 플레이어: ", self.answer_player)
                input("정답은? ")

                if self.answer_right():
                    self.player_point[self.answer_player] += 1
                    break

                else:
                    self.answer_player_okay.remove(self.answer_player)
                    continue 

            if self.is_same() == ('A', 'B'):
                self.deck_A.pop()
                self.deck_B.pop()

            elif self.is_same() == ('A', 'C'):
                self.deck_A.pop()
                self.deck_C.pop()

            elif self.is_same() == ('A', 'D'):
                self.deck_A.pop()
                self.deck_D.pop()

            elif self.is_same() == ('B', 'C'):
                self.deck_B.pop()
                self.deck_C.pop()

            elif self.is_same() == ('B', 'D'):
                self.deck_B.pop()
                self.deck_D.pop()

            elif self.is_same() == ('C', 'D'):
                self.deck_C.pop()
                self.deck_D.pop()    
                
                 

        
        # 같은 색이 없을 시 턴을 종료한다
        else:
            print("사상가와 주제 간에 같은 색이 없으므로 턴을 종료합니다\n")
            return True


    
ethic_game = ethic_game()


ethic_game.game()
