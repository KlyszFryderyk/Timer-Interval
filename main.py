import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('./my.kv')

class Menu(Screen):
	time_of_round = NumericProperty()
	time_of_rest = NumericProperty()
	number_of_rounds = NumericProperty()

	def inc_tor(self):
		self.time_of_round +=5
	def inc_torest(self):
		self.time_of_rest +=2
	def inc_nor(self):
		self.number_of_rounds +=1

	def dec_tor(self):
		if self.time_of_round > 0:
			self.time_of_round -=5
	def dec_torest(self):
		if self.time_of_rest > 0:
			self.time_of_rest -=2
	def dec_nor(self):
		if self.number_of_rounds > 0:
			self.number_of_rounds -=1

class Counter(Screen):
	pass

sm = ScreenManager()
sm.add_widget(Menu(name='Menu'))
sm.add_widget(Counter(name='Counter'))

class MyApp(App):
	def build(self):
		return sm


if __name__ == "__main__":
	MyApp().run()
