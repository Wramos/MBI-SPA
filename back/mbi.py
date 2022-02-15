import random
import re

class mbi:

    #Arrays used to generate the MBI ID
    typeC = ['1','2','3','4','5','6','7','8','9']
    typeN = ['0','1','2','3','4','5','6','7','8','9']
    typeA = ['A','C','D','E','F','G','H','J','K','M','N','P','Q','R','T','U','V','X','Y']
    typeAN = ['0','1','2','3','4','5','6','7','8','9','A','C','D','E','F','G','H','J','K','M','N','P','Q','R','T','U','V','X','Y']

    def __init__(self) -> None:
        pass
        
    #Verify whether an MBI ID matches a regex
    def verify(self, verifyMBI):
        #This step covers some edge cases but might not be necessary
        if len(verifyMBI) != 11:
            return "This does not match MBI format"
        if re.match(r'\b[1-9][AC-HJKMNP-RT-Yac-hjkmnp-rt-y][AC-HJKMNP-RT-Yac-hjkmnp-rt-y0-9][0-9]-?[AC-HJKMNP-RT-Yac-hjkmnp-rt-y][AC-HJKMNP-RT-Yac-hjkmnp-rt-y0-9][0-9]-?[AC-HJKMNP-RT-Yac-hjkmnp-rt-y]{2}\d{2}\b', \
            verifyMBI):
            return "This matches MBI format"
        else:
            return "This does not match MBI format"

    #Generate an MBI ID to match the MBI Format
    def generate(self):
        generatedMbi = ''.join(map(str,[\
            random.choice(self.typeC), \
            random.choice(self.typeA), \
            random.choice(self.typeAN), \
            random.choice(self.typeN), \
            random.choice(self.typeA), \
            random.choice(self.typeAN), \
            random.choice(self.typeN), \
            random.choice(self.typeA), \
            random.choice(self.typeA), \
            random.choice(self.typeN), \
            random.choice(self.typeN)]))
        return generatedMbi