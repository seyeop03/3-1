import random

class Character:

  def __init__(self, speed):
    self.speed = speed


class Item:

  def __init__(self, item_type, speed_change):
    self.item_type = item_type
    self.speed_change = speed_change


class Player:

  def __init__(self, name):
    self.name = name # 플레이어의 이름 저장
    self.speed = 0 # 플레이어의 속도: 선택한 character의 속도!
    self.round_speed = 0 # 아이템 적용 후 플레이어의 속도
    self.play_records = [] # 플레이어의 경기 기록: 라운드별 주행 시간[초]


  def add_play_record(self, record_in_hr):
    """
    - 플레이어의 경기 기록을 받아 저장합니다.
    - 시간 단위로 들어온 기록을 초 단위의 기록으로 변환해 저장합니다.
    - Game 클래스의 play_round() 함수에서 호출됩니다. 
    """
    # TODO : 플레이어의 경기 기록을 초 단위로 변환해 저장
    record_in_sec = 3600*record_in_hr
    self.play_records.append(3600*record_in_hr)
    return 3600*record_in_hr
       
    
class Game:

  def __init__(self):
    self.num_rounds = 3
    self.player_list = []
    self.item_list = []
    self.character_list = [] # 사용 X


  def set_players(self):
    """
    - 5명의 플레이어를 생성하는 함수입니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    """
    print("******************* 게임 접속 *******************")

    for i in range(5):            
        if i == 0:
            self.player_list.append(input("Player {}의 이름을 입력해주세요: ".format(i+1)))
            globals()['player{}'.format(i+1)] = Player(self.player_list[i])
        else:
            while True:
                auth=1
                tmp_name = input("Player {}의 이름을 입력해주세요: ".format(i+1))
                for j in range(i):
                    if tmp_name==self.player_list[j]:
                        print("이미 사용중인 이름입니다. 다른 이름을 사용해주세요\n")
                        auth=0
                        break            
                if auth==1:
                    self.player_list.append(tmp_name)
                    globals()['player{}'.format(i+1)] = Player(self.player_list[i])
                    break
    # TODO : 사용자로부터 플레이어의 이름을 입력받아 Player 객체를 생성하고 플레이어 목록(self.player_list)에 추가



  def start_game(self):
    """
    - 게임 규칙의 [게임 시작 전] 부분을 담당하는 함수입니다. 
    - 3 종류의 캐릭터와 2 종류의 아이템을 초기화하고, 사용자의 입력을 받아 각 플레이어의 속도를 설정합니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    """

    # TODO (1): 범위 내의 속도를 가진 세 종류의 캐릭터를 생성
    print("\n******************* 캐릭터 선택 *******************")
    while True:
        character1 = Character(random.randint(100,180))   ## 각각의 종류는 다른 캐릭터를 가져야 함.
        character2 = Character(random.randint(100,180))   
        character3 = Character(random.randint(100,180))
        if (character1.speed==character2.speed or
            character2.speed==character3.speed or
            character3.speed==character1.speed):
            continue
        else:
            break

    # TODO (2): 사용자의 입력을 받아 플레이어의 고유 속도를 설정하고, 선택된 캐릭터의 속도를 출력
    for i in range(5):        
        while True:
            v=input(globals()['player{}'.format(i+1)].name+"의 캐릭터 선택 차례입니다. 1,2,3 중 하나의 값을 입력해주세요.")
        
            if v=='1':
                globals()['player{}'.format(i+1)].speed = character1.speed
                print(globals()['player{}'.format(i+1)].name,"의 고유속도는 시속",character1.speed,"입니다.")
                break
            elif v=='2':
                globals()['player{}'.format(i+1)].speed = character2.speed
                print(globals()['player{}'.format(i+1)].name,"의 고유속도는 시속",character2.speed,"입니다.")
                break
            elif v=='3':
                globals()['player{}'.format(i+1)].speed = character3.speed
                print(globals()['player{}'.format(i+1)].name,"의 고유속도는 시속",character3.speed,"입니다.")
                break
            else:
                print("반드시 1,2,3 중 하나의 값만 입력해주세요 !")
                continue
    
    # TODO (3): 두 종류의 아이템을 생성해 아이템 목록(self.item_list)에 추가
   
    globals()['item{}'.format(1)]= Item("booster", random.randint(30,60))
    globals()['item{}'.format(2)]= Item("banana_slip", -random.randint(20,40))
    self.item_list.append(item1.item_type)
    self.item_list.append(item2.item_type)

  def play_round(self):
    """
    - 게임 규칙의 [라운드 시작 전], [라운드 진행], [라운드 종료 후] 부분을 담당하는 함수입니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    """

    #### [라운드 시작 전]
    # TODO (1) - 1: 트랙의 길이를 결정해 변수에 저장하고, 출력
    track_len = random.randint(5,30)
    print("이번 라운드의 트랙 길이는 ",track_len," km 입니다\n")

    # TODO (1) - 2: 5명의 플레이어에게 아이템을 랜덤하게 적용시키고, 적용된 아이템과 적용 후 플레이어의 속도를 출력
    for i in range(5):
        tmp_item = random.choice(self.item_list)
        if (tmp_item == item1.item_type):   
            globals()['player{}'.format(i+1)].round_speed = globals()['player{}'.format(i+1)].speed + item1.speed_change
            print("Player ",globals()['player{}'.format(i+1)].name,"는 ",item1.item_type," 덕분에 ",
                  "시속",globals()['player{}'.format(i+1)].round_speed," 로 이번 트랙을 질주합니다! 화이팅~~")
        elif tmp_item == item2.item_type:           
            globals()['player{}'.format(i+1)].round_speed = globals()['player{}'.format(i+1)].speed + item2.speed_change
            print("Player ",globals()['player{}'.format(i+1)].name,"는 ",item2.item_type," 때문에 ",
                  "시속 ",globals()['player{}'.format(i+1)].round_speed," 로 이번 트랙을 질주합니다! 화이팅ㅠㅠ")        

         #### [라운드 진행] , [라운드 종료 후]
    # TODO (2) : 플레이어가 트랙을 도는 데 걸린 시간을 초 단위로 출력하고,
    # 플레이어의 경기 기록에 추가. Player 클래스의 함수를 사용
    print("[경기 진행중...]")
    print("[라운드 결과]")
    for i in range(5):
        tmp_rec = globals()['player{}'.format(i+1)].add_play_record(track_len/globals()['player{}'.format(i+1)].round_speed)
        print(globals()['player{}'.format(i+1)].name,"의 주행 시간: ",tmp_rec)
        

    
  def game_result(self):
    """
    - 게임 규칙의 [게임 종료 후] 부분을 담당하는 함수입니다. 
    - 1, 2, 3순위까지 플레이어의 이름과 합산기록을 출력합니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    - 파이썬의 sorted() 함수와 sort() 함수사용
    """
    # TODO : 사용자를 합산 기록 순으로 정렬하고, 상위 3명의 경기 기록 합산을 출력합니다.
    record_dic = {}
    rank = 1
    for i in range(5):
        record_dic[globals()['player{}'.format(i+1)].name] =globals()['player{}'.format(i+1)].play_records[0]+globals()['player{}'.format(i+1)].play_records[1]+globals()['player{}'.format(i+1)].play_records[2]       
    dic_sorted = sorted(record_dic.items(), reverse=False, key=lambda x: x[1])
    for key, value in dic_sorted:
        print('{}위:'.format(rank),key,"(총 주행 시간: {}초)".format(value))
        rank+=1
        if rank==4:
            break

  def game(self):
    """
    - 게임 운영을 위한 함수입니다. 
    """
    self.set_players()
    self.start_game()

    print("\n******************* 게임 시작 *******************")
    for i in range(3):
      print(f"============= ROUND {i+1} =============")
      self.play_round()
      print()
    print()

    print("******************* 명예의 전당 *******************")
    self.game_result()
    



if __name__ == '__main__':
  """
    - 코드를 실행하는 부분입니다. 
    - 역시 별도의 코드 작성이 필요 X
    """
  game = Game()
  game.game()

