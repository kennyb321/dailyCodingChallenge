
#Daily Coding Challenge
#7/20/21

'''
This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
'''




def reverseString(string):
    newString = ''
    length = len(string)
    for i in range(length-1, -1, -1):
        newString = newString + str(string[i])
    return newString
    


def isEven(word):
    if (len(word) % 2) == 0:
        return True
    else:
        return False

def isPalindrome(word):
    length = len(word)
    #if word is only one letter, its a palindrome
    if len(word) == 1:
        return True
    
    #special case for 3 letter word. Easy to solve.
    if length == 3:
        if word[0] == word[2]:
            return True
    #if word is even, cut the word in half and test if the first
    #half is equal to the reverse of the second half
    if isEven(word):
        length = len(word)
        halfLength = length / 2 
        w1 = word[:int(halfLength)]
        w2 = word[int(halfLength):]
        w2 = reverseString(w2)
        if w1 == w2:
            return True
        else:
            return False
        
        
    else:
        #if word is odd, we remove the middle letter,
        #then apply the same method as for even words
        middleIndex = int(length//2)
        middleLetter = word[middleIndex]
        w1 = word[:middleIndex]
        w2 = word[middleIndex+1:]
        if w1 == reverseString(w2):
            
            return True
        else:
            return False
        
        
def test(word1, word2):
        
    if isPalindrome(word1 + word2):
        return True
    
def returnIndeceList(list):
        indeces = []
        length = len(list)
        for i in range(length-1):
            for j in range(length-1, 0, -1):
                
                #cannot test a word against itself
                if i==j:
                    continue
                
                elif test(list[i], list[j]):
                    indeces.append((i, j))
        
        return indeces
            
                 
                
def main():
    list1 = ['da', 'd', 'han', 'nah', 'ba', 'abb']
    list2 = ["code", "edoc", "da", "d"]
    list3 = ['att', 'tta', 'ahgf', 'ffgha', 'thy', 'klk', 'tyu', 'lll', 'uhgt', 'uyt']
    
    
    print('List 1: ' + str(list1))
    print('List2: ' + str(list2))
    print('List3: ' + str(list3))
    
    indeces1 = returnIndeceList(list1)
    indeces2 = returnIndeceList(list2)
    indeces3 = returnIndeceList(list3)
    
    print('Indeces1: ' + str(indeces1))
    print('Indeces2: ' + str(indeces2))
    print('Indeces3: ' + str(indeces3))
    

if __name__ == '__main__':
    main()
    
    

    
    
   
    

    
   

                        