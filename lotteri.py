import random 


class lotteri:

    def __init__(self):

        self.list_vinster = [
        "solstol", 
        "iphone",
        "Handduk",
        "ockelbo 500",
         "Polaris RMK",
           "elsparkcykel",
            "BMX",
            "skateboard",
            "Hawaii resa",
            "bulle och saft ",                       
              "hörlurar",   
                "headset",
                "konsert med queen ",
                "lidl matkasse",
                "coop matkasse",
                "ica matkasse ",
                "margarin",
                "Bregott",
                "ficklampa",
                "kex",]


    def get_vinst (self):
        slumptal = random.randint(0,19)
        return self.list_vinster [slumptal]