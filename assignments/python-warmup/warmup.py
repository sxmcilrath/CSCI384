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
     j = 1;
     for i in range(len(text) - 1 ):
          if(dict.get(text[i:i+2]) is None):
               dict[text[i:i+2]] = 1;
          else:
               dict[text[i:i+2]] += 1;
     
     return dict

# Use this to check if a character is a letter
alphacap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_cipher(plaintext, key):
     pass

def crack_caesar(ciphertext):
     pass

 
    
    
def vowel_path(board):
    # I can't believe I'm giving you this much starter code...
    n = len(board)
    m = len(board[0])
    best = [[None for j in range(m)] for i in range(n)]

    # add code here    

    return best[n-1][m-1]
        
    


