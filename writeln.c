import sys
def putc(c:chr):
    f1=sys.stdout
    f1.write(c)
    

def puts(s:str):
    f1=sys.stdout
    f1.write(s)
    
def putinteger(i):
    f1=sys.stdout
    f1.write(str(i))
    
def putfloat(i):
    f1=sys.stdout
    f1.write(str(i))
   

def console_writeline(*args):
    ss=args[0].split("{")
    if(len(args)!=len(ss)):
        return
    puts(ss[0])
    for val in range(len(ss)):
        
        if val>0 and val <len(args):
            bb=ss[val]
            aa=bb.split("}")
            i=int(aa[0])
            k=args[i+1]
            
            
            puts(str(k))

            puts(aa[1])

print("\033c\033[43;30m")
console_writeline("hello world.... {0} integer={1} float={2} char={3}\n","hi",1,3.1415927,chr(65))
