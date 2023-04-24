import lotteri
import  os 

lotteriet = lotteri.lotteri()
looping = True 

while looping:

    os.system('cls' if os.name == 'nt' else 'clear')
    antal_lotter = input ("\n\t\t hur många lotter vill du ha? max 3 st: ")
    
    try:
       int_antal_lotter = int(antal_lotter)
       i = 0
       if (int_antal_lotter <4):
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("\n\t\t grattis du vann:")

            while i  <int_antal_lotter:
                vinst = lotteriet.get_vinst()

                print("\t\t" + vinst)
                i+=1
           
       elif (int_antal_lotter >3):
           print ("\n\t\t du har valt för många lotter ") 
    
    except ValueError:
       print ("endast siffor tillåtna!") 
    
    print("--------------------------------------------")
    spela_igen = input("\n\t\tvill du spela igen? j/n ")
   
    if (spela_igen == "n"):
        break 

