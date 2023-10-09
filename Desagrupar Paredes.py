lista  = App.ActiveDocument.Objects
lista2 = Gui.Selection.getSelection()

if lista2 == []:
	for i in lista:
		try:	
			if i.IfcType == 'Wall':
				lista3 = i.Additions 
				i.Additions = []
				i.Visibility = True
				i.MoveBase = True
				for j in lista3:
					j.Visibility = True
		except:
			pass
else:
	for i in lista2:
		try:	
			if i.IfcType == 'Wall':
				lista3 = i.Additions 
				i.Additions = []
				i.Visibility = True
				i.MoveBase = True
				for j in lista3:
					j.Visibility = True
				
		except:
			pass
	
	