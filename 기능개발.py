def solution(progresses, speeds):
    pointer = 0
    answer = []
    
    #하루 * 100
    for i in range(100):
    
    #하루의 순환
   #progresses 처음부터 끝까지 순환 
        for a, i in enumerate(progresses):
         #만약 100보다 크면 pass
            if progresses[a] >= 100:
               pass
        #100보다 작으면 스피드 더해준다
            else:
             progresses[a] = progresses[a] + speeds[a]
        #그렇게 포인터가 100이상이되는 날 저녁이면
        if progresses[pointer] >= 100:
            if min(progresses) >= 100:
                    answer.append(len(progresses) - pointer)
            else:
            #다음 포인터를 찾는다
             for i in range(pointer+1, len(progresses)):
                if progresses[i] < 100:
                    temp = pointer
                    pointer = i
                    answer.append(pointer - temp)
                    break    
        if min(progresses) >= 100: break

    return answer