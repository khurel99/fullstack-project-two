
#tempertaure huwirgah function
def tem_changer(inp, outp, temperature):

    if inp == "C" and outp == "F":
        output_tem = float(temperature*1.8 + 32)
        print(f"{temperature}C=",output_tem,"F")
    elif inp == "F" and outp == "C":
        output_tem = float((temperature-32)/1.8)
        print(f"{temperature}F=",output_tem,"C")
    elif inp == "C" and outp == "K":
        output_tem = float(temperature+273.15)
        print(f"{temperature}C=",output_tem,"K")
    elif inp == "K" and outp == "C":
        output_tem = float(temperature-273.15)
        print(f"{temperature}K=",output_tem,"C")
    elif inp == "F" and outp == "K":
        output_tem = float((temperature-32)*1.8 + 273.15)
        print(f"{temperature}F=",output_tem,"K")
    elif inp == "K" and outp == "F":
        output_tem = float((temperature-273.15)*1.8 + 32.0)
        print(f"{temperature}K=",output_tem,"F")

#Y eswel y darwal code ehelne
command = input("program ajluulah bol Y ugui bol N darna uu!\n")

while command=="Y" or command=="y":
    #eh temperature iin input heseg
    input_t = input("eh temperature iig oruulna uu! C or F or K\n")
    if input_t != "C" and input_t != "F" and input_t != "K":
        input_t = input("zuwhun tom C,F,K iin ali negiig oruulna uu!\n")

    #zoriltot temperature iin input heseg
    output_t = input("zoriltot temperature iig oruulna uu! C or F or K\n")
    if output_t != "C" and output_t != "F" and output_t != "K":
        output_t = input("zuwhun tom C,F,K iin ali negiig oruulna uu!\n")
    
    #temperature iin input heseg
    try:
        tem = float(input("temperature iin utga iig oruulna uu!\n"))
    except:
        tem = float(input("zuwhun toon utga oruulna uu!\n"))
    if input_t == "K" and tem < 0:
        tem = float(input("Kelvin 0 ees doosh baij bolohgvi tul zuw utga oruulna uu!\n"))

    #temperature horwuulelt
    tem_changer(input_t, output_t, tem)

    command = input("program ajluulah bol Y ugui bol N darna uu!\n")
