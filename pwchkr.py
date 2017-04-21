'''
YOUR TASK The First:
Write a function that uses list comprehension to return whether a password meets a minimum threshold: it contains a mixture of upper- and lowercase letters, and at least one number.
YOUR TASK The Second:
Write a function that uses list comprehension to return a password's strength rating. This function should return a low integer for a weak password and a higher integer for a stronger password. (Suggested scale: 1-10) 
Consider these criteria:
 mixture of upper- and lower-case
inclusion of numerals
inclusion of these non-alphanumeric chars: . ? ! & # , ; : - _ *
'''

def checkURself(pas):
    ret1 = False
    ret2 = False
    ret3 = False
    hiLetters = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    lowLetters = "qwertyuioplkjhgfdsazxcvbnm"
    numbers = [str(i) for i in range(0,10)]
    password = [pas[i] for i in range(len(pas))]
    lo = [lowLetters[i] for i in range(len(lowLetters))]
    hi = [hiLetters[i] for i in range(len(hiLetters))]
    for i in password:
        if(i in numbers):
            ret1 = True
        if(i in lo):
            ret2 = True
        if (i in hi):
            ret3 = True
    ret = ret1 and ret2 and ret3 
    print ret
    return ret

def rating(pas):
    hiLetters = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    lowLetters = "qwertyuioplkjhgfdsazxcvbnm"
    things = ". ? ! & # , ; : - _ *"
    numbers = [str(i) for i in range(0,10)]
    password = [pas[i] for i in range(len(pas))]
    lo = [lowLetters[i] for i in range(len(lowLetters))]
    hi = [hiLetters[i] for i in range(len(hiLetters))]
    thing = [things[i] for i in range(len(things))]
    val = 0
    for i in password:
        if(i in numbers):
            val+=2
        if(i in lo):
            val+=1
        if (i in hi):
            val+=2
        if(i in thing):
            val+=3
    print val
    return val

    
#checkURself('baukdyu238r7')
#checkURself('baukdYu238r7')
#checkURself('bau')

rating('wuiegfweui239847JJGF')
rating('ekjrgfukwergfurefger')
rating('FJHJSDUIOD998')
rating('bayle')
