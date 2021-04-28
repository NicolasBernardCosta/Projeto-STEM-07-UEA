# Projeto-STEM-07-UEA

#Código do App em .py

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.properties import ObjectProperty

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



#Código do design do App em .kv

Manager:
	Menu:
		name:'menu'
	Game:
		name:'game'
	Comandos:
		name:'comando'
	Hardware:
		name:'hardware'
	Experimentos:
		name:'experimento'
	Variaveis:
		name:'variavel'
	Entradas:
		name:'entrada'
	Saidas:
		name:'saida'
	Matematica:
		name:'matematica'
	Controles:
		name:'controle'
	Ferramentas:
		name:'ferramenta'
	Sensores:
		name:'sensor'
	Arduino:
		name:'arduino'
	
<MenuButton@Button>:
	font_size:'50sp'
	background_normal:'menuButton.png'
	background_down:'menuButtonpressed.png'
	border: 90,90,90,90

<Menu>:
	BoxLayout:
		canvas:
			Color:
				rgba:1,1,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		Widget:
		BoxLayout:
			padding:"100dp"
			spacing:"150dp"
			MenuButton:
				text:'Start'
				on_press:
				on_release:app.root.current = 'game'
			MenuButton:
				text:'Exit'
				on_press:
				on_release:app.Stop()



<Game>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,0.9,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'menu'
			MenuButton:
				text:'Comandos'
				on_press:
				on_release:app.root.current = 'comando'
			MenuButton:
				text:'Hardware'
				on_press:
				on_release:app.root.current = 'hardware'
			MenuButton:
				text:'Experimentos'
				on_press:
				on_release:app.root.current = 'experimento'


<Comandos>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,0.9,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'game'
			MenuButton:
				text:'Variáveis'
				on_press:
				on_release:app.root.current = 'variavel'
			MenuButton:
				text:'Entrada'
				on_press:
				on_release:app.root.current = 'entrada'
			MenuButton:
				text:'Saída'
				on_press:
				on_release:app.root.current = 'saida'
			MenuButton:
				text:'Matemática'
				on_press:
				on_release:app.root.current = 'matematica'
			MenuButton:
				text:'Controles'
				on_press:
				on_release:app.root.current = 'controle'


<Variaveis>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,0.9,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'comando'

<Entradas>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,0.9,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'comando'

<Saidas>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,0.9,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'comando'

<Matematica>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,0.9,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'comando'

<Controles>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,0.9,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'comando'


<Hardware>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,1,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation:'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'game'
			MenuButton:
				text:'Ferramentas'
				on_press:
				on_release:app.root.current = 'ferramenta'
			MenuButton:
				text:'Sensores'
				on_press:
				on_release:app.root.current = 'sensor'
			MenuButton:
				text:'Arduino'
				on_press:
				on_release:app.root.current = 'arduino'


<Ferramentas>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,0.9,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'hardware'

<Sensores>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,0.9,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'hardware'

<Arduino>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,0.9,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation: 'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'hardware'


<Experimentos>:
	FloatLayout:
		canvas:
			Color:
				rgba:1,1,1,1
			Rectangle:
				size:self.size
				pos:self.pos
		orientation:'vertical'
		padding: '200dp', '50dp'
		spacing:'100dp'
		BoxLayout:
			orientation: "vertical"
			padding:"200dp", "50dp"
			spacing:"100dp"
			MenuButton:
				text:'Voltar'
				on_release:app.root.current = 'game'

