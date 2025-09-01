'''
Created on May 26, 2023

Starter code for warm-up assignment
CSCI 384, Wheaton College (IL)
'''

def bigram_freq(text) :
     #just need to iterate through text and either make a new entry in dict
     #or inc when seen again
     #currently assuming len(text) > 1
     dict = {}
     for i in range(len(text) - 1 ):
          if(dict.get(text[i:i+2]) is None):
               dict[text[i:i+2]] = 1;
          else:
               dict[text[i:i+2]] += 1;
     
     return dict

# Use this to check if a character is a letter
alphacap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_cipher(plaintext, key):
    
    charList = list(plaintext) #strings are immutable 
    for i, ch in enumerate(charList):
        if ch in alphacap:
            index = alphacap.index(ch)     
            charList[i] = alphacap[(index + key) % 26]
    return ''.join(charList)

def crack_caesar(ciphertext):
     #need to go through and count occurences to find what E is 
     dict = {}
     max = None
     for ch in ciphertext:
          if ch in alphacap:
               if(dict.get(ch) is None):
                    dict[ch] = 1;
                    if max == None:
                         max = ch
               else:
                    dict[ch] += 1;
                    if dict[max] < dict[ch]:
                         max = ch
     #calculate shift
     shift = (alphacap.index(max) - alphacap.index('E')) % 26
     return caesar_cipher(ciphertext, -shift) #pretty sure I can just use old function

    
def vowel_path(board):
     # I can't believe I'm giving you this much starter code...
     n = len(board)
     m = len(board[0])
     best = [[None for j in range(m)] for i in range(n)]
     # add code here    
     vowels = 'aeiou'

     #get value
     def helper(ch):
        if ch in vowels:
            return 1
        elif ch == 'y':
            return 0.5
        else:
            return 0

     #set starting point
     best[0][0] = helper(board[0][0])

     #need to make exceptions for first row and column
     for j in range(1, m):
          best[0][j] = best[0][j-1] + helper(board[0][j])
     for i in range(1, n):
          best[i][0] = best[i-1][0] + helper(board[i][0])

     for i in range(1, n):
          for j in range(1, m):
               best[i][j] = helper(board[i][j]) + max(best[i-1][j], best[i][j-1])

     return best[n-1][m-1]
        
    


