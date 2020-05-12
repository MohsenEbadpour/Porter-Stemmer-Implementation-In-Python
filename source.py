class Porter:
    def VC_Equivalent(self, word: str):
        word = word.lower()
        vc = ""
        for letter in word:
            if letter in "aeiouy":
                vc += "V"
            else:
                vc += "C"
        return vc

    def Measure(self, word: str):
        word = word.lower()
        vc = self.VC_Equivalent(word)
        return vc.count("VC")

    def Contain_Vowel_Checker(self, word: str):
        word = word.lower()
        word_vc = self.VC_Equivalent(word)
        if "V" in word_vc:
            if word_vc.find("V") == word_vc.rfind("V") == (len(word_vc)-1):
                return False
            return True
        else:
            return False


    def Contain_Double_Consonant_Checker(self, word: str):
        word = word.lower()
        if self.VC_Equivalent(word).endswith("CC"):
            if word[-1] == word[-2]:
                return True
        return False

    def Star_O_Checker(self, word: str):
        word = word.lower()
        if self.VC_Equivalent(word).endswith("CVC"):
            if not(word[-1] in "wxy"):
                return True
        return False

    def Step_1A(self, word: str):
        word = word.lower()

        if word.endswith("sses"):
           word = word[:len(word)-2]

        elif word.endswith("ies"):
            word = word[:len(word)-2]

        elif word.endswith("ss"):
            word = word

        elif word.endswith("s"):
            word = word[:len(word)-1]

        return word

    def Step_1B_Cleaner(self, word: str):
        word = word.lower()
        if word.endswith("at"):
            word = word + "e"

        elif word.endswith("bl"):
            word = word + "e"

        elif (self.Contain_Double_Consonant_Checker(word) and not((word.endswith("l")or(word.endswith("s")or(word.endswith("z")))))):
            word = word[:len(word)-1]

        elif self.Measure(word) == 1 and self.Star_O_Checker(word):
            word = word + "e"

        return word


    def Step_1B(self, word: str):
        word = word.lower()
        need_to_clean = False

        if self.Measure(word) > 1:
            if word.endswith("eed"):
               word = word[:len(word)-1]

            elif self.Contain_Vowel_Checker(word):
                if word.endswith("ed"):
                    word = word[:len(word)-2]
                    need_to_clean = True

                elif word.endswith("ing"):
                    word = word[:len(word)-3]
                    need_to_clean = True

        if need_to_clean:
            word = self.Step_1B_Cleaner(word)
        return word

    def Step_1C(self, word: str):
        word = word.lower()
        if self.Contain_Vowel_Checker(word):
            if word.endswith("y"):
                word = word[:len(word)-1]
                word = word + "i"
        return word

    def Step_2(self, word: str):
        word = word.lower()
        
        if self.Measure(word) > 0:
            if word.endswith("ational"):
                    word = word[:len(word)-5]
                    word = word + "e"
            
            elif word.endswith("tional"): #Try to Solve Error
                    word = word[:len(word)-2]

            elif word.endswith("enci"): #Try to Solve Error
                    word = word[:len(word)-1]
                    word = word + "e"

            elif word.endswith("anci"): #Try to Solve Error
                    word = word[:len(word)-1]
                    word = word + "e"

            elif word.endswith("izer"): #Try to Solve Error
                    word = word[:len(word)-1]

            elif word.endswith("abli"): #Try to Solve Error
                    word = word[:len(word)-1]
                    word = word + "e"
            
            elif word.endswith("alli"): #Try to Solve Error
                    word = word[:len(word)-2]
            
            elif word.endswith("entli"): #Try to Solve Error
                    word = word[:len(word)-2]
            
            elif word.endswith("eli"): #Try to Solve Error
                    word = word[:len(word)-2]

            elif word.endswith("ousli"): #Try to Solve Error
                    word = word[:len(word)-2]

            elif word.endswith("ization"):
                    word = word[:len(word)-5]
                    word = word + "e"

            elif word.endswith("ation"): #Try to Solve Error
                    word = word[:len(word)-3]
                    word = word + "e"

            elif word.endswith("ator"): #Try to Solve Error
                    word = word[:len(word)-2]
                    word = word + "e"
            
            elif word.endswith("alism"): #Try to Solve Error
                    word = word[:len(word)-3]
            
            elif word.endswith("iveness"): #Try to Solve Error
                    word = word[:len(word)-4]

            elif word.endswith("fulness"): #Try to Solve Error
                    word = word[:len(word)-4]

            elif word.endswith("ousness"): #Try to Solve Error
                    word = word[:len(word)-4]

            elif word.endswith("aliti"): #Try to Solve Error
                    word = word[:len(word)-3]

            elif word.endswith("iviti"): #Try to Solve Error
                    word = word[:len(word)-3]
                    word = word + "e"

            elif word.endswith("biliti"):
                    word = word[:len(word)-5]
                    word = word + "le"

        return word
    
    def Step_3(self, word: str):
        word = word.lower()

        if self.Measure(word) > 0:
            if word.endswith("icate"):
                    word = word[:len(word)-3]
            
            elif word.endswith("ative"): #Try to Solve Error
                    word = word[:len(word)-5]
            
            elif word.endswith("alize"): #Try to Solve Error
                    word = word[:len(word)-3]
            
            elif word.endswith("iciti"): #Try to Solve Error
                    word = word[:len(word)-3]
            
            elif word.endswith("ical"): #Try to Solve Error
                    word = word[:len(word)-2]

            elif word.endswith("ful"):
                    word = word[:len(word)-3]

            elif word.endswith("ness"):
                    word = word[:len(word)-4]
        
        return word

    def Step_4(self, word: str):
        word = word.lower()

        if self.Measure(word) > 1: # Try to Solve Error
            if word.endswith("al"):
                    word = word[:len(word)-2]

            elif word.endswith("ance"):
                    word = word[:len(word)-4]
            
            elif word.endswith("ence"):# Try to Solve Error
                    word = word[:len(word)-4]

            elif word.endswith("er"):# Try to Solve Error
                    word = word[:len(word)-2]

            elif word.endswith("ic"):# Try to Solve Error
                    word = word[:len(word)-2]
            
            elif word.endswith("able"):# Try to Solve Error
                    word = word[:len(word)-4]
            
            elif word.endswith("ible"):# Try to Solve Error
                    word = word[:len(word)-4]

            elif word.endswith("ant"):# Try to Solve Error
                    word = word[:len(word)-3]
            
            elif word.endswith("ement"):# Try to Solve Error
                    word = word[:len(word)-5]
            
            elif word.endswith("ment"):# Try to Solve Error
                    word = word[:len(word)-4]

            elif word.endswith("ent"):
                    word = word[:len(word)-3]

            elif word.endswith("sion") or word.endswith("tion"):# Try to Solve Error
                    word = word[:len(word)-3]

            elif word.endswith("ou"):# Try to Solve Error
                    word = word[:len(word)-2]
            
            elif word.endswith("ism"):# Try to Solve Error
                    word = word[:len(word)-3]

            elif word.endswith("ate"):# Try to Solve Error
                    word = word[:len(word)-3]

            elif word.endswith("iti"):# Try to Solve Error
                    word = word[:len(word)-3]

            elif word.endswith("ous"):# Try to Solve Error
                    word = word[:len(word)-3]

            elif word.endswith("ive"):
                    word = word[:len(word)-3]

            elif word.endswith("ize"):# Try to Solve Error
                    word = word[:len(word)-3]
        
        return word

    def Step_5A(self, word: str):
        word = word.lower()

        if self.Measure(word) > 1:
            if word.endswith("e"):
                    word = word[:len(word)-1]
            elif ((self.Measure(word))and(not(self.Star_O_Checker(word)))) ==1 and word.endswith("ness") :
                word = word[:len(word)-4]

        return word

    def Step_5B(self, word: str):
        word = word.lower()
        if self.Measure(word) > 1 and self.Contain_Double_Consonant_Checker(word) and word.endswith("l"): 
            word = word[:len(word)-1]
        return word


    def Execute(self,word:str):
        if not word.isalpha():
            raise ValueError("Letters of Entered Word Is Not Alphabet")
        word = word.lower()
        word = self.Step_1A(word)

        word = self.Step_1B(word)

        word = self.Step_1B_Cleaner(word)

        word = self.Step_1C(word)

        word = self.Step_2(word)

        word = self.Step_3(word)

        word = self.Step_4(word)

        word = self.Step_5A(word)

        word = self.Step_5B(word)


        return word

if __name__ == "__main__":
    print("\n[*] Porter Algorithm Implementation")
    
    from nltk.stem import PorterStemmer
    from nltk.tokenize import sent_tokenize, word_tokenize
    ps = PorterStemmer()

    porter = Porter()
    words = list(open("input_long_text.txt","r").read().split())
    all_word = 0
    eq = 0 
    le = 0
    gr = 0
    err = 0
    for word in words : 
        if not(word.isalpha()):
            continue
        all_word+=1
        w1 = str(porter.Execute(word))
        w2 = str(ps.stem((word.lower())))
        if w1 == w2 :
            eq+=1
        elif len(w1)<len(w2):
            le+=1
        elif len(w1)>len(w2):
            gr+=1
        else: 
            err+=1

    print("All Words:",all_word)
    print("Exact Stemming Accuracy:",(round((eq/all_word)*100,2)),"%")


