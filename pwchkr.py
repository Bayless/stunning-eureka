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


    
checkURself('baukdyu238r7')
checkURself('baukdYu238r7')
checkURself('bau')
