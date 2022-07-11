import random

# 山札
deck = []
# 自分の手札
mydeck = []
# ディーラーの手札
dealer = []
# 山札の数字が被らないように要素数をカウント
elementCount = []
# 勝負結果
match_result = ""
# 自分の手持ちチップ
chip = 100
# 賭けられたチップ数
throwChip = ""

# ゲーム進行
def maingame():
    print("--------------------------------------------------------------------------------------------------------------")
    print("人生をかけたブラックジャック会場へようこそ")
    while chip > 0:
        print("--------------------------------------------------------------------------------------------------------------")
        print("あなたが賭けたいチップの数を入力してください")
        print("所持チップ数：" + str(chip))
        jadgement()
        print("賭けたチップ：" + str(throwChip) + "枚")
        print("それではカードを配布します")
        input()
        deckIni()
        deckDes()
        print("ディーラー：", end="")
        print(dealer)
        print("自分：", end="")
        print(mydeck)
        call(mydeck)
        callDealer(dealer)
        print("結果を発表します")
        input()
        result()
        chipCal(throwChip)
        if chip < 0:
            print("あなたのチップがなくなったため、ゲームを終了します")

# デッキを初期化
def deckIni():
    global deck
    global elementCount
    deck = []
    elementCount = []

    for count in range(4):
        for num in range(1, 11):
            if num == 10:
                for i in range(4):
                    deck.append(num)
            else:
                deck.append(num)

# デッキからカードを初期配布
def deckDes():
    global dealer
    global mydeck
    dealer = []
    mydeck = []

    dealer.append(deck[rand_int()])
    dealer.append(deck[rand_int()])
    mydeck.append(deck[rand_int()])
    mydeck.append(deck[rand_int()])

# 山札からカードを一枚ひく
def deckDraw(person):
    person.append(deck[rand_int()])

# 勝負結果から手持ちチップを計算する
def chipCal(throwChip):
    global chip
    if match_result == "Win":
        chip += int(throwChip)
    elif match_result == "Lose":
        chip -= int(throwChip)
    
    print("あなたのチップは" + str(chip) + "になりました")

# 結果を計算してmatch_resultに結果を格納
def result():
    global match_result

    if sum(mydeck) < 22 and sum(dealer) < 22:
        deal = 21 - sum(dealer)
        my = 21 - sum(mydeck)
        if deal > my:
            print("あなたの勝ちです")
            match_result = "Win"
        elif deal < my:
            print("あなたの負けです")
            match_result = "Lose"
        else:
            print("引き分けです")
            match_result = "Drow"
    elif sum(mydeck) < 22 and sum(dealer) >= 22:
        print("あなたの勝ちです")
        match_result = "Win"
    elif sum(mydeck) >= 22 and sum(dealer) < 22:
        print("あなたの負けです")
        match_result = "Lose"
    else:
        print("引き分けです")
        match_result = "Drow"

# 1～52の要素をランダムに返す
def rand_int():
    global elementCount

    while True:
        rand = random.randint(0, 51)
        if not rand in elementCount:
            elementCount.append(rand)
            break

    return rand

# hit or stand を受け取って処理する
def call(person):
    while True:
        if sum(mydeck) < 22:
            print("あなたの番です")
            print(mydeck)
            print("hitかstandを選択してください")
            status = input()

            if status == "hit":
                deckDraw(person)
                print("一枚カードをひきました")
            elif status == "stand":
                break
            else:
                print("「hit」もしくは「stand」を入力してください")
        elif sum(mydeck) >= 22:
            print(mydeck)
            print("あなたのカード合計が21を超えました")
            break

# ディーラーの手札を自動でドロー
def callDealer(person):
    print("ディーラーの番です")
    input()
    while True:
        if sum(dealer) < 16:
            deckDraw(person)
            print("ディーラーは一枚カードをひきました")
            print(dealer)
        elif sum(dealer) >= 16:
            print("ディーラーはstandを選択しました")
            break

# 記入されたチップの判定
def jadgement():
    global throwChip
    throwChip = ""

    while not throwChip.isdigit():
        print("数字を入力してください")
        throwChip = input()
    while int(throwChip) > chip:
        print("所持しているチップ範囲内で選択してください")
        print("所持チップ数：" + str(chip))
        throwChip = input()

maingame()