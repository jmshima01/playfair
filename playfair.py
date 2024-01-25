from enum import Enum
from sys import argv

class pair(Enum):
    SAME_ROW = 1
    SAME_COL = 2
    NEITHER = 3

class Playfair():
    def __init__(self,key,plaintext):
        self.plaintext = self.__clean_plaintext(plaintext)
        self.k = self.__fill_key(key)
        self.m = self.__make_matrix()
    
    def __pair_type(self,x,y):
        xloc = 0
        yloc = 0
        for i in range(5):
            for j in range(5):
                if self.m[i][j] == x:
                    xloc = (i,j)
                elif self.m[i][j] == y:
                    yloc = (i,j)
        
        if xloc[0] == yloc[0]:
            return pair.SAME_ROW
        elif xloc[1] == yloc[1]:
            return pair.SAME_COL
        else:
            return pair.NEITHER
        
    def __fill_key(self,key):
        key = key.lower()
        if len(key)>25:
            print("err: key too large")
            exit(-1)

        if len(key)==25:
            return key
        
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

    def __make_matrix(self):
        matrix = [[0]*5 for i in range(5)]
        ind = 0
        for i in range(5):
            for j in range(5):
                matrix[i][j] = self.k[ind]
                ind+=1
        return matrix

    def __clean_plaintext(self,p):
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

    def __getloc(self, c, pos):
        for i in range(5):
            for j in range(5):
                if self.m[i][j] == c:
                    if pos=='x':
                        return i
                    else:
                        return j

    def __encrypt_pair(self, par):
        
        if pair.SAME_ROW == self.__pair_type(par[0],par[1]):
            return self.m[self.__getloc(par[0],'x')][(self.__getloc(par[0],'y')+1)%5] + self.m[self.__getloc(par[1],'x')][(self.__getloc(par[1],'y')+1)%5]      
        elif pair.SAME_COL == self.__pair_type(par[0],par[1]):
            return self.m[(self.__getloc(par[0],'x')+1)%5][self.__getloc(par[0],'y')] + self.m[(self.__getloc(par[1],'x')+1)%5][self.__getloc(par[1],'y')] 
        else: # NEITHER
            par0x = self.__getloc(par[0],'x')
            par0y = self.__getloc(par[0],'y')
            par1x = self.__getloc(par[1],'x')
            par1y = self.__getloc(par[1],'y')
            return self.m[par0x][par1y] + self.m[par1x][par0y]

    def encrypt(self):
        m = self.m
        p = self.plaintext
        c = ""
        print(p)
        for i in m: 
            print(i)
        for x in p:
            c+= self.__encrypt_pair(x)
        print(c.upper())
    
if __name__ == '__main__':
    # p = "Must see you over Cadogan West. Coming at once."
    # key = "MFHIKUNOPQZVWXYELARGDSTBC"

    if len(argv) != 3:
        print("usage: python3 playfair.py key_str plain_text")
        exit(-1)
    
    playfair = Playfair(argv[1],argv[2])
    
    playfair.encrypt()

