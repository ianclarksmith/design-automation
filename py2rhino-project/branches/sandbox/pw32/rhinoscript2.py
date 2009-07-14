# -*- coding: mbcs -*-
# Created by makepy.py version 0.4.97
# By python version 2.5.4 (r254:67916, Apr 27 2009, 15:41:14) [MSC v.1310 32 bit (Intel)]
# From type library 'RhinoScript.tlb'
# On Tue Jul 14 11:40:21 2009
"""RhinoScript 4.0 Type Library"""
makepy_version = '0.4.97'
python_version = 0x20504f0

import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{75B1E1B4-8CAA-43C3-975E-373504024FDB}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IRhinoScript(DispatchBaseClass):
	CLSID = IID('{DC7E0867-5922-4DCB-935F-585F81484030}')
	coclass_clsid = IID('{48B5D8DC-EDB1-45A9-981B-6C96169A0E7D}')

	def ACos(self, vx=defaultNamedNotOptArg):
		"""ACos"""
		return self._ApplyTypes_(757, 1, (12, 0), ((12, 0),), u'ACos', None,vx
			)

	def ACosH(self, vx=defaultNamedNotOptArg):
		"""ACosH"""
		return self._ApplyTypes_(763, 1, (12, 0), ((12, 0),), u'ACosH', None,vx
			)

	def ASin(self, vx=defaultNamedNotOptArg):
		"""ASin"""
		return self._ApplyTypes_(756, 1, (12, 0), ((12, 0),), u'ASin', None,vx
			)

	def ASinH(self, vx=defaultNamedNotOptArg):
		"""ASinH"""
		return self._ApplyTypes_(762, 1, (12, 0), ((12, 0),), u'ASinH', None,vx
			)

	def ATan2(self, vy=defaultNamedNotOptArg, vx=defaultNamedNotOptArg):
		"""ATan2"""
		return self._ApplyTypes_(758, 1, (12, 0), ((12, 0), (12, 0)), u'ATan2', None,vy
			, vx)

	def ATanH(self, vx=defaultNamedNotOptArg):
		"""ATanH"""
		return self._ApplyTypes_(764, 1, (12, 0), ((12, 0),), u'ATanH', None,vx
			)

	def AddAlias(self, vaName=defaultNamedNotOptArg, vaMacro=defaultNamedNotOptArg):
		"""AddAlias"""
		return self._ApplyTypes_(709, 1, (12, 0), ((12, 0), (12, 0)), u'AddAlias', None,vaName
			, vaMacro)

	def AddArc(self, vaPlane=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg):
		"""AddArc"""
		return self._ApplyTypes_(651, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddArc', None,vaPlane
			, vaRadius, vaAngle)

	def AddArc3Pt(self, vaPt1=defaultNamedNotOptArg, vaPt2=defaultNamedNotOptArg, vaPt3=defaultNamedNotOptArg):
		"""AddArc3Pt"""
		return self._ApplyTypes_(82, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddArc3Pt', None,vaPt1
			, vaPt2, vaPt3)

	def AddBox(self, vaCorners=defaultNamedNotOptArg):
		"""AddBox"""
		return self._ApplyTypes_(72, 1, (12, 0), ((12, 0),), u'AddBox', None,vaCorners
			)

	def AddCircle(self, vaPlane=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg):
		"""AddCircle"""
		return self._ApplyTypes_(83, 1, (12, 0), ((12, 0), (12, 0)), u'AddCircle', None,vaPlane
			, vaRadius)

	def AddCircle3Pt(self, vaPt1=defaultNamedNotOptArg, vaPt2=defaultNamedNotOptArg, vaPt3=defaultNamedNotOptArg):
		"""AddCircle3Pt"""
		return self._ApplyTypes_(84, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddCircle3Pt', None,vaPt1
			, vaPt2, vaPt3)

	def AddClippingPlane(self, vaPlane=defaultNamedNotOptArg, vaDX=defaultNamedNotOptArg, vaDY=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""AddClippingPlane"""
		return self._ApplyTypes_(904, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'AddClippingPlane', None,vaPlane
			, vaDX, vaDY, vaView)

	def AddCone(self, vaCenter=defaultNamedNotOptArg, vaHeight=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg, vaCap=defaultNamedOptArg):
		"""AddCone"""
		return self._ApplyTypes_(75, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'AddCone', None,vaCenter
			, vaHeight, vaRadius, vaCap)

	def AddCurve(self, vaPoints=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg):
		"""AddCurve"""
		return self._ApplyTypes_(77, 1, (12, 0), ((12, 0), (12, 16)), u'AddCurve', None,vaPoints
			, vaDegree)

	def AddCutPlane(self, vaObjects=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""AddCutPlane"""
		return self._ApplyTypes_(822, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'AddCutPlane', None,vaObjects
			, vaStart, vaEnd, vaView)

	def AddCylinder(self, vaCenter=defaultNamedNotOptArg, vaHeight=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg, vaCap=defaultNamedOptArg):
		"""AddCylinder"""
		return self._ApplyTypes_(73, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'AddCylinder', None,vaCenter
			, vaHeight, vaRadius, vaCap)

	def AddDimStyle(self, vaStyle=defaultNamedOptArg):
		"""AddDimStyle"""
		return self._ApplyTypes_(455, 1, (12, 0), ((12, 16),), u'AddDimStyle', None,vaStyle
			)

	def AddDirectionalLight(self, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg):
		"""AddDirectionalLight"""
		return self._ApplyTypes_(153, 1, (12, 0), ((12, 0), (12, 0)), u'AddDirectionalLight', None,vaStart
			, vaEnd)

	def AddEdgeSrf(self, vaObjects=defaultNamedNotOptArg):
		"""AddEdgeSrf"""
		return self._ApplyTypes_(203, 1, (12, 0), ((12, 0),), u'AddEdgeSrf', None,vaObjects
			)

	def AddEllipse(self, vaPlane=defaultNamedNotOptArg, vaDX=defaultNamedNotOptArg, vaDY=defaultNamedNotOptArg):
		"""AddEllipse"""
		return self._ApplyTypes_(679, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddEllipse', None,vaPlane
			, vaDX, vaDY)

	def AddEllipse3Pt(self, vaCenter=defaultNamedNotOptArg, vaSecond=defaultNamedNotOptArg, vaThird=defaultNamedNotOptArg):
		"""AddEllipse3Pt"""
		return self._ApplyTypes_(680, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddEllipse3Pt', None,vaCenter
			, vaSecond, vaThird)

	def AddFilletCurve(self, vaCrv0=defaultNamedNotOptArg, vaCrv1=defaultNamedNotOptArg, vaRadius=defaultNamedOptArg, vaPt0=defaultNamedOptArg
			, vaPt1=defaultNamedOptArg):
		"""AddFilletCurve"""
		return self._ApplyTypes_(574, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16)), u'AddFilletCurve', None,vaCrv0
			, vaCrv1, vaRadius, vaPt0, vaPt1)

	def AddGroup(self, vaName=defaultNamedOptArg):
		"""AddGroup"""
		return self._ApplyTypes_(133, 1, (12, 0), ((12, 16),), u'AddGroup', None,vaName
			)

	def AddHatch(self, vaCurve=defaultNamedNotOptArg, vaHatch=defaultNamedOptArg, vaScale=defaultNamedOptArg, vaRotation=defaultNamedOptArg):
		"""AddHatch"""
		return self._ApplyTypes_(835, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), u'AddHatch', None,vaCurve
			, vaHatch, vaScale, vaRotation)

	def AddHatchPatterns(self, vaFileName=defaultNamedNotOptArg, vaReplace=defaultNamedOptArg):
		"""AddHatchPatterns"""
		return self._ApplyTypes_(826, 1, (12, 0), ((12, 0), (12, 16)), u'AddHatchPatterns', None,vaFileName
			, vaReplace)

	def AddHatches(self, vaCurve=defaultNamedNotOptArg, vaHatch=defaultNamedOptArg, vaScale=defaultNamedOptArg, vaRotation=defaultNamedOptArg):
		"""AddHatches"""
		return self._ApplyTypes_(836, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), u'AddHatches', None,vaCurve
			, vaHatch, vaScale, vaRotation)

	def AddInterpCrvOnSrf(self, vaObject=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg):
		"""AddInterpCrvOnSrf"""
		return self._ApplyTypes_(513, 1, (12, 0), ((12, 0), (12, 0)), u'AddInterpCrvOnSrf', None,vaObject
			, vaPoints)

	def AddInterpCrvOnSrfUV(self, vaObject=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg):
		"""AddInterpCrvOnSrfUV"""
		return self._ApplyTypes_(641, 1, (12, 0), ((12, 0), (12, 0)), u'AddInterpCrvOnSrfUV', None,vaObject
			, vaPoints)

	def AddInterpCurve(self, vaPoints=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg, vaKnot=defaultNamedOptArg, vaCV1=defaultNamedOptArg
			, vaCVn1=defaultNamedOptArg):
		"""AddInterpCurve"""
		return self._ApplyTypes_(268, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16), (12, 16)), u'AddInterpCurve', None,vaPoints
			, vaDegree, vaKnot, vaCV1, vaCVn1)

	def AddInterpCurveEx(self, vaPoints=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg, vaKnotSpacing=defaultNamedOptArg, vaSharp=defaultNamedOptArg
			, vaStartTangent=defaultNamedOptArg, vaEndTangent=defaultNamedOptArg):
		"""AddInterpCurveEx"""
		return self._ApplyTypes_(520, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'AddInterpCurveEx', None,vaPoints
			, vaDegree, vaKnotSpacing, vaSharp, vaStartTangent, vaEndTangent
			)

	def AddLayer(self, vaName=defaultNamedOptArg, vaColor=defaultNamedOptArg, vaVisible=defaultNamedOptArg, vaLocked=defaultNamedOptArg
			, vaParent=defaultNamedOptArg):
		"""AddLayer"""
		return self._ApplyTypes_(3, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'AddLayer', None,vaName
			, vaColor, vaVisible, vaLocked, vaParent)

	def AddLeader(self, vaPoints=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaText=defaultNamedOptArg):
		"""AddLeader"""
		return self._ApplyTypes_(321, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'AddLeader', None,vaPoints
			, vaView, vaText)

	def AddLine(self, vaPoint1=defaultNamedNotOptArg, vaPoint2=defaultNamedNotOptArg):
		"""AddLine"""
		return self._ApplyTypes_(70, 1, (12, 0), ((12, 0), (12, 0)), u'AddLine', None,vaPoint1
			, vaPoint2)

	def AddLinearLight(self, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaWidth=defaultNamedOptArg):
		"""AddLinearLight"""
		return self._ApplyTypes_(154, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'AddLinearLight', None,vaStart
			, vaEnd, vaWidth)

	def AddLoftSrf(self, vaObjects=defaultNamedNotOptArg, vaStartPt=defaultNamedOptArg, vaEndPt=defaultNamedOptArg, vaType=defaultNamedOptArg
			, vaSimplify=defaultNamedOptArg, vaVal=defaultNamedOptArg, vaClosed=defaultNamedOptArg):
		"""AddLoftSrf"""
		return self._ApplyTypes_(567, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'AddLoftSrf', None,vaObjects
			, vaStartPt, vaEndPt, vaType, vaSimplify, vaVal
			, vaClosed)

	def AddMaterialToLayer(self, vaLayer=defaultNamedNotOptArg):
		"""AddMaterialToLayer"""
		return self._ApplyTypes_(173, 1, (12, 0), ((12, 0),), u'AddMaterialToLayer', None,vaLayer
			)

	def AddMaterialToObject(self, vaObject=defaultNamedNotOptArg):
		"""AddMaterialToObject"""
		return self._ApplyTypes_(174, 1, (12, 0), ((12, 0),), u'AddMaterialToObject', None,vaObject
			)

	def AddMesh(self, vaVertices=defaultNamedNotOptArg, vaFaces=defaultNamedNotOptArg, vaNormals=defaultNamedOptArg, vaTextures=defaultNamedOptArg
			, vaColors=defaultNamedOptArg):
		"""AddMesh"""
		return self._ApplyTypes_(494, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16)), u'AddMesh', None,vaVertices
			, vaFaces, vaNormals, vaTextures, vaColors)

	def AddNamedCPlane(self, vaName=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""AddNamedCPlane"""
		return self._ApplyTypes_(280, 1, (12, 0), ((12, 0), (12, 16)), u'AddNamedCPlane', None,vaName
			, vaView)

	def AddNamedView(self, vaName=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""AddNamedView"""
		return self._ApplyTypes_(281, 1, (12, 0), ((12, 0), (12, 16)), u'AddNamedView', None,vaName
			, vaView)

	def AddNurbsCurve(self, vaPoints=defaultNamedNotOptArg, vaKnots=defaultNamedNotOptArg, vaDegree=defaultNamedNotOptArg, vaWeights=defaultNamedOptArg):
		"""AddNurbsCurve"""
		return self._ApplyTypes_(309, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'AddNurbsCurve', None,vaPoints
			, vaKnots, vaDegree, vaWeights)

	def AddNurbsSurface(self, vaPointCount=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg, vaKnotsU=defaultNamedNotOptArg, vaKnotsV=defaultNamedNotOptArg
			, vaDegree=defaultNamedNotOptArg, vaWeights=defaultNamedOptArg):
		"""AddNurbsSurface"""
		return self._ApplyTypes_(435, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0), (12, 16)), u'AddNurbsSurface', None,vaPointCount
			, vaPoints, vaKnotsU, vaKnotsV, vaDegree, vaWeights
			)

	def AddObjectMesh(self, vaObject=defaultNamedNotOptArg, vaQuality=defaultNamedOptArg, vaEnable=defaultNamedOptArg):
		"""AddObjectMesh"""
		return self._ApplyTypes_(866, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'AddObjectMesh', None,vaObject
			, vaQuality, vaEnable)

	def AddObjectToGroup(self, vaObject=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""AddObjectToGroup"""
		return self._ApplyTypes_(134, 1, (12, 0), ((12, 0), (12, 0)), u'AddObjectToGroup', None,vaObject
			, vaName)

	def AddObjectsToGroup(self, vaObjects=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""AddObjectsToGroup"""
		return self._ApplyTypes_(135, 1, (12, 0), ((12, 0), (12, 0)), u'AddObjectsToGroup', None,vaObjects
			, vaName)

	def AddPlanarMesh(self, vaCurve=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""AddPlanarMesh"""
		return self._ApplyTypes_(915, 1, (12, 0), ((12, 0), (12, 16)), u'AddPlanarMesh', None,vaCurve
			, vaDelete)

	def AddPlanarSrf(self, vaObjects=defaultNamedNotOptArg):
		"""AddPlanarSrf"""
		return self._ApplyTypes_(371, 1, (12, 0), ((12, 0),), u'AddPlanarSrf', None,vaObjects
			)

	def AddPlaneSurface(self, vaPlane=defaultNamedNotOptArg, vaDX=defaultNamedNotOptArg, vaDY=defaultNamedNotOptArg):
		"""AddPlaneSurface"""
		return self._ApplyTypes_(648, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddPlaneSurface', None,vaPlane
			, vaDX, vaDY)

	def AddPoint(self, vaPoint=defaultNamedNotOptArg):
		"""AddPoint"""
		return self._ApplyTypes_(68, 1, (12, 0), ((12, 0),), u'AddPoint', None,vaPoint
			)

	def AddPointCloud(self, vaCloud=defaultNamedNotOptArg):
		"""AddPointCloud"""
		return self._ApplyTypes_(69, 1, (12, 0), ((12, 0),), u'AddPointCloud', None,vaCloud
			)

	def AddPointLight(self, vaPoint=defaultNamedNotOptArg):
		"""AddPointLight"""
		return self._ApplyTypes_(155, 1, (12, 0), ((12, 0),), u'AddPointLight', None,vaPoint
			)

	def AddPoints(self, vaCloud=defaultNamedNotOptArg):
		"""AddPoints"""
		return self._ApplyTypes_(526, 1, (12, 0), ((12, 0),), u'AddPoints', None,vaCloud
			)

	def AddPolyline(self, vaPoints=defaultNamedNotOptArg):
		"""AddPolyline"""
		return self._ApplyTypes_(85, 1, (12, 0), ((12, 0),), u'AddPolyline', None,vaPoints
			)

	def AddRailRevSrf(self, vaProfile=defaultNamedNotOptArg, vaRail=defaultNamedNotOptArg, vaAxis=defaultNamedNotOptArg):
		"""AddRailRevSrf"""
		return self._ApplyTypes_(536, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddRailRevSrf', None,vaProfile
			, vaRail, vaAxis)

	def AddRectangularLight(self, vaOrigin=defaultNamedNotOptArg, vaX=defaultNamedNotOptArg, vaY=defaultNamedNotOptArg):
		"""AddRectangularLight"""
		return self._ApplyTypes_(156, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddRectangularLight', None,vaOrigin
			, vaX, vaY)

	def AddRevSrf(self, vaObject=defaultNamedNotOptArg, vaAxis=defaultNamedNotOptArg, vaSA=defaultNamedOptArg, vaEA=defaultNamedOptArg):
		"""AddRevSrf"""
		return self._ApplyTypes_(535, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'AddRevSrf', None,vaObject
			, vaAxis, vaSA, vaEA)

	def AddSearchPath(self, vaFolder=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""AddSearchPath"""
		return self._ApplyTypes_(511, 1, (12, 0), ((12, 0), (12, 16)), u'AddSearchPath', None,vaFolder
			, vaIndex)

	def AddSphere(self, vaCenter=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg):
		"""AddSphere"""
		return self._ApplyTypes_(71, 1, (12, 0), ((12, 0), (12, 0)), u'AddSphere', None,vaCenter
			, vaRadius)

	def AddSpotLight(self, vaBase=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg, vaApex=defaultNamedNotOptArg):
		"""AddSpotLight"""
		return self._ApplyTypes_(157, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddSpotLight', None,vaBase
			, vaRadius, vaApex)

	def AddSrfContourCrvs(self, vaObject=defaultNamedNotOptArg, va0=defaultNamedNotOptArg, va1=defaultNamedOptArg, va2=defaultNamedOptArg):
		"""AddSrfContourCrvs"""
		return self._ApplyTypes_(747, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'AddSrfContourCrvs', None,vaObject
			, va0, va1, va2)

	def AddSrfControlPtGrid(self, vaCount=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg):
		"""AddSrfControlPtGrid"""
		return self._ApplyTypes_(294, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'AddSrfControlPtGrid', None,vaCount
			, vaPoints, vaDegree)

	def AddSrfPt(self, vaPoints=defaultNamedNotOptArg):
		"""AddSrfPt"""
		return self._ApplyTypes_(204, 1, (12, 0), ((12, 0),), u'AddSrfPt', None,vaPoints
			)

	def AddSrfPtGrid(self, vaCount=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg, vaClosed=defaultNamedOptArg):
		"""AddSrfPtGrid"""
		return self._ApplyTypes_(293, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'AddSrfPtGrid', None,vaCount
			, vaPoint, vaDegree, vaClosed)

	def AddSrfSectionCrvs(self, vaObject=defaultNamedNotOptArg, vaPlane=defaultNamedNotOptArg):
		"""AddSrfSectionCrvs"""
		return self._ApplyTypes_(803, 1, (12, 0), ((12, 0), (12, 0)), u'AddSrfSectionCrvs', None,vaObject
			, vaPlane)

	def AddStartupScript(self, vaScript=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""AddStartupScript"""
		return self._ApplyTypes_(714, 1, (12, 0), ((12, 0), (12, 16)), u'AddStartupScript', None,vaScript
			, vaIndex)

	def AddSubCrv(self, vaObject=defaultNamedNotOptArg, vaParam0=defaultNamedNotOptArg, vaParam1=defaultNamedNotOptArg):
		"""AddSubCrv"""
		return self._ApplyTypes_(681, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddSubCrv', None,vaObject
			, vaParam0, vaParam1)

	def AddSweep1(self, vaRail=defaultNamedNotOptArg, vaCurves=defaultNamedNotOptArg, vaStartPoint=defaultNamedOptArg, vaEndPoint=defaultNamedOptArg
			, vaClosed=defaultNamedOptArg, vaStyle=defaultNamedOptArg, vaStyleArg=defaultNamedOptArg, vaSimplify=defaultNamedOptArg, vaSimplifyArg=defaultNamedOptArg):
		"""AddSweep1"""
		return self._ApplyTypes_(893, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'AddSweep1', None,vaRail
			, vaCurves, vaStartPoint, vaEndPoint, vaClosed, vaStyle
			, vaStyleArg, vaSimplify, vaSimplifyArg)

	def AddSweep2(self, vaRail=defaultNamedNotOptArg, vaCurves=defaultNamedNotOptArg, vaStartPoint=defaultNamedOptArg, vaEndPoint=defaultNamedOptArg
			, vaClosed=defaultNamedOptArg, vaSimpleSweep=defaultNamedOptArg, vaSameHeight=defaultNamedOptArg, vaSimplify=defaultNamedOptArg, vaSimplifyArg=defaultNamedOptArg):
		"""AddSweep2"""
		return self._ApplyTypes_(894, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'AddSweep2', None,vaRail
			, vaCurves, vaStartPoint, vaEndPoint, vaClosed, vaSimpleSweep
			, vaSameHeight, vaSimplify, vaSimplifyArg)

	def AddText(self, vaText=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaHeight=defaultNamedOptArg, vaFont=defaultNamedOptArg
			, vaStyle=defaultNamedOptArg):
		"""AddText"""
		return self._ApplyTypes_(76, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16)), u'AddText', None,vaText
			, vaPoint, vaHeight, vaFont, vaStyle)

	def AddTextDot(self, vaText=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""AddTextDot"""
		return self._ApplyTypes_(320, 1, (12, 0), ((12, 0), (12, 0)), u'AddTextDot', None,vaText
			, vaPoint)

	def AddToolBar(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""AddToolBar"""
		return self._ApplyTypes_(219, 1, (12, 0), ((12, 0), (12, 0)), u'AddToolBar', None,vaAlias
			, vaName)

	def AddToolBarButton(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""AddToolBarButton"""
		return self._ApplyTypes_(220, 1, (12, 0), ((12, 0), (12, 0)), u'AddToolBarButton', None,vaAlias
			, vaName)

	def AddToolBarCollection(self, vaFile=defaultNamedNotOptArg):
		"""AddToolBarCollection"""
		return self._ApplyTypes_(221, 1, (12, 0), ((12, 0),), u'AddToolBarCollection', None,vaFile
			)

	def AddTorus(self, vaCenter=defaultNamedNotOptArg, vaRadius1=defaultNamedNotOptArg, vaRadius2=defaultNamedNotOptArg, vaDirection=defaultNamedOptArg):
		"""AddTorus"""
		return self._ApplyTypes_(74, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'AddTorus', None,vaCenter
			, vaRadius1, vaRadius2, vaDirection)

	def AliasCount(self):
		"""AliasCount"""
		return self._ApplyTypes_(706, 1, (12, 0), (), u'AliasCount', None,)

	def AliasMacro(self, vaName=defaultNamedNotOptArg, vaMacro=defaultNamedOptArg):
		"""AliasMacro"""
		return self._ApplyTypes_(708, 1, (12, 0), ((12, 0), (12, 16)), u'AliasMacro', None,vaName
			, vaMacro)

	def AliasNames(self):
		"""AliasNames"""
		return self._ApplyTypes_(707, 1, (12, 0), (), u'AliasNames', None,)

	def AllObjects(self, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""AllObjects"""
		return self._ApplyTypes_(30, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'AllObjects', None,vaSelect
			, vaIncludeLights, vaIncludeGrips)

	def AllProcedures(self, vaAll=defaultNamedOptArg):
		"""AllProcedures"""
		return self._ApplyTypes_(503, 1, (12, 0), ((12, 16),), u'AllProcedures', None,vaAll
			)

	def Angle(self, vaFrom=defaultNamedNotOptArg, vaTo=defaultNamedNotOptArg, vaWorld=defaultNamedOptArg):
		"""Angle"""
		return self._ApplyTypes_(115, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'Angle', None,vaFrom
			, vaTo, vaWorld)

	def Angle2(self, vaFirst=defaultNamedNotOptArg, vaSecond=defaultNamedNotOptArg):
		"""Angle2"""
		return self._ApplyTypes_(116, 1, (12, 0), ((12, 0), (12, 0)), u'Angle2', None,vaFirst
			, vaSecond)

	def AppearanceColor(self, vaItem=defaultNamedNotOptArg, vaColor=defaultNamedOptArg):
		"""AppearanceColor"""
		return self._ApplyTypes_(335, 1, (12, 0), ((12, 0), (12, 16)), u'AppearanceColor', None,vaItem
			, vaColor)

	def AppearanceDisplay(self, vaItem=defaultNamedNotOptArg, vaDisplay=defaultNamedOptArg):
		"""AppearanceDisplay"""
		return self._ApplyTypes_(752, 1, (12, 0), ((12, 0), (12, 16)), u'AppearanceDisplay', None,vaItem
			, vaDisplay)

	def ArcAngle(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""ArcAngle"""
		return self._ApplyTypes_(86, 1, (12, 0), ((12, 0), (12, 16)), u'ArcAngle', None,vaObject
			, vaIndex)

	def ArcCenterPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""ArcCenterPoint"""
		return self._ApplyTypes_(87, 1, (12, 0), ((12, 0), (12, 16)), u'ArcCenterPoint', None,vaObject
			, vaIndex)

	def ArcMidPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""ArcMidPoint"""
		return self._ApplyTypes_(88, 1, (12, 0), ((12, 0), (12, 16)), u'ArcMidPoint', None,vaObject
			, vaIndex)

	def ArcRadius(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""ArcRadius"""
		return self._ApplyTypes_(89, 1, (12, 0), ((12, 0), (12, 16)), u'ArcRadius', None,vaObject
			, vaIndex)

	def AttributeDataCount(self, vaObject=defaultNamedNotOptArg):
		"""AttributeDataCount"""
		return self._ApplyTypes_(685, 1, (12, 0), ((12, 0),), u'AttributeDataCount', None,vaObject
			)

	def AutosaveFile(self, vaFile=defaultNamedOptArg):
		"""AutosaveFile"""
		return self._ApplyTypes_(428, 1, (12, 0), ((12, 16),), u'AutosaveFile', None,vaFile
			)

	def AutosaveInterval(self, vaMinutes=defaultNamedOptArg):
		"""AutosaveInterval"""
		return self._ApplyTypes_(429, 1, (12, 0), ((12, 16),), u'AutosaveInterval', None,vaMinutes
			)

	def BackgroundBitmap(self, vaView=defaultNamedOptArg, vaFileName=defaultNamedOptArg, vaPoint=defaultNamedOptArg, vaWidth=defaultNamedOptArg):
		"""BackgroundBitmap"""
		return self._ApplyTypes_(780, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), u'BackgroundBitmap', None,vaView
			, vaFileName, vaPoint, vaWidth)

	def BlockContainerCount(self, vaName=defaultNamedNotOptArg):
		"""BlockContainerCount"""
		return self._ApplyTypes_(411, 1, (12, 0), ((12, 0),), u'BlockContainerCount', None,vaName
			)

	def BlockContainers(self, vaName=defaultNamedNotOptArg):
		"""BlockContainers"""
		return self._ApplyTypes_(412, 1, (12, 0), ((12, 0),), u'BlockContainers', None,vaName
			)

	def BlockCount(self):
		"""BlockCount"""
		return self._ApplyTypes_(397, 1, (12, 0), (), u'BlockCount', None,)

	def BlockDescription(self, vaName=defaultNamedNotOptArg, vaDesc=defaultNamedOptArg):
		"""BlockDescription"""
		return self._ApplyTypes_(400, 1, (12, 0), ((12, 0), (12, 16)), u'BlockDescription', None,vaName
			, vaDesc)

	def BlockInstanceCount(self, vaName=defaultNamedNotOptArg):
		"""BlockInstanceCount"""
		return self._ApplyTypes_(404, 1, (12, 0), ((12, 0),), u'BlockInstanceCount', None,vaName
			)

	def BlockInstanceInsertPoint(self, vaObject=defaultNamedNotOptArg):
		"""BlockInstanceInsertPoint"""
		return self._ApplyTypes_(413, 1, (12, 0), ((12, 0),), u'BlockInstanceInsertPoint', None,vaObject
			)

	def BlockInstanceName(self, vaObject=defaultNamedNotOptArg):
		"""BlockInstanceName"""
		return self._ApplyTypes_(571, 1, (12, 0), ((12, 0),), u'BlockInstanceName', None,vaObject
			)

	def BlockInstanceXform(self, vaObject=defaultNamedNotOptArg):
		"""BlockInstanceXform"""
		return self._ApplyTypes_(415, 1, (12, 0), ((12, 0),), u'BlockInstanceXform', None,vaObject
			)

	def BlockInstances(self, vaName=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg):
		"""BlockInstances"""
		return self._ApplyTypes_(414, 1, (12, 0), ((12, 0), (12, 16)), u'BlockInstances', None,vaName
			, vaSelect)

	def BlockNames(self, vaSort=defaultNamedOptArg):
		"""BlockNames"""
		return self._ApplyTypes_(396, 1, (12, 0), ((12, 16),), u'BlockNames', None,vaSort
			)

	def BlockObjectCount(self, vaName=defaultNamedNotOptArg):
		"""BlockObjectCount"""
		return self._ApplyTypes_(416, 1, (12, 0), ((12, 0),), u'BlockObjectCount', None,vaName
			)

	def BlockObjects(self, vaName=defaultNamedNotOptArg):
		"""BlockObjects"""
		return self._ApplyTypes_(417, 1, (12, 0), ((12, 0),), u'BlockObjects', None,vaName
			)

	def BlockPath(self, vaName=defaultNamedNotOptArg):
		"""BlockPath"""
		return self._ApplyTypes_(408, 1, (12, 0), ((12, 0),), u'BlockPath', None,vaName
			)

	def BlockURL(self, vaName=defaultNamedNotOptArg, vaNew=defaultNamedOptArg):
		"""BlockURL"""
		return self._ApplyTypes_(402, 1, (12, 0), ((12, 0), (12, 16)), u'BlockURL', None,vaName
			, vaNew)

	def BlockURLTag(self, vaName=defaultNamedNotOptArg, vaNew=defaultNamedOptArg):
		"""BlockURLTag"""
		return self._ApplyTypes_(403, 1, (12, 0), ((12, 0), (12, 16)), u'BlockURLTag', None,vaName
			, vaNew)

	def BooleanDifference(self, vaInBreps0=defaultNamedNotOptArg, vaInBreps1=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""BooleanDifference"""
		return self._ApplyTypes_(508, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'BooleanDifference', None,vaInBreps0
			, vaInBreps1, vaDelete)

	def BooleanIntersection(self, vaInBreps0=defaultNamedNotOptArg, vaInBreps1=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""BooleanIntersection"""
		return self._ApplyTypes_(507, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'BooleanIntersection', None,vaInBreps0
			, vaInBreps1, vaDelete)

	def BooleanUnion(self, vaObjects=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""BooleanUnion"""
		return self._ApplyTypes_(506, 1, (12, 0), ((12, 0), (12, 16)), u'BooleanUnion', None,vaObjects
			, vaDelete)

	def BoundingBox(self, vaObjects=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaSystem=defaultNamedOptArg):
		"""BoundingBox"""
		return self._ApplyTypes_(117, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'BoundingBox', None,vaObjects
			, vaView, vaSystem)

	def BoxMorphObject(self, vaObject=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""BoxMorphObject"""
		return self._ApplyTypes_(918, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'BoxMorphObject', None,vaObject
			, vaPoints, vaCopy)

	def BrepClosestPoint(self, vaBrep=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""BrepClosestPoint"""
		return self._ApplyTypes_(514, 1, (12, 0), ((12, 0), (12, 0)), u'BrepClosestPoint', None,vaBrep
			, vaPoint)

	def BrowseForFolder(self, vaPath=defaultNamedOptArg, vaMessage=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""BrowseForFolder"""
		return self._ApplyTypes_(146, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'BrowseForFolder', None,vaPath
			, vaMessage, vaTitle)

	def BuildDate(self):
		"""BuildDate"""
		return self._ApplyTypes_(360, 1, (12, 0), (), u'BuildDate', None,)

	def CapPlanarHoles(self, vaObject=defaultNamedNotOptArg):
		"""CapPlanarHoles"""
		return self._ApplyTypes_(701, 1, (12, 0), ((12, 0),), u'CapPlanarHoles', None,vaObject
			)

	def Ceil(self, var=defaultNamedNotOptArg):
		"""Ceil"""
		return self._ApplyTypes_(766, 1, (12, 0), ((12, 0),), u'Ceil', None,var
			)

	def CheckListBox(self, vaList=defaultNamedNotOptArg, vaValues=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""CheckListBox"""
		return self._ApplyTypes_(52, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'CheckListBox', None,vaList
			, vaValues, vaPrompt, vaTitle)

	def CircleCenterPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CircleCenterPoint"""
		return self._ApplyTypes_(90, 1, (12, 0), ((12, 0), (12, 16)), u'CircleCenterPoint', None,vaObject
			, vaIndex)

	def CircleCircumference(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CircleCircumference"""
		return self._ApplyTypes_(91, 1, (12, 0), ((12, 0), (12, 16)), u'CircleCircumference', None,vaObject
			, vaIndex)

	def CircleRadius(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CircleRadius"""
		return self._ApplyTypes_(92, 1, (12, 0), ((12, 0), (12, 16)), u'CircleRadius', None,vaObject
			, vaIndex)

	def ClearCommandHistory(self):
		"""ClearCommandHistory"""
		return self._ApplyTypes_(592, 1, (12, 0), (), u'ClearCommandHistory', None,)

	def ClipboardText(self, vaText=defaultNamedOptArg):
		"""ClipboardText"""
		return self._ApplyTypes_(245, 1, (12, 0), ((12, 16),), u'ClipboardText', None,vaText
			)

	def CloseCurve(self, vaObject=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""CloseCurve"""
		return self._ApplyTypes_(440, 1, (12, 0), ((12, 0), (12, 16)), u'CloseCurve', None,vaObject
			, vaTolerance)

	def CloseToolBarCollection(self, vaAlias=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg):
		"""CloseToolBarCollection"""
		return self._ApplyTypes_(222, 1, (12, 0), ((12, 0), (12, 16)), u'CloseToolBarCollection', None,vaAlias
			, vaPrompt)

	def ColorAdjustLuma(self, vaRGB=defaultNamedNotOptArg, vaLuma=defaultNamedNotOptArg, vaScale=defaultNamedOptArg):
		"""ColorAdjustLuma"""
		return self._ApplyTypes_(878, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'ColorAdjustLuma', None,vaRGB
			, vaLuma, vaScale)

	def ColorBlueValue(self, vaRGB=defaultNamedNotOptArg):
		"""ColorBlueValue"""
		return self._ApplyTypes_(882, 1, (12, 0), ((12, 0),), u'ColorBlueValue', None,vaRGB
			)

	def ColorGreenValue(self, vaRGB=defaultNamedNotOptArg):
		"""ColorGreenValue"""
		return self._ApplyTypes_(881, 1, (12, 0), ((12, 0),), u'ColorGreenValue', None,vaRGB
			)

	def ColorHLSToRGB(self, vaUpperBound=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ColorHLSToRGB"""
		return self._ApplyTypes_(877, 1, (12, 0), ((12, 0), (12, 16)), u'ColorHLSToRGB', None,vaUpperBound
			, vaValue)

	def ColorRGBToHLS(self, vaHLS=defaultNamedNotOptArg):
		"""ColorRGBToHLS"""
		return self._ApplyTypes_(876, 1, (12, 0), ((12, 0),), u'ColorRGBToHLS', None,vaHLS
			)

	def ColorRedValue(self, vaRGB=defaultNamedNotOptArg):
		"""ColorRedValue"""
		return self._ApplyTypes_(880, 1, (12, 0), ((12, 0),), u'ColorRedValue', None,vaRGB
			)

	def ComboListBox(self, vaList=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""ComboListBox"""
		return self._ApplyTypes_(53, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'ComboListBox', None,vaList
			, vaPrompt, vaTitle)

	def Command(self, vaCmd=defaultNamedNotOptArg, vaMode=defaultNamedOptArg):
		"""Command"""
		return self._ApplyTypes_(1, 1, (12, 0), ((12, 0), (12, 16)), u'Command', None,vaCmd
			, vaMode)

	def CommandHistory(self):
		"""CommandHistory"""
		return self._ApplyTypes_(591, 1, (12, 0), (), u'CommandHistory', None,)

	def CompareGeometry(self, vaObj1=defaultNamedNotOptArg, vaObj2=defaultNamedNotOptArg):
		"""CompareGeometry"""
		return self._ApplyTypes_(598, 1, (12, 0), ((12, 0), (12, 0)), u'CompareGeometry', None,vaObj1
			, vaObj2)

	def ConvertCurveToPolyline(self, vaObject=defaultNamedNotOptArg, vaLineAngleTolerance=defaultNamedOptArg, vaLineTolerance=defaultNamedOptArg, vaDelete=defaultNamedOptArg):
		"""ConvertCurveToPolyline"""
		return self._ApplyTypes_(377, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), u'ConvertCurveToPolyline', None,vaObject
			, vaLineAngleTolerance, vaLineTolerance, vaDelete)

	def CopyMaterial(self, vaSrcIndex=defaultNamedNotOptArg, vaDstIndex=defaultNamedNotOptArg):
		"""CopyMaterial"""
		return self._ApplyTypes_(812, 1, (12, 0), ((12, 0), (12, 0)), u'CopyMaterial', None,vaSrcIndex
			, vaDstIndex)

	def CopyObject(self, vaObject=defaultNamedNotOptArg, vaStart=defaultNamedOptArg, vaEnd=defaultNamedOptArg):
		"""CopyObject"""
		return self._ApplyTypes_(184, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'CopyObject', None,vaObject
			, vaStart, vaEnd)

	def CopyObjects(self, vaObjects=defaultNamedNotOptArg, vaStart=defaultNamedOptArg, vaEnd=defaultNamedOptArg):
		"""CopyObjects"""
		return self._ApplyTypes_(295, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'CopyObjects', None,vaObjects
			, vaStart, vaEnd)

	def CosH(self, vx=defaultNamedNotOptArg):
		"""CosH"""
		return self._ApplyTypes_(760, 1, (12, 0), ((12, 0),), u'CosH', None,vx
			)

	def CreatePreviewImage(self, vaFileName=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaSize=defaultNamedOptArg, vaFlags=defaultNamedOptArg
			, vaWireframe=defaultNamedOptArg):
		"""CreatePreviewImage"""
		return self._ApplyTypes_(388, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16), (12, 16)), u'CreatePreviewImage', None,vaFileName
			, vaView, vaSize, vaFlags, vaWireframe)

	def CullDuplicateNumbers(self, vaNumbers=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""CullDuplicateNumbers"""
		return self._ApplyTypes_(550, 1, (12, 0), ((12, 0), (12, 16)), u'CullDuplicateNumbers', None,vaNumbers
			, vaTolerance)

	def CullDuplicatePoints(self, vaPoints=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""CullDuplicatePoints"""
		return self._ApplyTypes_(548, 1, (12, 0), ((12, 0), (12, 16)), u'CullDuplicatePoints', None,vaPoints
			, vaTolerance)

	def CullDuplicateStrings(self, vaStrings=defaultNamedNotOptArg, vaCaseSensitive=defaultNamedOptArg):
		"""CullDuplicateStrings"""
		return self._ApplyTypes_(549, 1, (12, 0), ((12, 0), (12, 16)), u'CullDuplicateStrings', None,vaStrings
			, vaCaseSensitive)

	def CurrentDetail(self, vaLayout=defaultNamedNotOptArg, vaDetail=defaultNamedOptArg, vaNames=defaultNamedOptArg):
		"""CurrentDetail"""
		return self._ApplyTypes_(923, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'CurrentDetail', None,vaLayout
			, vaDetail, vaNames)

	def CurrentDimStyle(self, vaStyle=defaultNamedOptArg):
		"""CurrentDimStyle"""
		return self._ApplyTypes_(453, 1, (12, 0), ((12, 16),), u'CurrentDimStyle', None,vaStyle
			)

	def CurrentHatchPattern(self, vaHatch=defaultNamedOptArg):
		"""CurrentHatchPattern"""
		return self._ApplyTypes_(827, 1, (12, 0), ((12, 16),), u'CurrentHatchPattern', None,vaHatch
			)

	def CurrentLayer(self, vaName=defaultNamedOptArg):
		"""CurrentLayer"""
		return self._ApplyTypes_(5, 1, (12, 0), ((12, 16),), u'CurrentLayer', None,vaName
			)

	def CurrentPrinter(self, vaPrinter=defaultNamedOptArg):
		"""CurrentPrinter"""
		return self._ApplyTypes_(358, 1, (12, 0), ((12, 16),), u'CurrentPrinter', None,vaPrinter
			)

	def CurrentView(self, vaView=defaultNamedOptArg, vaNames=defaultNamedOptArg):
		"""CurrentView"""
		return self._ApplyTypes_(251, 1, (12, 0), ((12, 16), (12, 16)), u'CurrentView', None,vaView
			, vaNames)

	def CurveArcLengthPoint(self, vaObject=defaultNamedNotOptArg, vaLength=defaultNamedNotOptArg, vaStart=defaultNamedOptArg):
		"""CurveArcLengthPoint"""
		return self._ApplyTypes_(658, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'CurveArcLengthPoint', None,vaObject
			, vaLength, vaStart)

	def CurveArea(self, vaObject=defaultNamedNotOptArg):
		"""CurveArea"""
		return self._ApplyTypes_(643, 1, (12, 0), ((12, 0),), u'CurveArea', None,vaObject
			)

	def CurveAreaCentroid(self, vaObject=defaultNamedNotOptArg):
		"""CurveAreaCentroid"""
		return self._ApplyTypes_(677, 1, (12, 0), ((12, 0),), u'CurveAreaCentroid', None,vaObject
			)

	def CurveArrows(self, vaObject=defaultNamedNotOptArg, vaFlags=defaultNamedOptArg):
		"""CurveArrows"""
		return self._ApplyTypes_(578, 1, (12, 0), ((12, 0), (12, 16)), u'CurveArrows', None,vaObject
			, vaFlags)

	def CurveBooleanDifference(self, vaCurveA=defaultNamedNotOptArg, vaCurveB=defaultNamedNotOptArg):
		"""CurveBooleanDifference"""
		return self._ApplyTypes_(811, 1, (12, 0), ((12, 0), (12, 0)), u'CurveBooleanDifference', None,vaCurveA
			, vaCurveB)

	def CurveBooleanIntersection(self, vaCurveA=defaultNamedNotOptArg, vaCurveB=defaultNamedNotOptArg):
		"""CurveBooleanIntersection"""
		return self._ApplyTypes_(810, 1, (12, 0), ((12, 0), (12, 0)), u'CurveBooleanIntersection', None,vaCurveA
			, vaCurveB)

	def CurveBooleanUnion(self, vaObjects=defaultNamedNotOptArg):
		"""CurveBooleanUnion"""
		return self._ApplyTypes_(809, 1, (12, 0), ((12, 0),), u'CurveBooleanUnion', None,vaObjects
			)

	def CurveBrepIntersect(self, vaCurve=defaultNamedNotOptArg, vaBrep=defaultNamedNotOptArg, vaTol=defaultNamedOptArg):
		"""CurveBrepIntersect"""
		return self._ApplyTypes_(545, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'CurveBrepIntersect', None,vaCurve
			, vaBrep, vaTol)

	def CurveClosestObject(self, vaCurve=defaultNamedNotOptArg, vaObjects=defaultNamedNotOptArg):
		"""CurveClosestObject"""
		return self._ApplyTypes_(870, 1, (12, 0), ((12, 0), (12, 0)), u'CurveClosestObject', None,vaCurve
			, vaObjects)

	def CurveClosestPoint(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveClosestPoint"""
		return self._ApplyTypes_(93, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'CurveClosestPoint', None,vaObject
			, vaPoint, vaIndex)

	def CurveContourPoints(self, vaObject=defaultNamedNotOptArg, vaBase=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaInterval=defaultNamedOptArg):
		"""CurveContourPoints"""
		return self._ApplyTypes_(748, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'CurveContourPoints', None,vaObject
			, vaBase, vaEnd, vaInterval)

	def CurveCurvature(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""CurveCurvature"""
		return self._ApplyTypes_(379, 1, (12, 0), ((12, 0), (12, 0)), u'CurveCurvature', None,vaObject
			, vaParam)

	def CurveCurveIntersection(self, vaCrvA=defaultNamedNotOptArg, vaCrvB=defaultNamedOptArg, vaTol=defaultNamedOptArg):
		"""CurveCurveIntersection"""
		return self._ApplyTypes_(423, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'CurveCurveIntersection', None,vaCrvA
			, vaCrvB, vaTol)

	def CurveDegree(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveDegree"""
		return self._ApplyTypes_(94, 1, (12, 0), ((12, 0), (12, 16)), u'CurveDegree', None,vaObject
			, vaIndex)

	def CurveDeviation(self, vaCrvA=defaultNamedNotOptArg, vaCrvB=defaultNamedNotOptArg):
		"""CurveDeviation"""
		return self._ApplyTypes_(687, 1, (12, 0), ((12, 0), (12, 0)), u'CurveDeviation', None,vaCrvA
			, vaCrvB)

	def CurveDim(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg):
		"""CurveDim"""
		return self._ApplyTypes_(381, 1, (12, 0), ((12, 0), (12, 0)), u'CurveDim', None,vaObject
			, vaIndex)

	def CurveDirectionsMatch(self, vaCrv1=defaultNamedNotOptArg, vaCrv2=defaultNamedNotOptArg):
		"""CurveDirectionsMatch"""
		return self._ApplyTypes_(543, 1, (12, 0), ((12, 0), (12, 0)), u'CurveDirectionsMatch', None,vaCrv1
			, vaCrv2)

	def CurveDiscontinuity(self, vaObject=defaultNamedNotOptArg, vaType=defaultNamedNotOptArg):
		"""CurveDiscontinuity"""
		return self._ApplyTypes_(579, 1, (12, 0), ((12, 0), (12, 0)), u'CurveDiscontinuity', None,vaObject
			, vaType)

	def CurveDomain(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveDomain"""
		return self._ApplyTypes_(95, 1, (12, 0), ((12, 0), (12, 16)), u'CurveDomain', None,vaObject
			, vaIndex)

	def CurveEditPoints(self, vaObject=defaultNamedNotOptArg, vaReturnParameters=defaultNamedOptArg, vaIndex=defaultNamedOptArg):
		"""CurveEditPoints"""
		return self._ApplyTypes_(442, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'CurveEditPoints', None,vaObject
			, vaReturnParameters, vaIndex)

	def CurveEndPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveEndPoint"""
		return self._ApplyTypes_(96, 1, (12, 0), ((12, 0), (12, 16)), u'CurveEndPoint', None,vaObject
			, vaIndex)

	def CurveEvaluate(self, vaCrv=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaDevCount=defaultNamedNotOptArg):
		"""CurveEvaluate"""
		return self._ApplyTypes_(489, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'CurveEvaluate', None,vaCrv
			, vaParam, vaDevCount)

	def CurveFilletPoints(self, vaCrv0=defaultNamedNotOptArg, vaCrv1=defaultNamedNotOptArg, vaRadius=defaultNamedOptArg, vaPt0=defaultNamedOptArg
			, vaPt1=defaultNamedOptArg):
		"""CurveFilletPoints"""
		return self._ApplyTypes_(572, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16)), u'CurveFilletPoints', None,vaCrv0
			, vaCrv1, vaRadius, vaPt0, vaPt1)

	def CurveFrame(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""CurveFrame"""
		return self._ApplyTypes_(675, 1, (12, 0), ((12, 0), (12, 0)), u'CurveFrame', None,vaObject
			, vaParam)

	def CurveKnotCount(self, vaObject=defaultNamedNotOptArg):
		"""CurveKnotCount"""
		return self._ApplyTypes_(310, 1, (12, 0), ((12, 0),), u'CurveKnotCount', None,vaObject
			)

	def CurveKnots(self, vaObject=defaultNamedNotOptArg):
		"""CurveKnots"""
		return self._ApplyTypes_(311, 1, (12, 0), ((12, 0),), u'CurveKnots', None,vaObject
			)

	def CurveLength(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg, vaDomain=defaultNamedOptArg):
		"""CurveLength"""
		return self._ApplyTypes_(97, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'CurveLength', None,vaObject
			, vaIndex, vaDomain)

	def CurveMeshIntersection(self, vaCurve=defaultNamedNotOptArg, vaMesh=defaultNamedNotOptArg, vaReturnFaces=defaultNamedOptArg):
		"""CurveMeshIntersection"""
		return self._ApplyTypes_(842, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'CurveMeshIntersection', None,vaCurve
			, vaMesh, vaReturnFaces)

	def CurveMidPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveMidPoint"""
		return self._ApplyTypes_(577, 1, (12, 0), ((12, 0), (12, 16)), u'CurveMidPoint', None,vaObject
			, vaIndex)

	def CurveNormal(self, vaObject=defaultNamedNotOptArg):
		"""CurveNormal"""
		return self._ApplyTypes_(521, 1, (12, 0), ((12, 0),), u'CurveNormal', None,vaObject
			)

	def CurvePerpFrame(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""CurvePerpFrame"""
		return self._ApplyTypes_(676, 1, (12, 0), ((12, 0), (12, 0)), u'CurvePerpFrame', None,vaObject
			, vaParam)

	def CurvePlane(self, vaName=defaultNamedNotOptArg):
		"""CurvePlane"""
		return self._ApplyTypes_(609, 1, (12, 0), ((12, 0),), u'CurvePlane', None,vaName
			)

	def CurvePointCount(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurvePointCount"""
		return self._ApplyTypes_(98, 1, (12, 0), ((12, 0), (12, 16)), u'CurvePointCount', None,vaObject
			, vaIndex)

	def CurvePoints(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurvePoints"""
		return self._ApplyTypes_(308, 1, (12, 0), ((12, 0), (12, 16)), u'CurvePoints', None,vaObject
			, vaIndex)

	def CurveRadius(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveRadius"""
		return self._ApplyTypes_(80, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'CurveRadius', None,vaObject
			, vaPoint, vaIndex)

	def CurveSeam(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""CurveSeam"""
		return self._ApplyTypes_(527, 1, (12, 0), ((12, 0), (12, 0)), u'CurveSeam', None,vaObject
			, vaParam)

	def CurveStartPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveStartPoint"""
		return self._ApplyTypes_(99, 1, (12, 0), ((12, 0), (12, 16)), u'CurveStartPoint', None,vaObject
			, vaIndex)

	def CurveSurfaceIntersection(self, vaCrv=defaultNamedNotOptArg, vaSrf=defaultNamedNotOptArg, vaTol=defaultNamedOptArg, vaAngleTol=defaultNamedOptArg):
		"""CurveSurfaceIntersection"""
		return self._ApplyTypes_(424, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'CurveSurfaceIntersection', None,vaCrv
			, vaSrf, vaTol, vaAngleTol)

	def CurveTangent(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveTangent"""
		return self._ApplyTypes_(363, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'CurveTangent', None,vaObject
			, vaParam, vaIndex)

	def CurveWeights(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveWeights"""
		return self._ApplyTypes_(314, 1, (12, 0), ((12, 0), (12, 16)), u'CurveWeights', None,vaObject
			, vaIndex)

	def DefaultRenderer(self, vaRenderer=defaultNamedOptArg):
		"""DefaultRenderer"""
		return self._ApplyTypes_(316, 1, (12, 0), ((12, 16),), u'DefaultRenderer', None,vaRenderer
			)

	def DeleteAlias(self, vaName=defaultNamedNotOptArg):
		"""DeleteAlias"""
		return self._ApplyTypes_(710, 1, (12, 0), ((12, 0),), u'DeleteAlias', None,vaName
			)

	def DeleteAttributeData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""DeleteAttributeData"""
		return self._ApplyTypes_(684, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'DeleteAttributeData', None,vaObject
			, vaApp, vaKey)

	def DeleteBlock(self, vaName=defaultNamedNotOptArg):
		"""DeleteBlock"""
		return self._ApplyTypes_(418, 1, (12, 0), ((12, 0),), u'DeleteBlock', None,vaName
			)

	def DeleteDimStyle(self, vaStyle=defaultNamedNotOptArg):
		"""DeleteDimStyle"""
		return self._ApplyTypes_(456, 1, (12, 0), ((12, 0),), u'DeleteDimStyle', None,vaStyle
			)

	def DeleteDocumentData(self, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""DeleteDocumentData"""
		return self._ApplyTypes_(237, 1, (12, 0), ((12, 16), (12, 16)), u'DeleteDocumentData', None,vaApp
			, vaKey)

	def DeleteGroup(self, vaName=defaultNamedNotOptArg):
		"""DeleteGroup"""
		return self._ApplyTypes_(136, 1, (12, 0), ((12, 0),), u'DeleteGroup', None,vaName
			)

	def DeleteLayer(self, vaName=defaultNamedNotOptArg):
		"""DeleteLayer"""
		return self._ApplyTypes_(4, 1, (12, 0), ((12, 0),), u'DeleteLayer', None,vaName
			)

	def DeleteNamedCPlane(self, vaName=defaultNamedNotOptArg):
		"""DeleteNamedCPlane"""
		return self._ApplyTypes_(284, 1, (12, 0), ((12, 0),), u'DeleteNamedCPlane', None,vaName
			)

	def DeleteNamedView(self, vaName=defaultNamedNotOptArg):
		"""DeleteNamedView"""
		return self._ApplyTypes_(285, 1, (12, 0), ((12, 0),), u'DeleteNamedView', None,vaName
			)

	def DeleteObject(self, vaObject=defaultNamedNotOptArg):
		"""DeleteObject"""
		return self._ApplyTypes_(185, 1, (12, 0), ((12, 0),), u'DeleteObject', None,vaObject
			)

	def DeleteObjectData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""DeleteObjectData"""
		return self._ApplyTypes_(238, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'DeleteObjectData', None,vaObject
			, vaApp, vaKey)

	def DeleteObjects(self, vaObjects=defaultNamedNotOptArg):
		"""DeleteObjects"""
		return self._ApplyTypes_(186, 1, (12, 0), ((12, 0),), u'DeleteObjects', None,vaObjects
			)

	def DeleteSearchPath(self, vaFolder=defaultNamedNotOptArg):
		"""DeleteSearchPath"""
		return self._ApplyTypes_(512, 1, (12, 0), ((12, 0),), u'DeleteSearchPath', None,vaFolder
			)

	def DeleteStartupScript(self, vaScript=defaultNamedNotOptArg):
		"""DeleteStartupScript"""
		return self._ApplyTypes_(715, 1, (12, 0), ((12, 0),), u'DeleteStartupScript', None,vaScript
			)

	def DeleteToolBar(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""DeleteToolBar"""
		return self._ApplyTypes_(223, 1, (12, 0), ((12, 0), (12, 0)), u'DeleteToolBar', None,vaAlias
			, vaName)

	def DetailNames(self, vaLayout=defaultNamedNotOptArg, vaNames=defaultNamedOptArg):
		"""DetailNames"""
		return self._ApplyTypes_(922, 1, (12, 0), ((12, 0), (12, 16)), u'DetailNames', None,vaLayout
			, vaNames)

	def Deviation(self, var=defaultNamedNotOptArg):
		"""Deviation"""
		return self._ApplyTypes_(773, 1, (12, 0), ((12, 0),), u'Deviation', None,var
			)

	def DimScale(self, vaScale=defaultNamedNotOptArg):
		"""DimScale"""
		return self._ApplyTypes_(460, 1, (12, 0), ((12, 0),), u'DimScale', None,vaScale
			)

	def DimStyleAnglePrecision(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleAnglePrecision"""
		return self._ApplyTypes_(464, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleAnglePrecision', None,vaStyle
			, vaValue)

	def DimStyleArrowSize(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleArrowSize"""
		return self._ApplyTypes_(468, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleArrowSize', None,vaStyle
			, vaValue)

	def DimStyleCount(self):
		"""DimStyleCount"""
		return self._ApplyTypes_(451, 1, (12, 0), (), u'DimStyleCount', None,)

	def DimStyleExtension(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleExtension"""
		return self._ApplyTypes_(466, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleExtension', None,vaStyle
			, vaValue)

	def DimStyleFont(self, vaStyle=defaultNamedNotOptArg, vaFont=defaultNamedOptArg):
		"""DimStyleFont"""
		return self._ApplyTypes_(462, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleFont', None,vaStyle
			, vaFont)

	def DimStyleLeaderArrowSize(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleLeaderArrowSize"""
		return self._ApplyTypes_(704, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleLeaderArrowSize', None,vaStyle
			, vaValue)

	def DimStyleLinearPrecision(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleLinearPrecision"""
		return self._ApplyTypes_(463, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleLinearPrecision', None,vaStyle
			, vaValue)

	def DimStyleNames(self, vaSort=defaultNamedOptArg):
		"""DimStyleNames"""
		return self._ApplyTypes_(452, 1, (12, 0), ((12, 16),), u'DimStyleNames', None,vaSort
			)

	def DimStyleNumberFormat(self, vaStyle=defaultNamedNotOptArg, vaFormat=defaultNamedOptArg):
		"""DimStyleNumberFormat"""
		return self._ApplyTypes_(459, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleNumberFormat', None,vaStyle
			, vaFormat)

	def DimStyleOffset(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleOffset"""
		return self._ApplyTypes_(467, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleOffset', None,vaStyle
			, vaValue)

	def DimStyleTextAlignment(self, vaStyle=defaultNamedNotOptArg, vaAlignment=defaultNamedOptArg):
		"""DimStyleTextAlignment"""
		return self._ApplyTypes_(461, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleTextAlignment', None,vaStyle
			, vaAlignment)

	def DimStyleTextGap(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleTextGap"""
		return self._ApplyTypes_(741, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleTextGap', None,vaStyle
			, vaValue)

	def DimStyleTextHeight(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleTextHeight"""
		return self._ApplyTypes_(465, 1, (12, 0), ((12, 0), (12, 16)), u'DimStyleTextHeight', None,vaStyle
			, vaValue)

	def DimensionStyle(self, vaObject=defaultNamedNotOptArg, vaStyle=defaultNamedOptArg):
		"""DimensionStyle"""
		return self._ApplyTypes_(703, 1, (12, 0), ((12, 0), (12, 16)), u'DimensionStyle', None,vaObject
			, vaStyle)

	def DimensionText(self, vaObject=defaultNamedNotOptArg):
		"""DimensionText"""
		return self._ApplyTypes_(469, 1, (12, 0), ((12, 0),), u'DimensionText', None,vaObject
			)

	def DimensionUserText(self, vaObject=defaultNamedNotOptArg, vaText=defaultNamedOptArg):
		"""DimensionUserText"""
		return self._ApplyTypes_(563, 1, (12, 0), ((12, 0), (12, 16)), u'DimensionUserText', None,vaObject
			, vaText)

	def DimensionValue(self, vaObject=defaultNamedNotOptArg):
		"""DimensionValue"""
		return self._ApplyTypes_(568, 1, (12, 0), ((12, 0),), u'DimensionValue', None,vaObject
			)

	def DisjointMeshCount(self, vaMesh=defaultNamedNotOptArg):
		"""DisjointMeshCount"""
		return self._ApplyTypes_(721, 1, (12, 0), ((12, 0),), u'DisjointMeshCount', None,vaMesh
			)

	def DisplayOleAlerts(self, vaDisplay=defaultNamedNotOptArg):
		"""DisplayOleAlerts"""
		return self._ApplyTypes_(896, 1, (12, 0), ((12, 0),), u'DisplayOleAlerts', None,vaDisplay
			)

	def Distance(self, vaFrom=defaultNamedNotOptArg, vaTo=defaultNamedNotOptArg):
		"""Distance"""
		return self._ApplyTypes_(118, 1, (12, 0), ((12, 0), (12, 0)), u'Distance', None,vaFrom
			, vaTo)

	def DistanceToPlane(self, vaPlane=defaultNamedNotOptArg, vaPt=defaultNamedNotOptArg):
		"""DistanceToPlane"""
		return self._ApplyTypes_(628, 1, (12, 0), ((12, 0), (12, 0)), u'DistanceToPlane', None,vaPlane
			, vaPt)

	def DivideCurve(self, vaObject=defaultNamedNotOptArg, vaCount=defaultNamedNotOptArg, vaCreate=defaultNamedOptArg, vaPoints=defaultNamedOptArg):
		"""DivideCurve"""
		return self._ApplyTypes_(78, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'DivideCurve', None,vaObject
			, vaCount, vaCreate, vaPoints)

	def DivideCurveEquidistant(self, vaCurve=defaultNamedNotOptArg, vaLength=defaultNamedNotOptArg, vaCreate=defaultNamedOptArg, vaPoints=defaultNamedOptArg):
		"""DivideCurveEquidistant"""
		return self._ApplyTypes_(913, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'DivideCurveEquidistant', None,vaCurve
			, vaLength, vaCreate, vaPoints)

	def DivideCurveLength(self, vaObject=defaultNamedNotOptArg, vaLength=defaultNamedNotOptArg, vaCreate=defaultNamedOptArg, vaPoints=defaultNamedOptArg):
		"""DivideCurveLength"""
		return self._ApplyTypes_(374, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'DivideCurveLength', None,vaObject
			, vaLength, vaCreate, vaPoints)

	def DocumentDataCount(self):
		"""DocumentDataCount"""
		return self._ApplyTypes_(239, 1, (12, 0), (), u'DocumentDataCount', None,)

	def DocumentModified(self, vaModified=defaultNamedOptArg):
		"""DocumentModified"""
		return self._ApplyTypes_(323, 1, (12, 0), ((12, 16),), u'DocumentModified', None,vaModified
			)

	def DocumentName(self):
		"""DocumentName"""
		return self._ApplyTypes_(113, 1, (12, 0), (), u'DocumentName', None,)

	def DocumentPath(self):
		"""DocumentPath"""
		return self._ApplyTypes_(301, 1, (12, 0), (), u'DocumentPath', None,)

	def DocumentURL(self, vaURL=defaultNamedOptArg):
		"""DocumentURL"""
		return self._ApplyTypes_(275, 1, (12, 0), ((12, 16),), u'DocumentURL', None,vaURL
			)

	def DuplicateEdgeCurves(self, vaObject=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg):
		"""DuplicateEdgeCurves"""
		return self._ApplyTypes_(657, 1, (12, 0), ((12, 0), (12, 16)), u'DuplicateEdgeCurves', None,vaObject
			, vaSelect)

	def DuplicateMeshBorder(self, vaMesh=defaultNamedNotOptArg):
		"""DuplicateMeshBorder"""
		return self._ApplyTypes_(853, 1, (12, 0), ((12, 0),), u'DuplicateMeshBorder', None,vaMesh
			)

	def DuplicateSurfaceBorder(self, vaSurface=defaultNamedNotOptArg):
		"""DuplicateSurfaceBorder"""
		return self._ApplyTypes_(852, 1, (12, 0), ((12, 0),), u'DuplicateSurfaceBorder', None,vaSurface
			)

	def E(self):
		"""E"""
		return self._ApplyTypes_(774, 1, (12, 0), (), u'E', None,)

	def EdgeAnalysisColor(self, vaColor=defaultNamedOptArg):
		"""EdgeAnalysisColor"""
		return self._ApplyTypes_(449, 1, (12, 0), ((12, 16),), u'EdgeAnalysisColor', None,vaColor
			)

	def EdgeAnalysisMode(self, vaMode=defaultNamedOptArg):
		"""EdgeAnalysisMode"""
		return self._ApplyTypes_(448, 1, (12, 0), ((12, 16),), u'EdgeAnalysisMode', None,vaMode
			)

	def EditBox(self, vaString=defaultNamedOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""EditBox"""
		return self._ApplyTypes_(54, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'EditBox', None,vaString
			, vaPrompt, vaTitle)

	def EllipseCenterPoint(self, vaObject=defaultNamedNotOptArg):
		"""EllipseCenterPoint"""
		return self._ApplyTypes_(524, 1, (12, 0), ((12, 0),), u'EllipseCenterPoint', None,vaObject
			)

	def EllipseQuadPoints(self, vaObject=defaultNamedNotOptArg):
		"""EllipseQuadPoints"""
		return self._ApplyTypes_(525, 1, (12, 0), ((12, 0),), u'EllipseQuadPoints', None,vaObject
			)

	def EnableAutosave(self, vaEnable=defaultNamedOptArg):
		"""EnableAutosave"""
		return self._ApplyTypes_(430, 1, (12, 0), ((12, 16),), u'EnableAutosave', None,vaEnable
			)

	def EnableHistoryRecording(self, vaEnable=defaultNamedOptArg):
		"""EnableHistoryRecording"""
		return self._ApplyTypes_(735, 1, (12, 0), ((12, 16),), u'EnableHistoryRecording', None,vaEnable
			)

	def EnableLight(self, vaLight=defaultNamedNotOptArg, vaBool=defaultNamedOptArg):
		"""EnableLight"""
		return self._ApplyTypes_(158, 1, (12, 0), ((12, 0), (12, 16)), u'EnableLight', None,vaLight
			, vaBool)

	def EnableObjectGrips(self, vaObject=defaultNamedNotOptArg, vaEnable=defaultNamedOptArg):
		"""EnableObjectGrips"""
		return self._ApplyTypes_(499, 1, (12, 0), ((12, 0), (12, 16)), u'EnableObjectGrips', None,vaObject
			, vaEnable)

	def EnableObjectMesh(self, vaObject=defaultNamedNotOptArg, vaEnable=defaultNamedOptArg):
		"""EnableObjectMesh"""
		return self._ApplyTypes_(856, 1, (12, 0), ((12, 0), (12, 16)), u'EnableObjectMesh', None,vaObject
			, vaEnable)

	def EnableRedraw(self, vaRedraw=defaultNamedOptArg):
		"""EnableRedraw"""
		return self._ApplyTypes_(317, 1, (12, 0), ((12, 16),), u'EnableRedraw', None,vaRedraw
			)

	def EvaluateCurve(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""EvaluateCurve"""
		return self._ApplyTypes_(100, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'EvaluateCurve', None,vaObject
			, vaParam, vaIndex)

	def EvaluatePlane(self, vaPlane=defaultNamedNotOptArg, vaParameter=defaultNamedNotOptArg):
		"""EvaluatePlane"""
		return self._ApplyTypes_(751, 1, (12, 0), ((12, 0), (12, 0)), u'EvaluatePlane', None,vaPlane
			, vaParameter)

	def EvaluateSurface(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""EvaluateSurface"""
		return self._ApplyTypes_(205, 1, (12, 0), ((12, 0), (12, 0)), u'EvaluateSurface', None,vaObject
			, vaParam)

	def ExeFolder(self):
		"""ExeFolder"""
		return self._ApplyTypes_(21, 1, (12, 0), (), u'ExeFolder', None,)

	def Exit(self):
		"""Exit"""
		return self._ApplyTypes_(537, 1, (12, 0), (), u'Exit', None,)

	def ExpandLayer(self, vaName=defaultNamedNotOptArg, vaExpand=defaultNamedNotOptArg):
		"""ExpandLayer"""
		return self._ApplyTypes_(690, 1, (12, 0), ((12, 0), (12, 0)), u'ExpandLayer', None,vaName
			, vaExpand)

	def ExplodeBlockInstance(self, vaObject=defaultNamedNotOptArg):
		"""ExplodeBlockInstance"""
		return self._ApplyTypes_(419, 1, (12, 0), ((12, 0),), u'ExplodeBlockInstance', None,vaObject
			)

	def ExplodeCurves(self, vaObject=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""ExplodeCurves"""
		return self._ApplyTypes_(446, 1, (12, 0), ((12, 0), (12, 16)), u'ExplodeCurves', None,vaObject
			, vaDelete)

	def ExplodeHatch(self, vaObject=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""ExplodeHatch"""
		return self._ApplyTypes_(841, 1, (12, 0), ((12, 0), (12, 16)), u'ExplodeHatch', None,vaObject
			, vaDelete)

	def ExplodeMeshes(self, vaMeshes=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""ExplodeMeshes"""
		return self._ApplyTypes_(903, 1, (12, 0), ((12, 0), (12, 16)), u'ExplodeMeshes', None,vaMeshes
			, vaDelete)

	def ExplodePolysurfaces(self, vaObjects=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""ExplodePolysurfaces"""
		return self._ApplyTypes_(447, 1, (12, 0), ((12, 0), (12, 16)), u'ExplodePolysurfaces', None,vaObjects
			, vaDelete)

	def ExtendCurve(self, vaObject=defaultNamedNotOptArg, vaType=defaultNamedNotOptArg, vaSide=defaultNamedNotOptArg, vaObjects=defaultNamedNotOptArg):
		"""ExtendCurve"""
		return self._ApplyTypes_(438, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'ExtendCurve', None,vaObject
			, vaType, vaSide, vaObjects)

	def ExtendCurveLength(self, vaObject=defaultNamedNotOptArg, vaType=defaultNamedNotOptArg, vaSide=defaultNamedNotOptArg, vaLength=defaultNamedNotOptArg):
		"""ExtendCurveLength"""
		return self._ApplyTypes_(436, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'ExtendCurveLength', None,vaObject
			, vaType, vaSide, vaLength)

	def ExtendCurvePoint(self, vaObject=defaultNamedNotOptArg, vaSize=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""ExtendCurvePoint"""
		return self._ApplyTypes_(437, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ExtendCurvePoint', None,vaObject
			, vaSize, vaPoint)

	def ExtractIsoCurve(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg):
		"""ExtractIsoCurve"""
		return self._ApplyTypes_(488, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ExtractIsoCurve', None,vaObject
			, vaParam, vaDir)

	def ExtractPreviewImage(self, vaFileName=defaultNamedNotOptArg, vaModelName=defaultNamedOptArg):
		"""ExtractPreviewImage"""
		return self._ApplyTypes_(389, 1, (12, 0), ((12, 0), (12, 16)), u'ExtractPreviewImage', None,vaFileName
			, vaModelName)

	def ExtrudeCurve(self, vaCurve=defaultNamedNotOptArg, vaPath=defaultNamedNotOptArg):
		"""ExtrudeCurve"""
		return self._ApplyTypes_(538, 1, (12, 0), ((12, 0), (12, 0)), u'ExtrudeCurve', None,vaCurve
			, vaPath)

	def ExtrudeCurvePoint(self, vaCurve=defaultNamedNotOptArg, vaApex=defaultNamedNotOptArg):
		"""ExtrudeCurvePoint"""
		return self._ApplyTypes_(540, 1, (12, 0), ((12, 0), (12, 0)), u'ExtrudeCurvePoint', None,vaCurve
			, vaApex)

	def ExtrudeCurveStraight(self, vaCurve=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg):
		"""ExtrudeCurveStraight"""
		return self._ApplyTypes_(539, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ExtrudeCurveStraight', None,vaCurve
			, vaStart, vaEnd)

	def ExtrudeCurveTapered(self, vaCurve=defaultNamedNotOptArg, vaDistance=defaultNamedNotOptArg, vaDirection=defaultNamedNotOptArg, vaBase=defaultNamedNotOptArg
			, vaAngle=defaultNamedNotOptArg, vaCornerType=defaultNamedOptArg):
		"""ExtrudeCurveTapered"""
		return self._ApplyTypes_(914, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0), (12, 16)), u'ExtrudeCurveTapered', None,vaCurve
			, vaDistance, vaDirection, vaBase, vaAngle, vaCornerType
			)

	def ExtrudeSurface(self, vaSurface=defaultNamedNotOptArg, vaCurve=defaultNamedNotOptArg, vaCap=defaultNamedOptArg):
		"""ExtrudeSurface"""
		return self._ApplyTypes_(541, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'ExtrudeSurface', None,vaSurface
			, vaCurve, vaCap)

	def FairCurve(self, vaObject=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""FairCurve"""
		return self._ApplyTypes_(599, 1, (12, 0), ((12, 0), (12, 16)), u'FairCurve', None,vaObject
			, vaTolerance)

	def FindFile(self, vaFile=defaultNamedNotOptArg):
		"""FindFile"""
		return self._ApplyTypes_(81, 1, (12, 0), ((12, 0),), u'FindFile', None,vaFile
			)

	def FirstObject(self, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""FirstObject"""
		return self._ApplyTypes_(31, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'FirstObject', None,vaSelect
			, vaIncludeLights, vaIncludeGrips)

	def FitCurve(self, vaCrv=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg, vaTol=defaultNamedOptArg, vaAngTol=defaultNamedOptArg):
		"""FitCurve"""
		return self._ApplyTypes_(813, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), u'FitCurve', None,vaCrv
			, vaDegree, vaTol, vaAngTol)

	def FitSurface(self, vaSrf=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg, vaTol=defaultNamedOptArg):
		"""FitSurface"""
		return self._ApplyTypes_(815, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'FitSurface', None,vaSrf
			, vaDegree, vaTol)

	def FlashObject(self, vaObjects=defaultNamedNotOptArg, vaStyle=defaultNamedOptArg):
		"""FlashObject"""
		return self._ApplyTypes_(869, 1, (12, 0), ((12, 0), (12, 16)), u'FlashObject', None,vaObjects
			, vaStyle)

	def FlipSurface(self, vaObject=defaultNamedNotOptArg, vaReverse=defaultNamedOptArg):
		"""FlipSurface"""
		return self._ApplyTypes_(718, 1, (12, 0), ((12, 0), (12, 16)), u'FlipSurface', None,vaObject
			, vaReverse)

	def Floor(self, var=defaultNamedNotOptArg):
		"""Floor"""
		return self._ApplyTypes_(767, 1, (12, 0), ((12, 0),), u'Floor', None,var
			)

	def GetAngle(self, vaPoint=defaultNamedOptArg, vaRef=defaultNamedOptArg, vaDefault=defaultNamedOptArg, vaPrompt=defaultNamedOptArg):
		"""GetAngle"""
		return self._ApplyTypes_(277, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), u'GetAngle', None,vaPoint
			, vaRef, vaDefault, vaPrompt)

	def GetAttributeData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""GetAttributeData"""
		return self._ApplyTypes_(682, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'GetAttributeData', None,vaObject
			, vaApp, vaKey)

	def GetBoolean(self, vaPrompt=defaultNamedNotOptArg, vaItems=defaultNamedNotOptArg, vaDefaults=defaultNamedNotOptArg):
		"""GetBoolean"""
		return self._ApplyTypes_(622, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'GetBoolean', None,vaPrompt
			, vaItems, vaDefaults)

	def GetBox(self, vaMode=defaultNamedOptArg, vaPoint=defaultNamedOptArg, vaPrompt1=defaultNamedOptArg, vaPrompt2=defaultNamedOptArg
			, vaPrompt3=defaultNamedOptArg):
		"""GetBox"""
		return self._ApplyTypes_(342, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'GetBox', None,vaMode
			, vaPoint, vaPrompt1, vaPrompt2, vaPrompt3)

	def GetColor(self, vaColor=defaultNamedOptArg):
		"""GetColor"""
		return self._ApplyTypes_(65, 1, (12, 0), ((12, 16),), u'GetColor', None,vaColor
			)

	def GetCurveObject(self, vaPrompt=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg, vaSelect=defaultNamedOptArg):
		"""GetCurveObject"""
		return self._ApplyTypes_(575, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'GetCurveObject', None,vaPrompt
			, vaPreSelect, vaSelect)

	def GetDistance(self, vaPoint=defaultNamedOptArg, vaDefault=defaultNamedOptArg, vaPrompt1=defaultNamedOptArg, vaPrompt2=defaultNamedOptArg):
		"""GetDistance"""
		return self._ApplyTypes_(66, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), u'GetDistance', None,vaPoint
			, vaDefault, vaPrompt1, vaPrompt2)

	def GetDocumentData(self, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""GetDocumentData"""
		return self._ApplyTypes_(240, 1, (12, 0), ((12, 16), (12, 16)), u'GetDocumentData', None,vaApp
			, vaKey)

	def GetInteger(self, vaPrompt=defaultNamedOptArg, vaDefault=defaultNamedOptArg, vaMin=defaultNamedOptArg, vaMax=defaultNamedOptArg):
		"""GetInteger"""
		return self._ApplyTypes_(64, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), u'GetInteger', None,vaPrompt
			, vaDefault, vaMin, vaMax)

	def GetLayer(self, vaPrompt=defaultNamedOptArg, vaLayer=defaultNamedOptArg, vaNewButton=defaultNamedOptArg, vaCurrentButton=defaultNamedOptArg):
		"""GetLayer"""
		return self._ApplyTypes_(672, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), u'GetLayer', None,vaPrompt
			, vaLayer, vaNewButton, vaCurrentButton)

	def GetLinetype(self, vaLinetype=defaultNamedOptArg):
		"""GetLinetype"""
		return self._ApplyTypes_(673, 1, (12, 0), ((12, 16),), u'GetLinetype', None,vaLinetype
			)

	def GetObject(self, vaPrompt=defaultNamedOptArg, vaType=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg, vaSelect=defaultNamedOptArg
			, vaObjects=defaultNamedOptArg):
		"""GetObject"""
		return self._ApplyTypes_(32, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'GetObject', None,vaPrompt
			, vaType, vaPreSelect, vaSelect, vaObjects)

	def GetObjectData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""GetObjectData"""
		return self._ApplyTypes_(241, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'GetObjectData', None,vaObject
			, vaApp, vaKey)

	def GetObjectEx(self, vaPrompt=defaultNamedOptArg, vaType=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg, vaSelect=defaultNamedOptArg
			, vaObjects=defaultNamedOptArg):
		"""GetObjectEx"""
		return self._ApplyTypes_(819, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'GetObjectEx', None,vaPrompt
			, vaType, vaPreSelect, vaSelect, vaObjects)

	def GetObjectGrip(self, vaPrompt=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg, vaSelect=defaultNamedOptArg):
		"""GetObjectGrip"""
		return self._ApplyTypes_(561, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'GetObjectGrip', None,vaPrompt
			, vaPreSelect, vaSelect)

	def GetObjectGrips(self, vaPrompt=defaultNamedNotOptArg, vaPreSelect=defaultNamedNotOptArg, vaSelect=defaultNamedNotOptArg):
		"""GetObjectGrips"""
		return self._ApplyTypes_(562, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'GetObjectGrips', None,vaPrompt
			, vaPreSelect, vaSelect)

	def GetObjects(self, vaPrompt=defaultNamedOptArg, vaType=defaultNamedOptArg, vaGroup=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg
			, vaSelect=defaultNamedOptArg, vaObjects=defaultNamedOptArg):
		"""GetObjects"""
		return self._ApplyTypes_(33, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'GetObjects', None,vaPrompt
			, vaType, vaGroup, vaPreSelect, vaSelect, vaObjects
			)

	def GetObjectsEx(self, vaPrompt=defaultNamedOptArg, vaType=defaultNamedOptArg, vaGroup=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg
			, vaSelect=defaultNamedOptArg, vaObjects=defaultNamedOptArg):
		"""GetObjectsEx"""
		return self._ApplyTypes_(820, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'GetObjectsEx', None,vaPrompt
			, vaType, vaGroup, vaPreSelect, vaSelect, vaObjects
			)

	def GetPlugInObject(self, vaName=defaultNamedNotOptArg):
		"""GetPlugInObject"""
		return self._ApplyTypes_(636, 1, (12, 0), ((12, 0),), u'GetPlugInObject', None,vaName
			)

	def GetPoint(self, vaPrompt=defaultNamedOptArg, vaPoint=defaultNamedOptArg, vaDistance=defaultNamedOptArg, vaPlane=defaultNamedOptArg):
		"""GetPoint"""
		return self._ApplyTypes_(61, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), u'GetPoint', None,vaPrompt
			, vaPoint, vaDistance, vaPlane)

	def GetPointCoordinates(self, vaPrompt=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg):
		"""GetPointCoordinates"""
		return self._ApplyTypes_(645, 1, (12, 0), ((12, 16), (12, 16)), u'GetPointCoordinates', None,vaPrompt
			, vaPreSelect)

	def GetPointOnCurve(self, vaObject=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg):
		"""GetPointOnCurve"""
		return self._ApplyTypes_(147, 1, (12, 0), ((12, 0), (12, 16)), u'GetPointOnCurve', None,vaObject
			, vaPrompt)

	def GetPointOnLine(self, vaPrompt=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaTracking=defaultNamedOptArg):
		"""GetPointOnLine"""
		return self._ApplyTypes_(798, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'GetPointOnLine', None,vaPrompt
			, vaStart, vaEnd, vaTracking)

	def GetPointOnMesh(self, vaObject=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg):
		"""GetPointOnMesh"""
		return self._ApplyTypes_(401, 1, (12, 0), ((12, 0), (12, 16)), u'GetPointOnMesh', None,vaObject
			, vaPrompt)

	def GetPointOnPlane(self, vaPrompt=defaultNamedOptArg, vaPlane=defaultNamedOptArg, vaPoint=defaultNamedOptArg):
		"""GetPointOnPlane"""
		return self._ApplyTypes_(797, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'GetPointOnPlane', None,vaPrompt
			, vaPlane, vaPoint)

	def GetPointOnSurface(self, vaObject=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg):
		"""GetPointOnSurface"""
		return self._ApplyTypes_(148, 1, (12, 0), ((12, 0), (12, 16)), u'GetPointOnSurface', None,vaObject
			, vaPrompt)

	def GetPoints(self, vaDraw=defaultNamedOptArg, vaPlane=defaultNamedOptArg, vaPrompt1=defaultNamedOptArg, vaPrompt2=defaultNamedOptArg
			, vaMax=defaultNamedOptArg, vaBase=defaultNamedOptArg):
		"""GetPoints"""
		return self._ApplyTypes_(67, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'GetPoints', None,vaDraw
			, vaPlane, vaPrompt1, vaPrompt2, vaMax, vaBase
			)

	def GetPrintWidth(self, vaPrintWidth=defaultNamedOptArg):
		"""GetPrintWidth"""
		return self._ApplyTypes_(674, 1, (12, 0), ((12, 16),), u'GetPrintWidth', None,vaPrintWidth
			)

	def GetReal(self, vaPrompt=defaultNamedOptArg, vaDefault=defaultNamedOptArg, vaMin=defaultNamedOptArg, vaMax=defaultNamedOptArg):
		"""GetReal"""
		return self._ApplyTypes_(63, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), u'GetReal', None,vaPrompt
			, vaDefault, vaMin, vaMax)

	def GetRectangle(self, vaMode=defaultNamedOptArg, vaPoint=defaultNamedOptArg, vaPrompt1=defaultNamedOptArg, vaPrompt2=defaultNamedOptArg
			, vaPrompt3=defaultNamedOptArg, vaPlane=defaultNamedOptArg):
		"""GetRectangle"""
		return self._ApplyTypes_(341, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'GetRectangle', None,vaMode
			, vaPoint, vaPrompt1, vaPrompt2, vaPrompt3, vaPlane
			)

	def GetSettings(self, vaFile=defaultNamedNotOptArg, vaSection=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""GetSettings"""
		return self._ApplyTypes_(246, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'GetSettings', None,vaFile
			, vaSection, vaKey)

	def GetString(self, vaPrompt=defaultNamedOptArg, vaDefault=defaultNamedOptArg, vaStrings=defaultNamedOptArg):
		"""GetString"""
		return self._ApplyTypes_(62, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'GetString', None,vaPrompt
			, vaDefault, vaStrings)

	def GetSurfaceIsoParamPoint(self, vaBrep=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg):
		"""GetSurfaceIsoParamPoint"""
		return self._ApplyTypes_(775, 1, (12, 0), ((12, 0), (12, 16)), u'GetSurfaceIsoParamPoint', None,vaBrep
			, vaPrompt)

	def GetSurfaceObject(self, vaPrompt=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg, vaSelect=defaultNamedOptArg):
		"""GetSurfaceObject"""
		return self._ApplyTypes_(576, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'GetSurfaceObject', None,vaPrompt
			, vaPreSelect, vaSelect)

	def GetUserText(self, vaObject=defaultNamedNotOptArg, vaKey=defaultNamedOptArg, vaMode=defaultNamedOptArg):
		"""GetUserText"""
		return self._ApplyTypes_(729, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'GetUserText', None,vaObject
			, vaKey, vaMode)

	def GroupCount(self):
		"""GroupCount"""
		return self._ApplyTypes_(137, 1, (12, 0), (), u'GroupCount', None,)

	def GroupNames(self):
		"""GroupNames"""
		return self._ApplyTypes_(138, 1, (12, 0), (), u'GroupNames', None,)

	def HatchPattern(self, vaObject=defaultNamedNotOptArg, vaHatch=defaultNamedOptArg):
		"""HatchPattern"""
		return self._ApplyTypes_(837, 1, (12, 0), ((12, 0), (12, 16)), u'HatchPattern', None,vaObject
			, vaHatch)

	def HatchPatternCount(self):
		"""HatchPatternCount"""
		return self._ApplyTypes_(828, 1, (12, 0), (), u'HatchPatternCount', None,)

	def HatchPatternDescription(self, vaHatch=defaultNamedNotOptArg):
		"""HatchPatternDescription"""
		return self._ApplyTypes_(829, 1, (12, 0), ((12, 0),), u'HatchPatternDescription', None,vaHatch
			)

	def HatchPatternFillType(self, vaHatch=defaultNamedNotOptArg):
		"""HatchPatternFillType"""
		return self._ApplyTypes_(831, 1, (12, 0), ((12, 0),), u'HatchPatternFillType', None,vaHatch
			)

	def HatchPatternNames(self):
		"""HatchPatternNames"""
		return self._ApplyTypes_(830, 1, (12, 0), (), u'HatchPatternNames', None,)

	def HatchRotation(self, vaObject=defaultNamedNotOptArg, vaRotation=defaultNamedOptArg):
		"""HatchRotation"""
		return self._ApplyTypes_(839, 1, (12, 0), ((12, 0), (12, 16)), u'HatchRotation', None,vaObject
			, vaRotation)

	def HatchScale(self, vaObject=defaultNamedNotOptArg, vaScale=defaultNamedOptArg):
		"""HatchScale"""
		return self._ApplyTypes_(838, 1, (12, 0), ((12, 0), (12, 16)), u'HatchScale', None,vaObject
			, vaScale)

	def Help(self, vaTopic=defaultNamedOptArg):
		"""Help"""
		return self._ApplyTypes_(22, 1, (12, 0), ((12, 16),), u'Help', None,vaTopic
			)

	def HiddenObjects(self, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""HiddenObjects"""
		return self._ApplyTypes_(366, 1, (12, 0), ((12, 16), (12, 16)), u'HiddenObjects', None,vaIncludeLights
			, vaIncludeGrips)

	def HideGroup(self, vaName=defaultNamedNotOptArg):
		"""HideGroup"""
		return self._ApplyTypes_(871, 1, (12, 0), ((12, 0),), u'HideGroup', None,vaName
			)

	def HideObject(self, vaObject=defaultNamedNotOptArg):
		"""HideObject"""
		return self._ApplyTypes_(187, 1, (12, 0), ((12, 0),), u'HideObject', None,vaObject
			)

	def HideObjects(self, vaObjects=defaultNamedNotOptArg):
		"""HideObjects"""
		return self._ApplyTypes_(303, 1, (12, 0), ((12, 0),), u'HideObjects', None,vaObjects
			)

	def HideToolBar(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""HideToolBar"""
		return self._ApplyTypes_(224, 1, (12, 0), ((12, 0), (12, 0)), u'HideToolBar', None,vaAlias
			, vaName)

	def HtmlBox(self, vaFile=defaultNamedNotOptArg, vaArgs=defaultNamedOptArg, vaOptions=defaultNamedOptArg, vaModal=defaultNamedOptArg):
		"""HtmlBox"""
		return self._ApplyTypes_(276, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), u'HtmlBox', None,vaFile
			, vaArgs, vaOptions, vaModal)

	def Hypot(self, vx=defaultNamedNotOptArg, vy=defaultNamedOptArg):
		"""Hypot"""
		return self._ApplyTypes_(765, 1, (12, 0), ((12, 0), (12, 16)), u'Hypot', None,vx
			, vy)

	def InCommand(self, vaScript=defaultNamedOptArg):
		"""InCommand"""
		return self._ApplyTypes_(596, 1, (12, 0), ((12, 16),), u'InCommand', None,vaScript
			)

	def InsertBlock(self, vaName=defaultNamedNotOptArg, vaPt=defaultNamedNotOptArg, vaScale=defaultNamedOptArg, vaAngle=defaultNamedOptArg
			, vaRotate=defaultNamedOptArg):
		"""InsertBlock"""
		return self._ApplyTypes_(633, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16)), u'InsertBlock', None,vaName
			, vaPt, vaScale, vaAngle, vaRotate)

	def InsertCurveKnot(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaSym=defaultNamedOptArg):
		"""InsertCurveKnot"""
		return self._ApplyTypes_(515, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'InsertCurveKnot', None,vaObject
			, vaParam, vaSym)

	def InsertSurfaceKnot(self, vaSrf=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg, vaSym=defaultNamedOptArg):
		"""InsertSurfaceKnot"""
		return self._ApplyTypes_(516, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'InsertSurfaceKnot', None,vaSrf
			, vaParam, vaDir, vaSym)

	def InstallFolder(self):
		"""InstallFolder"""
		return self._ApplyTypes_(23, 1, (12, 0), (), u'InstallFolder', None,)

	def IntegerBox(self, vaPrompt=defaultNamedOptArg, vaInteger=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""IntegerBox"""
		return self._ApplyTypes_(55, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'IntegerBox', None,vaPrompt
			, vaInteger, vaTitle)

	def IntersectBreps(self, vaBrep0=defaultNamedNotOptArg, vaBrep1=defaultNamedNotOptArg, vaTol=defaultNamedOptArg):
		"""IntersectBreps"""
		return self._ApplyTypes_(544, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'IntersectBreps', None,vaBrep0
			, vaBrep1, vaTol)

	def IntersectPlanes(self, vaPlaneA=defaultNamedNotOptArg, vaPlaneB=defaultNamedNotOptArg, vaPlaneC=defaultNamedNotOptArg):
		"""IntersectPlanes"""
		return self._ApplyTypes_(745, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'IntersectPlanes', None,vaPlaneA
			, vaPlaneB, vaPlaneC)

	def InvertSelectedObjects(self, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""InvertSelectedObjects"""
		return self._ApplyTypes_(34, 1, (12, 0), ((12, 16), (12, 16)), u'InvertSelectedObjects', None,vaIncludeLights
			, vaIncludeGrips)

	def IsAlias(self, vaName=defaultNamedNotOptArg):
		"""IsAlias"""
		return self._ApplyTypes_(711, 1, (12, 0), ((12, 0),), u'IsAlias', None,vaName
			)

	def IsAlignedDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsAlignedDimension"""
		return self._ApplyTypes_(566, 1, (12, 0), ((12, 0),), u'IsAlignedDimension', None,vaObject
			)

	def IsAngularDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsAngularDimension"""
		return self._ApplyTypes_(338, 1, (12, 0), ((12, 0),), u'IsAngularDimension', None,vaObject
			)

	def IsArc(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsArc"""
		return self._ApplyTypes_(101, 1, (12, 0), ((12, 0), (12, 16)), u'IsArc', None,vaObject
			, vaIndex)

	def IsAttributeData(self, vaObject=defaultNamedNotOptArg):
		"""IsAttributeData"""
		return self._ApplyTypes_(686, 1, (12, 0), ((12, 0),), u'IsAttributeData', None,vaObject
			)

	def IsBackgroundBitmap(self, vaView=defaultNamedOptArg):
		"""IsBackgroundBitmap"""
		return self._ApplyTypes_(779, 1, (12, 0), ((12, 16),), u'IsBackgroundBitmap', None,vaView
			)

	def IsBlock(self, vaName=defaultNamedNotOptArg):
		"""IsBlock"""
		return self._ApplyTypes_(398, 1, (12, 0), ((12, 0),), u'IsBlock', None,vaName
			)

	def IsBlockEmbedded(self, vaName=defaultNamedNotOptArg):
		"""IsBlockEmbedded"""
		return self._ApplyTypes_(405, 1, (12, 0), ((12, 0),), u'IsBlockEmbedded', None,vaName
			)

	def IsBlockInUse(self, vaName=defaultNamedNotOptArg, vaWhere=defaultNamedOptArg):
		"""IsBlockInUse"""
		return self._ApplyTypes_(406, 1, (12, 0), ((12, 0), (12, 16)), u'IsBlockInUse', None,vaName
			, vaWhere)

	def IsBlockInstance(self, vaObject=defaultNamedNotOptArg):
		"""IsBlockInstance"""
		return self._ApplyTypes_(420, 1, (12, 0), ((12, 0),), u'IsBlockInstance', None,vaObject
			)

	def IsBlockReference(self, vaName=defaultNamedNotOptArg):
		"""IsBlockReference"""
		return self._ApplyTypes_(407, 1, (12, 0), ((12, 0),), u'IsBlockReference', None,vaName
			)

	def IsBrep(self, vaObject=defaultNamedNotOptArg):
		"""IsBrep"""
		return self._ApplyTypes_(206, 1, (12, 0), ((12, 0),), u'IsBrep', None,vaObject
			)

	def IsBrepManifold(self, vaBrep=defaultNamedNotOptArg):
		"""IsBrepManifold"""
		return self._ApplyTypes_(854, 1, (12, 0), ((12, 0),), u'IsBrepManifold', None,vaBrep
			)

	def IsCircle(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCircle"""
		return self._ApplyTypes_(102, 1, (12, 0), ((12, 0), (12, 16)), u'IsCircle', None,vaObject
			, vaIndex)

	def IsClippingPlane(self, vaObject=defaultNamedNotOptArg):
		"""IsClippingPlane"""
		return self._ApplyTypes_(905, 1, (12, 0), ((12, 0),), u'IsClippingPlane', None,vaObject
			)

	def IsCommand(self, vaName=defaultNamedNotOptArg):
		"""IsCommand"""
		return self._ApplyTypes_(530, 1, (12, 0), ((12, 0),), u'IsCommand', None,vaName
			)

	def IsCone(self, vaObject=defaultNamedNotOptArg):
		"""IsCone"""
		return self._ApplyTypes_(885, 1, (12, 0), ((12, 0),), u'IsCone', None,vaObject
			)

	def IsCurve(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCurve"""
		return self._ApplyTypes_(103, 1, (12, 0), ((12, 0), (12, 16)), u'IsCurve', None,vaObject
			, vaIndex)

	def IsCurveClosable(self, vaObject=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""IsCurveClosable"""
		return self._ApplyTypes_(441, 1, (12, 0), ((12, 0), (12, 16)), u'IsCurveClosable', None,vaObject
			, vaTolerance)

	def IsCurveClosed(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCurveClosed"""
		return self._ApplyTypes_(104, 1, (12, 0), ((12, 0), (12, 16)), u'IsCurveClosed', None,vaObject
			, vaIndex)

	def IsCurveInPlane(self, vaObject=defaultNamedNotOptArg, vaPlane=defaultNamedOptArg):
		"""IsCurveInPlane"""
		return self._ApplyTypes_(483, 1, (12, 0), ((12, 0), (12, 16)), u'IsCurveInPlane', None,vaObject
			, vaPlane)

	def IsCurveLinear(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCurveLinear"""
		return self._ApplyTypes_(105, 1, (12, 0), ((12, 0), (12, 16)), u'IsCurveLinear', None,vaObject
			, vaIndex)

	def IsCurvePeriodic(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCurvePeriodic"""
		return self._ApplyTypes_(106, 1, (12, 0), ((12, 0), (12, 16)), u'IsCurvePeriodic', None,vaObject
			, vaIndex)

	def IsCurvePlanar(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCurvePlanar"""
		return self._ApplyTypes_(107, 1, (12, 0), ((12, 0), (12, 16)), u'IsCurvePlanar', None,vaObject
			, vaIndex)

	def IsCurveRational(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg):
		"""IsCurveRational"""
		return self._ApplyTypes_(380, 1, (12, 0), ((12, 0), (12, 0)), u'IsCurveRational', None,vaObject
			, vaIndex)

	def IsCylinder(self, vaObject=defaultNamedNotOptArg):
		"""IsCylinder"""
		return self._ApplyTypes_(884, 1, (12, 0), ((12, 0),), u'IsCylinder', None,vaObject
			)

	def IsDetail(self, vaLayout=defaultNamedNotOptArg, vaDetail=defaultNamedNotOptArg):
		"""IsDetail"""
		return self._ApplyTypes_(921, 1, (12, 0), ((12, 0), (12, 0)), u'IsDetail', None,vaLayout
			, vaDetail)

	def IsDiameterDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsDiameterDimension"""
		return self._ApplyTypes_(565, 1, (12, 0), ((12, 0),), u'IsDiameterDimension', None,vaObject
			)

	def IsDimStyle(self, vaStyle=defaultNamedNotOptArg):
		"""IsDimStyle"""
		return self._ApplyTypes_(454, 1, (12, 0), ((12, 0),), u'IsDimStyle', None,vaStyle
			)

	def IsDimStyleReference(self, vaStyle=defaultNamedNotOptArg):
		"""IsDimStyleReference"""
		return self._ApplyTypes_(457, 1, (12, 0), ((12, 0),), u'IsDimStyleReference', None,vaStyle
			)

	def IsDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsDimension"""
		return self._ApplyTypes_(564, 1, (12, 0), ((12, 0),), u'IsDimension', None,vaObject
			)

	def IsDirectionalLight(self, vaLight=defaultNamedNotOptArg):
		"""IsDirectionalLight"""
		return self._ApplyTypes_(159, 1, (12, 0), ((12, 0),), u'IsDirectionalLight', None,vaLight
			)

	def IsDocumentData(self):
		"""IsDocumentData"""
		return self._ApplyTypes_(278, 1, (12, 0), (), u'IsDocumentData', None,)

	def IsDocumentModified(self):
		"""IsDocumentModified"""
		return self._ApplyTypes_(273, 1, (12, 0), (), u'IsDocumentModified', None,)

	def IsEllipse(self, vaObject=defaultNamedNotOptArg):
		"""IsEllipse"""
		return self._ApplyTypes_(523, 1, (12, 0), ((12, 0),), u'IsEllipse', None,vaObject
			)

	def IsGroup(self, vaName=defaultNamedNotOptArg):
		"""IsGroup"""
		return self._ApplyTypes_(139, 1, (12, 0), ((12, 0),), u'IsGroup', None,vaName
			)

	def IsGroupEmpty(self, vaName=defaultNamedNotOptArg):
		"""IsGroupEmpty"""
		return self._ApplyTypes_(140, 1, (12, 0), ((12, 0),), u'IsGroupEmpty', None,vaName
			)

	def IsHatch(self, vaObject=defaultNamedNotOptArg):
		"""IsHatch"""
		return self._ApplyTypes_(840, 1, (12, 0), ((12, 0),), u'IsHatch', None,vaObject
			)

	def IsHatchPattern(self, vaHatch=defaultNamedNotOptArg):
		"""IsHatchPattern"""
		return self._ApplyTypes_(832, 1, (12, 0), ((12, 0),), u'IsHatchPattern', None,vaHatch
			)

	def IsHatchPatternCurrent(self, vaHatch=defaultNamedNotOptArg):
		"""IsHatchPatternCurrent"""
		return self._ApplyTypes_(833, 1, (12, 0), ((12, 0),), u'IsHatchPatternCurrent', None,vaHatch
			)

	def IsHatchPatternReference(self, vaHatch=defaultNamedNotOptArg):
		"""IsHatchPatternReference"""
		return self._ApplyTypes_(834, 1, (12, 0), ((12, 0),), u'IsHatchPatternReference', None,vaHatch
			)

	def IsLayer(self, vaName=defaultNamedNotOptArg):
		"""IsLayer"""
		return self._ApplyTypes_(6, 1, (12, 0), ((12, 0),), u'IsLayer', None,vaName
			)

	def IsLayerChangeable(self, vaName=defaultNamedNotOptArg):
		"""IsLayerChangeable"""
		return self._ApplyTypes_(18, 1, (12, 0), ((12, 0),), u'IsLayerChangeable', None,vaName
			)

	def IsLayerChildOf(self, vaName=defaultNamedNotOptArg, vaParent=defaultNamedNotOptArg):
		"""IsLayerChildOf"""
		return self._ApplyTypes_(692, 1, (12, 0), ((12, 0), (12, 0)), u'IsLayerChildOf', None,vaName
			, vaParent)

	def IsLayerCurrent(self, vaName=defaultNamedNotOptArg):
		"""IsLayerCurrent"""
		return self._ApplyTypes_(313, 1, (12, 0), ((12, 0),), u'IsLayerCurrent', None,vaName
			)

	def IsLayerEmpty(self, vaName=defaultNamedNotOptArg):
		"""IsLayerEmpty"""
		return self._ApplyTypes_(7, 1, (12, 0), ((12, 0),), u'IsLayerEmpty', None,vaName
			)

	def IsLayerExpanded(self, vaName=defaultNamedNotOptArg):
		"""IsLayerExpanded"""
		return self._ApplyTypes_(689, 1, (12, 0), ((12, 0),), u'IsLayerExpanded', None,vaName
			)

	def IsLayerLocked(self, vaName=defaultNamedNotOptArg):
		"""IsLayerLocked"""
		return self._ApplyTypes_(8, 1, (12, 0), ((12, 0),), u'IsLayerLocked', None,vaName
			)

	def IsLayerOn(self, vaName=defaultNamedNotOptArg):
		"""IsLayerOn"""
		return self._ApplyTypes_(9, 1, (12, 0), ((12, 0),), u'IsLayerOn', None,vaName
			)

	def IsLayerParentOf(self, vaName=defaultNamedNotOptArg, vaParent=defaultNamedNotOptArg):
		"""IsLayerParentOf"""
		return self._ApplyTypes_(693, 1, (12, 0), ((12, 0), (12, 0)), u'IsLayerParentOf', None,vaName
			, vaParent)

	def IsLayerReference(self, vaName=defaultNamedNotOptArg):
		"""IsLayerReference"""
		return self._ApplyTypes_(10, 1, (12, 0), ((12, 0),), u'IsLayerReference', None,vaName
			)

	def IsLayerSelectable(self, vaName=defaultNamedNotOptArg):
		"""IsLayerSelectable"""
		return self._ApplyTypes_(19, 1, (12, 0), ((12, 0),), u'IsLayerSelectable', None,vaName
			)

	def IsLayerVisible(self, vaName=defaultNamedNotOptArg):
		"""IsLayerVisible"""
		return self._ApplyTypes_(20, 1, (12, 0), ((12, 0),), u'IsLayerVisible', None,vaName
			)

	def IsLayout(self, vaLayout=defaultNamedNotOptArg):
		"""IsLayout"""
		return self._ApplyTypes_(920, 1, (12, 0), ((12, 0),), u'IsLayout', None,vaLayout
			)

	def IsLayoutObject(self, vaObject=defaultNamedNotOptArg):
		"""IsLayoutObject"""
		return self._ApplyTypes_(919, 1, (12, 0), ((12, 0),), u'IsLayoutObject', None,vaObject
			)

	def IsLeader(self, vaObject=defaultNamedNotOptArg):
		"""IsLeader"""
		return self._ApplyTypes_(337, 1, (12, 0), ((12, 0),), u'IsLeader', None,vaObject
			)

	def IsLight(self, vaLight=defaultNamedNotOptArg):
		"""IsLight"""
		return self._ApplyTypes_(160, 1, (12, 0), ((12, 0),), u'IsLight', None,vaLight
			)

	def IsLightEnabled(self, vaLight=defaultNamedNotOptArg):
		"""IsLightEnabled"""
		return self._ApplyTypes_(161, 1, (12, 0), ((12, 0),), u'IsLightEnabled', None,vaLight
			)

	def IsLightReference(self, vaLight=defaultNamedNotOptArg):
		"""IsLightReference"""
		return self._ApplyTypes_(162, 1, (12, 0), ((12, 0),), u'IsLightReference', None,vaLight
			)

	def IsLine(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsLine"""
		return self._ApplyTypes_(108, 1, (12, 0), ((12, 0), (12, 16)), u'IsLine', None,vaObject
			, vaIndex)

	def IsLinearDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsLinearDimension"""
		return self._ApplyTypes_(339, 1, (12, 0), ((12, 0),), u'IsLinearDimension', None,vaObject
			)

	def IsLinearLight(self, vaLight=defaultNamedNotOptArg):
		"""IsLinearLight"""
		return self._ApplyTypes_(163, 1, (12, 0), ((12, 0),), u'IsLinearLight', None,vaLight
			)

	def IsLinetype(self, vaName=defaultNamedNotOptArg):
		"""IsLinetype"""
		return self._ApplyTypes_(607, 1, (12, 0), ((12, 0),), u'IsLinetype', None,vaName
			)

	def IsLinetypeReference(self, vaName=defaultNamedNotOptArg):
		"""IsLinetypeReference"""
		return self._ApplyTypes_(608, 1, (12, 0), ((12, 0),), u'IsLinetypeReference', None,vaName
			)

	def IsMaterialDefault(self, vaIndex=defaultNamedNotOptArg):
		"""IsMaterialDefault"""
		return self._ApplyTypes_(175, 1, (12, 0), ((12, 0),), u'IsMaterialDefault', None,vaIndex
			)

	def IsMaterialReference(self, vaIndex=defaultNamedNotOptArg):
		"""IsMaterialReference"""
		return self._ApplyTypes_(176, 1, (12, 0), ((12, 0),), u'IsMaterialReference', None,vaIndex
			)

	def IsMesh(self, vaObject=defaultNamedNotOptArg):
		"""IsMesh"""
		return self._ApplyTypes_(119, 1, (12, 0), ((12, 0),), u'IsMesh', None,vaObject
			)

	def IsMeshClosed(self, vaObject=defaultNamedNotOptArg):
		"""IsMeshClosed"""
		return self._ApplyTypes_(355, 1, (12, 0), ((12, 0),), u'IsMeshClosed', None,vaObject
			)

	def IsMeshManifold(self, vaMesh=defaultNamedNotOptArg):
		"""IsMeshManifold"""
		return self._ApplyTypes_(855, 1, (12, 0), ((12, 0),), u'IsMeshManifold', None,vaMesh
			)

	def IsNurbsCurve(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsNurbsCurve"""
		return self._ApplyTypes_(109, 1, (12, 0), ((12, 0), (12, 16)), u'IsNurbsCurve', None,vaObject
			, vaIndex)

	def IsObject(self, vaObject=defaultNamedNotOptArg):
		"""IsObject"""
		return self._ApplyTypes_(46, 1, (12, 0), ((12, 0),), u'IsObject', None,vaObject
			)

	def IsObjectData(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectData"""
		return self._ApplyTypes_(279, 1, (12, 0), ((12, 0),), u'IsObjectData', None,vaObject
			)

	def IsObjectHidden(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectHidden"""
		return self._ApplyTypes_(47, 1, (12, 0), ((12, 0),), u'IsObjectHidden', None,vaObject
			)

	def IsObjectInBox(self, vaObject=defaultNamedNotOptArg, vaBox=defaultNamedNotOptArg, vaFlag=defaultNamedOptArg):
		"""IsObjectInBox"""
		return self._ApplyTypes_(799, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'IsObjectInBox', None,vaObject
			, vaBox, vaFlag)

	def IsObjectInGroup(self, vaObject=defaultNamedNotOptArg, vaGroup=defaultNamedNotOptArg):
		"""IsObjectInGroup"""
		return self._ApplyTypes_(188, 1, (12, 0), ((12, 0), (12, 0)), u'IsObjectInGroup', None,vaObject
			, vaGroup)

	def IsObjectLocked(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectLocked"""
		return self._ApplyTypes_(48, 1, (12, 0), ((12, 0),), u'IsObjectLocked', None,vaObject
			)

	def IsObjectNormal(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectNormal"""
		return self._ApplyTypes_(49, 1, (12, 0), ((12, 0),), u'IsObjectNormal', None,vaObject
			)

	def IsObjectReference(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectReference"""
		return self._ApplyTypes_(271, 1, (12, 0), ((12, 0),), u'IsObjectReference', None,vaObject
			)

	def IsObjectSelectable(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectSelectable"""
		return self._ApplyTypes_(307, 1, (12, 0), ((12, 0),), u'IsObjectSelectable', None,vaObject
			)

	def IsObjectSelected(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectSelected"""
		return self._ApplyTypes_(50, 1, (12, 0), ((12, 0),), u'IsObjectSelected', None,vaObject
			)

	def IsObjectSolid(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectSolid"""
		return self._ApplyTypes_(189, 1, (12, 0), ((12, 0),), u'IsObjectSolid', None,vaObject
			)

	def IsObjectValid(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectValid"""
		return self._ApplyTypes_(522, 1, (12, 0), ((12, 0),), u'IsObjectValid', None,vaObject
			)

	def IsOrdinateDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsOrdinateDimension"""
		return self._ApplyTypes_(659, 1, (12, 0), ((12, 0),), u'IsOrdinateDimension', None,vaObject
			)

	def IsParameterOnSurface(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""IsParameterOnSurface"""
		return self._ApplyTypes_(879, 1, (12, 0), ((12, 0), (12, 0)), u'IsParameterOnSurface', None,vaObject
			, vaParam)

	def IsPlaneSurface(self, vaObject=defaultNamedNotOptArg):
		"""IsPlaneSurface"""
		return self._ApplyTypes_(638, 1, (12, 0), ((12, 0),), u'IsPlaneSurface', None,vaObject
			)

	def IsPoint(self, vaObject=defaultNamedNotOptArg):
		"""IsPoint"""
		return self._ApplyTypes_(120, 1, (12, 0), ((12, 0),), u'IsPoint', None,vaObject
			)

	def IsPointCloud(self, vaObject=defaultNamedNotOptArg):
		"""IsPointCloud"""
		return self._ApplyTypes_(121, 1, (12, 0), ((12, 0),), u'IsPointCloud', None,vaObject
			)

	def IsPointInSurface(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""IsPointInSurface"""
		return self._ApplyTypes_(443, 1, (12, 0), ((12, 0), (12, 0)), u'IsPointInSurface', None,vaObject
			, vaPoint)

	def IsPointLight(self, vaLight=defaultNamedNotOptArg):
		"""IsPointLight"""
		return self._ApplyTypes_(164, 1, (12, 0), ((12, 0),), u'IsPointLight', None,vaLight
			)

	def IsPointOnCurve(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsPointOnCurve"""
		return self._ApplyTypes_(318, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'IsPointOnCurve', None,vaObject
			, vaPoint, vaIndex)

	def IsPointOnSurface(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""IsPointOnSurface"""
		return self._ApplyTypes_(319, 1, (12, 0), ((12, 0), (12, 0)), u'IsPointOnSurface', None,vaObject
			, vaPoint)

	def IsPolyCurve(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsPolyCurve"""
		return self._ApplyTypes_(368, 1, (12, 0), ((12, 0), (12, 16)), u'IsPolyCurve', None,vaObject
			, vaIndex)

	def IsPolySurface(self, vaObject=defaultNamedNotOptArg):
		"""IsPolySurface"""
		return self._ApplyTypes_(207, 1, (12, 0), ((12, 0),), u'IsPolySurface', None,vaObject
			)

	def IsPolySurfaceClosed(self, vaObject=defaultNamedNotOptArg):
		"""IsPolySurfaceClosed"""
		return self._ApplyTypes_(208, 1, (12, 0), ((12, 0),), u'IsPolySurfaceClosed', None,vaObject
			)

	def IsPolySurfacePlanar(self, vaObject=defaultNamedNotOptArg):
		"""IsPolySurfacePlanar"""
		return self._ApplyTypes_(209, 1, (12, 0), ((12, 0),), u'IsPolySurfacePlanar', None,vaObject
			)

	def IsPolyline(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsPolyline"""
		return self._ApplyTypes_(110, 1, (12, 0), ((12, 0), (12, 16)), u'IsPolyline', None,vaObject
			, vaIndex)

	def IsProcedure(self, vaName=defaultNamedNotOptArg):
		"""IsProcedure"""
		return self._ApplyTypes_(287, 1, (12, 0), ((12, 0),), u'IsProcedure', None,vaName
			)

	def IsRadialDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsRadialDimension"""
		return self._ApplyTypes_(340, 1, (12, 0), ((12, 0),), u'IsRadialDimension', None,vaObject
			)

	def IsRectangularLight(self, vaLight=defaultNamedNotOptArg):
		"""IsRectangularLight"""
		return self._ApplyTypes_(165, 1, (12, 0), ((12, 0),), u'IsRectangularLight', None,vaLight
			)

	def IsSphere(self, vaObject=defaultNamedNotOptArg):
		"""IsSphere"""
		return self._ApplyTypes_(883, 1, (12, 0), ((12, 0),), u'IsSphere', None,vaObject
			)

	def IsSpotLight(self, vaLight=defaultNamedNotOptArg):
		"""IsSpotLight"""
		return self._ApplyTypes_(166, 1, (12, 0), ((12, 0),), u'IsSpotLight', None,vaLight
			)

	def IsSurface(self, vaObject=defaultNamedNotOptArg):
		"""IsSurface"""
		return self._ApplyTypes_(210, 1, (12, 0), ((12, 0),), u'IsSurface', None,vaObject
			)

	def IsSurfaceClosed(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""IsSurfaceClosed"""
		return self._ApplyTypes_(211, 1, (12, 0), ((12, 0), (12, 0)), u'IsSurfaceClosed', None,vaObject
			, vaValue)

	def IsSurfacePeriodic(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""IsSurfacePeriodic"""
		return self._ApplyTypes_(212, 1, (12, 0), ((12, 0), (12, 0)), u'IsSurfacePeriodic', None,vaObject
			, vaValue)

	def IsSurfacePlanar(self, vaObject=defaultNamedNotOptArg, vaTol=defaultNamedOptArg):
		"""IsSurfacePlanar"""
		return self._ApplyTypes_(213, 1, (12, 0), ((12, 0), (12, 16)), u'IsSurfacePlanar', None,vaObject
			, vaTol)

	def IsSurfaceRational(self, vaObject=defaultNamedNotOptArg):
		"""IsSurfaceRational"""
		return self._ApplyTypes_(434, 1, (12, 0), ((12, 0),), u'IsSurfaceRational', None,vaObject
			)

	def IsSurfaceSingular(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""IsSurfaceSingular"""
		return self._ApplyTypes_(214, 1, (12, 0), ((12, 0), (12, 0)), u'IsSurfaceSingular', None,vaObject
			, vaValue)

	def IsSurfaceTrimmed(self, vaObject=defaultNamedNotOptArg):
		"""IsSurfaceTrimmed"""
		return self._ApplyTypes_(269, 1, (12, 0), ((12, 0),), u'IsSurfaceTrimmed', None,vaObject
			)

	def IsText(self, vaObject=defaultNamedNotOptArg):
		"""IsText"""
		return self._ApplyTypes_(122, 1, (12, 0), ((12, 0),), u'IsText', None,vaObject
			)

	def IsTextDot(self, vaObject=defaultNamedNotOptArg):
		"""IsTextDot"""
		return self._ApplyTypes_(336, 1, (12, 0), ((12, 0),), u'IsTextDot', None,vaObject
			)

	def IsToolBar(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""IsToolBar"""
		return self._ApplyTypes_(225, 1, (12, 0), ((12, 0), (12, 0)), u'IsToolBar', None,vaAlias
			, vaName)

	def IsToolBarCollection(self, vaFile=defaultNamedNotOptArg):
		"""IsToolBarCollection"""
		return self._ApplyTypes_(226, 1, (12, 0), ((12, 0),), u'IsToolBarCollection', None,vaFile
			)

	def IsToolBarVisible(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""IsToolBarVisible"""
		return self._ApplyTypes_(227, 1, (12, 0), ((12, 0), (12, 0)), u'IsToolBarVisible', None,vaAlias
			, vaName)

	def IsToolbarDocked(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""IsToolbarDocked"""
		return self._ApplyTypes_(724, 1, (12, 0), ((12, 0), (12, 0)), u'IsToolbarDocked', None,vaAlias
			, vaName)

	def IsTorus(self, vaObject=defaultNamedNotOptArg):
		"""IsTorus"""
		return self._ApplyTypes_(886, 1, (12, 0), ((12, 0),), u'IsTorus', None,vaObject
			)

	def IsUserText(self, vaObject=defaultNamedNotOptArg):
		"""IsUserText"""
		return self._ApplyTypes_(730, 1, (12, 0), ((12, 0),), u'IsUserText', None,vaObject
			)

	def IsVectorParallelTo(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""IsVectorParallelTo"""
		return self._ApplyTypes_(660, 1, (12, 0), ((12, 0), (12, 0)), u'IsVectorParallelTo', None,vaVec0
			, vaVec1)

	def IsVectorPerpendicularTo(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""IsVectorPerpendicularTo"""
		return self._ApplyTypes_(661, 1, (12, 0), ((12, 0), (12, 0)), u'IsVectorPerpendicularTo', None,vaVec0
			, vaVec1)

	def IsVectorTiny(self, vaVec=defaultNamedNotOptArg):
		"""IsVectorTiny"""
		return self._ApplyTypes_(610, 1, (12, 0), ((12, 0),), u'IsVectorTiny', None,vaVec
			)

	def IsVectorZero(self, vaVec=defaultNamedNotOptArg):
		"""IsVectorZero"""
		return self._ApplyTypes_(611, 1, (12, 0), ((12, 0),), u'IsVectorZero', None,vaVec
			)

	def IsView(self, vaView=defaultNamedNotOptArg):
		"""IsView"""
		return self._ApplyTypes_(252, 1, (12, 0), ((12, 0),), u'IsView', None,vaView
			)

	def IsViewCurrent(self, vaView=defaultNamedNotOptArg):
		"""IsViewCurrent"""
		return self._ApplyTypes_(253, 1, (12, 0), ((12, 0),), u'IsViewCurrent', None,vaView
			)

	def IsViewMaximized(self, vaView=defaultNamedOptArg):
		"""IsViewMaximized"""
		return self._ApplyTypes_(254, 1, (12, 0), ((12, 16),), u'IsViewMaximized', None,vaView
			)

	def IsViewPerspective(self, vaView=defaultNamedOptArg):
		"""IsViewPerspective"""
		return self._ApplyTypes_(255, 1, (12, 0), ((12, 16),), u'IsViewPerspective', None,vaView
			)

	def IsViewTitleVisible(self, vaView=defaultNamedOptArg):
		"""IsViewTitleVisible"""
		return self._ApplyTypes_(256, 1, (12, 0), ((12, 16),), u'IsViewTitleVisible', None,vaView
			)

	def IsVisibleInView(self, vaObject=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""IsVisibleInView"""
		return self._ApplyTypes_(727, 1, (12, 0), ((12, 0), (12, 16)), u'IsVisibleInView', None,vaObject
			, vaView)

	def IsWallpaper(self, vaView=defaultNamedOptArg):
		"""IsWallpaper"""
		return self._ApplyTypes_(531, 1, (12, 0), ((12, 16),), u'IsWallpaper', None,vaView
			)

	def IsXformIdentity(self, vaXform=defaultNamedNotOptArg):
		"""IsXformIdentity"""
		return self._ApplyTypes_(786, 1, (12, 0), ((12, 0),), u'IsXformIdentity', None,vaXform
			)

	def IsXformSimilarity(self, vaXform=defaultNamedNotOptArg):
		"""IsXformSimilarity"""
		return self._ApplyTypes_(787, 1, (12, 0), ((12, 0),), u'IsXformSimilarity', None,vaXform
			)

	def IsXformZero(self, vaXform=defaultNamedNotOptArg):
		"""IsXformZero"""
		return self._ApplyTypes_(785, 1, (12, 0), ((12, 0),), u'IsXformZero', None,vaXform
			)

	def JoinArrays(self, vaFirst=defaultNamedNotOptArg, vaSecond=defaultNamedNotOptArg):
		"""JoinArrays"""
		return self._ApplyTypes_(547, 1, (12, 0), ((12, 0), (12, 0)), u'JoinArrays', None,vaFirst
			, vaSecond)

	def JoinCurves(self, vaObjects=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""JoinCurves"""
		return self._ApplyTypes_(111, 1, (12, 0), ((12, 0), (12, 16)), u'JoinCurves', None,vaObjects
			, vaDelete)

	def JoinSurfaces(self, vaObjects=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""JoinSurfaces"""
		return self._ApplyTypes_(487, 1, (12, 0), ((12, 0), (12, 16)), u'JoinSurfaces', None,vaObjects
			, vaDelete)

	def LastCommandName(self):
		"""LastCommandName"""
		return self._ApplyTypes_(594, 1, (12, 0), (), u'LastCommandName', None,)

	def LastCommandResult(self):
		"""LastCommandResult"""
		return self._ApplyTypes_(292, 1, (12, 0), (), u'LastCommandResult', None,)

	def LastCreatedObjects(self, vaSelect=defaultNamedOptArg):
		"""LastCreatedObjects"""
		return self._ApplyTypes_(485, 1, (12, 0), ((12, 16),), u'LastCreatedObjects', None,vaSelect
			)

	def LastLoadedScriptFile(self):
		"""LastLoadedScriptFile"""
		return self._ApplyTypes_(373, 1, (12, 0), (), u'LastLoadedScriptFile', None,)

	def LastObject(self, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""LastObject"""
		return self._ApplyTypes_(35, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'LastObject', None,vaSelect
			, vaIncludeLights, vaIncludeGrips)

	def LayerChildCount(self, vaName=defaultNamedNotOptArg):
		"""LayerChildCount"""
		return self._ApplyTypes_(694, 1, (12, 0), ((12, 0),), u'LayerChildCount', None,vaName
			)

	def LayerChildren(self, vaName=defaultNamedNotOptArg):
		"""LayerChildren"""
		return self._ApplyTypes_(691, 1, (12, 0), ((12, 0),), u'LayerChildren', None,vaName
			)

	def LayerColor(self, vaName=defaultNamedNotOptArg, vaColor=defaultNamedOptArg):
		"""LayerColor"""
		return self._ApplyTypes_(11, 1, (12, 0), ((12, 0), (12, 16)), u'LayerColor', None,vaName
			, vaColor)

	def LayerCount(self):
		"""LayerCount"""
		return self._ApplyTypes_(12, 1, (12, 0), (), u'LayerCount', None,)

	def LayerLinetype(self, vaLayer=defaultNamedNotOptArg, vaLinetype=defaultNamedOptArg):
		"""LayerLinetype"""
		return self._ApplyTypes_(602, 1, (12, 0), ((12, 0), (12, 16)), u'LayerLinetype', None,vaLayer
			, vaLinetype)

	def LayerLocked(self, vaLayer=defaultNamedNotOptArg, vaLocked=defaultNamedOptArg):
		"""LayerLocked"""
		return self._ApplyTypes_(601, 1, (12, 0), ((12, 0), (12, 16)), u'LayerLocked', None,vaLayer
			, vaLocked)

	def LayerMaterialIndex(self, vaName=defaultNamedNotOptArg):
		"""LayerMaterialIndex"""
		return self._ApplyTypes_(13, 1, (12, 0), ((12, 0),), u'LayerMaterialIndex', None,vaName
			)

	def LayerMode(self, vaName=defaultNamedNotOptArg, vaMode=defaultNamedOptArg):
		"""LayerMode"""
		return self._ApplyTypes_(14, 1, (12, 0), ((12, 0), (12, 16)), u'LayerMode', None,vaName
			, vaMode)

	def LayerNames(self, vaSort=defaultNamedOptArg):
		"""LayerNames"""
		return self._ApplyTypes_(15, 1, (12, 0), ((12, 16),), u'LayerNames', None,vaSort
			)

	def LayerOrder(self, vaName=defaultNamedNotOptArg):
		"""LayerOrder"""
		return self._ApplyTypes_(17, 1, (12, 0), ((12, 0),), u'LayerOrder', None,vaName
			)

	def LayerPrintColor(self, vaLayer=defaultNamedNotOptArg, vaPrintColor=defaultNamedOptArg):
		"""LayerPrintColor"""
		return self._ApplyTypes_(603, 1, (12, 0), ((12, 0), (12, 16)), u'LayerPrintColor', None,vaLayer
			, vaPrintColor)

	def LayerPrintWidth(self, vaLayer=defaultNamedNotOptArg, vaPrintWidth=defaultNamedOptArg):
		"""LayerPrintWidth"""
		return self._ApplyTypes_(604, 1, (12, 0), ((12, 0), (12, 16)), u'LayerPrintWidth', None,vaLayer
			, vaPrintWidth)

	def LayerVisible(self, vaLayer=defaultNamedNotOptArg, vaVisible=defaultNamedOptArg):
		"""LayerVisible"""
		return self._ApplyTypes_(600, 1, (12, 0), ((12, 0), (12, 16)), u'LayerVisible', None,vaLayer
			, vaVisible)

	def LeaderText(self, vaObject=defaultNamedNotOptArg, vaText=defaultNamedOptArg):
		"""LeaderText"""
		return self._ApplyTypes_(895, 1, (12, 0), ((12, 0), (12, 16)), u'LeaderText', None,vaObject
			, vaText)

	def LightColor(self, vaLight=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""LightColor"""
		return self._ApplyTypes_(167, 1, (12, 0), ((12, 0), (12, 16)), u'LightColor', None,vaLight
			, vaValue)

	def LightCount(self):
		"""LightCount"""
		return self._ApplyTypes_(168, 1, (12, 0), (), u'LightCount', None,)

	def LightDirection(self, vaLight=defaultNamedNotOptArg, vaPoint=defaultNamedOptArg):
		"""LightDirection"""
		return self._ApplyTypes_(491, 1, (12, 0), ((12, 0), (12, 16)), u'LightDirection', None,vaLight
			, vaPoint)

	def LightLocation(self, vaLight=defaultNamedNotOptArg, vaPoint=defaultNamedOptArg):
		"""LightLocation"""
		return self._ApplyTypes_(490, 1, (12, 0), ((12, 0), (12, 16)), u'LightLocation', None,vaLight
			, vaPoint)

	def LightName(self, vaLight=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""LightName"""
		return self._ApplyTypes_(169, 1, (12, 0), ((12, 0), (12, 16)), u'LightName', None,vaLight
			, vaValue)

	def LightObjects(self):
		"""LightObjects"""
		return self._ApplyTypes_(170, 1, (12, 0), (), u'LightObjects', None,)

	def LineClosestPoint(self, vaLine=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""LineClosestPoint"""
		return self._ApplyTypes_(899, 1, (12, 0), ((12, 0), (12, 0)), u'LineClosestPoint', None,vaLine
			, vaPoint)

	def LineFitFromPoints(self, vaPoints=defaultNamedNotOptArg):
		"""LineFitFromPoints"""
		return self._ApplyTypes_(726, 1, (12, 0), ((12, 0),), u'LineFitFromPoints', None,vaPoints
			)

	def LineIsFartherThan(self, vaLine=defaultNamedNotOptArg, vaDist=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg):
		"""LineIsFartherThan"""
		return self._ApplyTypes_(902, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'LineIsFartherThan', None,vaLine
			, vaDist, vaPoints)

	def LineLineIntersection(self, vaLine0=defaultNamedNotOptArg, vaLine1=defaultNamedNotOptArg, vaPlanar=defaultNamedOptArg):
		"""LineLineIntersection"""
		return self._ApplyTypes_(736, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'LineLineIntersection', None,vaLine0
			, vaLine1, vaPlanar)

	def LineMaxDistanceTo(self, vaLine=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg):
		"""LineMaxDistanceTo"""
		return self._ApplyTypes_(901, 1, (12, 0), ((12, 0), (12, 0)), u'LineMaxDistanceTo', None,vaLine
			, vaPoints)

	def LineMinDistanceTo(self, vaLine=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg):
		"""LineMinDistanceTo"""
		return self._ApplyTypes_(900, 1, (12, 0), ((12, 0), (12, 0)), u'LineMinDistanceTo', None,vaLine
			, vaPoints)

	def LinePlane(self, vaLine=defaultNamedNotOptArg):
		"""LinePlane"""
		return self._ApplyTypes_(898, 1, (12, 0), ((12, 0),), u'LinePlane', None,vaLine
			)

	def LinePlaneIntersection(self, vaLine=defaultNamedNotOptArg, vaPlane=defaultNamedNotOptArg):
		"""LinePlaneIntersection"""
		return self._ApplyTypes_(743, 1, (12, 0), ((12, 0), (12, 0)), u'LinePlaneIntersection', None,vaLine
			, vaPlane)

	def LineTransform(self, vaLine=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""LineTransform"""
		return self._ApplyTypes_(897, 1, (12, 0), ((12, 0), (12, 0)), u'LineTransform', None,vaLine
			, vaPoint)

	def LinetypeCount(self):
		"""LinetypeCount"""
		return self._ApplyTypes_(605, 1, (12, 0), (), u'LinetypeCount', None,)

	def LinetypeNames(self, vaSort=defaultNamedNotOptArg):
		"""LinetypeNames"""
		return self._ApplyTypes_(606, 1, (12, 0), ((12, 0),), u'LinetypeNames', None,vaSort
			)

	def ListBox(self, vaList=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""ListBox"""
		return self._ApplyTypes_(56, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'ListBox', None,vaList
			, vaPrompt, vaTitle)

	def LocaleID(self):
		"""LocaleID"""
		return self._ApplyTypes_(450, 1, (12, 0), (), u'LocaleID', None,)

	def LockGroup(self, vaName=defaultNamedNotOptArg):
		"""LockGroup"""
		return self._ApplyTypes_(873, 1, (12, 0), ((12, 0),), u'LockGroup', None,vaName
			)

	def LockObject(self, vaObject=defaultNamedNotOptArg):
		"""LockObject"""
		return self._ApplyTypes_(190, 1, (12, 0), ((12, 0),), u'LockObject', None,vaObject
			)

	def LockObjects(self, vaObjects=defaultNamedNotOptArg):
		"""LockObjects"""
		return self._ApplyTypes_(304, 1, (12, 0), ((12, 0),), u'LockObjects', None,vaObjects
			)

	def LockedObjects(self, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""LockedObjects"""
		return self._ApplyTypes_(365, 1, (12, 0), ((12, 16), (12, 16)), u'LockedObjects', None,vaIncludeLights
			, vaIncludeGrips)

	def Log10(self, var=defaultNamedNotOptArg):
		"""Log10"""
		return self._ApplyTypes_(777, 1, (12, 0), ((12, 0),), u'Log10', None,var
			)

	def MakeArray(self, vaRGB=defaultNamedNotOptArg):
		"""MakeArray"""
		return self._ApplyTypes_(875, 1, (12, 0), ((12, 0),), u'MakeArray', None,vaRGB
			)

	def MakeCurveNonPeriodic(self, vaObject=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""MakeCurveNonPeriodic"""
		return self._ApplyTypes_(925, 1, (12, 0), ((12, 0), (12, 16)), u'MakeCurveNonPeriodic', None,vaObject
			, vaDelete)

	def MakeCurvePeriodic(self, vaObject=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""MakeCurvePeriodic"""
		return self._ApplyTypes_(444, 1, (12, 0), ((12, 0), (12, 16)), u'MakeCurvePeriodic', None,vaObject
			, vaDelete)

	def MakeSurfaceNonPeriodic(self, vaObject=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""MakeSurfaceNonPeriodic"""
		return self._ApplyTypes_(926, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'MakeSurfaceNonPeriodic', None,vaObject
			, vaDir, vaDelete)

	def MakeSurfacePeriodic(self, vaObject=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""MakeSurfacePeriodic"""
		return self._ApplyTypes_(445, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'MakeSurfacePeriodic', None,vaObject
			, vaDir, vaDelete)

	def MatchMaterial(self, vaSrc=defaultNamedNotOptArg, vaDest=defaultNamedNotOptArg):
		"""MatchMaterial"""
		return self._ApplyTypes_(322, 1, (12, 0), ((12, 0), (12, 0)), u'MatchMaterial', None,vaSrc
			, vaDest)

	def MatchObjectAttributes(self, vaTarget=defaultNamedNotOptArg, vaSource=defaultNamedOptArg):
		"""MatchObjectAttributes"""
		return self._ApplyTypes_(781, 1, (12, 0), ((12, 0), (12, 16)), u'MatchObjectAttributes', None,vaTarget
			, vaSource)

	def MaterialBump(self, vaIndex=defaultNamedNotOptArg, vaBump=defaultNamedOptArg):
		"""MaterialBump"""
		return self._ApplyTypes_(177, 1, (12, 0), ((12, 0), (12, 16)), u'MaterialBump', None,vaIndex
			, vaBump)

	def MaterialColor(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialColor"""
		return self._ApplyTypes_(178, 1, (12, 0), ((12, 0), (12, 16)), u'MaterialColor', None,vaIndex
			, vaValue)

	def MaterialEnvironmentMap(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialEnvironmentMap"""
		return self._ApplyTypes_(754, 1, (12, 0), ((12, 0), (12, 16)), u'MaterialEnvironmentMap', None,vaIndex
			, vaValue)

	def MaterialName(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialName"""
		return self._ApplyTypes_(179, 1, (12, 0), ((12, 0), (12, 16)), u'MaterialName', None,vaIndex
			, vaValue)

	def MaterialReflectiveColor(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialReflectiveColor"""
		return self._ApplyTypes_(180, 1, (12, 0), ((12, 0), (12, 16)), u'MaterialReflectiveColor', None,vaIndex
			, vaValue)

	def MaterialShine(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialShine"""
		return self._ApplyTypes_(181, 1, (12, 0), ((12, 0), (12, 16)), u'MaterialShine', None,vaIndex
			, vaValue)

	def MaterialTexture(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialTexture"""
		return self._ApplyTypes_(182, 1, (12, 0), ((12, 0), (12, 16)), u'MaterialTexture', None,vaIndex
			, vaValue)

	def MaterialTransparency(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialTransparency"""
		return self._ApplyTypes_(183, 1, (12, 0), ((12, 0), (12, 16)), u'MaterialTransparency', None,vaIndex
			, vaValue)

	def MaterialTransparencyMap(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialTransparencyMap"""
		return self._ApplyTypes_(753, 1, (12, 0), ((12, 0), (12, 16)), u'MaterialTransparencyMap', None,vaIndex
			, vaValue)

	def Max(self, var=defaultNamedNotOptArg):
		"""Max"""
		return self._ApplyTypes_(768, 1, (12, 0), ((12, 0),), u'Max', None,var
			)

	def MaximizeRestoreView(self, vaView=defaultNamedOptArg):
		"""MaximizeRestoreView"""
		return self._ApplyTypes_(257, 1, (12, 0), ((12, 16),), u'MaximizeRestoreView', None,vaView
			)

	def Mean(self, var=defaultNamedNotOptArg):
		"""Mean"""
		return self._ApplyTypes_(771, 1, (12, 0), ((12, 0),), u'Mean', None,var
			)

	def Median(self, var=defaultNamedNotOptArg):
		"""Median"""
		return self._ApplyTypes_(772, 1, (12, 0), ((12, 0),), u'Median', None,var
			)

	def MeshArea(self, vaObject=defaultNamedNotOptArg):
		"""MeshArea"""
		return self._ApplyTypes_(353, 1, (12, 0), ((12, 0),), u'MeshArea', None,vaObject
			)

	def MeshAreaCentroid(self, vaObject=defaultNamedNotOptArg):
		"""MeshAreaCentroid"""
		return self._ApplyTypes_(477, 1, (12, 0), ((12, 0),), u'MeshAreaCentroid', None,vaObject
			)

	def MeshBooleanDifference(self, vaMeshes0=defaultNamedNotOptArg, vaMeshes1=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""MeshBooleanDifference"""
		return self._ApplyTypes_(732, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'MeshBooleanDifference', None,vaMeshes0
			, vaMeshes1, vaDelete)

	def MeshBooleanIntersection(self, vaMeshes0=defaultNamedNotOptArg, vaMeshes1=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""MeshBooleanIntersection"""
		return self._ApplyTypes_(733, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'MeshBooleanIntersection', None,vaMeshes0
			, vaMeshes1, vaDelete)

	def MeshBooleanSplit(self, vaMeshes0=defaultNamedNotOptArg, vaMeshes1=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""MeshBooleanSplit"""
		return self._ApplyTypes_(734, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'MeshBooleanSplit', None,vaMeshes0
			, vaMeshes1, vaDelete)

	def MeshBooleanUnion(self, vaMeshes=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""MeshBooleanUnion"""
		return self._ApplyTypes_(731, 1, (12, 0), ((12, 0), (12, 16)), u'MeshBooleanUnion', None,vaMeshes
			, vaDelete)

	def MeshClosestPoint(self, vaMesh=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""MeshClosestPoint"""
		return self._ApplyTypes_(750, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'MeshClosestPoint', None,vaMesh
			, vaPoint, vaTolerance)

	def MeshContourPoints(self, vaObject=defaultNamedNotOptArg, vaBase=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaInterval=defaultNamedOptArg
			, vaConcident=defaultNamedOptArg):
		"""MeshContourPoints"""
		return self._ApplyTypes_(123, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16), (12, 16)), u'MeshContourPoints', None,vaObject
			, vaBase, vaEnd, vaInterval, vaConcident)

	def MeshFaceCenters(self, vaObject=defaultNamedNotOptArg):
		"""MeshFaceCenters"""
		return self._ApplyTypes_(570, 1, (12, 0), ((12, 0),), u'MeshFaceCenters', None,vaObject
			)

	def MeshFaceCount(self, vaObject=defaultNamedNotOptArg):
		"""MeshFaceCount"""
		return self._ApplyTypes_(124, 1, (12, 0), ((12, 0),), u'MeshFaceCount', None,vaObject
			)

	def MeshFaceNormals(self, vaObject=defaultNamedNotOptArg):
		"""MeshFaceNormals"""
		return self._ApplyTypes_(569, 1, (12, 0), ((12, 0),), u'MeshFaceNormals', None,vaObject
			)

	def MeshFaceVertices(self, vaObject=defaultNamedNotOptArg):
		"""MeshFaceVertices"""
		return self._ApplyTypes_(495, 1, (12, 0), ((12, 0),), u'MeshFaceVertices', None,vaObject
			)

	def MeshFaces(self, vaObject=defaultNamedNotOptArg, vaQuads=defaultNamedOptArg):
		"""MeshFaces"""
		return self._ApplyTypes_(125, 1, (12, 0), ((12, 0), (12, 16)), u'MeshFaces', None,vaObject
			, vaQuads)

	def MeshHasFaceNormals(self, vaObject=defaultNamedNotOptArg):
		"""MeshHasFaceNormals"""
		return self._ApplyTypes_(696, 1, (12, 0), ((12, 0),), u'MeshHasFaceNormals', None,vaObject
			)

	def MeshHasTextureCoordinates(self, vaObject=defaultNamedNotOptArg):
		"""MeshHasTextureCoordinates"""
		return self._ApplyTypes_(697, 1, (12, 0), ((12, 0),), u'MeshHasTextureCoordinates', None,vaObject
			)

	def MeshHasVertexColors(self, vaObject=defaultNamedNotOptArg):
		"""MeshHasVertexColors"""
		return self._ApplyTypes_(698, 1, (12, 0), ((12, 0),), u'MeshHasVertexColors', None,vaObject
			)

	def MeshHasVertexNormals(self, vaObject=defaultNamedNotOptArg):
		"""MeshHasVertexNormals"""
		return self._ApplyTypes_(695, 1, (12, 0), ((12, 0),), u'MeshHasVertexNormals', None,vaObject
			)

	def MeshMeshIntersection(self, vaMesh0=defaultNamedNotOptArg, vaMesh1=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""MeshMeshIntersection"""
		return self._ApplyTypes_(749, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'MeshMeshIntersection', None,vaMesh0
			, vaMesh1, vaTolerance)

	def MeshNakedEdgePoints(self, vaObject=defaultNamedNotOptArg):
		"""MeshNakedEdgePoints"""
		return self._ApplyTypes_(580, 1, (12, 0), ((12, 0),), u'MeshNakedEdgePoints', None,vaObject
			)

	def MeshOffset(self, vaMesh=defaultNamedNotOptArg, vaDistance=defaultNamedNotOptArg):
		"""MeshOffset"""
		return self._ApplyTypes_(720, 1, (12, 0), ((12, 0), (12, 0)), u'MeshOffset', None,vaMesh
			, vaDistance)

	def MeshPolyline(self, vaCrv=defaultNamedNotOptArg):
		"""MeshPolyline"""
		return self._ApplyTypes_(546, 1, (12, 0), ((12, 0),), u'MeshPolyline', None,vaCrv
			)

	def MeshQuadCount(self, vaObject=defaultNamedNotOptArg):
		"""MeshQuadCount"""
		return self._ApplyTypes_(350, 1, (12, 0), ((12, 0),), u'MeshQuadCount', None,vaObject
			)

	def MeshQuadsToTriangles(self, vaObject=defaultNamedNotOptArg):
		"""MeshQuadsToTriangles"""
		return self._ApplyTypes_(352, 1, (12, 0), ((12, 0),), u'MeshQuadsToTriangles', None,vaObject
			)

	def MeshTextureCoordinates(self, vaObject=defaultNamedNotOptArg):
		"""MeshTextureCoordinates"""
		return self._ApplyTypes_(425, 1, (12, 0), ((12, 0),), u'MeshTextureCoordinates', None,vaObject
			)

	def MeshTriangleCount(self, vaObject=defaultNamedNotOptArg):
		"""MeshTriangleCount"""
		return self._ApplyTypes_(351, 1, (12, 0), ((12, 0),), u'MeshTriangleCount', None,vaObject
			)

	def MeshVertexColors(self, vaObject=defaultNamedNotOptArg, vaColors=defaultNamedOptArg):
		"""MeshVertexColors"""
		return self._ApplyTypes_(699, 1, (12, 0), ((12, 0), (12, 16)), u'MeshVertexColors', None,vaObject
			, vaColors)

	def MeshVertexCount(self, vaObject=defaultNamedNotOptArg):
		"""MeshVertexCount"""
		return self._ApplyTypes_(126, 1, (12, 0), ((12, 0),), u'MeshVertexCount', None,vaObject
			)

	def MeshVertexNormals(self, vaObject=defaultNamedNotOptArg):
		"""MeshVertexNormals"""
		return self._ApplyTypes_(426, 1, (12, 0), ((12, 0),), u'MeshVertexNormals', None,vaObject
			)

	def MeshVertices(self, vaObject=defaultNamedNotOptArg):
		"""MeshVertices"""
		return self._ApplyTypes_(127, 1, (12, 0), ((12, 0),), u'MeshVertices', None,vaObject
			)

	def MeshVolume(self, vaObject=defaultNamedNotOptArg):
		"""MeshVolume"""
		return self._ApplyTypes_(354, 1, (12, 0), ((12, 0),), u'MeshVolume', None,vaObject
			)

	def MeshVolumeCentroid(self, vaObject=defaultNamedNotOptArg):
		"""MeshVolumeCentroid"""
		return self._ApplyTypes_(478, 1, (12, 0), ((12, 0),), u'MeshVolumeCentroid', None,vaObject
			)

	def MessageBeep(self, vaType=defaultNamedOptArg):
		"""MessageBeep"""
		return self._ApplyTypes_(149, 1, (12, 0), ((12, 16),), u'MessageBeep', None,vaType
			)

	def MessageBox(self, vaText=defaultNamedNotOptArg, vaType=defaultNamedOptArg, vaCaption=defaultNamedOptArg):
		"""MessageBox"""
		return self._ApplyTypes_(150, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'MessageBox', None,vaText
			, vaType, vaCaption)

	def Min(self, var=defaultNamedNotOptArg):
		"""Min"""
		return self._ApplyTypes_(769, 1, (12, 0), ((12, 0),), u'Min', None,var
			)

	def MirrorObject(self, vaObject=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""MirrorObject"""
		return self._ApplyTypes_(589, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'MirrorObject', None,vaObject
			, vaStart, vaEnd, vaCopy)

	def MirrorObjects(self, vaObjects=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""MirrorObjects"""
		return self._ApplyTypes_(590, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'MirrorObjects', None,vaObjects
			, vaStart, vaEnd, vaCopy)

	def MoveObject(self, vaObject=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedOptArg):
		"""MoveObject"""
		return self._ApplyTypes_(270, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'MoveObject', None,vaObject
			, vaStart, vaEnd)

	def MoveObjects(self, vaObjects=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedOptArg):
		"""MoveObjects"""
		return self._ApplyTypes_(296, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'MoveObjects', None,vaObjects
			, vaStart, vaEnd)

	def MovePlane(self, vaPlane=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg):
		"""MovePlane"""
		return self._ApplyTypes_(631, 1, (12, 0), ((12, 0), (12, 0)), u'MovePlane', None,vaPlane
			, vaOrigin)

	def MultiListBox(self, vaList=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""MultiListBox"""
		return self._ApplyTypes_(57, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'MultiListBox', None,vaList
			, vaPrompt, vaTitle)

	def NamedCPlane(self, vaName=defaultNamedNotOptArg):
		"""NamedCPlane"""
		return self._ApplyTypes_(286, 1, (12, 0), ((12, 0),), u'NamedCPlane', None,vaName
			)

	def NamedCPlanes(self):
		"""NamedCPlanes"""
		return self._ApplyTypes_(258, 1, (12, 0), (), u'NamedCPlanes', None,)

	def NamedViews(self):
		"""NamedViews"""
		return self._ApplyTypes_(259, 1, (12, 0), (), u'NamedViews', None,)

	def NextObject(self, vaObject=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""NextObject"""
		return self._ApplyTypes_(36, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), u'NextObject', None,vaObject
			, vaSelect, vaIncludeLights, vaIncludeGrips)

	def NextObjectGrip(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg, vaDir=defaultNamedOptArg, vaSelect=defaultNamedOptArg):
		"""NextObjectGrip"""
		return self._ApplyTypes_(558, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'NextObjectGrip', None,vaObject
			, vaIndex, vaDir, vaSelect)

	def NormalObjects(self, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""NormalObjects"""
		return self._ApplyTypes_(364, 1, (12, 0), ((12, 16), (12, 16)), u'NormalObjects', None,vaIncludeLights
			, vaIncludeGrips)

	def Notes(self, vaNotes=defaultNamedOptArg):
		"""Notes"""
		return self._ApplyTypes_(274, 1, (12, 0), ((12, 16),), u'Notes', None,vaNotes
			)

	def ObjectColor(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ObjectColor"""
		return self._ApplyTypes_(191, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectColor', None,vaObject
			, vaValue)

	def ObjectColorSource(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ObjectColorSource"""
		return self._ApplyTypes_(192, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectColorSource', None,vaObject
			, vaValue)

	def ObjectDataCount(self, vaObject=defaultNamedNotOptArg):
		"""ObjectDataCount"""
		return self._ApplyTypes_(242, 1, (12, 0), ((12, 0),), u'ObjectDataCount', None,vaObject
			)

	def ObjectDescription(self, vaObject=defaultNamedNotOptArg):
		"""ObjectDescription"""
		return self._ApplyTypes_(470, 1, (12, 0), ((12, 0),), u'ObjectDescription', None,vaObject
			)

	def ObjectDump(self, vaObject=defaultNamedNotOptArg, vaType=defaultNamedOptArg):
		"""ObjectDump"""
		return self._ApplyTypes_(705, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectDump', None,vaObject
			, vaType)

	def ObjectGripCount(self, vaObject=defaultNamedNotOptArg):
		"""ObjectGripCount"""
		return self._ApplyTypes_(500, 1, (12, 0), ((12, 0),), u'ObjectGripCount', None,vaObject
			)

	def ObjectGripLocation(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg, vaPt=defaultNamedOptArg):
		"""ObjectGripLocation"""
		return self._ApplyTypes_(556, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'ObjectGripLocation', None,vaObject
			, vaIndex, vaPt)

	def ObjectGripLocations(self, vaObject=defaultNamedNotOptArg, vaPoints=defaultNamedOptArg):
		"""ObjectGripLocations"""
		return self._ApplyTypes_(557, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectGripLocations', None,vaObject
			, vaPoints)

	def ObjectGripsOn(self, vaObject=defaultNamedNotOptArg):
		"""ObjectGripsOn"""
		return self._ApplyTypes_(497, 1, (12, 0), ((12, 0),), u'ObjectGripsOn', None,vaObject
			)

	def ObjectGripsSelected(self, vaObject=defaultNamedNotOptArg):
		"""ObjectGripsSelected"""
		return self._ApplyTypes_(498, 1, (12, 0), ((12, 0),), u'ObjectGripsSelected', None,vaObject
			)

	def ObjectGroups(self, vaObject=defaultNamedNotOptArg):
		"""ObjectGroups"""
		return self._ApplyTypes_(193, 1, (12, 0), ((12, 0),), u'ObjectGroups', None,vaObject
			)

	def ObjectHasMesh(self, vaObject=defaultNamedNotOptArg):
		"""ObjectHasMesh"""
		return self._ApplyTypes_(867, 1, (12, 0), ((12, 0),), u'ObjectHasMesh', None,vaObject
			)

	def ObjectLayer(self, vaObject=defaultNamedNotOptArg, vaLayer=defaultNamedOptArg):
		"""ObjectLayer"""
		return self._ApplyTypes_(51, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectLayer', None,vaObject
			, vaLayer)

	def ObjectLayout(self, vaObject=defaultNamedNotOptArg, vaLayout=defaultNamedOptArg, vaNames=defaultNamedOptArg):
		"""ObjectLayout"""
		return self._ApplyTypes_(924, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'ObjectLayout', None,vaObject
			, vaLayout, vaNames)

	def ObjectLinetype(self, vaObject=defaultNamedNotOptArg, vaLinetype=defaultNamedOptArg):
		"""ObjectLinetype"""
		return self._ApplyTypes_(646, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectLinetype', None,vaObject
			, vaLinetype)

	def ObjectLinetypeSource(self, vaObject=defaultNamedNotOptArg, vaSource=defaultNamedOptArg):
		"""ObjectLinetypeSource"""
		return self._ApplyTypes_(647, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectLinetypeSource', None,vaObject
			, vaSource)

	def ObjectMaterialIndex(self, vaObject=defaultNamedNotOptArg):
		"""ObjectMaterialIndex"""
		return self._ApplyTypes_(194, 1, (12, 0), ((12, 0),), u'ObjectMaterialIndex', None,vaObject
			)

	def ObjectMaterialSource(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ObjectMaterialSource"""
		return self._ApplyTypes_(195, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectMaterialSource', None,vaObject
			, vaValue)

	def ObjectMeshDensity(self, vaObject=defaultNamedNotOptArg, vaDensity=defaultNamedOptArg):
		"""ObjectMeshDensity"""
		return self._ApplyTypes_(858, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectMeshDensity', None,vaObject
			, vaDensity)

	def ObjectMeshMaxAngle(self, vaObject=defaultNamedNotOptArg, vaAngle=defaultNamedOptArg):
		"""ObjectMeshMaxAngle"""
		return self._ApplyTypes_(859, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectMeshMaxAngle', None,vaObject
			, vaAngle)

	def ObjectMeshMaxAspectRatio(self, vaObject=defaultNamedNotOptArg, vaRatio=defaultNamedOptArg):
		"""ObjectMeshMaxAspectRatio"""
		return self._ApplyTypes_(860, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectMeshMaxAspectRatio', None,vaObject
			, vaRatio)

	def ObjectMeshMaxDistEdgeToSrf(self, vaObject=defaultNamedNotOptArg, vaDistance=defaultNamedOptArg):
		"""ObjectMeshMaxDistEdgeToSrf"""
		return self._ApplyTypes_(863, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectMeshMaxDistEdgeToSrf', None,vaObject
			, vaDistance)

	def ObjectMeshMaxEdgeLength(self, vaObject=defaultNamedNotOptArg, vaLength=defaultNamedOptArg):
		"""ObjectMeshMaxnEdgeLength"""
		return self._ApplyTypes_(862, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectMeshMaxEdgeLength', None,vaObject
			, vaLength)

	def ObjectMeshMinEdgeLength(self, vaObject=defaultNamedNotOptArg, vaLength=defaultNamedOptArg):
		"""ObjectMeshMinEdgeLength"""
		return self._ApplyTypes_(861, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectMeshMinEdgeLength', None,vaObject
			, vaLength)

	def ObjectMeshMinInitialGridQuads(self, vaObject=defaultNamedNotOptArg, vaQuads=defaultNamedOptArg):
		"""ObjectMeshMinInitialGridQuads"""
		return self._ApplyTypes_(864, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectMeshMinInitialGridQuads', None,vaObject
			, vaQuads)

	def ObjectMeshQuality(self, vaObject=defaultNamedNotOptArg, vaQuality=defaultNamedOptArg):
		"""ObjectMeshQuality"""
		return self._ApplyTypes_(857, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectMeshQuality', None,vaObject
			, vaQuality)

	def ObjectMeshSettings(self, vaObject=defaultNamedNotOptArg, vaFlags=defaultNamedOptArg):
		"""ObjectMeshSettings"""
		return self._ApplyTypes_(865, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectMeshSettings', None,vaObject
			, vaFlags)

	def ObjectName(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ObjectName"""
		return self._ApplyTypes_(196, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectName', None,vaObject
			, vaValue)

	def ObjectNames(self, vaObjects=defaultNamedNotOptArg, vaNames=defaultNamedOptArg):
		"""ObjectNames"""
		return self._ApplyTypes_(639, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectNames', None,vaObjects
			, vaNames)

	def ObjectPrintColor(self, vaObject=defaultNamedNotOptArg, vaColor=defaultNamedNotOptArg):
		"""ObjectPrintColor"""
		return self._ApplyTypes_(805, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectPrintColor', None,vaObject
			, vaColor)

	def ObjectPrintColorSource(self, vaObject=defaultNamedNotOptArg, vaSource=defaultNamedNotOptArg):
		"""ObjectPrintColorSource"""
		return self._ApplyTypes_(806, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectPrintColorSource', None,vaObject
			, vaSource)

	def ObjectPrintWidth(self, vaObject=defaultNamedNotOptArg, vavaWidth=defaultNamedNotOptArg):
		"""ObjectPrintWidth"""
		return self._ApplyTypes_(807, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectPrintWidth', None,vaObject
			, vavaWidth)

	def ObjectPrintWidthSource(self, vaObject=defaultNamedNotOptArg, vaSource=defaultNamedNotOptArg):
		"""ObjectPrintWidthSource"""
		return self._ApplyTypes_(808, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectPrintWidthSource', None,vaObject
			, vaSource)

	def ObjectTopGroup(self, vaObject=defaultNamedNotOptArg):
		"""ObjectTopGroup"""
		return self._ApplyTypes_(197, 1, (12, 0), ((12, 0),), u'ObjectTopGroup', None,vaObject
			)

	def ObjectType(self, vaObject=defaultNamedNotOptArg):
		"""ObjectType"""
		return self._ApplyTypes_(198, 1, (12, 0), ((12, 0),), u'ObjectType', None,vaObject
			)

	def ObjectURL(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ObjectURL"""
		return self._ApplyTypes_(199, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectURL', None,vaObject
			, vaValue)

	def ObjectsByColor(self, vaColor=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""ObjectsByColor"""
		return self._ApplyTypes_(37, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'ObjectsByColor', None,vaColor
			, vaSelect, vaIncludeLights)

	def ObjectsByGroup(self, vaGroup=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg):
		"""ObjectsByGroup"""
		return self._ApplyTypes_(38, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectsByGroup', None,vaGroup
			, vaSelect)

	def ObjectsByLayer(self, vaLayer=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg):
		"""ObjectsByLayer"""
		return self._ApplyTypes_(39, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectsByLayer', None,vaLayer
			, vaSelect)

	def ObjectsByName(self, vaName=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""ObjectsByName"""
		return self._ApplyTypes_(40, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'ObjectsByName', None,vaName
			, vaSelect, vaIncludeLights)

	def ObjectsByType(self, vaType=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg):
		"""ObjectsByType"""
		return self._ApplyTypes_(41, 1, (12, 0), ((12, 0), (12, 16)), u'ObjectsByType', None,vaType
			, vaSelect)

	def ObjectsByURL(self, vaURL=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""ObjectsByURL"""
		return self._ApplyTypes_(42, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'ObjectsByURL', None,vaURL
			, vaSelect, vaIncludeLights)

	def OffsetCurve(self, vaObject=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg, vaDistance=defaultNamedNotOptArg, vaNormal=defaultNamedOptArg
			, vaCorner=defaultNamedOptArg):
		"""OffsetCurve"""
		return self._ApplyTypes_(634, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16), (12, 16)), u'OffsetCurve', None,vaObject
			, vaOrigin, vaDistance, vaNormal, vaCorner)

	def OffsetCurveOnSurface(self, vaCurve=defaultNamedNotOptArg, vaSurface=defaultNamedNotOptArg, vaDistance=defaultNamedNotOptArg):
		"""OffsetCurveOnSurface"""
		return self._ApplyTypes_(906, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'OffsetCurveOnSurface', None,vaCurve
			, vaSurface, vaDistance)

	def OffsetSurface(self, vaObject=defaultNamedNotOptArg, vaDistance=defaultNamedNotOptArg):
		"""OffsetSurface"""
		return self._ApplyTypes_(635, 1, (12, 0), ((12, 0), (12, 0)), u'OffsetSurface', None,vaObject
			, vaDistance)

	def OpenFileName(self, vaTitle=defaultNamedOptArg, vaFilter=defaultNamedOptArg, vaPath=defaultNamedOptArg, vaFile=defaultNamedOptArg
			, vaExt=defaultNamedOptArg):
		"""OpenFileName"""
		return self._ApplyTypes_(151, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'OpenFileName', None,vaTitle
			, vaFilter, vaPath, vaFile, vaExt)

	def OpenFileNames(self, vaTitle=defaultNamedOptArg, vaFilter=defaultNamedOptArg, vaPath=defaultNamedOptArg, vaFile=defaultNamedOptArg
			, vaExt=defaultNamedOptArg):
		"""OpenFileNames"""
		return self._ApplyTypes_(821, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'OpenFileNames', None,vaTitle
			, vaFilter, vaPath, vaFile, vaExt)

	def OpenToolBarCollection(self, vaFile=defaultNamedNotOptArg):
		"""OpenToolBarCollection"""
		return self._ApplyTypes_(228, 1, (12, 0), ((12, 0),), u'OpenToolBarCollection', None,vaFile
			)

	def OrientObject(self, vaObject=defaultNamedNotOptArg, vaFrom=defaultNamedNotOptArg, vaTo=defaultNamedNotOptArg, vaFlags=defaultNamedOptArg):
		"""OrientObject"""
		return self._ApplyTypes_(390, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'OrientObject', None,vaObject
			, vaFrom, vaTo, vaFlags)

	def OrientObjects(self, vaObjects=defaultNamedNotOptArg, vaFrom=defaultNamedNotOptArg, vaTo=defaultNamedNotOptArg, vaFlags=defaultNamedOptArg):
		"""OrientObjects"""
		return self._ApplyTypes_(391, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'OrientObjects', None,vaObjects
			, vaFrom, vaTo, vaFlags)

	def Ortho(self, vaMode=defaultNamedOptArg):
		"""Ortho"""
		return self._ApplyTypes_(345, 1, (12, 0), ((12, 16),), u'Ortho', None,vaMode
			)

	def Osnap(self, vaMode=defaultNamedOptArg):
		"""Osnap"""
		return self._ApplyTypes_(347, 1, (12, 0), ((12, 16),), u'Osnap', None,vaMode
			)

	def OsnapDialog(self, vaMode=defaultNamedOptArg):
		"""OsnapDialog"""
		return self._ApplyTypes_(349, 1, (12, 0), ((12, 16),), u'OsnapDialog', None,vaMode
			)

	def OsnapMode(self, vaModes=defaultNamedOptArg):
		"""OsnapMode"""
		return self._ApplyTypes_(343, 1, (12, 0), ((12, 16),), u'OsnapMode', None,vaModes
			)

	def PI(self):
		"""PI"""
		return self._ApplyTypes_(663, 1, (12, 0), (), u'PI', None,)

	def ParentLayer(self, vaName=defaultNamedNotOptArg, vaParent=defaultNamedOptArg):
		"""ParentLayer"""
		return self._ApplyTypes_(688, 1, (12, 0), ((12, 0), (12, 16)), u'ParentLayer', None,vaName
			, vaParent)

	def Planar(self, vaMode=defaultNamedOptArg):
		"""Planar"""
		return self._ApplyTypes_(346, 1, (12, 0), ((12, 16),), u'Planar', None,vaMode
			)

	def PlanarClosedCurveContainment(self, vaCrv1=defaultNamedNotOptArg, vaCrv2=defaultNamedNotOptArg, vaPlane=defaultNamedOptArg, vaTol=defaultNamedOptArg):
		"""PlanarClosedCurveContainment"""
		return self._ApplyTypes_(480, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'PlanarClosedCurveContainment', None,vaCrv1
			, vaCrv2, vaPlane, vaTol)

	def PlanarCurveCollision(self, vaCrv1=defaultNamedNotOptArg, vaCrv2=defaultNamedNotOptArg, vaPlane=defaultNamedOptArg, vaTol=defaultNamedOptArg):
		"""PlanarCurveCollision"""
		return self._ApplyTypes_(481, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'PlanarCurveCollision', None,vaCrv1
			, vaCrv2, vaPlane, vaTol)

	def PlaneClosestPoint(self, vaPlane=defaultNamedNotOptArg, vaPt=defaultNamedNotOptArg, vaReturnPt=defaultNamedOptArg):
		"""PlaneClosestPoint"""
		return self._ApplyTypes_(629, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'PlaneClosestPoint', None,vaPlane
			, vaPt, vaReturnPt)

	def PlaneEquation(self, vaPlane=defaultNamedNotOptArg):
		"""PlaneEquation"""
		return self._ApplyTypes_(642, 1, (12, 0), ((12, 0),), u'PlaneEquation', None,vaPlane
			)

	def PlaneFitFromPoints(self, vaPoints=defaultNamedNotOptArg):
		"""PlaneFitFromPoints"""
		return self._ApplyTypes_(725, 1, (12, 0), ((12, 0),), u'PlaneFitFromPoints', None,vaPoints
			)

	def PlaneFromFrame(self, vaOrigin=defaultNamedNotOptArg, vaX=defaultNamedNotOptArg, vaY=defaultNamedNotOptArg):
		"""PlaneFromFrame"""
		return self._ApplyTypes_(627, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'PlaneFromFrame', None,vaOrigin
			, vaX, vaY)

	def PlaneFromNormal(self, vaOrigin=defaultNamedNotOptArg, vaNormal=defaultNamedNotOptArg):
		"""PlaneFromNormal"""
		return self._ApplyTypes_(626, 1, (12, 0), ((12, 0), (12, 0)), u'PlaneFromNormal', None,vaOrigin
			, vaNormal)

	def PlaneFromPoints(self, vaOrigin=defaultNamedNotOptArg, vaX=defaultNamedNotOptArg, vaY=defaultNamedNotOptArg):
		"""PlaneFromPoints"""
		return self._ApplyTypes_(649, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'PlaneFromPoints', None,vaOrigin
			, vaX, vaY)

	def PlanePlaneIntersection(self, vaPlaneA=defaultNamedNotOptArg, vaPlaneB=defaultNamedNotOptArg):
		"""PlanePlaneIntersection"""
		return self._ApplyTypes_(744, 1, (12, 0), ((12, 0), (12, 0)), u'PlanePlaneIntersection', None,vaPlaneA
			, vaPlaneB)

	def PlaneTransform(self, vaPlane=defaultNamedNotOptArg, vaXform=defaultNamedNotOptArg):
		"""PlaneTransform"""
		return self._ApplyTypes_(801, 1, (12, 0), ((12, 0), (12, 0)), u'PlaneTransform', None,vaPlane
			, vaXform)

	def PlugIns(self, vaTypes=defaultNamedOptArg, vaLoaded=defaultNamedOptArg):
		"""PlugIns"""
		return self._ApplyTypes_(315, 1, (12, 0), ((12, 16), (12, 16)), u'PlugIns', None,vaTypes
			, vaLoaded)

	def PointAdd(self, vaPt0=defaultNamedNotOptArg, vaPt1=defaultNamedNotOptArg):
		"""PointAdd"""
		return self._ApplyTypes_(666, 1, (12, 0), ((12, 0), (12, 0)), u'PointAdd', None,vaPt0
			, vaPt1)

	def PointArrayBoundingBox(self, vaPoints=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaSystem=defaultNamedOptArg):
		"""PointArrayBoundingBox"""
		return self._ApplyTypes_(746, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'PointArrayBoundingBox', None,vaPoints
			, vaView, vaSystem)

	def PointArrayClosestPoint(self, vaPoints=defaultNamedNotOptArg, vaPt=defaultNamedNotOptArg):
		"""PointArrayClosestPoint"""
		return self._ApplyTypes_(742, 1, (12, 0), ((12, 0), (12, 0)), u'PointArrayClosestPoint', None,vaPoints
			, vaPt)

	def PointArrayTransform(self, vaPoints=defaultNamedNotOptArg, vaXform=defaultNamedNotOptArg):
		"""PointArrayTransform"""
		return self._ApplyTypes_(802, 1, (12, 0), ((12, 0), (12, 0)), u'PointArrayTransform', None,vaPoints
			, vaXform)

	def PointCloudCount(self, vaObject=defaultNamedNotOptArg):
		"""PointCloudCount"""
		return self._ApplyTypes_(128, 1, (12, 0), ((12, 0),), u'PointCloudCount', None,vaObject
			)

	def PointCloudPoints(self, vaObject=defaultNamedNotOptArg):
		"""PointCloudPoints"""
		return self._ApplyTypes_(129, 1, (12, 0), ((12, 0),), u'PointCloudPoints', None,vaObject
			)

	def PointCompare(self, vaPt0=defaultNamedNotOptArg, vaPt1=defaultNamedNotOptArg, vaTol=defaultNamedOptArg):
		"""PointCompare"""
		return self._ApplyTypes_(667, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'PointCompare', None,vaPt0
			, vaPt1, vaTol)

	def PointCoordinates(self, vaObject=defaultNamedNotOptArg, vaNewPt=defaultNamedOptArg):
		"""PointCoordinates"""
		return self._ApplyTypes_(130, 1, (12, 0), ((12, 0), (12, 16)), u'PointCoordinates', None,vaObject
			, vaNewPt)

	def PointDivide(self, vaPt=defaultNamedNotOptArg, vaDivide=defaultNamedNotOptArg):
		"""PointDivide"""
		return self._ApplyTypes_(668, 1, (12, 0), ((12, 0), (12, 0)), u'PointDivide', None,vaPt
			, vaDivide)

	def PointInPlanarClosedCurve(self, vaPt=defaultNamedNotOptArg, vaCrv=defaultNamedNotOptArg, vaPlane=defaultNamedOptArg, vaTol=defaultNamedOptArg):
		"""PointInPlanarClosedCurve"""
		return self._ApplyTypes_(482, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'PointInPlanarClosedCurve', None,vaPt
			, vaCrv, vaPlane, vaTol)

	def PointScale(self, vaPt=defaultNamedNotOptArg, vaScale=defaultNamedNotOptArg):
		"""PointScale"""
		return self._ApplyTypes_(669, 1, (12, 0), ((12, 0), (12, 0)), u'PointScale', None,vaPt
			, vaScale)

	def PointSubtract(self, vaPt0=defaultNamedNotOptArg, vaPt1=defaultNamedNotOptArg):
		"""PointSubtract"""
		return self._ApplyTypes_(670, 1, (12, 0), ((12, 0), (12, 0)), u'PointSubtract', None,vaPt0
			, vaPt1)

	def PointTransform(self, vaPt=defaultNamedNotOptArg, vaXform=defaultNamedNotOptArg):
		"""PointTransform"""
		return self._ApplyTypes_(671, 1, (12, 0), ((12, 0), (12, 0)), u'PointTransform', None,vaPt
			, vaXform)

	def PointsAreCoplanar(self, vaPoints=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""PointsAreCoplanar"""
		return self._ApplyTypes_(593, 1, (12, 0), ((12, 0), (12, 16)), u'PointsAreCoplanar', None,vaPoints
			, vaTolerance)

	def Polar(self, vaPoint=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg, vaDistance=defaultNamedNotOptArg, vaPlane=defaultNamedNotOptArg):
		"""Polar"""
		return self._ApplyTypes_(662, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'Polar', None,vaPoint
			, vaAngle, vaDistance, vaPlane)

	def PolyCurveCount(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""PolyCurveCount"""
		return self._ApplyTypes_(369, 1, (12, 0), ((12, 0), (12, 16)), u'PolyCurveCount', None,vaObject
			, vaIndex)

	def PolylineVertices(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""PolylineVertices"""
		return self._ApplyTypes_(112, 1, (12, 0), ((12, 0), (12, 16)), u'PolylineVertices', None,vaObject
			, vaIndex)

	def PopupMenu(self, vaItems=defaultNamedNotOptArg, vaModes=defaultNamedOptArg, vaPoint=defaultNamedOptArg, vaView=defaultNamedOptArg):
		"""PopupMenu"""
		return self._ApplyTypes_(595, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), u'PopupMenu', None,vaItems
			, vaModes, vaPoint, vaView)

	def PrevObjectGrip(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg, vaDir=defaultNamedOptArg, vaSelect=defaultNamedOptArg):
		"""PrevObjectGrip"""
		return self._ApplyTypes_(559, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'PrevObjectGrip', None,vaObject
			, vaIndex, vaDir, vaSelect)

	def PrevSelectedObjects(self, vaSelect=defaultNamedOptArg):
		"""PrevSelectedObjects"""
		return self._ApplyTypes_(486, 1, (12, 0), ((12, 16),), u'PrevSelectedObjects', None,vaSelect
			)

	def Print(self, vaCmd=defaultNamedOptArg):
		"""Print"""
		return self._ApplyTypes_(2, 1, (12, 0), ((12, 16),), u'Print', None,vaCmd
			)

	def PrintEx(self, vaText=defaultNamedOptArg):
		"""PrintEx"""
		return self._ApplyTypes_(370, 1, (12, 0), ((12, 16),), u'PrintEx', None,vaText
			)

	def PrinterNames(self):
		"""PrinterNames"""
		return self._ApplyTypes_(356, 1, (12, 0), (), u'PrinterNames', None,)

	def ProjectCurveToMesh(self, vaCurves=defaultNamedNotOptArg, vaMeshes=defaultNamedNotOptArg, vaDirection=defaultNamedNotOptArg):
		"""ProjectCurveToMesh"""
		return self._ApplyTypes_(911, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ProjectCurveToMesh', None,vaCurves
			, vaMeshes, vaDirection)

	def ProjectCurveToSurface(self, vaCurves=defaultNamedNotOptArg, vaSurfaces=defaultNamedNotOptArg, vaDirection=defaultNamedNotOptArg):
		"""ProjectCurveToSurface"""
		return self._ApplyTypes_(891, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ProjectCurveToSurface', None,vaCurves
			, vaSurfaces, vaDirection)

	def ProjectOsnaps(self, vaMode=defaultNamedOptArg):
		"""ProjectOsnaps"""
		return self._ApplyTypes_(348, 1, (12, 0), ((12, 16),), u'ProjectOsnaps', None,vaMode
			)

	def ProjectPointToMesh(self, vaPoints=defaultNamedNotOptArg, vaMeshes=defaultNamedNotOptArg, vaDirection=defaultNamedNotOptArg):
		"""ProjectPointToMesh"""
		return self._ApplyTypes_(912, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ProjectPointToMesh', None,vaPoints
			, vaMeshes, vaDirection)

	def ProjectPointToSurface(self, vaPoints=defaultNamedNotOptArg, vaSurfaces=defaultNamedNotOptArg, vaDirection=defaultNamedNotOptArg):
		"""ProjectPointToSurface"""
		return self._ApplyTypes_(892, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ProjectPointToSurface', None,vaPoints
			, vaSurfaces, vaDirection)

	def Prompt(self, vaPrompt=defaultNamedOptArg):
		"""Prompt"""
		return self._ApplyTypes_(24, 1, (12, 0), ((12, 16),), u'Prompt', None,vaPrompt
			)

	def PropertyListBox(self, vaList=defaultNamedNotOptArg, vaValues=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""PropertyListBox"""
		return self._ApplyTypes_(58, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'PropertyListBox', None,vaList
			, vaValues, vaPrompt, vaTitle)

	def Pt2Str(self, vaPoint=defaultNamedNotOptArg, vaPrecision=defaultNamedOptArg, vaSpace=defaultNamedOptArg):
		"""Pt2Str"""
		return self._ApplyTypes_(297, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'Pt2Str', None,vaPoint
			, vaPrecision, vaSpace)

	def PullCurve(self, vaObject=defaultNamedNotOptArg, vaCurve=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""PullCurve"""
		return self._ApplyTypes_(493, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'PullCurve', None,vaObject
			, vaCurve, vaDelete)

	def PullCurveToMesh(self, vaMesh=defaultNamedNotOptArg, vaCurve=defaultNamedNotOptArg):
		"""PullCurveToMesh"""
		return self._ApplyTypes_(719, 1, (12, 0), ((12, 0), (12, 0)), u'PullCurveToMesh', None,vaMesh
			, vaCurve)

	def PullPoints(self, vaObject=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg):
		"""PullPoints"""
		return self._ApplyTypes_(716, 1, (12, 0), ((12, 0), (12, 0)), u'PullPoints', None,vaObject
			, vaPoints)

	def PurgeLayer(self, vaLayer=defaultNamedNotOptArg):
		"""PurgeLayer"""
		return self._ApplyTypes_(291, 1, (12, 0), ((12, 0),), u'PurgeLayer', None,vaLayer
			)

	def ReadFileVersion(self):
		"""ReadFileVersion"""
		return self._ApplyTypes_(737, 1, (12, 0), (), u'ReadFileVersion', None,)

	def RealBox(self, vaPrompt=defaultNamedOptArg, vaReal=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""RealBox"""
		return self._ApplyTypes_(59, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'RealBox', None,vaPrompt
			, vaReal, vaTitle)

	def RebuildCurve(self, vaCrv=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg, vaPointCount=defaultNamedOptArg):
		"""RebuildCurve"""
		return self._ApplyTypes_(814, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'RebuildCurve', None,vaCrv
			, vaDegree, vaPointCount)

	def RebuildSurface(self, vaSrf=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg, vaPointCount=defaultNamedOptArg):
		"""RebuildSurface"""
		return self._ApplyTypes_(816, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'RebuildSurface', None,vaSrf
			, vaDegree, vaPointCount)

	def RectangularLightPlane(self, vaLight=defaultNamedNotOptArg):
		"""RectangularLightPlane"""
		return self._ApplyTypes_(776, 1, (12, 0), ((12, 0),), u'RectangularLightPlane', None,vaLight
			)

	def Redraw(self):
		"""Redraw"""
		return self._ApplyTypes_(114, 1, (12, 0), (), u'Redraw', None,)

	def ReferenceObjects(self, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""ReferenceObjects"""
		return self._ApplyTypes_(367, 1, (12, 0), ((12, 16), (12, 16)), u'ReferenceObjects', None,vaIncludeLights
			, vaIncludeGrips)

	def RegistryKey(self):
		"""RegistryKey"""
		return self._ApplyTypes_(25, 1, (12, 0), (), u'RegistryKey', None,)

	def RemapObject(self, vaObject=defaultNamedNotOptArg, vaSrcPlane=defaultNamedNotOptArg, vaDstPlane=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""RemapObject"""
		return self._ApplyTypes_(655, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'RemapObject', None,vaObject
			, vaSrcPlane, vaDstPlane, vaCopy)

	def RemapObjects(self, vaObjects=defaultNamedNotOptArg, vaSrcPlane=defaultNamedNotOptArg, vaDstPlane=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""RemapObjects"""
		return self._ApplyTypes_(656, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'RemapObjects', None,vaObjects
			, vaSrcPlane, vaDstPlane, vaCopy)

	def RemoveCurveKnot(self, vaCurve=defaultNamedNotOptArg, vaKnot=defaultNamedNotOptArg):
		"""RemoveCurveKnot"""
		return self._ApplyTypes_(916, 1, (12, 0), ((12, 0), (12, 0)), u'RemoveCurveKnot', None,vaCurve
			, vaKnot)

	def RemoveObjectFromAllGroups(self, vaObject=defaultNamedNotOptArg):
		"""RemoveObjectFromAllGroups"""
		return self._ApplyTypes_(141, 1, (12, 0), ((12, 0),), u'RemoveObjectFromAllGroups', None,vaObject
			)

	def RemoveObjectFromGroup(self, vaObject=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""RemoveObjectFromGroup"""
		return self._ApplyTypes_(142, 1, (12, 0), ((12, 0), (12, 0)), u'RemoveObjectFromGroup', None,vaObject
			, vaName)

	def RemoveObjectFromTopGroup(self, vaObject=defaultNamedNotOptArg):
		"""RemoveObjectFromTopGroup"""
		return self._ApplyTypes_(143, 1, (12, 0), ((12, 0),), u'RemoveObjectFromTopGroup', None,vaObject
			)

	def RemoveObjectsFromGroup(self, vaObjects=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""RemoveObjectsFromGroup"""
		return self._ApplyTypes_(144, 1, (12, 0), ((12, 0), (12, 0)), u'RemoveObjectsFromGroup', None,vaObjects
			, vaName)

	def RemoveSurfaceKnot(self, vaSurface=defaultNamedNotOptArg, vaKnot=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg):
		"""RemoveSurfaceKnot"""
		return self._ApplyTypes_(917, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'RemoveSurfaceKnot', None,vaSurface
			, vaKnot, vaDir)

	def RenameBlock(self, vaOld=defaultNamedNotOptArg, vaNew=defaultNamedNotOptArg):
		"""RenameBlock"""
		return self._ApplyTypes_(399, 1, (12, 0), ((12, 0), (12, 0)), u'RenameBlock', None,vaOld
			, vaNew)

	def RenameDimStyle(self, vaOld=defaultNamedNotOptArg, vaNew=defaultNamedNotOptArg):
		"""RenameDimStyle"""
		return self._ApplyTypes_(458, 1, (12, 0), ((12, 0), (12, 0)), u'RenameDimStyle', None,vaOld
			, vaNew)

	def RenameGroup(self, vaOld=defaultNamedNotOptArg, vaNew=defaultNamedNotOptArg):
		"""RenameGroup"""
		return self._ApplyTypes_(145, 1, (12, 0), ((12, 0), (12, 0)), u'RenameGroup', None,vaOld
			, vaNew)

	def RenameLayer(self, vaOld=defaultNamedNotOptArg, vaNew=defaultNamedNotOptArg):
		"""RenameLayer"""
		return self._ApplyTypes_(16, 1, (12, 0), ((12, 0), (12, 0)), u'RenameLayer', None,vaOld
			, vaNew)

	def RenameView(self, vaOld=defaultNamedNotOptArg, vaNew=defaultNamedNotOptArg):
		"""RenameView"""
		return self._ApplyTypes_(260, 1, (12, 0), ((12, 0), (12, 0)), u'RenameView', None,vaOld
			, vaNew)

	def RenderAntialias(self, vaValue=defaultNamedOptArg):
		"""RenderAntialias"""
		return self._ApplyTypes_(333, 1, (12, 0), ((12, 16),), u'RenderAntialias', None,vaValue
			)

	def RenderColor(self, vaItem=defaultNamedNotOptArg, vaColor=defaultNamedOptArg):
		"""RenderColor"""
		return self._ApplyTypes_(331, 1, (12, 0), ((12, 0), (12, 16)), u'RenderColor', None,vaItem
			, vaColor)

	def RenderMeshDensity(self, vaDensity=defaultNamedOptArg):
		"""RenderMeshDensity"""
		return self._ApplyTypes_(844, 1, (12, 0), ((12, 16),), u'RenderMeshDensity', None,vaDensity
			)

	def RenderMeshMaxAngle(self, vaAngle=defaultNamedOptArg):
		"""RenderMeshMaxAngle"""
		return self._ApplyTypes_(845, 1, (12, 0), ((12, 16),), u'RenderMeshMaxAngle', None,vaAngle
			)

	def RenderMeshMaxAspectRatio(self, vaRatio=defaultNamedOptArg):
		"""RenderMeshMaxAspectRatio"""
		return self._ApplyTypes_(846, 1, (12, 0), ((12, 16),), u'RenderMeshMaxAspectRatio', None,vaRatio
			)

	def RenderMeshMaxDistEdgeToSrf(self, vaDistance=defaultNamedOptArg):
		"""RenderMeshMaxDistEdgeToSrf"""
		return self._ApplyTypes_(849, 1, (12, 0), ((12, 16),), u'RenderMeshMaxDistEdgeToSrf', None,vaDistance
			)

	def RenderMeshMaxEdgeLength(self, vaLength=defaultNamedOptArg):
		"""RenderMeshMaxEdgeLength"""
		return self._ApplyTypes_(848, 1, (12, 0), ((12, 16),), u'RenderMeshMaxEdgeLength', None,vaLength
			)

	def RenderMeshMinEdgeLength(self, vaLength=defaultNamedOptArg):
		"""RenderMeshMinEdgeLength"""
		return self._ApplyTypes_(847, 1, (12, 0), ((12, 16),), u'RenderMeshMinEdgeLength', None,vaLength
			)

	def RenderMeshMinInitialGridQuads(self, vaQuads=defaultNamedOptArg):
		"""RenderMeshMinInitialGridQuads"""
		return self._ApplyTypes_(850, 1, (12, 0), ((12, 16),), u'RenderMeshMinInitialGridQuads', None,vaQuads
			)

	def RenderMeshQuality(self, vaQuality=defaultNamedOptArg):
		"""RenderMeshQuality"""
		return self._ApplyTypes_(843, 1, (12, 0), ((12, 16),), u'RenderMeshQuality', None,vaQuality
			)

	def RenderMeshSettings(self, vaFlags=defaultNamedOptArg):
		"""RenderMeshSettings"""
		return self._ApplyTypes_(851, 1, (12, 0), ((12, 16),), u'RenderMeshSettings', None,vaFlags
			)

	def RenderResolution(self, vaSizes=defaultNamedOptArg):
		"""RenderResolution"""
		return self._ApplyTypes_(332, 1, (12, 0), ((12, 16),), u'RenderResolution', None,vaSizes
			)

	def RenderSettings(self, vaSetting=defaultNamedOptArg):
		"""RenderSettings"""
		return self._ApplyTypes_(334, 1, (12, 0), ((12, 16),), u'RenderSettings', None,vaSetting
			)

	def RestoreNamedCPlane(self, vaName=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""RestoreNamedCPlane"""
		return self._ApplyTypes_(282, 1, (12, 0), ((12, 0), (12, 16)), u'RestoreNamedCPlane', None,vaName
			, vaView)

	def RestoreNamedView(self, vaName=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaRestoreBitmap=defaultNamedOptArg):
		"""RestoreNamedView"""
		return self._ApplyTypes_(283, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'RestoreNamedView', None,vaName
			, vaView, vaRestoreBitmap)

	def ReverseCurve(self, vaObject=defaultNamedNotOptArg):
		"""ReverseCurve"""
		return self._ApplyTypes_(542, 1, (12, 0), ((12, 0),), u'ReverseCurve', None,vaObject
			)

	def ReverseSurface(self, vaObject=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg):
		"""ReverseSurface"""
		return self._ApplyTypes_(927, 1, (12, 0), ((12, 0), (12, 0)), u'ReverseSurface', None,vaObject
			, vaDir)

	def RotateCamera(self, vaView=defaultNamedOptArg, vaDir=defaultNamedOptArg, vaAngle=defaultNamedOptArg):
		"""RotateCamera"""
		return self._ApplyTypes_(519, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'RotateCamera', None,vaView
			, vaDir, vaAngle)

	def RotateObject(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg, vaAxis=defaultNamedOptArg
			, vaCopy=defaultNamedOptArg):
		"""RotateObject"""
		return self._ApplyTypes_(392, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16), (12, 16)), u'RotateObject', None,vaObject
			, vaPoint, vaAngle, vaAxis, vaCopy)

	def RotateObjects(self, vaObjects=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg, vaAxis=defaultNamedOptArg
			, vaCopy=defaultNamedOptArg):
		"""RotateObjects"""
		return self._ApplyTypes_(393, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16), (12, 16)), u'RotateObjects', None,vaObjects
			, vaPoint, vaAngle, vaAxis, vaCopy)

	def RotatePlane(self, vaPlane=defaultNamedNotOptArg, vaDegrees=defaultNamedNotOptArg, vaX=defaultNamedNotOptArg):
		"""RotatePlane"""
		return self._ApplyTypes_(630, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'RotatePlane', None,vaPlane
			, vaDegrees, vaX)

	def RotateView(self, vaView=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg):
		"""RotateView"""
		return self._ApplyTypes_(650, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'RotateView', None,vaView
			, vaDir, vaAngle)

	def SaveFileName(self, vaTitle=defaultNamedOptArg, vaFilter=defaultNamedOptArg, vaPath=defaultNamedOptArg, vaFile=defaultNamedOptArg
			, vaExt=defaultNamedOptArg):
		"""SaveFileName"""
		return self._ApplyTypes_(152, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'SaveFileName', None,vaTitle
			, vaFilter, vaPath, vaFile, vaExt)

	def SaveSettings(self, vaFile=defaultNamedNotOptArg, vaSection=defaultNamedOptArg, vaKey=defaultNamedOptArg, vaValue=defaultNamedOptArg):
		"""SaveSettings"""
		return self._ApplyTypes_(247, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), u'SaveSettings', None,vaFile
			, vaSection, vaKey, vaValue)

	def SaveToolBarCollection(self, vaAlias=defaultNamedNotOptArg):
		"""SaveToolBarCollection"""
		return self._ApplyTypes_(229, 1, (12, 0), ((12, 0),), u'SaveToolBarCollection', None,vaAlias
			)

	def SaveToolBarCollectionAs(self, vaAlias=defaultNamedNotOptArg, vaFile=defaultNamedOptArg):
		"""SaveToolBarCollectionAs"""
		return self._ApplyTypes_(230, 1, (12, 0), ((12, 0), (12, 16)), u'SaveToolBarCollectionAs', None,vaAlias
			, vaFile)

	def ScaleObject(self, vaObject=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg, vaScale=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""ScaleObject"""
		return self._ApplyTypes_(585, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'ScaleObject', None,vaObject
			, vaOrigin, vaScale, vaCopy)

	def ScaleObjects(self, vaObjects=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg, vaScale=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""ScaleObjects"""
		return self._ApplyTypes_(586, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), u'ScaleObjects', None,vaObjects
			, vaOrigin, vaScale, vaCopy)

	def ScreenSize(self):
		"""ScreenSize"""
		return self._ApplyTypes_(553, 1, (12, 0), (), u'ScreenSize', None,)

	def SdkVersion(self):
		"""SdkVersion"""
		return self._ApplyTypes_(359, 1, (12, 0), (), u'SdkVersion', None,)

	def SearchPathCount(self):
		"""SearchPathCount"""
		return self._ApplyTypes_(509, 1, (12, 0), (), u'SearchPathCount', None,)

	def SearchPathList(self):
		"""SearchPathList"""
		return self._ApplyTypes_(510, 1, (12, 0), (), u'SearchPathList', None,)

	def SelectObject(self, vaObject=defaultNamedNotOptArg):
		"""SelectObject"""
		return self._ApplyTypes_(200, 1, (12, 0), ((12, 0),), u'SelectObject', None,vaObject
			)

	def SelectObjectGrip(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg):
		"""SelectObjectGrip"""
		return self._ApplyTypes_(554, 1, (12, 0), ((12, 0), (12, 0)), u'SelectObjectGrip', None,vaObject
			, vaIndex)

	def SelectObjectGrips(self, vaObject=defaultNamedNotOptArg):
		"""SelectObjectGrips"""
		return self._ApplyTypes_(501, 1, (12, 0), ((12, 0),), u'SelectObjectGrips', None,vaObject
			)

	def SelectObjects(self, vaObjects=defaultNamedNotOptArg):
		"""SelectObjects"""
		return self._ApplyTypes_(298, 1, (12, 0), ((12, 0),), u'SelectObjects', None,vaObjects
			)

	def SelectedObjectGrips(self, vaObject=defaultNamedNotOptArg):
		"""SelectedObjectGrips"""
		return self._ApplyTypes_(560, 1, (12, 0), ((12, 0),), u'SelectedObjectGrips', None,vaObject
			)

	def SelectedObjects(self, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""SelectedObjects"""
		return self._ApplyTypes_(43, 1, (12, 0), ((12, 16), (12, 16)), u'SelectedObjects', None,vaIncludeLights
			, vaIncludeGrips)

	def SendKeystrokes(self, vaStr=defaultNamedOptArg, vaReturn=defaultNamedOptArg):
		"""SendKeystrokes"""
		return self._ApplyTypes_(496, 1, (12, 0), ((12, 16), (12, 16)), u'SendKeystrokes', None,vaStr
			, vaReturn)

	def SetAttributeData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedNotOptArg, vaKey=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""SetAttributeData"""
		return self._ApplyTypes_(683, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'SetAttributeData', None,vaObject
			, vaApp, vaKey, vaValue)

	def SetDocumentData(self, vaApp=defaultNamedNotOptArg, vaKey=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""SetDocumentData"""
		return self._ApplyTypes_(243, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'SetDocumentData', None,vaApp
			, vaKey, vaValue)

	def SetObjectData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedNotOptArg, vaKey=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""SetObjectData"""
		return self._ApplyTypes_(244, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'SetObjectData', None,vaObject
			, vaApp, vaKey, vaValue)

	def SetUserText(self, vaObject=defaultNamedNotOptArg, vaKey=defaultNamedNotOptArg, vaText=defaultNamedOptArg, vaMode=defaultNamedOptArg):
		"""SetUserText"""
		return self._ApplyTypes_(728, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'SetUserText', None,vaObject
			, vaKey, vaText, vaMode)

	def ShearObject(self, vaObject=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg, vaRefPt=defaultNamedNotOptArg, vaDegrees=defaultNamedNotOptArg
			, vaCopy=defaultNamedOptArg):
		"""ShearObject"""
		return self._ApplyTypes_(587, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 16)), u'ShearObject', None,vaObject
			, vaOrigin, vaRefPt, vaDegrees, vaCopy)

	def ShearObjects(self, vaObjects=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg, vaRefPt=defaultNamedNotOptArg, vaDegrees=defaultNamedNotOptArg
			, vaCopy=defaultNamedOptArg):
		"""ShearObjects"""
		return self._ApplyTypes_(588, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 16)), u'ShearObjects', None,vaObjects
			, vaOrigin, vaRefPt, vaDegrees, vaCopy)

	def ShortPath(self, vaObject=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg):
		"""ShortPath"""
		return self._ApplyTypes_(702, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ShortPath', None,vaObject
			, vaStart, vaEnd)

	def ShowGrid(self, vaView=defaultNamedOptArg, vaShow=defaultNamedOptArg):
		"""ShowGrid"""
		return self._ApplyTypes_(738, 1, (12, 0), ((12, 16), (12, 16)), u'ShowGrid', None,vaView
			, vaShow)

	def ShowGridAxes(self, vaView=defaultNamedOptArg, vaShow=defaultNamedOptArg):
		"""ShowGridAxes"""
		return self._ApplyTypes_(739, 1, (12, 0), ((12, 16), (12, 16)), u'ShowGridAxes', None,vaView
			, vaShow)

	def ShowGroup(self, vaName=defaultNamedNotOptArg):
		"""ShowGroup"""
		return self._ApplyTypes_(872, 1, (12, 0), ((12, 0),), u'ShowGroup', None,vaName
			)

	def ShowObject(self, vaObject=defaultNamedNotOptArg):
		"""ShowObject"""
		return self._ApplyTypes_(201, 1, (12, 0), ((12, 0),), u'ShowObject', None,vaObject
			)

	def ShowObjects(self, vaObjects=defaultNamedNotOptArg):
		"""ShowObjects"""
		return self._ApplyTypes_(305, 1, (12, 0), ((12, 0),), u'ShowObjects', None,vaObjects
			)

	def ShowToolBar(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""ShowToolBar"""
		return self._ApplyTypes_(231, 1, (12, 0), ((12, 0), (12, 0)), u'ShowToolBar', None,vaAlias
			, vaName)

	def ShowViewTitle(self, vaView=defaultNamedOptArg, vaValue=defaultNamedOptArg):
		"""ShowViewTitle"""
		return self._ApplyTypes_(261, 1, (12, 0), ((12, 16), (12, 16)), u'ShowViewTitle', None,vaView
			, vaValue)

	def ShowWorldAxes(self, vaView=defaultNamedOptArg, vaShow=defaultNamedOptArg):
		"""ShowWorldAxes"""
		return self._ApplyTypes_(740, 1, (12, 0), ((12, 16), (12, 16)), u'ShowWorldAxes', None,vaView
			, vaShow)

	def ShrinkTrimmedSurface(self, vaObject=defaultNamedNotOptArg):
		"""ShrinkTrimmedSurface"""
		return self._ApplyTypes_(700, 1, (12, 0), ((12, 0),), u'ShrinkTrimmedSurface', None,vaObject
			)

	def SimplifyArray(self, vaArray=defaultNamedNotOptArg):
		"""SimplifyArray"""
		return self._ApplyTypes_(597, 1, (12, 0), ((12, 0),), u'SimplifyArray', None,vaArray
			)

	def SimplifyCurve(self, vaObject=defaultNamedNotOptArg, vaFlags=defaultNamedOptArg):
		"""SimplifyCurve"""
		return self._ApplyTypes_(573, 1, (12, 0), ((12, 0), (12, 16)), u'SimplifyCurve', None,vaObject
			, vaFlags)

	def SinH(self, vx=defaultNamedNotOptArg):
		"""SinH"""
		return self._ApplyTypes_(759, 1, (12, 0), ((12, 0),), u'SinH', None,vx
			)

	def Sleep(self, vaTime=defaultNamedNotOptArg):
		"""Sleep"""
		return self._ApplyTypes_(248, 1, (12, 0), ((12, 0),), u'Sleep', None,vaTime
			)

	def Snap(self, vaMode=defaultNamedOptArg):
		"""Snap"""
		return self._ApplyTypes_(344, 1, (12, 0), ((12, 16),), u'Snap', None,vaMode
			)

	def Sort(self, vaStrings=defaultNamedNotOptArg, vaMode=defaultNamedOptArg, vaNoCase=defaultNamedOptArg):
		"""Sort"""
		return self._ApplyTypes_(249, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'Sort', None,vaStrings
			, vaMode, vaNoCase)

	def SortNumbers(self, vaNumbers=defaultNamedNotOptArg, vaAscending=defaultNamedOptArg):
		"""SortNumbers"""
		return self._ApplyTypes_(552, 1, (12, 0), ((12, 0), (12, 16)), u'SortNumbers', None,vaNumbers
			, vaAscending)

	def SortPointList(self, vaPoints=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""SortPointList"""
		return self._ApplyTypes_(644, 1, (12, 0), ((12, 0), (12, 16)), u'SortPointList', None,vaPoints
			, vaTolerance)

	def SortPoints(self, vaPoints=defaultNamedNotOptArg, vaAscending=defaultNamedOptArg, vaOrder=defaultNamedOptArg):
		"""SortPoints"""
		return self._ApplyTypes_(551, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'SortPoints', None,vaPoints
			, vaAscending, vaOrder)

	def SortStrings(self, vaStrings=defaultNamedNotOptArg, vaMode=defaultNamedOptArg, vaNoCase=defaultNamedOptArg):
		"""SortStrings"""
		return self._ApplyTypes_(640, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'SortStrings', None,vaStrings
			, vaMode, vaNoCase)

	def SplitBrep(self, vaObject=defaultNamedNotOptArg, vaCutter=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""SplitBrep"""
		return self._ApplyTypes_(637, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'SplitBrep', None,vaObject
			, vaCutter, vaDelete)

	def SplitCurve(self, vaCrv=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""SplitCurve"""
		return self._ApplyTypes_(504, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'SplitCurve', None,vaCrv
			, vaParam, vaDelete)

	def SplitDisjointMesh(self, vaMesh=defaultNamedNotOptArg, vaDelete=defaultNamedNotOptArg):
		"""SplitDisjointMesh"""
		return self._ApplyTypes_(722, 1, (12, 0), ((12, 0), (12, 0)), u'SplitDisjointMesh', None,vaMesh
			, vaDelete)

	def SpoolToPrinter(self, vaFile=defaultNamedNotOptArg, vaPrinter=defaultNamedNotOptArg):
		"""SpoolToPrinter"""
		return self._ApplyTypes_(357, 1, (12, 0), ((12, 0), (12, 0)), u'SpoolToPrinter', None,vaFile
			, vaPrinter)

	def SpotLightHardness(self, vaLight=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""SpotLightHardness"""
		return self._ApplyTypes_(171, 1, (12, 0), ((12, 0), (12, 16)), u'SpotLightHardness', None,vaLight
			, vaValue)

	def SpotLightRadius(self, vaLight=defaultNamedNotOptArg, vaRadius=defaultNamedOptArg):
		"""SpotLightRadius"""
		return self._ApplyTypes_(584, 1, (12, 0), ((12, 0), (12, 16)), u'SpotLightRadius', None,vaLight
			, vaRadius)

	def SpotLightShadowIntensity(self, vaLight=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""SpotLightShadowIntensity"""
		return self._ApplyTypes_(172, 1, (12, 0), ((12, 0), (12, 16)), u'SpotLightShadowIntensity', None,vaLight
			, vaValue)

	def StartupScriptCount(self):
		"""StartupScriptCount"""
		return self._ApplyTypes_(712, 1, (12, 0), (), u'StartupScriptCount', None,)

	def StartupScriptList(self):
		"""StartupScriptList"""
		return self._ApplyTypes_(713, 1, (12, 0), (), u'StartupScriptList', None,)

	def StatusBarDistance(self, vaDistance=defaultNamedOptArg):
		"""StatusBarDistance"""
		return self._ApplyTypes_(26, 1, (12, 0), ((12, 16),), u'StatusBarDistance', None,vaDistance
			)

	def StatusBarMessage(self, vaText=defaultNamedOptArg):
		"""StatusBarMessage"""
		return self._ApplyTypes_(28, 1, (12, 0), ((12, 16),), u'StatusBarMessage', None,vaText
			)

	def StatusBarNumber(self, vaNumber=defaultNamedOptArg):
		"""StatusBarNumber"""
		return self._ApplyTypes_(312, 1, (12, 0), ((12, 16),), u'StatusBarNumber', None,vaNumber
			)

	def StatusBarPoint(self, vaPoint=defaultNamedOptArg):
		"""StatusBarPoint"""
		return self._ApplyTypes_(27, 1, (12, 0), ((12, 16),), u'StatusBarPoint', None,vaPoint
			)

	def Str2Pt(self, vaStr=defaultNamedNotOptArg):
		"""Str2Pt"""
		return self._ApplyTypes_(409, 1, (12, 0), ((12, 0),), u'Str2Pt', None,vaStr
			)

	def Str2PtArray(self, vaStr=defaultNamedNotOptArg):
		"""Str2PtArray"""
		return self._ApplyTypes_(410, 1, (12, 0), ((12, 0),), u'Str2PtArray', None,vaStr
			)

	def StringBox(self, vaPrompt=defaultNamedOptArg, vaString=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""StringBox"""
		return self._ApplyTypes_(60, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'StringBox', None,vaPrompt
			, vaString, vaTitle)

	def Strtok(self, vaString=defaultNamedNotOptArg, vaSeps=defaultNamedOptArg):
		"""Strtok"""
		return self._ApplyTypes_(250, 1, (12, 0), ((12, 0), (12, 16)), u'Strtok', None,vaString
			, vaSeps)

	def Sum(self, var=defaultNamedNotOptArg):
		"""Sum"""
		return self._ApplyTypes_(770, 1, (12, 0), ((12, 0),), u'Sum', None,var
			)

	def SurfaceArea(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceArea"""
		return self._ApplyTypes_(382, 1, (12, 0), ((12, 0),), u'SurfaceArea', None,vaObject
			)

	def SurfaceAreaCentroid(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceAreaCentroid"""
		return self._ApplyTypes_(384, 1, (12, 0), ((12, 0),), u'SurfaceAreaCentroid', None,vaObject
			)

	def SurfaceAreaMoments(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceAreaMoments"""
		return self._ApplyTypes_(386, 1, (12, 0), ((12, 0),), u'SurfaceAreaMoments', None,vaObject
			)

	def SurfaceClosestPoint(self, vaObject=defaultNamedNotOptArg, vaPt=defaultNamedNotOptArg):
		"""SurfaceClosestPoint"""
		return self._ApplyTypes_(215, 1, (12, 0), ((12, 0), (12, 0)), u'SurfaceClosestPoint', None,vaObject
			, vaPt)

	def SurfaceCone(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceCone"""
		return self._ApplyTypes_(889, 1, (12, 0), ((12, 0),), u'SurfaceCone', None,vaObject
			)

	def SurfaceContourPoints(self, vaObject=defaultNamedNotOptArg, vaBase=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaInterval=defaultNamedOptArg
			, vaAngle=defaultNamedOptArg):
		"""SurfaceContourPoints"""
		return self._ApplyTypes_(79, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16), (12, 16)), u'SurfaceContourPoints', None,vaObject
			, vaBase, vaEnd, vaInterval, vaAngle)

	def SurfaceCurvature(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""SurfaceCurvature"""
		return self._ApplyTypes_(378, 1, (12, 0), ((12, 0), (12, 0)), u'SurfaceCurvature', None,vaObject
			, vaParam)

	def SurfaceCurvatureAnalysis(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceCurvatureAnalysis"""
		return self._ApplyTypes_(632, 1, (12, 0), ((12, 0),), u'SurfaceCurvatureAnalysis', None,vaObject
			)

	def SurfaceCylinder(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceCylinder"""
		return self._ApplyTypes_(888, 1, (12, 0), ((12, 0),), u'SurfaceCylinder', None,vaObject
			)

	def SurfaceDegree(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""SurfaceDegree"""
		return self._ApplyTypes_(216, 1, (12, 0), ((12, 0), (12, 16)), u'SurfaceDegree', None,vaObject
			, vaValue)

	def SurfaceDomain(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""SurfaceDomain"""
		return self._ApplyTypes_(217, 1, (12, 0), ((12, 0), (12, 0)), u'SurfaceDomain', None,vaObject
			, vaValue)

	def SurfaceEditPoints(self, vaObject=defaultNamedNotOptArg, vaReturnParameters=defaultNamedOptArg, vaReturnAll=defaultNamedOptArg):
		"""SurfaceEditPoints"""
		return self._ApplyTypes_(427, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'SurfaceEditPoints', None,vaObject
			, vaReturnParameters, vaReturnAll)

	def SurfaceEvaluate(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaDerCount=defaultNamedNotOptArg):
		"""SurfaceEvaluate"""
		return self._ApplyTypes_(583, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'SurfaceEvaluate', None,vaObject
			, vaParam, vaDerCount)

	def SurfaceFrame(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""SurfaceFrame"""
		return self._ApplyTypes_(623, 1, (12, 0), ((12, 0), (12, 0)), u'SurfaceFrame', None,vaObject
			, vaParam)

	def SurfaceIsocurveDensity(self, vaObject=defaultNamedNotOptArg, vaDensity=defaultNamedOptArg):
		"""SurfaceIsocurveDensity"""
		return self._ApplyTypes_(361, 1, (12, 0), ((12, 0), (12, 16)), u'SurfaceIsocurveDensity', None,vaObject
			, vaDensity)

	def SurfaceKnotCount(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceKnotCount"""
		return self._ApplyTypes_(431, 1, (12, 0), ((12, 0),), u'SurfaceKnotCount', None,vaObject
			)

	def SurfaceKnots(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceKnots"""
		return self._ApplyTypes_(432, 1, (12, 0), ((12, 0),), u'SurfaceKnots', None,vaObject
			)

	def SurfaceNormal(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""SurfaceNormal"""
		return self._ApplyTypes_(362, 1, (12, 0), ((12, 0), (12, 0)), u'SurfaceNormal', None,vaObject
			, vaParam)

	def SurfacePointCount(self, vaObject=defaultNamedNotOptArg):
		"""SurfacePointCount"""
		return self._ApplyTypes_(218, 1, (12, 0), ((12, 0),), u'SurfacePointCount', None,vaObject
			)

	def SurfacePoints(self, vaObject=defaultNamedNotOptArg, vaReturnAll=defaultNamedOptArg):
		"""SurfacePoints"""
		return self._ApplyTypes_(372, 1, (12, 0), ((12, 0), (12, 16)), u'SurfacePoints', None,vaObject
			, vaReturnAll)

	def SurfacePrincipalCurvature(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""SurfacePrincipalCurvature"""
		return self._ApplyTypes_(717, 1, (12, 0), ((12, 0), (12, 0)), u'SurfacePrincipalCurvature', None,vaObject
			, vaPoint)

	def SurfaceSeam(self, vaObject=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""SurfaceSeam"""
		return self._ApplyTypes_(804, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'SurfaceSeam', None,vaObject
			, vaDir, vaParam)

	def SurfaceSphere(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceSphere"""
		return self._ApplyTypes_(887, 1, (12, 0), ((12, 0),), u'SurfaceSphere', None,vaObject
			)

	def SurfaceSurfaceIntersection(self, vaSrfA=defaultNamedNotOptArg, vaSrfB=defaultNamedNotOptArg, vaTol=defaultNamedOptArg, vaCreate=defaultNamedOptArg):
		"""SurfaceSurfaceIntersection"""
		return self._ApplyTypes_(484, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), u'SurfaceSurfaceIntersection', None,vaSrfA
			, vaSrfB, vaTol, vaCreate)

	def SurfaceTorus(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceTorus"""
		return self._ApplyTypes_(890, 1, (12, 0), ((12, 0),), u'SurfaceTorus', None,vaObject
			)

	def SurfaceVolume(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceVolume"""
		return self._ApplyTypes_(383, 1, (12, 0), ((12, 0),), u'SurfaceVolume', None,vaObject
			)

	def SurfaceVolumeCentroid(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceVolumeCentroid"""
		return self._ApplyTypes_(385, 1, (12, 0), ((12, 0),), u'SurfaceVolumeCentroid', None,vaObject
			)

	def SurfaceVolumeMoments(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceVolumeMoments"""
		return self._ApplyTypes_(387, 1, (12, 0), ((12, 0),), u'SurfaceVolumeMoments', None,vaObject
			)

	def SurfaceWeights(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceWeights"""
		return self._ApplyTypes_(433, 1, (12, 0), ((12, 0),), u'SurfaceWeights', None,vaObject
			)

	def SynchronizeCPlanes(self, vaView=defaultNamedOptArg):
		"""SynchronizeCPlanes"""
		return self._ApplyTypes_(289, 1, (12, 0), ((12, 16),), u'SynchronizeCPlanes', None,vaView
			)

	def TanH(self, vx=defaultNamedNotOptArg):
		"""TanH"""
		return self._ApplyTypes_(761, 1, (12, 0), ((12, 0),), u'TanH', None,vx
			)

	def TemplateFile(self, vaFile=defaultNamedOptArg):
		"""TemplateFile"""
		return self._ApplyTypes_(529, 1, (12, 0), ((12, 16),), u'TemplateFile', None,vaFile
			)

	def TemplateFolder(self, vaFolder=defaultNamedOptArg):
		"""TemplateFolder"""
		return self._ApplyTypes_(528, 1, (12, 0), ((12, 16),), u'TemplateFolder', None,vaFolder
			)

	def TextDotPoint(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedOptArg):
		"""TextDotPoint"""
		return self._ApplyTypes_(422, 1, (12, 0), ((12, 0), (12, 16)), u'TextDotPoint', None,vaObject
			, vaPoint)

	def TextDotText(self, vaObject=defaultNamedNotOptArg, vaText=defaultNamedOptArg):
		"""TextDotText"""
		return self._ApplyTypes_(421, 1, (12, 0), ((12, 0), (12, 16)), u'TextDotText', None,vaObject
			, vaText)

	def TextObjectFont(self, vaObject=defaultNamedNotOptArg, vaFont=defaultNamedOptArg):
		"""TextObjectFont"""
		return self._ApplyTypes_(474, 1, (12, 0), ((12, 0), (12, 16)), u'TextObjectFont', None,vaObject
			, vaFont)

	def TextObjectHeight(self, vaObject=defaultNamedNotOptArg, vaSize=defaultNamedOptArg):
		"""TextObjectHeight"""
		return self._ApplyTypes_(473, 1, (12, 0), ((12, 0), (12, 16)), u'TextObjectHeight', None,vaObject
			, vaSize)

	def TextObjectPlane(self, vaObject=defaultNamedNotOptArg, vaPlane=defaultNamedOptArg):
		"""TextObjectPlane"""
		return self._ApplyTypes_(476, 1, (12, 0), ((12, 0), (12, 16)), u'TextObjectPlane', None,vaObject
			, vaPlane)

	def TextObjectPoint(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedOptArg):
		"""TextObjectPoint"""
		return self._ApplyTypes_(471, 1, (12, 0), ((12, 0), (12, 16)), u'TextObjectPoint', None,vaObject
			, vaPoint)

	def TextObjectStyle(self, vaObject=defaultNamedNotOptArg, vaStyle=defaultNamedOptArg):
		"""TextObjectStyle"""
		return self._ApplyTypes_(475, 1, (12, 0), ((12, 0), (12, 16)), u'TextObjectStyle', None,vaObject
			, vaStyle)

	def TextObjectText(self, vaObject=defaultNamedNotOptArg, vaText=defaultNamedOptArg):
		"""TextObjectText"""
		return self._ApplyTypes_(472, 1, (12, 0), ((12, 0), (12, 16)), u'TextObjectText', None,vaObject
			, vaText)

	def TextOut(self, vaText=defaultNamedNotOptArg, vaTitle=defaultNamedOptArg):
		"""TextOut"""
		return self._ApplyTypes_(755, 1, (12, 0), ((12, 0), (12, 16)), u'TextOut', None,vaText
			, vaTitle)

	def TiltView(self, vaView=defaultNamedOptArg, vaDir=defaultNamedOptArg, vaAngle=defaultNamedOptArg):
		"""TiltView"""
		return self._ApplyTypes_(518, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'TiltView', None,vaView
			, vaDir, vaAngle)

	def ToDegrees(self, vaRadians=defaultNamedNotOptArg):
		"""ToDegrees"""
		return self._ApplyTypes_(664, 1, (12, 0), ((12, 0),), u'ToDegrees', None,vaRadians
			)

	def ToRadians(self, vaDegrees=defaultNamedNotOptArg):
		"""ToRadians"""
		return self._ApplyTypes_(665, 1, (12, 0), ((12, 0),), u'ToRadians', None,vaDegrees
			)

	def ToolBarCollectionCount(self):
		"""ToolBarCollectionCount"""
		return self._ApplyTypes_(232, 1, (12, 0), (), u'ToolBarCollectionCount', None,)

	def ToolBarCollectionNames(self, vaPath=defaultNamedOptArg):
		"""ToolBarCollectionNames"""
		return self._ApplyTypes_(234, 1, (12, 0), ((12, 16),), u'ToolBarCollectionNames', None,vaPath
			)

	def ToolBarCollectionPath(self, vaAlias=defaultNamedNotOptArg):
		"""ToolBarCollectionPath"""
		return self._ApplyTypes_(233, 1, (12, 0), ((12, 0),), u'ToolBarCollectionPath', None,vaAlias
			)

	def ToolBarCount(self, vaAlias=defaultNamedNotOptArg):
		"""ToolBarCount"""
		return self._ApplyTypes_(235, 1, (12, 0), ((12, 0),), u'ToolBarCount', None,vaAlias
			)

	def ToolBarNames(self, vaAlias=defaultNamedNotOptArg):
		"""ToolBarNames"""
		return self._ApplyTypes_(236, 1, (12, 0), ((12, 0),), u'ToolBarNames', None,vaAlias
			)

	def TransformObject(self, vaObject=defaultNamedNotOptArg, vaXform=defaultNamedNotOptArg):
		"""TransformObject"""
		return self._ApplyTypes_(272, 1, (12, 0), ((12, 0), (12, 0)), u'TransformObject', None,vaObject
			, vaXform)

	def TransformObjects(self, vaObjects=defaultNamedNotOptArg, vaXform=defaultNamedNotOptArg):
		"""TransformObjects"""
		return self._ApplyTypes_(302, 1, (12, 0), ((12, 0), (12, 0)), u'TransformObjects', None,vaObjects
			, vaXform)

	def TrimCurve(self, vaCrv=defaultNamedNotOptArg, vaInterval=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""TrimCurve"""
		return self._ApplyTypes_(505, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), u'TrimCurve', None,vaCrv
			, vaInterval, vaDelete)

	def UnifyMeshNormals(self, vaMesh=defaultNamedNotOptArg):
		"""UnifyMeshNormals"""
		return self._ApplyTypes_(723, 1, (12, 0), ((12, 0),), u'UnifyMeshNormals', None,vaMesh
			)

	def UnitAbsoluteTolerance(self, vaTol=defaultNamedOptArg):
		"""UnitAbsoluteTolerance"""
		return self._ApplyTypes_(324, 1, (12, 0), ((12, 16),), u'UnitAbsoluteTolerance', None,vaTol
			)

	def UnitAngleTolerance(self, vaTol=defaultNamedOptArg):
		"""UnitAngleTolerance"""
		return self._ApplyTypes_(325, 1, (12, 0), ((12, 16),), u'UnitAngleTolerance', None,vaTol
			)

	def UnitCustomUnitSystem(self, vaValue=defaultNamedNotOptArg, vaScale=defaultNamedOptArg, vaName=defaultNamedOptArg):
		"""UnitCustomUnitSystem"""
		return self._ApplyTypes_(326, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'UnitCustomUnitSystem', None,vaValue
			, vaScale, vaName)

	def UnitDistanceDisplayMode(self, vaMode=defaultNamedOptArg):
		"""UnitDistanceDisplayMode"""
		return self._ApplyTypes_(327, 1, (12, 0), ((12, 16),), u'UnitDistanceDisplayMode', None,vaMode
			)

	def UnitDistanceDisplayPrecision(self, vaPrecision=defaultNamedOptArg):
		"""UnitDistanceDisplayPrecision"""
		return self._ApplyTypes_(328, 1, (12, 0), ((12, 16),), u'UnitDistanceDisplayPrecision', None,vaPrecision
			)

	def UnitRelativeTolerance(self, vaTol=defaultNamedOptArg):
		"""UnitRelativeTolerance"""
		return self._ApplyTypes_(329, 1, (12, 0), ((12, 16),), u'UnitRelativeTolerance', None,vaTol
			)

	def UnitScale(self, vaTo=defaultNamedNotOptArg, vaFrom=defaultNamedOptArg):
		"""UnitScale"""
		return self._ApplyTypes_(868, 1, (12, 0), ((12, 0), (12, 16)), u'UnitScale', None,vaTo
			, vaFrom)

	def UnitSystem(self, vaSystem=defaultNamedOptArg, vaScale=defaultNamedOptArg):
		"""UnitSystem"""
		return self._ApplyTypes_(330, 1, (12, 0), ((12, 16), (12, 16)), u'UnitSystem', None,vaSystem
			, vaScale)

	def UnitSystemName(self, vaCapitalize=defaultNamedOptArg, vaSingular=defaultNamedOptArg, vaAbbreviate=defaultNamedOptArg):
		"""UnitSystemName"""
		return self._ApplyTypes_(492, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'UnitSystemName', None,vaCapitalize
			, vaSingular, vaAbbreviate)

	def UnlockGroup(self, vaName=defaultNamedNotOptArg):
		"""UnlockGroup"""
		return self._ApplyTypes_(874, 1, (12, 0), ((12, 0),), u'UnlockGroup', None,vaName
			)

	def UnlockObject(self, vaObject=defaultNamedNotOptArg):
		"""UnlockObject"""
		return self._ApplyTypes_(202, 1, (12, 0), ((12, 0),), u'UnlockObject', None,vaObject
			)

	def UnlockObjects(self, vaObjects=defaultNamedNotOptArg):
		"""UnlockObjects"""
		return self._ApplyTypes_(306, 1, (12, 0), ((12, 0),), u'UnlockObjects', None,vaObjects
			)

	def UnselectAllObjects(self):
		"""UnselectAllObjects"""
		return self._ApplyTypes_(44, 1, (12, 0), (), u'UnselectAllObjects', None,)

	def UnselectObject(self, vaObject=defaultNamedNotOptArg):
		"""UnselectObject"""
		return self._ApplyTypes_(299, 1, (12, 0), ((12, 0),), u'UnselectObject', None,vaObject
			)

	def UnselectObjectGrip(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg):
		"""UnselectObjectGrip"""
		return self._ApplyTypes_(555, 1, (12, 0), ((12, 0), (12, 0)), u'UnselectObjectGrip', None,vaObject
			, vaIndex)

	def UnselectObjectGrips(self, vaObject=defaultNamedNotOptArg):
		"""UnselectObjectGrips"""
		return self._ApplyTypes_(502, 1, (12, 0), ((12, 0),), u'UnselectObjectGrips', None,vaObject
			)

	def UnselectObjects(self, vaObjects=defaultNamedNotOptArg):
		"""UnselectObjects"""
		return self._ApplyTypes_(300, 1, (12, 0), ((12, 0),), u'UnselectObjects', None,vaObjects
			)

	def UnselectedObjects(self, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""UnselectedObjects"""
		return self._ApplyTypes_(45, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'UnselectedObjects', None,vaSelect
			, vaIncludeLights, vaIncludeGrips)

	def VectorAdd(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorAdd"""
		return self._ApplyTypes_(612, 1, (12, 0), ((12, 0), (12, 0)), u'VectorAdd', None,vaVec0
			, vaVec1)

	def VectorCompare(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorCompare"""
		return self._ApplyTypes_(613, 1, (12, 0), ((12, 0), (12, 0)), u'VectorCompare', None,vaVec0
			, vaVec1)

	def VectorCreate(self, vaPt0=defaultNamedNotOptArg, vaPt1=defaultNamedNotOptArg):
		"""VectorCreate"""
		return self._ApplyTypes_(614, 1, (12, 0), ((12, 0), (12, 0)), u'VectorCreate', None,vaPt0
			, vaPt1)

	def VectorCrossProduct(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorCrossProduct"""
		return self._ApplyTypes_(615, 1, (12, 0), ((12, 0), (12, 0)), u'VectorCrossProduct', None,vaVec0
			, vaVec1)

	def VectorDivide(self, vaVec=defaultNamedNotOptArg, vaScale=defaultNamedNotOptArg):
		"""VectorDivide"""
		return self._ApplyTypes_(625, 1, (12, 0), ((12, 0), (12, 0)), u'VectorDivide', None,vaVec
			, vaScale)

	def VectorDotProduct(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorDotProduct"""
		return self._ApplyTypes_(616, 1, (12, 0), ((12, 0), (12, 0)), u'VectorDotProduct', None,vaVec0
			, vaVec1)

	def VectorLength(self, vaVec=defaultNamedNotOptArg):
		"""VectorLength"""
		return self._ApplyTypes_(617, 1, (12, 0), ((12, 0),), u'VectorLength', None,vaVec
			)

	def VectorMultiply(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorMultiply"""
		return self._ApplyTypes_(624, 1, (12, 0), ((12, 0), (12, 0)), u'VectorMultiply', None,vaVec0
			, vaVec1)

	def VectorReverse(self, vaVec=defaultNamedNotOptArg):
		"""VectorReverse"""
		return self._ApplyTypes_(618, 1, (12, 0), ((12, 0),), u'VectorReverse', None,vaVec
			)

	def VectorRotate(self, vaVec=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg, vaAxis=defaultNamedNotOptArg):
		"""VectorRotate"""
		return self._ApplyTypes_(678, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'VectorRotate', None,vaVec
			, vaAngle, vaAxis)

	def VectorScale(self, vaVec=defaultNamedNotOptArg, vaScale=defaultNamedNotOptArg):
		"""VectorScale"""
		return self._ApplyTypes_(619, 1, (12, 0), ((12, 0), (12, 0)), u'VectorScale', None,vaVec
			, vaScale)

	def VectorSubtract(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorSubtract"""
		return self._ApplyTypes_(620, 1, (12, 0), ((12, 0), (12, 0)), u'VectorSubtract', None,vaVec0
			, vaVec1)

	def VectorTransform(self, vaVector=defaultNamedNotOptArg, vaXform=defaultNamedNotOptArg):
		"""VectorTransform"""
		return self._ApplyTypes_(800, 1, (12, 0), ((12, 0), (12, 0)), u'VectorTransform', None,vaVector
			, vaXform)

	def VectorUnitize(self, vaVec=defaultNamedNotOptArg):
		"""VectorUnitize"""
		return self._ApplyTypes_(621, 1, (12, 0), ((12, 0),), u'VectorUnitize', None,vaVec
			)

	def Version(self):
		"""Version"""
		return self._ApplyTypes_(288, 1, (12, 0), (), u'Version', None,)

	def ViewCPlane(self, vaView=defaultNamedOptArg, vaValue=defaultNamedOptArg):
		"""ViewCPlane"""
		return self._ApplyTypes_(264, 1, (12, 0), ((12, 16), (12, 16)), u'ViewCPlane', None,vaView
			, vaValue)

	def ViewCamera(self, vaView=defaultNamedOptArg, vaCamera=defaultNamedOptArg):
		"""ViewCamera"""
		return self._ApplyTypes_(394, 1, (12, 0), ((12, 16), (12, 16)), u'ViewCamera', None,vaView
			, vaCamera)

	def ViewCameraLens(self, vaView=defaultNamedOptArg, vaValue=defaultNamedOptArg):
		"""ViewCameraLens"""
		return self._ApplyTypes_(262, 1, (12, 0), ((12, 16), (12, 16)), u'ViewCameraLens', None,vaView
			, vaValue)

	def ViewCameraPlane(self, vaView=defaultNamedOptArg):
		"""ViewCameraPlane"""
		return self._ApplyTypes_(778, 1, (12, 0), ((12, 16),), u'ViewCameraPlane', None,vaView
			)

	def ViewCameraTarget(self, vaView=defaultNamedOptArg, vaCamera=defaultNamedOptArg, vaTarget=defaultNamedOptArg):
		"""ViewCameraTarget"""
		return self._ApplyTypes_(263, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'ViewCameraTarget', None,vaView
			, vaCamera, vaTarget)

	def ViewCameraUp(self, vaView=defaultNamedOptArg, vaUp=defaultNamedOptArg):
		"""ViewCameraUp"""
		return self._ApplyTypes_(517, 1, (12, 0), ((12, 16), (12, 16)), u'ViewCameraUp', None,vaView
			, vaUp)

	def ViewDisplayMode(self, vaView=defaultNamedOptArg, vaMode=defaultNamedOptArg):
		"""ViewDisplayMode"""
		return self._ApplyTypes_(290, 1, (12, 0), ((12, 16), (12, 16)), u'ViewDisplayMode', None,vaView
			, vaMode)

	def ViewDisplayModeEx(self, vaView=defaultNamedOptArg, vaMode=defaultNamedOptArg, vaNames=defaultNamedOptArg):
		"""ViewDisplayModeEx"""
		return self._ApplyTypes_(910, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), u'ViewDisplayModeEx', None,vaView
			, vaMode, vaNames)

	def ViewDisplayModeName(self, vaMode=defaultNamedNotOptArg):
		"""ViewDisplayModeName"""
		return self._ApplyTypes_(909, 1, (12, 0), ((12, 0),), u'ViewDisplayModeName', None,vaMode
			)

	def ViewDisplayModes(self, vaNames=defaultNamedOptArg):
		"""ViewDisplayModes"""
		return self._ApplyTypes_(908, 1, (12, 0), ((12, 16),), u'ViewDisplayModes', None,vaNames
			)

	def ViewNames(self, vaNames=defaultNamedOptArg, vaTypes=defaultNamedOptArg):
		"""ViewNames"""
		return self._ApplyTypes_(265, 1, (12, 0), ((12, 16), (12, 16)), u'ViewNames', None,vaNames
			, vaTypes)

	def ViewNearCorners(self, vaView=defaultNamedOptArg):
		"""ViewNearCorners"""
		return self._ApplyTypes_(823, 1, (12, 0), ((12, 16),), u'ViewNearCorners', None,vaView
			)

	def ViewProjection(self, vaView=defaultNamedOptArg, vaValue=defaultNamedOptArg):
		"""ViewProjection"""
		return self._ApplyTypes_(266, 1, (12, 0), ((12, 16), (12, 16)), u'ViewProjection', None,vaView
			, vaValue)

	def ViewRadius(self, vaView=defaultNamedOptArg, vaRadius=defaultNamedOptArg):
		"""ViewRadius"""
		return self._ApplyTypes_(824, 1, (12, 0), ((12, 16), (12, 16)), u'ViewRadius', None,vaView
			, vaRadius)

	def ViewSize(self, vaView=defaultNamedOptArg):
		"""ViewSize"""
		return self._ApplyTypes_(267, 1, (12, 0), ((12, 16),), u'ViewSize', None,vaView
			)

	def ViewTarget(self, vaView=defaultNamedOptArg, vaTarget=defaultNamedOptArg):
		"""ViewTarget"""
		return self._ApplyTypes_(395, 1, (12, 0), ((12, 16), (12, 16)), u'ViewTarget', None,vaView
			, vaTarget)

	def ViewTitle(self, vaView=defaultNamedNotOptArg):
		"""ViewTitle"""
		return self._ApplyTypes_(907, 1, (12, 0), ((12, 0),), u'ViewTitle', None,vaView
			)

	def VisibleObjects(self, vaView=defaultNamedOptArg, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg, vaIncludeGrips=defaultNamedOptArg):
		"""VisibleObjects"""
		return self._ApplyTypes_(825, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), u'VisibleObjects', None,vaView
			, vaSelect, vaIncludeLights, vaIncludeGrips)

	def Wallpaper(self, vaView=defaultNamedOptArg, vaFileName=defaultNamedOptArg, vaHidden=defaultNamedOptArg, vaGrayscale=defaultNamedOptArg):
		"""Wallpaper"""
		return self._ApplyTypes_(532, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), u'Wallpaper', None,vaView
			, vaFileName, vaHidden, vaGrayscale)

	def WallpaperGrayScale(self, vaView=defaultNamedOptArg, vaGrayscale=defaultNamedOptArg):
		"""WallpaperGrayScale"""
		return self._ApplyTypes_(534, 1, (12, 0), ((12, 16), (12, 16)), u'WallpaperGrayScale', None,vaView
			, vaGrayscale)

	def WallpaperHidden(self, vaView=defaultNamedOptArg, vaHidden=defaultNamedOptArg):
		"""WallpaperHidden"""
		return self._ApplyTypes_(533, 1, (12, 0), ((12, 16), (12, 16)), u'WallpaperHidden', None,vaView
			, vaHidden)

	def WindowHandle(self):
		"""WindowHandle"""
		return self._ApplyTypes_(29, 1, (12, 0), (), u'WindowHandle', None,)

	def WorkingFolder(self, vaFolder=defaultNamedOptArg):
		"""WorkingFolder"""
		return self._ApplyTypes_(439, 1, (12, 0), ((12, 16),), u'WorkingFolder', None,vaFolder
			)

	def WorldXYPlane(self):
		"""WorldXYPlane"""
		return self._ApplyTypes_(652, 1, (12, 0), (), u'WorldXYPlane', None,)

	def WorldYZPlane(self):
		"""WorldYZPlane"""
		return self._ApplyTypes_(653, 1, (12, 0), (), u'WorldYZPlane', None,)

	def WorldZXPlane(self):
		"""WorldZXPlane"""
		return self._ApplyTypes_(654, 1, (12, 0), (), u'WorldZXPlane', None,)

	def XformCPlaneToWorld(self, vaPoint=defaultNamedNotOptArg, vaPlane=defaultNamedNotOptArg):
		"""XformCPlaneToWorld"""
		return self._ApplyTypes_(131, 1, (12, 0), ((12, 0), (12, 0)), u'XformCPlaneToWorld', None,vaPoint
			, vaPlane)

	def XformChangeBasis(self, va0=defaultNamedNotOptArg, va1=defaultNamedOptArg, va2=defaultNamedOptArg, va3=defaultNamedOptArg
			, va4=defaultNamedOptArg, va5=defaultNamedOptArg):
		"""XformChangeBasis"""
		return self._ApplyTypes_(796, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'XformChangeBasis', None,va0
			, va1, va2, va3, va4, va5
			)

	def XformCompare(self, vaXform0=defaultNamedNotOptArg, vaXform1=defaultNamedNotOptArg):
		"""XformCompare"""
		return self._ApplyTypes_(789, 1, (12, 0), ((12, 0), (12, 0)), u'XformCompare', None,vaXform0
			, vaXform1)

	def XformDeterminant(self, vaXform=defaultNamedNotOptArg):
		"""XformDeterminant"""
		return self._ApplyTypes_(818, 1, (12, 0), ((12, 0),), u'XformDeterminant', None,vaXform
			)

	def XformDiagonal(self, vaValue=defaultNamedNotOptArg):
		"""XformDiagonal"""
		return self._ApplyTypes_(784, 1, (12, 0), ((12, 0),), u'XformDiagonal', None,vaValue
			)

	def XformIdentity(self):
		"""XformIdentity"""
		return self._ApplyTypes_(783, 1, (12, 0), (), u'XformIdentity', None,)

	def XformInverse(self, vaXform=defaultNamedNotOptArg):
		"""XformInverse"""
		return self._ApplyTypes_(817, 1, (12, 0), ((12, 0),), u'XformInverse', None,vaXform
			)

	def XformMirror(self, vaPoint=defaultNamedNotOptArg, vaNormal=defaultNamedNotOptArg):
		"""XformMirror"""
		return self._ApplyTypes_(795, 1, (12, 0), ((12, 0), (12, 0)), u'XformMirror', None,vaPoint
			, vaNormal)

	def XformMultiply(self, vaXform0=defaultNamedNotOptArg, vaXform1=defaultNamedNotOptArg):
		"""XformMultiply"""
		return self._ApplyTypes_(788, 1, (12, 0), ((12, 0), (12, 0)), u'XformMultiply', None,vaXform0
			, vaXform1)

	def XformPlanarProjection(self, vaPlane=defaultNamedNotOptArg):
		"""XformPlanarProjection"""
		return self._ApplyTypes_(793, 1, (12, 0), ((12, 0),), u'XformPlanarProjection', None,vaPlane
			)

	def XformRotation(self, va0=defaultNamedNotOptArg, va1=defaultNamedOptArg, va2=defaultNamedOptArg, va3=defaultNamedOptArg
			, va4=defaultNamedOptArg, va5=defaultNamedOptArg):
		"""XformRotation"""
		return self._ApplyTypes_(794, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), u'XformRotation', None,va0
			, va1, va2, va3, va4, va5
			)

	def XformScale(self, va0=defaultNamedNotOptArg, va1=defaultNamedOptArg, va2=defaultNamedOptArg, va3=defaultNamedOptArg):
		"""XformScale"""
		return self._ApplyTypes_(790, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), u'XformScale', None,va0
			, va1, va2, va3)

	def XformScreenToWorld(self, vaPoint=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaScreenToClient=defaultNamedOptArg):
		"""XformScreenToWorld"""
		return self._ApplyTypes_(581, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'XformScreenToWorld', None,vaPoint
			, vaView, vaScreenToClient)

	def XformShear(self, va0=defaultNamedNotOptArg, va1=defaultNamedOptArg, va2=defaultNamedOptArg, va3=defaultNamedOptArg):
		"""XformShear"""
		return self._ApplyTypes_(791, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), u'XformShear', None,va0
			, va1, va2, va3)

	def XformTranslation(self, vaVector=defaultNamedNotOptArg):
		"""XformTranslation"""
		return self._ApplyTypes_(792, 1, (12, 0), ((12, 0),), u'XformTranslation', None,vaVector
			)

	def XformWorldToCPlane(self, vaPoint=defaultNamedNotOptArg, vaPlane=defaultNamedNotOptArg):
		"""XformWorldToCPlane"""
		return self._ApplyTypes_(132, 1, (12, 0), ((12, 0), (12, 0)), u'XformWorldToCPlane', None,vaPoint
			, vaPlane)

	def XformWorldToScreen(self, vaPoint=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaClientToScreen=defaultNamedOptArg):
		"""XformWorldToScreen"""
		return self._ApplyTypes_(582, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'XformWorldToScreen', None,vaPoint
			, vaView, vaClientToScreen)

	def XformZero(self):
		"""XformZero"""
		return self._ApplyTypes_(782, 1, (12, 0), (), u'XformZero', None,)

	def ZoomBoundingBox(self, vaCorners=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaAll=defaultNamedOptArg):
		"""ZoomBoundingBox"""
		return self._ApplyTypes_(479, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), u'ZoomBoundingBox', None,vaCorners
			, vaView, vaAll)

	def ZoomExtents(self, vaView=defaultNamedOptArg, vaAll=defaultNamedOptArg):
		"""ZoomExtents"""
		return self._ApplyTypes_(375, 1, (12, 0), ((12, 16), (12, 16)), u'ZoomExtents', None,vaView
			, vaAll)

	def ZoomSelected(self, vaView=defaultNamedOptArg, vaAll=defaultNamedOptArg):
		"""ZoomSelected"""
		return self._ApplyTypes_(376, 1, (12, 0), ((12, 16), (12, 16)), u'ZoomSelected', None,vaView
			, vaAll)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

from win32com.client import CoClassBaseClass
class RhinoScript(CoClassBaseClass): # A CoClass
	CLSID = IID('{48B5D8DC-EDB1-45A9-981B-6C96169A0E7D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRhinoScript,
	]
	default_interface = IRhinoScript

RecordMap = {
}

CLSIDToClassMap = {
	'{48B5D8DC-EDB1-45A9-981B-6C96169A0E7D}' : RhinoScript,
	'{DC7E0867-5922-4DCB-935F-585F81484030}' : IRhinoScript,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
}


NamesToIIDMap = {
	'IRhinoScript' : '{DC7E0867-5922-4DCB-935F-585F81484030}',
}


