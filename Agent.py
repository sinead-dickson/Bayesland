import random
class agent():

    game_count = 0
    head_count = 0

    def __init__(self, bankroll):
        self.bankroll = bankroll

    def getBankroll(self):
        return self.bankroll

    def setBankroll(self,add,amount):
        if add:
            self.bankroll += amount
        else:
            self.bankroll -= amount

    def getKey(self):
        return random.randint(1,5)

    def setPast(self):
        self.game_count = self.game_count + 1
        self.head_count = self.head_count + 1

    def getPast(self):
        if self.game_count == 0:
            return random.randint(0, 100)/100
        return self.head_count/self.game_count
