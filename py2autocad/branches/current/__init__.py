from comtypes.client import GetActiveObject, CreateObject
from acad_model_space import AcadModelSpace

#Get running instance of the AutoCAD application
app = GetActiveObject("AutoCAD.Application")

#active document
ad = app.ActiveDocument

#model space
ms = AcadModelSpace(app.ActiveDocument.ModelSpace)
