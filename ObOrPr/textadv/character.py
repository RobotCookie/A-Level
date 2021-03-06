class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    def steal(self):
        print("You cannot steal from a neutral or friendly target")
    def hug(self):
        print("You cannot hug a neutral or enemy target")
class Enemy(Character):

    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.item = None
    def fight(self, combat_item):
        if self.weakness == combat_item:
            print("You killed",self.name,"with the",combat_item)
            Enemy.enemies_defeated += 1
            return True
        else:
            print("Your",combat_item,"does little against the might of",self.name)
            return False
    def set_weakness(self,char_weakness):
        self.weakness = char_weakness
    def get_weakness(self):
        return self.weakness
    def set_item(self,new_item):
        self.item = new_item
    def get_item(self):
        return self.item
    def set_defeated(self,new_defeated):
        Enemy.enemies_defeated = 0
    def get_defeated(self):
        return Enemy.enemies_defeated
    def steal(self):
        if self.item is not None:
            print("You steal a",self.item.get_name(),"from",self.name)
            return True
        else:
            print(self.name,"has nothing to steal")
            return False
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = 0
    def hug(self):
        if self.feeling > 10:
            print(self.name,"hugs you back")
        else:
            print(self.name,"doesn't want to hug you")
    def set_feeling(self,feel):
        self.feeling = feel
    def get_feeling(self):
        return self.feeling