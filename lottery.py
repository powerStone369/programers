def solution(lottos, win_nums):
    temp=[]
    for i in lottos:
        for j in win_nums:
            if i == j:
                temp.append(i)

    zero=0
    for i in lottos:
        if i==0:
            zero+=1
    
    win = len(temp) + zero
    answerWin = 0
    if win <= 1:
        answerWin = 6
    else :
        answerWin = 7 - win
    
    
    
    lose = len(temp)
    answerLose = 0
    
    if lose <= 1:
        answerLose = 6
    else :
        answerLose = 7 - lose
    
    answer = [answerWin, answerLose]
    return answer