from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
class app(App):
	def build(self):
		return main()

class main(BoxLayout):
	pass
app().run()