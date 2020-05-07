fname=''
lname=''
age=''
namelan=''
data={}
do={}
fln=''

def start(data):
    print('''                                                 
 mmmmm                                           
 #   "#  mmm    mmm    mmm    mmmm   mmm   m mm  
 #mmm#" "   #  #   "  #   "  #" "#  #"  #  #"  #                                                                                                           
 #      m"""#   """m   """m  #   #  #""""  #   #                                                                                                           
 #      "mm"#  "mmm"  "mmm"  "#m"#  "#mm"  #   #                                                                                                           
                              m  #   		by Alex10882            
                               ""       
''')
    namelan=input('SSID ')
    fname=input('Ftirstname of the owner ')
    lname=input('Lastname of the owner ')
    age=input('Receiving age ')
    data={'lname':lname, 'fname':fname, 'age':age, 'namelan':namelan }
    return(data)

def filename(fln):
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    filename=askopenfilename()
    fln=filename
    return(fln)

def genfla(do, fln ):
    w=open(fln, 'w')
    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20
    for i in range(np, vp):
        trk=f+l+str(i)+'\n'
        if len(trk)-1>=8:
            w.write(trk)
    w.close()

def genlfa(do, fln):
    w=open(fln, 'a')
    

    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20
    for i in range(np, vp):
        trk=l+f+str(i)+'\n'
        if len(trk)-1>=8: 
            w.write(trk)
    w.close()

def genafl(do, fln):
    w=open(fln, 'a')
    
    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20
    for i in range(np, vp):
        trk=str(i)+f+l+'\n'
        if len(trk)-1>=8:
            
            w.write(trk)
    w.close()

def genalf(do, fln):
    w=open(fln, 'a')
    
    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20
    for i in range(np, vp):
        trk=str(i)+l+f+'\n'
       
        if len(trk)-1>=8:
            
            w.write(trk)
    w.close()

def genlf(do, fln):
    w=open(fln, 'a')
    
    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    trk=l+f+'\n'
       
    if len(trk)-1>=8:
            
        w.write(trk)
    w.close()

def genfl(do, fln):
    w=open(fln, 'a')
    
    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    trk=f+l+'\n'
       
    if len(trk)-1>=8:
            
        w.write(trk)
    w.close()

def genlfy(do, fln):
    w=open(fln, 'a')
    

    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20

    for i in range(2020-vp, 2020-np):
        trk=l+f+str(i)+'\n'
        if len(trk)-1>=8: 
            w.write(trk)
    w.close()

def genfly(do, fln):
    w=open(fln, 'a')
    

    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20

    for i in range(2020-vp, 2020-np):
        trk=f+l+str(i)+'\n'
        if len(trk)-1>=8: 
            w.write(trk)
    w.close()

def genFL(do, fln):
    w=open(fln, 'a')
    

    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    f=f.upper()	
    l=l.upper()
    w.write(f+l+'\n')
    w.close()

def genLF(do, fln):
    w=open(fln, 'a')
    

    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    f=f.upper()	
    l=l.upper()
    w.write(l+f+'\n')
    w.close()

def genFLa(do, fln ):
    w=open(fln, 'a')
    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    f=f.upper()
    l=l.upper()
    np=a-20
    vp=a+20
    for i in range(np, vp):
        trk=f+l+str(i)+'\n'
        if len(trk)-1>=8:
            w.write(trk)
    w.close()

    
def genLFa(do, fln):
    w=open(fln, 'a')
    

    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20
    f=f.upper()
    l=l.upper()
    for i in range(np, vp):
        trk=l+f+str(i)+'\n'
        if len(trk)-1>=8: 
            w.write(trk)
    w.close()

def genaLF(do, fln):
    w=open(fln, 'a')
    
    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20
    l=l.upper()
    f=f.upper()
    for i in range(np, vp):
        trk=str(i)+l+f+'\n'
       
        if len(trk)-1>=8:
            
            w.write(trk)
    w.close()

def genaFL(do, fln):
    w=open(fln, 'a')
    
    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20
    f=f.upper()
    l=l.upper()
    for i in range(np, vp):
        trk=str(i)+f+l+'\n'
        if len(trk)-1>=8:
            
            w.write(trk)
    w.close()

def genLFy(do, fln):
    w=open(fln, 'a')
    

    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20
    f=f.upper()
    l=l.upper()
    for i in range(2020-vp, 2020-np):
        trk=l+f+str(i)+'\n'
        if len(trk)-1>=8: 
            w.write(trk)
    w.close()

def genFLy(do, fln):
    w=open(fln, 'a')
    

    f=do['fname']
    l=do['lname']
    a=do['age']
    a=int(a)
    np=a-20
    vp=a+20
    f=f.upper()
    l=l.upper()
    for i in range(2020-vp, 2020-np):
        trk=f+l+str(i)+'\n'
        if len(trk)-1>=8: 
            w.write(trk)
    w.close()




do=start(data)
fln=filename(fln)
genfla(do, fln )
genlfa(do, fln )
genafl(do, fln)
genalf(do, fln)
genlf(do, fln)
genfl(do, fln)
genlfy(do, fln)
genfly(do, fln)
genFL(do, fln)
genLF(do, fln)
genLFa(do, fln)
genFLa(do, fln)
genaLF(do, fln)
genaFL(do,fln)
genFLy(do, fln)
genLFy(do, fln)