def separate(x):
    if x<=7100*12:
        charge=x
    elif (x*0.05)<=18000:
        charge=x*(1-0.05)
    else:
        charge=x-18000
    netcharge=charge-132000
    if netcharge<=50000:
        progresstax=netcharge*0.02
    elif netcharge<=100000:
        progresstax=(netcharge-50000)*0.06+1000
    elif netcharge<=150000:
        progresstax=(netcharge-100000)*0.1+4000
    elif netcharge<=200000:
        progresstax=(netcharge-150000)*0.14+9000
    else:
        progresstax=(netcharge-200000)*0.17+16000
    standardtax=charge*0.15
    if progresstax<=10000:
        tax=0
    elif progresstax>standardtax:
        tax=standardtax-10000
    else:
        tax=progresstax-10000
    return tax
        
def combine(x,y):
    charge=0
    if x<=7100*12:
        charge+=x
    elif (x*0.05)<=18000:
        charge+=x*(1-0.05)
    else:
        charge+=(x-18000)
    if y<=7100*12:
        charge+=y
    elif (y*0.05)<=18000:
        charge+=y*(1-0.05)
    else:
        charge+=(y-18000)
    netcharge=charge-264000
    if netcharge<50000:
        progresstax=netcharge*0.02
    elif netcharge<100000:
        progresstax=(netcharge-50000)*0.06+1000
    elif netcharge<150000:
        progresstax=(netcharge-100000)*0.1+4000
    elif netcharge<200000:
        progresstax=(netcharge-150000)*0.14+9000
    else:
        progresstax=(netcharge-200000)*0.17+16000
    standardtax=charge*0.15
    if progresstax<10000:
        tax=0
    elif progresstax>standardtax:
        tax=standardtax-10000
    else:
        tax=progresstax-10000
    return tax

def main():
    print("Simple salaries tax calculator")
    print("------------------------------------------")
    status=0
    while (status<1) or (status>2):
        status = int(input("Your status(1=single/divorced/separated, 2=married): " ))
    if status==1:
        yourincome = int(input("Your income in HK$: "))
        yourtax=separate(yourincome)
        print("Your tax payable is: HK$"+str(yourtax))
    else:
        yourincome = int(input("Your income in HK$: "))
        spouseincome = int(input("Your spouse's income in HK$: "))
        yourtax=separate(yourincome)
        spousetax=separate(spouseincome)
        print("Your tax payable, under separate assessment, is: HK$"+str(yourtax))
        print("Your spouse's tax payable, under separate assessment, is: HK$"+str(spousetax))
        combintax=combine(yourincome, spouseincome)
        print("You and your spouse's tax payable, under joint assessment, is: HK$"+str(combintax))
        if combintax<yourtax+spousetax:
            print("You should choose for joint assessment.")
        else:
            print("You should choose for separate assessment.")
        #To show the results on the screen before the program close
        input()
    
if __name__ == "__main__":
    main()    