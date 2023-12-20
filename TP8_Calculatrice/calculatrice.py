from kivy.app import App
from kivy.core.window import Window


class Calculatrice(App):
    def build(self):
        pass

    def ajout(self, nbr):
        self.root.ids.ecran.text += nbr

    def calcul(self):
        try:
            reso = self.root.ids.ecran.text
            solution = eval(reso)
            self.root.ids.ecran.text = str(solution)
        except SyntaxError:
            self.root.ids.ecran.text = "Error: calcul incorrecte"

    def efface(self):
        self.root.ids.ecran.text = ""


Window.size = (400, 600)

Calculatrice().run()
