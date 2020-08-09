"""A temp"""
def temp():
    """input tempA"""
    atem = int(input())
    rtem = (atem+273.15)*(9/5)
    ktem = (atem+273.15)
    ftem = ((atem*9/5)+32)
    ntem = atem*33/100
    dtem = ((100-atem)*3/2)
    atem_re = (rtem-ktem)+ftem-(ntem/dtem)
    print("%0.02f A"%(atem_re))
temp()
