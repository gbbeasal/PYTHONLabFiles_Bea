s = 'This dinner is not that bad!'

if (("bad" in s) and ("not" in s)):
    #takes out punctuation
    tab = s.maketrans("!", " ")
    no_punc = s.translate(tab)
    
    e = list(no_punc.split(" ")) #converts string to list
    
    not_i = e.index('not')
    bad_i = e.index('bad')
    
    if not_i < bad_i: #index comparison
        g = ['good']
        e[not_i:bad_i+1] = g #replaces not...bad --> good
        
        #for returning punctuation
        if "" in e:
            punc = e.index("")
            e[punc] = "!"
            
        s2 = " ".join(e)
    else:
        s2 = s
else:
    s2 = s

print(s2)