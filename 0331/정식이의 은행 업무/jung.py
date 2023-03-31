import sys
sys.stdin = open('1.txt')

def e(e_zin, s_zin):
    for i in range(e_l):
        if e_zin[i] == '1':
            e_zin[i] = '0'
            s(e_zin, s_zin)
            e_zin[i] = '1'
        else:
            e_zin[i] = '1'
            s(e_zin, s_zin)
            e_zin[i] = '0'
            
def s(e_zin, s_zin):
    print(e_zin, s_zin)
    # for j in range(s_l):
    #     s_zin[j] = 0
    #     print(e_zin, s_zin)
    #     s_zin[j] = 1
    #     print(e_zin, s_zin)
    #     s_zin[j] = 2
        
            
            
            
        


'''
    for i in range(e_l):
        if e_zin[i] == 1:
            e_zin[i] == 0
            s()
        else:
            e_zin[i] == 1
            s() 
def s():
    for i in range(e_l):
'''


T = int(input())
for tc in range(1, T+1):
    e_zin = list(input())
    s_zin = list(input())
    e_l = len(e_zin)
    s_l = len(s_zin)
    print(e_l)
    print(s_l)
    e(e_zin, s_zin)
