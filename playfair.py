
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
            matrix[i][j] = ord(k[ind])-ord('a')
            ind+=1
    for i in matrix:
        print(i)

def clean_plaintext(p):
    p = p.lower()
    for i in p:
        if not i.isalpha():
            p = p.replace(i,"")
    print(p)

    filler='x'
    res = []
    
    for i in range(0,len(p)-1,2):
        res.append(p[i:i+2])
    print(res)


    print(res)
    return p



def encrypt(matrix,k,p):
    m = make_matrix(k)
    p = clean_plaintext(p)
    c = ""

    for i in range(5):
        for j in range(5):
            
            
    

if __name__ == '__main__':

    p = "Must see you over Cadogan West. Coming at once."
    matrix_key = "MONARCHY"
    f = __fill_key(matrix_key)
    print(f)
    clean_plaintext(p)
    make_matrix(matrix_key)