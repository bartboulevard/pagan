misfail = input("Sisestage fail, kus tahate komavigu parandada: ")

def paranda_komavead(lause):
    lause = lause.replace (" sest ", ", sest ")
    lause = lause.replace (" et ", ", et ")
    lause = lause.replace (" aga ", ", aga ")
    lause = lause.replace (" kuid ", ", kuid ")
    lause = lause.replace (" vaid ", ", vaid")
    lause = lause.replace (" siis ", ", siis ")
    print(lause)
    
fail = open(misfail, encoding="UTF-8")
a = ""
for rida in fail:
    a = a + rida
paranda_komavead(a)