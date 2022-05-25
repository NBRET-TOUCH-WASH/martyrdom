#coding:utf-8

class Nanomachines:
    """ nanomachines. harden in response to physical trauma.
    Jack cannot hurt them. """

    def __init__(self):
        self.ennemy = "Raiden"
        self.ennemyNickname = "Jack"

        self.shirt = "ripped"
        self.abs = "also ripped"



    def present_self(self):
        """ explains to the ennemy why the nanomachines user won't die """

        self.harden()
        print("Nanomachines, son.")
        print("They harden in response to physical trauma.")

        self.punch_ground()
        print("You can't hurt me, {}.".format(self.ennemyNickname))

        self.stomach_blow()
        self.laugh()
        print("What did I just say?")

        self.launch_ennemy_into_orbit()



    def laugh(self):
        """ laughs menacingly """
        print("*laughs*")



    def harden(self):
        """ makes the nanomachines harden in response to physical trauma """

        print("NANOMACHINES\t:\tHARD")
        print("ENNEMY\t\t:\t{}".format(self.ennemy))
        print("RTX\t\t:\tON")
        print("GLASSES\t\t:\tALSO ON")
        print("")



    def punch_ground(self):
        """ punches the ground to demonstrate the workings of said nanomachines """
        print("*punches ground vigorously*")



    def stomach_blow(self):
        """ stomachs the ennemy blow """
        print("*stomachs {}'s blow*".format(self.ennemy))



    def launch_ennemy_into_orbit(self):
        """ launches the ennemy into orbit with a single punch """
        print("*launches {} into orbit*".format(self.ennemy))

stevenArmstrong = Nanomachines()
stevenArmstrong.present_self()
