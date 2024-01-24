from enum import Enum

class pair(Enum):
    SAME_ROW = 1
    SAME_COL = 2
    NEITHER = 3

def pair_type(matrix,x,y):
    xloc = 0
    yloc = 0

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == x:
                xloc = (i,j)
            elif matrix[i][j] == y:
                yloc = (i,j)
    
    if xloc[0] == yloc[0]:
        return pair.SAME_ROW
    elif xloc[1] == yloc[1]:
        return pair.SAME_COL
    else:
        return pair.NEITHER
    
def __fill_key(key):
    if len(key)>25:
        print("key too large")
        exit(-1)

    if len(key)==25:
        return key
    key = key.lower()
    
    print(key)
    ran = 25-len(key)
    curr_char=ord('a')
    for i in range(ran):
        while 1: 
            if(chr(curr_char) in key):
                if chr(curr_char) == 'i':
                    curr_char+=2
                
                else: curr_char+=1
            
            else: break
    
        key+=chr(curr_char)
    
    return key

def make_matrix(key):
    k = __fill_key(key)
    matrix = [[0]*5 for i in range(5)]
    ind = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = k[ind]
            ind+=1

    
    return matrix

def clean_plaintext(p):
    p = p.lower()
    for i in p:
        if not i.isalpha():
            p = p.replace(i,"")

    filler='x'
    res = []
    i = 0
    while i <len(p)-1:    
        if(p[i] == p[i+1]):
            res.append(p[i]+filler)
            i+=1
        else:
            res.append(p[i:i+2])
            i+=2
    return res

def getloc(matrix, c, pos):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                if pos=='x':
                    return i
                else:
                    return j

def encrypt_pair(matrix,par):
    
    if pair.SAME_ROW == pair_type(matrix, par[0],par[1]):
        return matrix[getloc(matrix,par[0],'x')][(getloc(matrix,par[0],'y')+1)%5] + matrix[getloc(matrix,par[1],'x')][(getloc(matrix,par[1],'y')+1)%5]      
    elif pair.SAME_COL == pair_type(matrix, par[0],par[1]):
        return matrix[(getloc(matrix,par[0],'x')+1)%5][getloc(matrix,par[0],'y')] + matrix[(getloc(matrix,par[1],'x')+1)%5][getloc(matrix,par[1],'y')] 
    else:
        par0x = getloc(matrix,par[0],'x')
        par0y = getloc(matrix,par[0],'y')
        par1x = getloc(matrix,par[1],'x')
        par1y = getloc(matrix,par[1],'y')
        return matrix[par0x][par1y] + matrix[par1x][par0y]

def encrypt(k,p):
    m = make_matrix(k)
    p = clean_plaintext(p)
    c = ""
    print(p)
    for i in m: 
        print(i)
    for x in p:
        c+= encrypt_pair(m,x)
    print(c.upper())
    
if __name__ == '__main__':
    p = "Must see you over Cadogan West. Coming at once."
    key = ""
    key = __fill_key(key)
    encrypt(key,p)