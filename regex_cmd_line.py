import re

def build_lst(fout,exp):
    i = []

    for text in fout.readlines():
        i += re.findall(exp,text)
        return i


def ret_gex():
    fin = input('input file name')
    answer = input('final?')
    exp = input('input exp')
    return fin,answer,exp
def do_until(a=[]):
    fin,answer,exp=ret_gex()
    
    with open(fin,'r') as fout:
        if answer == 'y' or answer == 'yes':
            fout.close()
        else:
            a.append(build_lst(fout,exp))
            do_until(a=a)
    return a
 
print(do_until())