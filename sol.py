from solara import *


@solara.component
def Page():
	with Column():
		Title("THis app ")
	with Column(align="center"):
		Text("This sample app")
		Button("sample ",color="primary")
		Button("sample ",color="red")

# AND NOW RUN THIS APP