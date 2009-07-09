from comtypes.client import GetActiveObject, CreateObject

#Get running instance of the AutoCAD application
app = GetActiveObject("AutoCAD.Application")

#active document
ad = app.ActiveDocument

#model space
ms = ad.ModelSpace
