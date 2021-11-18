def paranda_komavead(lause):
    lause = lause.replace (" sest ", ", sest ")
    lause = lause.replace (" et ", ", et ")
    lause = lause.replace (" aga ", ", aga ")
    lause = lause.replace (" kuid ", ", kuid ")
    lause = lause.replace (" vaid ", ", vaid")
    lause = lause.replace (" siis ", ", siis ")
    print(lause)
    
paranda_komavead("olen loll sest ei õpi")
paranda_komavead("kui õpin siis ei ole enam loll")
paranda_komavead("õpin komavigu parandama et ma ei oleks loll")


        