def read_data():
    f=open('1.txt')
    readline=f.readlines()
    word=[]
    
    for line in readline:
        line=line.replace(',','')
        line=line.replace('.','')
        line=line.replace('-','')
        line=line.replace(':','')
        line=line.replace('"','')
        line=line.replace('!','')
        line=line.replace('?','')
        line=line.strip()
        wo=line.split(' ')
        
        word.extend(wo)
    return word

def clear_account(lists):
    wokey={}
    wokey=wokey.fromkeys(lists)
    word_1=list(wokey.keys())
    
    for i in word_1:
        wokey[i]=lists.count(i)
    del wokey['']
    del wokey['the']
    del wokey['to']
    del wokey['of']
    del wokey['a']
    del wokey['in']
    del wokey['for']
    del wokey['it']
    del wokey['and']
    return wokey

def sort_1(wokey):
    wokey_1={}
    wokey_1=sorted(wokey.items(),key=lambda d:d[1],reverse=True)
    
    return wokey_1

def main(wokey_1):
    i=0
    for x,y in wokey_1:
        if i<50:
            print (x,y)
            i+=1
            continue
        else:
             break
                
main(sort_1(clear_account(read_data())))