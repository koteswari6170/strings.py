# a="python"
# a[0]='p' #typeerror
# print(dir(str))
# n="hEllo pyThon"
# print(n.capitalize()) #Hello python
# b="venkat"
# print(b.capitalize()) #Venkat
# a="hEllo pyThon"
# print(a.casefold()) #hello python
# b="Himaja Pulahari"
# print(b.lower()) #himaja pulahari

# f="hEllo pyThon"
# print(len(f)) #12
# print(f.center(30)) #              hEllo pyThon
# print(f.center(50,'*'))
# print(f.center(40,'%'))
# h="venkat pulahari"
# print(type(h)) #str
# n=h.encode()
# print(n) #b'venkat pulahari'
# print(h.decode()) #attributeerror
# h=b"viswa"
# print(type(h)) #bytes
# print(h.encode())#attributeerror
# print(h.decode()) #viswa

# l="koteswari"
# print(l.upper()) #KOTESWARI
# print(l.lower()) #koteswari
# print(l.isupper()) #False
# print(l.islower()) #True
# b="CRICKET"
# print(b.isupper()) #True
# m="worldcup t20"
# print(m.islower()) #True
# t='kaVeri tUtukuri'
# print(t.title()) #Kaveri Tutukuri
# print(t.capitalize()) #Kaveri tutukuri
# print(t.istitle()) #False
# c="Banavathu Indu Priya"
# print(c.istitle()) #True

# n='hEllo pyThon'
# print(n.endswith()) #Typeerror:endswith() takes atleast 1 argument
# print(n.endswith('')) #True
# print(n.endswith(' ')) #False
# print(n.endswith('n')) #True
# print(n.endswith(""",""")) #False
# print(n.endswith("")) #True

# n='hEllo pyThon'
# print(n.startswith(''))#True
# print(n.startswith(' ')) #False
# print(n.startswith('h')) #True
# print(n.startswith('E')) #False
# b="kaveri"
# print(b.startswith('k')) #True
# print(b.startswith('v')) #false
# print(b.startswith(' ')) #false
# print(b.startswith("")) #True

# z='hEllo pyThon'
# print(z.startswith('')) #True
# print(z.startswith("")) #True
# print(z.startswith(' ')) #False
# print(z.startswith('h'))  #True

# print(z.startswith('p')) #False
# v=''
# g='    '
# print(v.isspace()) #False
# print(g.isspace()) #True
# 
# q="hEllo pyoTholno"
# print(len(q)) #15
# print(q.index('l')) #2
# print(q.index('l',4)) 
# print(q.index('o')) #4
# print(q.index('o',5)) 
# print(q.index('h')) #0
# r="hEllo pyThon programming"
# print(len(r)) #24
# print(r.index('u')) #ValueError:substring not found
# print(r.index('n')) #11
# print(r.rindex('E')) #1
# print(r.rindex('n')) #22

# v="dakshini dakshini"
# print(len(v)) #17
# print(v.index('k')) #2
# print(v.rindex('k')) #11
# print(v.index('s')) #3
# print(v.rindex('s')) #12
# r="hEllo pyThon programming"
# print(len(r)) #24
# print(len('josh innovations')) #16
# print(dir(str))
# n=[ 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# print(len(n)) #47
# w="_3hello"
# print(w.isidentifier()) #True
# b="python programming"
# print(b.count('p')) #2
# print(b.count('m')) #2
# print(b.count('i')) #1
# print(b.count('e')) #0

# h="python course"
# print(h.replace('course','programming')) #core programming
# g="core python programming core"
# print(g.replace('core',str(2)))# 2 python programming 2
# print(g.replace('core','2')) #2 python programming 2
# print(g.replace('o','k',1)) #ckre python programming core
# print(g.replace('o','k',2)) #ckre pythkn programming core
# print(g.replace('o','k',3)) #ckre pythkn prkgramming core
# print(g.replace('o','k',4)) #ckre pythkn prkgramming ckre
# # print(g.replace('o','k',5)) #ckre pytkon prkgramming ckre
# a="venkat kaveri"
# print(a.replace('venkat','chinna')) #chinna kaveri

# d="             python programming      .          "
# print(len(d)) #48
# print(d.strip()) # python programming    .
# print(d.lstrip()) # python programming    .
# print(d.rstrip()) #             python programming      .
# a="hello", "python",'pro'
# print(a,type(a)) #('hello', 'python', 'pro') tuple
# b=' world '.join(a)
# print(b) #hello world python pro
# print("Hello","python",sep="world") #helloworldpython 
# c="hey"
# d="*".join(c)
# print(d) #h*e*y
# e="hey",
# f="%".join(e)
# print(f) #hey
# e="hey",""
# f="%".join(e)
# print(f) #hey%
# a="hey","kavya "
# b="%".join(a)
# print(b) #hey%kavya

# c="Python Programming"
# print(c.removeprefix('P')) #ython programming
# print(c.removeprefix('p')) #python programming
# print(c.removeprefix('Py')) #thon programming
# print(c.removesuffix('g')) #Python Programmin
# print(c.removesuffix('ng')) #Python Programmi
# print(c.removesuffix('ming')) #Python Program

# a="core python"
# print(a.isalpha()) #False
# a="corepython"
# print(a.isalpha()) #True
# b="corepython23"
# print(b.isalpha())cls #False
# b="6"
# print(b.isalpha()) #False
# c="H"
# print(c.isalpha()) #True
# a=""
# print(a.isalpha()) #False
# b=" "
# print(b.isalpha()) #False
# v="august python"
# print(v.isascii()) #True
# b=chr(0) 
# c=chr(32)
# print(b.isspace()) #False
# print(c.isspaclsce()) #True
# print("hello"+chr(32)+"python") #hello python
# print("hello"+' '+"python") #hello python
# print("hello","python",sep=" ") #hello python
# print("hello","python") #hello python
# print(chr(32)+"hey") # hey
# print(chr(0)+"hey") #hey
# print(ord('a'))  #97
# print(ord('z')) #122
# print(ord('A')) #65
# print(ord('Z')) #90
# print(ord('0')) #48
# print(ord('9')) #57
# print(ord(' ')) #32
# print(ord('!')) #33

# a="hello python"
# print(a.isalnum()) #False
# b="hellopython"
# print(b.isalnum()) #True
# c="H"
# # print(c.isalnum()) #True
# d="6"
# print(d.isalnum()) #True
# f=""
# print(f.isalnum()) #False
# h=" "
# print(h.isalnum()) #False
# k="hello23"
# print(k.isalnum()) #True

# v=bin(5)
# print(v,type(v)) #0b101 str
# k=0b101
# print(k,type(k)) #5 int
# v=bin(10)
# print(v,type(v)) #0B1010 str
# a=0b1010
# print(a,type(a)) #10 int
# print(bin(23)) #0b10111
# print(0B10111) #23
# print(0b10111) #23

# f=oct(11)
# print(f,type(f)) #0o13 str
# print(0o13) #11
# print(0O13) #11
# a=oct(25)
# print(a,type(a)) #0o31 str
# print(0o31) #25
# print(0O31) #25

# d=hex(18)
# print(d,type(d)) #0x12 str
# print(0x12) #18
# print(0X12) #18
# z=hex(20)
# print(z,type(z)) #0x14 str
# print(0x14) #20
# print(0X14) #20










