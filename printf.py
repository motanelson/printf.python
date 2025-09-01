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
   

def printfst(*args):
    ss=args[0].split("%")
    if(len(args)!=len(ss)):
        return
    puts(ss[0])
    for val in range(len(args)):
        
        if val>0 and val <len(args):
            k=args[val]
            
            a=list(ss[val])
            if(a[0]=="d"):
                putinteger(k)
            if(a[0]=="f"):
                putfloat(k)
            if(a[0]=="s"):
                puts(k)
            if(a[0]=="c"):
                putc(k)

            s1=ss[val]
            puts(s1[1:])

print("\033c\033[43;30m")
printfst("hello world.... %s integer=%d float=%f char=%c\n","hi",1,3.1415927,chr(65))
