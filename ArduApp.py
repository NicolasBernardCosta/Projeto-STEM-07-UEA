# ProjetoSTEM---App-Kivy
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class Manager(ScreenManager):
	pass

class Menu(Screen):
	pass 

class Game(Screen):
	pass
	
class Comandos(Screen):
	pass

class Hardware(Screen):
	pass

class Experimentos(Screen):
	pass

class Variaveis(Screen):
	pass

class MyPopup(Popup):
	pass

class Entradas(Screen):
	pass

class Saidas(Screen):
	pass

class Matematica(Screen):
	pass

class Controles(Screen):
	pass

class Ferramentas(Screen):
	pass

class Sensores(Screen):
	pass

class Arduino(Screen):
	pass
	
class ArduApp(App):
	pass

if __name__ == "__main__":
	ArduApp().run()
