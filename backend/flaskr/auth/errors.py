class Invalid_authentification(Exception):
    def __init__(self,bad_parameter):
        self.bad_parameter=bad_parameter

    def __str__(self):
        print(f"Authentification not occurred. {self.bad_parameter}  is invalid " )
    pass