import re

def build_lst(fout,exp):
    '''
    returns a match for regexp.
    '''
    
    i = []

    for text in fout.readlines():
        i += re.findall(exp,text)
        return i

def ret_gex():
    '''
    sends input's for do_until to finish, or proceed to the next process (call to other function: dispatch)
    '''
    fin = input('input file name')
    answer = input('final?')
    exp = input('input exp')
    return fin,answer,exp
    
def do_until(a=[]):
    '''
////->calls ret_gex to ask user for inputs to use regexp functions on files;
//////////////////////->     opens files one at a time;
\\\\\\\\\\\\\\\\\\\\\\->     quits on entry of 'ret_gex' returns to 'answer' as 'y' and 'yes' from input;
    returns list.
    '''
    
    fin,answer,exp=ret_gex()
    
    with open(fin,'r') as fout:
        if answer == 'y' or answer == 'yes':
            a.append(build_lst(fout,exp))
            fout.close()
        else:
            a.append(build_lst(fout,exp))
            do_until(a=a)
    return a
 

if __name__ == "__main__":
    print(do_until())