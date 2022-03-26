import math

def find_my_value(final_state,val):
    for i in range(len(final_state)):
        for j in range(len(final_state)):
            if val==final_state[i][j]:
                return ([i,j])

def eucledean(i,j,x,y):
    ans=math.sqrt((i-x)**2+(j-y)**2)
    return ans

def manhattan(i,j,x,y):
    ans=abs(i-x)+abs(j-y)
    return ans

def main():
    initial_state=[[2,0,3],[1,8,4],[7,6,5]]
    final_state=[[1,2,3],[8,0,4],[7,6,5]]
    ans1=0
    ans2=0
    for i in range(len(initial_state)):
        for j in range(len(initial_state)):
            if initial_state[i][j]==0:
                continue
            pos=find_my_value(final_state,initial_state[i][j])
            x=pos[0]
            y=pos[1]
            ans1+=eucledean(i,j,x,y)
            ans2+=manhattan(i,j,x,y)
    
    print('Eucledian distance is :',ans1)
    print('Manhattan distance is :',ans2)

if __name__ == '__main__':
    main()