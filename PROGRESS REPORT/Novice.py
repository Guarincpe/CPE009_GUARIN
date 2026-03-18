from Character import Character

class Novice(Character):
   def BasicAttack(self, character):
      character.reduceHp(self.getDamage())
      print (f"{self.getUsername()} performed Basic Attack! {self.getDamage()}")
      