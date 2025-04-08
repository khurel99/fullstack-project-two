
#tempertaure huwirgah function
def calculate(a, b, uildel):
    if uildel == 1:
        output = str(a) + "+" + str(b) + "=" + str(a+b)
    elif uildel == 2:
        output = str(a) + "-" + str(b) + "=" + str(a-b)
    elif uildel == 3:
        output = str(a) + "*" + str(b) + "=" + str(a*b)
    elif uildel == 4:
        output = str(a) + "/" + str(b) + "=" + str(a/b)
    elif uildel == 5:
        output = str(a) + "-iin " + str(b) + " zereg=" + str(pow(a,b))
    elif uildel == 6:
        output = str(a) + "-iin " + str(b) + " zergiin yazguur=" + str(pow(a,1/b))
    elif uildel == 7:
        output = str(a) + "-g " + str(b) + "-t huwaahad garah uldegdel=" + str(a%b)
    return output

calculate_history = ""
#Y eswel y darwal code ehelne
command = input("program ajluulah bol Y ugui bol N darna uu! Umnuh history goo harah bol H darna uu!\n")

while command=="Y" or command=="y" or command=="H" or command=="h":
    if command=="Y" or command=="y":
        #eh temperature iin input heseg
        try:
            a = float(input("ehnii toog oruulna uu\n"))
        except:
            a = float(input("zuwhun toon utga oruulna uu!\n"))
        
        try:
            b = float(input("2 dahi toog oruulna uu\n"))
        except:
            b = float(input("zuwhun toon utga oruulna uu!\n"))
        

        #zoriltot temperature iin input heseg
        try:
            uildel = int(input("""uildliin dugaariig oruulan uu
1.nemeh
2.hasah
3.urjuuleh
4.huwaah
5.zeregt dewshuuleh
6.yazguur
7.vldegdel
"""))
        except:
            uildel = int(input("zuwhun uildliin dugaar boloh 1 buhel too oruulna uu!\n"))
        if uildel < 1 or uildel > 7:
            uildel = int(input("uildel iin dugaar n 1ees 7iin hoorond buhel too baih yostoi!dahin oruulna uu!\n"))
        
        if uildel == 4 and b == 0:
            b = float(input("toog 0t huwaaj bolohgui tul 2doh toog dahin oruulna uu!\n"))
        #temperature horwuulelt
        output = calculate(a, b, uildel)
        print(output)

        calculate_history = calculate_history + output + "\n"
    else:
        print(calculate_history)
    command = input("program ajluulah bol Y ugui bol N darna uu! Umnuh history goo harah bol H darna uu!\n")
