class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # converting strings to sorted char arrays
        sArray= sorted(list(s)); 
        tArray= sorted(list(t)); 
        lenght= len(sArray); 

        #checking for same lenght 
        if (lenght != len(tArray)):
            return False; 

        #checking for different characters
        for i in range (lenght):
            if sArray[i] != tArray[i]:
                return False; 

        return True;         


