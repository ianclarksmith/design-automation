# -*- coding: mbcs -*-
# Created by makepy.py version 0.4.95
# By python version 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)]
# From type library 'RhinoScript.tlb'
# On Wed Jan 09 10:00:02 2008
"""RhinoScript 4.0 Type Library"""
makepy_version = '0.4.95'
python_version = 0x20501f0

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

#code has been manually editied by Patrick Janssen and Jorg Kramer
from pw32 import RhinoUtils
class IRhinoScript(DispatchBaseClass):
	CLSID = IID('{DC7E0867-5922-4DCB-935F-585F81484030}')
	coclass_clsid = IID('{48B5D8DC-EDB1-45A9-981B-6C96169A0E7D}')

	def AddAlias(self, vaName=defaultNamedNotOptArg, vaMacro=defaultNamedNotOptArg):
		"""AddAlias"""
		return self._ApplyTypes_(709, 1, (12, 0), ((12, 0), (12, 0)), 'AddAlias', None,vaName
			, vaMacro)

	def AddArc(self, vaPlane=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg):
		"""AddArc"""
		return self._ApplyTypes_(651, 1, (12, 0), ((8197, 0), (12, 0), (12, 0)), 'AddArc', None,RhinoUtils.FlattenOnce(vaPlane)
			, vaRadius, vaAngle)

	def AddArc3Pt(self, vaPt1=defaultNamedNotOptArg, vaPt2=defaultNamedNotOptArg, vaPt3=defaultNamedNotOptArg):
		"""AddArc3Pt"""
		return self._ApplyTypes_(82, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'AddArc3Pt', None,vaPt1
			, vaPt2, vaPt3)

	def AddBox(self, vaCorners=defaultNamedNotOptArg):
		"""AddBox"""
		return self._ApplyTypes_(72, 1, (12, 0), ((8197, 0),), 'AddBox', None, RhinoUtils.FlattenOnce(vaCorners)
			)

	def AddCircle(self, vaPlane=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg):
		"""AddCircle"""
		return self._ApplyTypes_(83, 1, (12, 0), ((8197, 0), (12, 0)), 'AddCircle', None,RhinoUtils.FlattenOnce(vaPlane)
			, vaRadius)

	def AddCircle3Pt(self, vaPt1=defaultNamedNotOptArg, vaPt2=defaultNamedNotOptArg, vaPt3=defaultNamedNotOptArg):
		"""AddCircle3Pt"""
		return self._ApplyTypes_(84, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'AddCircle3Pt', None,vaPt1
			, vaPt2, vaPt3)

	def AddCone(self, vaCenter=defaultNamedNotOptArg, vaHeight=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg):
		"""AddCone"""
		return self._ApplyTypes_(75, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'AddCone', None,vaCenter
			, vaHeight, vaRadius)

	def AddCurve(self, vaPoints=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg):
		"""AddCurve"""
		return self._ApplyTypes_(77, 1, (12, 0), ((8197, 0), (12, 16)), 'AddCurve', None, RhinoUtils.FlattenOnce(vaPoints)
			, vaDegree)

	def AddCylinder(self, vaCenter=defaultNamedNotOptArg, vaHeight=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg):
		"""AddCylinder"""
		return self._ApplyTypes_(73, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'AddCylinder', None,vaCenter
			, vaHeight, vaRadius)

	def AddDimStyle(self, vaStyle=defaultNamedOptArg):
		"""AddDimStyle"""
		return self._ApplyTypes_(455, 1, (12, 0), ((12, 16),), 'AddDimStyle', None,vaStyle
			)

	def AddDirectionalLight(self, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg):
		"""AddDirectionalLight"""
		return self._ApplyTypes_(153, 1, (12, 0), ((12, 0), (12, 0)), 'AddDirectionalLight', None,vaStart
			, vaEnd)

	def AddEdgeSrf(self, vaObjects=defaultNamedNotOptArg):
		"""AddEdgeSrf"""
		return self._ApplyTypes_(203, 1, (12, 0), ((12, 0),), 'AddEdgeSrf', None,vaObjects
			)

	def AddEllipse(self, vaPlane=defaultNamedNotOptArg, vaDX=defaultNamedNotOptArg, vaDY=defaultNamedNotOptArg):
		"""AddEllipse"""
		return self._ApplyTypes_(679, 1, (12, 0), ((8197, 0), (12, 0), (12, 0)), 'AddEllipse', None,RhinoUtils.FlattenOnce(vaPlane)
			, vaDX, vaDY)

	def AddEllipse3Pt(self, vaCenter=defaultNamedNotOptArg, vaSecond=defaultNamedNotOptArg, vaThird=defaultNamedNotOptArg):
		"""AddEllipse3Pt"""
		return self._ApplyTypes_(680, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'AddEllipse3Pt', None,vaCenter
			, vaSecond, vaThird)

	def AddFilletCurve(self, vaCrv0=defaultNamedNotOptArg, vaCrv1=defaultNamedNotOptArg, vaRadius=defaultNamedOptArg, vaPt0=defaultNamedOptArg
			, vaPt1=defaultNamedOptArg):
		"""AddFilletCurve"""
		return self._ApplyTypes_(574, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16)), 'AddFilletCurve', None,vaCrv0
			, vaCrv1, vaRadius, vaPt0, vaPt1)

	def AddGroup(self, vaName=defaultNamedOptArg):
		"""AddGroup"""
		return self._ApplyTypes_(133, 1, (12, 0), ((12, 16),), 'AddGroup', None,vaName
			)

	def AddInterpCrvOnSrf(self, vaObject=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg):
		"""AddInterpCrvOnSrf"""
		return self._ApplyTypes_(513, 1, (12, 0), ((12, 0), (8197, 0)), 'AddInterpCrvOnSrf', None,vaObject
			, RhinoUtils.FlattenOnce(vaPoints))

	def AddInterpCrvOnSrfUV(self, vaObject=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg):
		"""AddInterpCrvOnSrfUV"""
		return self._ApplyTypes_(641, 1, (12, 0), ((12, 0), (8197, 0)), 'AddInterpCrvOnSrfUV', None,vaObject
			, RhinoUtils.FlattenOnce(vaPoints))

	def AddInterpCurve(self, vaPoints=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg, vaKnot=defaultNamedOptArg, vaCV1=defaultNamedOptArg
			, vaCVn1=defaultNamedOptArg):
		"""AddInterpCurve"""
		return self._ApplyTypes_(268, 1, (12, 0), ((8197, 0), (12, 16), (12, 16), (12, 16), (12, 16)), 'AddInterpCurve', None,RhinoUtils.FlattenOnce(vaPoints)
			, vaDegree, vaKnot, vaCV1, vaCVn1)

	def AddInterpCurveEx(self, vaPoints=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg, vaKnotSpacing=defaultNamedOptArg, vaSharp=defaultNamedOptArg
			, vaStartTangent=defaultNamedOptArg, vaEndTangent=defaultNamedOptArg):
		"""AddInterpCurveEx"""
		return self._ApplyTypes_(520, 1, (12, 0), ((8197, 0), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'AddInterpCurveEx', None,RhinoUtils.FlattenOnce(vaPoints)
			, vaDegree, vaKnotSpacing, vaSharp, vaStartTangent, vaEndTangent
			)

	def AddLayer(self, vaName=defaultNamedOptArg, vaColor=defaultNamedOptArg, vaVisible=defaultNamedOptArg, vaLocked=defaultNamedOptArg
			, vaParent=defaultNamedOptArg):
		"""AddLayer"""
		return self._ApplyTypes_(3, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'AddLayer', None,vaName
			, vaColor, vaVisible, vaLocked, vaParent)

	def AddLeader(self, vaPoints=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""AddLeader"""
		return self._ApplyTypes_(321, 1, (12, 0), ((8197, 0), (12, 16)), 'AddLeader', None,RhinoUtils.FlattenOnce(vaPoints)
			, vaView)

	def AddLine(self, vaPoint1=defaultNamedNotOptArg, vaPoint2=defaultNamedNotOptArg):
		"""AddLine"""
		return self._ApplyTypes_(70, 1, (12, 0), ((12, 0), (12, 0)), 'AddLine', None,vaPoint1
			, vaPoint2)

	def AddLinearLight(self, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaWidth=defaultNamedOptArg):
		"""AddLinearLight"""
		return self._ApplyTypes_(154, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'AddLinearLight', None,vaStart
			, vaEnd, vaWidth)

	def AddLoftSrf(self, vaObjects=defaultNamedNotOptArg, vaStartPt=defaultNamedOptArg, vaEndPt=defaultNamedOptArg, vaType=defaultNamedOptArg
			, vaSimplify=defaultNamedOptArg, vaVal=defaultNamedOptArg, vaClosed=defaultNamedOptArg):
		"""AddLoftSrf"""
		return self._ApplyTypes_(567, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'AddLoftSrf', None,vaObjects
			, vaStartPt, vaEndPt, vaType, vaSimplify, vaVal
			, vaClosed)

	def AddMaterialToLayer(self, vaLayer=defaultNamedNotOptArg):
		"""AddMaterialToLayer"""
		return self._ApplyTypes_(173, 1, (12, 0), ((12, 0),), 'AddMaterialToLayer', None,vaLayer
			)

	def AddMaterialToObject(self, vaObject=defaultNamedNotOptArg):
		"""AddMaterialToObject"""
		return self._ApplyTypes_(174, 1, (12, 0), ((12, 0),), 'AddMaterialToObject', None,vaObject
			)

	def AddMesh(self, vaVertices=defaultNamedNotOptArg, vaFaces=defaultNamedNotOptArg, vaNormals=defaultNamedOptArg, vaTextures=defaultNamedOptArg
			, vaColors=defaultNamedOptArg):
		"""AddMesh"""
		return self._ApplyTypes_(494, 1, (12, 0), ((8197, 0), (8197, 0), (8197, 16), (8197, 16), (12, 16)), 'AddMesh', None,RhinoUtils.FlattenOnce(vaVertices)
			, RhinoUtils.FlattenOnce(vaFaces), RhinoUtils.FlattenOnce(vaNormals), RhinoUtils.FlattenOnce(vaTextures), vaColors)

	def AddNamedCPlane(self, vaName=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""AddNamedCPlane"""
		return self._ApplyTypes_(280, 1, (12, 0), ((12, 0), (12, 16)), 'AddNamedCPlane', None,vaName
			, vaView)

	def AddNamedView(self, vaName=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""AddNamedView"""
		return self._ApplyTypes_(281, 1, (12, 0), ((12, 0), (12, 16)), 'AddNamedView', None,vaName
			, vaView)

	def AddNurbsCurve(self, vaPoints=defaultNamedNotOptArg, vaKnots=defaultNamedNotOptArg, vaDegree=defaultNamedNotOptArg, vaWeights=defaultNamedOptArg):
		"""AddNurbsCurve"""
		return self._ApplyTypes_(309, 1, (12, 0), ((8197, 0), (12, 0), (12, 0), (12, 16)), 'AddNurbsCurve', None,RhinoUtils.FlattenOnce(vaPoints)
			, vaKnots, vaDegree, vaWeights)

	##There is a problem with this one - not sure how to fix it...#!!!
	def AddNurbsSurface(self, vaPointCount=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg, vaKnotsU=defaultNamedNotOptArg, vaKnotsV=defaultNamedNotOptArg
			, vaDegree=defaultNamedNotOptArg, vaWeights=defaultNamedOptArg):
		"""AddNurbsSurface"""
		return self._ApplyTypes_(435, 1, (12, 0), ((12, 0), (8197, 0), (12, 0), (12, 0), (12, 0), (12, 16)), 'AddNurbsSurface', None,vaPointCount
			, vaPoints, vaKnotsU, vaKnotsV, vaDegree, vaWeights
			)

	def AddObjectToGroup(self, vaObject=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""AddObjectToGroup"""
		return self._ApplyTypes_(134, 1, (12, 0), ((12, 0), (12, 0)), 'AddObjectToGroup', None,vaObject
			, vaName)

	def AddObjectsToGroup(self, vaObjects=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""AddObjectsToGroup"""
		return self._ApplyTypes_(135, 1, (12, 0), ((12, 0), (12, 0)), 'AddObjectsToGroup', None,vaObjects
			, vaName)

	def AddPlanarSrf(self, vaObjects=defaultNamedNotOptArg):
		"""AddPlanarSrf"""
		return self._ApplyTypes_(371, 1, (12, 0), ((12, 0),), 'AddPlanarSrf', None,vaObjects
			)

	def AddPlaneSurface(self, vaPlane=defaultNamedNotOptArg, vaDX=defaultNamedNotOptArg, vaDY=defaultNamedNotOptArg):
		"""AddPlaneSurface"""
		return self._ApplyTypes_(648, 1, (12, 0), ((8197, 0), (12, 0), (12, 0)), 'AddPlaneSurface', None,RhinoUtils.FlattenOnce(vaPlane)
			, vaDX, vaDY)

	def AddPoint(self, vaPoint=defaultNamedNotOptArg):
		"""AddPoint"""
		return self._ApplyTypes_(68, 1, (12, 0), ((12, 0),), 'AddPoint', None,vaPoint
			)

	def AddPointCloud(self, vaCloud=defaultNamedNotOptArg):
		"""AddPointCloud"""
		return self._ApplyTypes_(69, 1, (12, 0), ((8197, 0),), 'AddPointCloud', None,RhinoUtils.FlattenOnce(vaCloud)
			)

	def AddPointLight(self, vaPoint=defaultNamedNotOptArg):
		"""AddPointLight"""
		return self._ApplyTypes_(155, 1, (12, 0), ((12, 0),), 'AddPointLight', None,vaPoint
			)

	def AddPoints(self, vaCloud=defaultNamedNotOptArg):
		"""AddPoints"""
		return self._ApplyTypes_(526, 1, (12, 0), ((8197, 0),), 'AddPoints', None,RhinoUtils.FlattenOnce(vaCloud)
			)

	def AddPolyline(self, vaPoints=defaultNamedNotOptArg):
		"""AddPolyline"""
		return self._ApplyTypes_(85, 1, (12, 0), ((8197, 0),), 'AddPolyline', None,RhinoUtils.FlattenOnce(vaPoints)
			)

	def AddRailRevSrf(self, vaProfile=defaultNamedNotOptArg, vaRail=defaultNamedNotOptArg, vaAxis=defaultNamedNotOptArg):
		"""AddRailRevSrf"""
		return self._ApplyTypes_(536, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'AddRailRevSrf', None,vaProfile
			, vaRail, vaAxis)

	def AddRectangularLight(self, vaOrigin=defaultNamedNotOptArg, vaX=defaultNamedNotOptArg, vaY=defaultNamedNotOptArg):
		"""AddRectangularLight"""
		return self._ApplyTypes_(156, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'AddRectangularLight', None,vaOrigin
			, vaX, vaY)

	def AddRevSrf(self, vaObject=defaultNamedNotOptArg, vaAxis=defaultNamedNotOptArg, vaSA=defaultNamedOptArg, vaEA=defaultNamedOptArg):
		"""AddRevSrf"""
		return self._ApplyTypes_(535, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), 'AddRevSrf', None,vaObject
			, vaAxis, vaSA, vaEA)

	def AddSearchPath(self, vaFolder=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""AddSearchPath"""
		return self._ApplyTypes_(511, 1, (12, 0), ((12, 0), (12, 16)), 'AddSearchPath', None,vaFolder
			, vaIndex)

	def AddSphere(self, vaCenter=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg):
		"""AddSphere"""
		return self._ApplyTypes_(71, 1, (12, 0), ((12, 0), (12, 0)), 'AddSphere', None,vaCenter
			, vaRadius)

	def AddSpotLight(self, vaBase=defaultNamedNotOptArg, vaRadius=defaultNamedNotOptArg, vaApex=defaultNamedNotOptArg):
		"""AddSpotLight"""
		return self._ApplyTypes_(157, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'AddSpotLight', None,vaBase
			, vaRadius, vaApex)

	def AddSrfControlPtGrid(self, vaCount=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg):
		"""AddSrfControlPtGrid"""
		return self._ApplyTypes_(294, 1, (12, 0), ((12, 0), (8197, 0), (12, 16)), 'AddSrfControlPtGrid', None,vaCount
			, RhinoUtils.FlattenOnce(vaPoints), vaDegree)

	def AddSrfPt(self, vaPoints=defaultNamedNotOptArg):
		"""AddSrfPt"""
		return self._ApplyTypes_(204, 1, (12, 0), ((8197, 0),), 'AddSrfPt', None,RhinoUtils.FlattenOnce(vaPoints)
			)

	def AddSrfPtGrid(self, vaCount=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaDegree=defaultNamedOptArg, vaClosed=defaultNamedOptArg):
		"""AddSrfPtGrid"""
		return self._ApplyTypes_(293, 1, (12, 0), ((12, 0), (8197, 0), (12, 16), (12, 16)), 'AddSrfPtGrid', None,vaCount
			, RhinoUtils.FlattenOnce(vaPoint), vaDegree, vaClosed)

	def AddStartupScript(self, vaScript=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""AddStartupScript"""
		return self._ApplyTypes_(714, 1, (12, 0), ((12, 0), (12, 16)), 'AddStartupScript', None,vaScript
			, vaIndex)

	def AddSubCrv(self, vaObject=defaultNamedNotOptArg, vaParam0=defaultNamedNotOptArg, vaParam1=defaultNamedNotOptArg):
		"""AddSubCrv"""
		return self._ApplyTypes_(681, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'AddSubCrv', None,vaObject
			, vaParam0, vaParam1)

	def AddText(self, vaText=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaHeight=defaultNamedOptArg, vaFont=defaultNamedOptArg
			, vaStyle=defaultNamedOptArg):
		"""AddText"""
		return self._ApplyTypes_(76, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16)), 'AddText', None,vaText
			, vaPoint, vaHeight, vaFont, vaStyle)

	def AddTextDot(self, vaText=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""AddTextDot"""
		return self._ApplyTypes_(320, 1, (12, 0), ((12, 0), (12, 0)), 'AddTextDot', None,vaText
			, vaPoint)

	def AddToolBar(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""AddToolBar"""
		return self._ApplyTypes_(219, 1, (12, 0), ((12, 0), (12, 0)), 'AddToolBar', None,vaAlias
			, vaName)

	def AddToolBarButton(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""AddToolBarButton"""
		return self._ApplyTypes_(220, 1, (12, 0), ((12, 0), (12, 0)), 'AddToolBarButton', None,vaAlias
			, vaName)

	def AddToolBarCollection(self, vaFile=defaultNamedNotOptArg):
		"""AddToolBarCollection"""
		return self._ApplyTypes_(221, 1, (12, 0), ((12, 0),), 'AddToolBarCollection', None,vaFile
			)

	def AddTorus(self, vaCenter=defaultNamedNotOptArg, vaRadius1=defaultNamedNotOptArg, vaRadius2=defaultNamedNotOptArg, vaDirection=defaultNamedOptArg):
		"""AddTorus"""
		return self._ApplyTypes_(74, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), 'AddTorus', None,vaCenter
			, vaRadius1, vaRadius2, vaDirection)

	def AliasCount(self):
		"""AliasCount"""
		return self._ApplyTypes_(706, 1, (12, 0), (), 'AliasCount', None,)

	def AliasMacro(self, vaName=defaultNamedNotOptArg, vaMacro=defaultNamedOptArg):
		"""AliasMacro"""
		return self._ApplyTypes_(708, 1, (12, 0), ((12, 0), (12, 16)), 'AliasMacro', None,vaName
			, vaMacro)

	def AliasNames(self):
		"""AliasNames"""
		return self._ApplyTypes_(707, 1, (12, 0), (), 'AliasNames', None,)

	def AllObjects(self, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""AllObjects"""
		return self._ApplyTypes_(30, 1, (12, 0), ((12, 16), (12, 16)), 'AllObjects', None,vaSelect
			, vaIncludeLights)

	def AllProcedures(self, vaAll=defaultNamedOptArg):
		"""AllProcedures"""
		return self._ApplyTypes_(503, 1, (12, 0), ((12, 16),), 'AllProcedures', None,vaAll
			)

	def Angle(self, vaFrom=defaultNamedNotOptArg, vaTo=defaultNamedNotOptArg, vaWorld=defaultNamedOptArg):
		"""Angle"""
		return self._ApplyTypes_(115, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'Angle', None,vaFrom
			, vaTo, vaWorld)

	def Angle2(self, vaFirst=defaultNamedNotOptArg, vaSecond=defaultNamedNotOptArg):
		"""Angle2"""
		return self._ApplyTypes_(116, 1, (12, 0), ((12, 0), (12, 0)), 'Angle2', None,vaFirst
			, vaSecond)

	def AppearanceColor(self, vaItem=defaultNamedNotOptArg, vaColor=defaultNamedOptArg):
		"""AppearanceColor"""
		return self._ApplyTypes_(335, 1, (12, 0), ((12, 0), (12, 16)), 'AppearanceColor', None,vaItem
			, vaColor)

	def ArcAngle(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""ArcAngle"""
		return self._ApplyTypes_(86, 1, (12, 0), ((12, 0), (12, 16)), 'ArcAngle', None,vaObject
			, vaIndex)

	def ArcCenterPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""ArcCenterPoint"""
		return self._ApplyTypes_(87, 1, (12, 0), ((12, 0), (12, 16)), 'ArcCenterPoint', None,vaObject
			, vaIndex)

	def ArcMidPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""ArcMidPoint"""
		return self._ApplyTypes_(88, 1, (12, 0), ((12, 0), (12, 16)), 'ArcMidPoint', None,vaObject
			, vaIndex)

	def ArcRadius(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""ArcRadius"""
		return self._ApplyTypes_(89, 1, (12, 0), ((12, 0), (12, 16)), 'ArcRadius', None,vaObject
			, vaIndex)

	def AttributeDataCount(self, vaObject=defaultNamedNotOptArg):
		"""AttributeDataCount"""
		return self._ApplyTypes_(685, 1, (12, 0), ((12, 0),), 'AttributeDataCount', None,vaObject
			)

	def AutosaveFile(self, vaFile=defaultNamedOptArg):
		"""AutosaveFile"""
		return self._ApplyTypes_(428, 1, (12, 0), ((12, 16),), 'AutosaveFile', None,vaFile
			)

	def AutosaveInterval(self, vaMinutes=defaultNamedOptArg):
		"""AutosaveInterval"""
		return self._ApplyTypes_(429, 1, (12, 0), ((12, 16),), 'AutosaveInterval', None,vaMinutes
			)

	def BlockContainerCount(self, vaName=defaultNamedNotOptArg):
		"""BlockContainerCount"""
		return self._ApplyTypes_(411, 1, (12, 0), ((12, 0),), 'BlockContainerCount', None,vaName
			)

	def BlockContainers(self, vaName=defaultNamedNotOptArg):
		"""BlockContainers"""
		return self._ApplyTypes_(412, 1, (12, 0), ((12, 0),), 'BlockContainers', None,vaName
			)

	def BlockCount(self):
		"""BlockCount"""
		return self._ApplyTypes_(397, 1, (12, 0), (), 'BlockCount', None,)

	def BlockDescription(self, vaName=defaultNamedNotOptArg, vaDesc=defaultNamedOptArg):
		"""BlockDescription"""
		return self._ApplyTypes_(400, 1, (12, 0), ((12, 0), (12, 16)), 'BlockDescription', None,vaName
			, vaDesc)

	def BlockInstanceCount(self, vaName=defaultNamedNotOptArg):
		"""BlockInstanceCount"""
		return self._ApplyTypes_(404, 1, (12, 0), ((12, 0),), 'BlockInstanceCount', None,vaName
			)

	def BlockInstanceInsertPoint(self, vaObject=defaultNamedNotOptArg):
		"""BlockInstanceInsertPoint"""
		return self._ApplyTypes_(413, 1, (12, 0), ((12, 0),), 'BlockInstanceInsertPoint', None,vaObject
			)

	def BlockInstanceName(self, vaObject=defaultNamedNotOptArg):
		"""BlockInstanceName"""
		return self._ApplyTypes_(571, 1, (12, 0), ((12, 0),), 'BlockInstanceName', None,vaObject
			)

	def BlockInstanceXform(self, vaObject=defaultNamedNotOptArg):
		"""BlockInstanceXform"""
		return self._ApplyTypes_(415, 1, (12, 0), ((12, 0),), 'BlockInstanceXform', None,vaObject
			)

	def BlockInstances(self, vaName=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg):
		"""BlockInstances"""
		return self._ApplyTypes_(414, 1, (12, 0), ((12, 0), (12, 16)), 'BlockInstances', None,vaName
			, vaSelect)

	def BlockNames(self, vaSort=defaultNamedOptArg):
		"""BlockNames"""
		return self._ApplyTypes_(396, 1, (12, 0), ((12, 16),), 'BlockNames', None,vaSort
			)

	def BlockObjectCount(self, vaName=defaultNamedNotOptArg):
		"""BlockObjectCount"""
		return self._ApplyTypes_(416, 1, (12, 0), ((12, 0),), 'BlockObjectCount', None,vaName
			)

	def BlockObjects(self, vaName=defaultNamedNotOptArg):
		"""BlockObjects"""
		return self._ApplyTypes_(417, 1, (12, 0), ((12, 0),), 'BlockObjects', None,vaName
			)

	def BlockPath(self, vaName=defaultNamedNotOptArg):
		"""BlockPath"""
		return self._ApplyTypes_(408, 1, (12, 0), ((12, 0),), 'BlockPath', None,vaName
			)

	def BlockURL(self, vaName=defaultNamedNotOptArg, vaNew=defaultNamedOptArg):
		"""BlockURL"""
		return self._ApplyTypes_(402, 1, (12, 0), ((12, 0), (12, 16)), 'BlockURL', None,vaName
			, vaNew)

	def BlockURLTag(self, vaName=defaultNamedNotOptArg, vaNew=defaultNamedOptArg):
		"""BlockURLTag"""
		return self._ApplyTypes_(403, 1, (12, 0), ((12, 0), (12, 16)), 'BlockURLTag', None,vaName
			, vaNew)

	def BooleanDifference(self, vaInBreps0=defaultNamedNotOptArg, vaInBreps1=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""BooleanDifference"""
		return self._ApplyTypes_(508, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'BooleanDifference', None, vaInBreps0
			, vaInBreps1, vaDelete)

	def BooleanIntersection(self, vaInBreps0=defaultNamedNotOptArg, vaInBreps1=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""BooleanIntersection"""
		return self._ApplyTypes_(507, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'BooleanIntersection', None, RhinoUtils.FlattenOnce(vaInBreps0)
			, RhinoUtils.FlattenOnce(vaInBreps1), vaDelete)

	def BooleanUnion(self, vaObjects=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""BooleanUnion"""
		return self._ApplyTypes_(506, 1, (12, 0), ((12, 0), (12, 16)), 'BooleanUnion', None, vaObjects
			, vaDelete)

	def BoundingBox(self, vaObjects=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaSystem=defaultNamedOptArg):
		"""BoundingBox"""
		return self._ApplyTypes_(117, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'BoundingBox', None,vaObjects
			, vaView, vaSystem)

	def BrepClosestPoint(self, vaBrep=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""BrepClosestPoint"""
		return self._ApplyTypes_(514, 1, (12, 0), ((12, 0), (12, 0)), 'BrepClosestPoint', None,vaBrep
			, vaPoint)

	def BrowseForFolder(self, vaPath=defaultNamedOptArg, vaMessage=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""BrowseForFolder"""
		return self._ApplyTypes_(146, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'BrowseForFolder', None,vaPath
			, vaMessage, vaTitle)

	def BuildDate(self):
		"""BuildDate"""
		return self._ApplyTypes_(360, 1, (12, 0), (), 'BuildDate', None,)

	def CapPlanarHoles(self, vaObject=defaultNamedNotOptArg):
		"""CapPlanarHoles"""
		return self._ApplyTypes_(701, 1, (12, 0), ((12, 0),), 'CapPlanarHoles', None,vaObject
			)

	def CheckListBox(self, vaList=defaultNamedNotOptArg, vaValues=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""CheckListBox"""
		return self._ApplyTypes_(52, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), 'CheckListBox', None,vaList
			, vaValues, vaPrompt, vaTitle)

	def CircleCenterPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CircleCenterPoint"""
		return self._ApplyTypes_(90, 1, (12, 0), ((12, 0), (12, 16)), 'CircleCenterPoint', None,vaObject
			, vaIndex)

	def CircleCircumference(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CircleCircumference"""
		return self._ApplyTypes_(91, 1, (12, 0), ((12, 0), (12, 16)), 'CircleCircumference', None,vaObject
			, vaIndex)

	def CircleRadius(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CircleRadius"""
		return self._ApplyTypes_(92, 1, (12, 0), ((12, 0), (12, 16)), 'CircleRadius', None,vaObject
			, vaIndex)

	def ClearCommandHistory(self):
		"""ClearCommandHistory"""
		return self._ApplyTypes_(592, 1, (12, 0), (), 'ClearCommandHistory', None,)

	def ClipboardText(self, vaText=defaultNamedOptArg):
		"""ClipboardText"""
		return self._ApplyTypes_(245, 1, (12, 0), ((12, 16),), 'ClipboardText', None,vaText
			)

	def CloseCurve(self, vaObject=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""CloseCurve"""
		return self._ApplyTypes_(440, 1, (12, 0), ((12, 0), (12, 16)), 'CloseCurve', None,vaObject
			, vaTolerance)

	def CloseToolBarCollection(self, vaAlias=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg):
		"""CloseToolBarCollection"""
		return self._ApplyTypes_(222, 1, (12, 0), ((12, 0), (12, 16)), 'CloseToolBarCollection', None,vaAlias
			, vaPrompt)

	def ComboListBox(self, vaList=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""ComboListBox"""
		return self._ApplyTypes_(53, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'ComboListBox', None,vaList
			, vaPrompt, vaTitle)

	def Command(self, vaCmd=defaultNamedNotOptArg, vaMode=defaultNamedOptArg):
		"""Command"""
		return self._ApplyTypes_(1, 1, (12, 0), ((12, 0), (12, 16)), 'Command', None,vaCmd
			, vaMode)

	def CommandHistory(self):
		"""CommandHistory"""
		return self._ApplyTypes_(591, 1, (12, 0), (), 'CommandHistory', None,)

	def CompareGeometry(self, vaObj1=defaultNamedNotOptArg, vaObj2=defaultNamedNotOptArg):
		"""CompareGeometry"""
		return self._ApplyTypes_(598, 1, (12, 0), ((12, 0), (12, 0)), 'CompareGeometry', None,vaObj1
			, vaObj2)

	def ConvertCurveToPolyline(self, vaObject=defaultNamedNotOptArg, vaLineAngleTolerance=defaultNamedOptArg, vaLineTolerance=defaultNamedOptArg, vaDelete=defaultNamedOptArg):
		"""ConvertCurveToPolyline"""
		return self._ApplyTypes_(377, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), 'ConvertCurveToPolyline', None,vaObject
			, vaLineAngleTolerance, vaLineTolerance, vaDelete)

	def CopyObject(self, vaObject=defaultNamedNotOptArg, vaStart=defaultNamedOptArg, vaEnd=defaultNamedOptArg):
		"""CopyObject"""
		return self._ApplyTypes_(184, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'CopyObject', None,vaObject
			, vaStart, vaEnd)

	def CopyObjects(self, vaObjects=defaultNamedNotOptArg, vaStart=defaultNamedOptArg, vaEnd=defaultNamedOptArg):
		"""CopyObjects"""
		return self._ApplyTypes_(295, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'CopyObjects', None,vaObjects
			, vaStart, vaEnd)

	def CreatePreviewImage(self, vaFileName=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaSize=defaultNamedOptArg, vaFlags=defaultNamedOptArg):
		"""CreatePreviewImage"""
		return self._ApplyTypes_(388, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), 'CreatePreviewImage', None,vaFileName
			, vaView, vaSize, vaFlags)

	def CullDuplicateNumbers(self, vaNumbers=defaultNamedNotOptArg):
		"""CullDuplicateNumbers"""
		return self._ApplyTypes_(550, 1, (12, 0), ((12, 0),), 'CullDuplicateNumbers', None,vaNumbers
			)

	def CullDuplicatePoints(self, vaPoints=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""CullDuplicatePoints"""
		return self._ApplyTypes_(548, 1, (12, 0), ((8197, 0), (12, 16)), 'CullDuplicatePoints', None,RhinoUtils.FlattenOnce(vaPoints)
			, vaTolerance)

	def CullDuplicateStrings(self, vaStrings=defaultNamedNotOptArg, vaCaseSensitive=defaultNamedOptArg):
		"""CullDuplicateStrings"""
		return self._ApplyTypes_(549, 1, (12, 0), ((12, 0), (12, 16)), 'CullDuplicateStrings', None,vaStrings
			, vaCaseSensitive)

	def CurrentDimStyle(self, vaStyle=defaultNamedOptArg):
		"""CurrentDimStyle"""
		return self._ApplyTypes_(453, 1, (12, 0), ((12, 16),), 'CurrentDimStyle', None,vaStyle
			)

	def CurrentLayer(self, vaName=defaultNamedOptArg):
		"""CurrentLayer"""
		return self._ApplyTypes_(5, 1, (12, 0), ((12, 16),), 'CurrentLayer', None,vaName
			)

	def CurrentPrinter(self, vaPrinter=defaultNamedOptArg):
		"""CurrentPrinter"""
		return self._ApplyTypes_(358, 1, (12, 0), ((12, 16),), 'CurrentPrinter', None,vaPrinter
			)

	def CurrentView(self, vaView=defaultNamedOptArg):
		"""CurrentView"""
		return self._ApplyTypes_(251, 1, (12, 0), ((12, 16),), 'CurrentView', None,vaView
			)

	def CurveArcLengthPoint(self, vaObject=defaultNamedNotOptArg, vaLength=defaultNamedNotOptArg, vaStart=defaultNamedOptArg):
		"""CurveArcLengthPoint"""
		return self._ApplyTypes_(658, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'CurveArcLengthPoint', None,vaObject
			, vaLength, vaStart)

	def CurveArea(self, vaObject=defaultNamedNotOptArg):
		"""CurveArea"""
		return self._ApplyTypes_(643, 1, (12, 0), ((12, 0),), 'CurveArea', None,vaObject
			)

	def CurveAreaCentroid(self, vaObject=defaultNamedNotOptArg):
		"""CurveAreaCentroid"""
		return self._ApplyTypes_(677, 1, (12, 0), ((12, 0),), 'CurveAreaCentroid', None,vaObject
			)

	def CurveArrows(self, vaObject=defaultNamedNotOptArg, vaFlags=defaultNamedOptArg):
		"""CurveArrows"""
		return self._ApplyTypes_(578, 1, (12, 0), ((12, 0), (12, 16)), 'CurveArrows', None,vaObject
			, vaFlags)

	def CurveBrepIntersect(self, vaCurve=defaultNamedNotOptArg, vaBrep=defaultNamedNotOptArg, vaTol=defaultNamedOptArg):
		"""CurveBrepIntersect"""
		return self._ApplyTypes_(545, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'CurveBrepIntersect', None,vaCurve
			, vaBrep, vaTol)

	def CurveClosestPoint(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveClosestPoint"""
		return self._ApplyTypes_(93, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'CurveClosestPoint', None,vaObject
			, vaPoint, vaIndex)

	def CurveCurvature(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""CurveCurvature"""
		return self._ApplyTypes_(379, 1, (12, 0), ((12, 0), (12, 0)), 'CurveCurvature', None,vaObject
			, vaParam)

	def CurveCurveIntersection(self, vaCrvA=defaultNamedNotOptArg, vaCrvB=defaultNamedOptArg, vaTol=defaultNamedOptArg):
		"""CurveCurveIntersection"""
		return self._ApplyTypes_(423, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'CurveCurveIntersection', None,vaCrvA
			, vaCrvB, vaTol)

	def CurveDegree(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveDegree"""
		return self._ApplyTypes_(94, 1, (12, 0), ((12, 0), (12, 16)), 'CurveDegree', None,vaObject
			, vaIndex)

	def CurveDeviation(self, vaCrvA=defaultNamedNotOptArg, vaCrvB=defaultNamedNotOptArg):
		"""CurveDeviation"""
		return self._ApplyTypes_(687, 1, (12, 0), ((12, 0), (12, 0)), 'CurveDeviation', None,vaCrvA
			, vaCrvB)

	def CurveDim(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg):
		"""CurveDim"""
		return self._ApplyTypes_(381, 1, (12, 0), ((12, 0), (12, 0)), 'CurveDim', None,vaObject
			, vaIndex)

	def CurveDirectionsMatch(self, vaCrv1=defaultNamedNotOptArg, vaCrv2=defaultNamedNotOptArg):
		"""CurveDirectionsMatch"""
		return self._ApplyTypes_(543, 1, (12, 0), ((12, 0), (12, 0)), 'CurveDirectionsMatch', None,vaCrv1
			, vaCrv2)

	def CurveDiscontinuity(self, vaObject=defaultNamedNotOptArg, vaType=defaultNamedNotOptArg):
		"""CurveDiscontinuity"""
		return self._ApplyTypes_(579, 1, (12, 0), ((12, 0), (12, 0)), 'CurveDiscontinuity', None,vaObject
			, vaType)

	def CurveDomain(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveDomain"""
		return self._ApplyTypes_(95, 1, (12, 0), ((12, 0), (12, 16)), 'CurveDomain', None,vaObject
			, vaIndex)

	def CurveEditPoints(self, vaObject=defaultNamedNotOptArg, vaReturnParameters=defaultNamedOptArg, vaIndex=defaultNamedOptArg):
		"""CurveEditPoints"""
		return self._ApplyTypes_(442, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'CurveEditPoints', None,vaObject
			, vaReturnParameters, vaIndex)

	def CurveEndPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveEndPoint"""
		return self._ApplyTypes_(96, 1, (12, 0), ((12, 0), (12, 16)), 'CurveEndPoint', None,vaObject
			, vaIndex)

	def CurveEvaluate(self, vaCrv=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaDevCount=defaultNamedNotOptArg):
		"""CurveEvaluate"""
		return self._ApplyTypes_(489, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'CurveEvaluate', None,vaCrv
			, vaParam, vaDevCount)

	def CurveFilletPoints(self, vaCrv0=defaultNamedNotOptArg, vaCrv1=defaultNamedNotOptArg, vaRadius=defaultNamedOptArg, vaPt0=defaultNamedOptArg
			, vaPt1=defaultNamedOptArg):
		"""CurveFilletPoints"""
		return self._ApplyTypes_(572, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16)), 'CurveFilletPoints', None,vaCrv0
			, vaCrv1, vaRadius, vaPt0, vaPt1)

	def CurveFrame(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""CurveFrame"""
		return self._ApplyTypes_(675, 1, (12, 0), ((12, 0), (12, 0)), 'CurveFrame', None,vaObject
			, vaParam)

	def CurveKnotCount(self, vaObject=defaultNamedNotOptArg):
		"""CurveKnotCount"""
		return self._ApplyTypes_(310, 1, (12, 0), ((12, 0),), 'CurveKnotCount', None,vaObject
			)

	def CurveKnots(self, vaObject=defaultNamedNotOptArg):
		"""CurveKnots"""
		return self._ApplyTypes_(311, 1, (12, 0), ((12, 0),), 'CurveKnots', None,vaObject
			)

	def CurveLength(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg, vaDomain=defaultNamedOptArg):
		"""CurveLength"""
		return self._ApplyTypes_(97, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'CurveLength', None,vaObject
			, vaIndex, vaDomain)

	def CurveMidPoint(self, vaObject=defaultNamedNotOptArg):
		"""CurveMidPoint"""
		return self._ApplyTypes_(577, 1, (12, 0), ((12, 0),), 'CurveMidPoint', None,vaObject
			)

	def CurveNormal(self, vaObject=defaultNamedNotOptArg):
		"""CurveNormal"""
		return self._ApplyTypes_(521, 1, (12, 0), ((12, 0),), 'CurveNormal', None,vaObject
			)

	def CurvePerpFrame(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""CurvePerpFrame"""
		return self._ApplyTypes_(676, 1, (12, 0), ((12, 0), (12, 0)), 'CurvePerpFrame', None,vaObject
			, vaParam)

	def CurvePlane(self, vaName=defaultNamedNotOptArg):
		"""CurvePlane"""
		return self._ApplyTypes_(609, 1, (12, 0), ((12, 0),), 'CurvePlane', None,vaName
			)

	def CurvePointCount(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurvePointCount"""
		return self._ApplyTypes_(98, 1, (12, 0), ((12, 0), (12, 16)), 'CurvePointCount', None,vaObject
			, vaIndex)

	def CurvePoints(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurvePoints"""
		return self._ApplyTypes_(308, 1, (12, 0), ((12, 0), (12, 16)), 'CurvePoints', None,vaObject
			, vaIndex)

	def CurveRadius(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveRadius"""
		return self._ApplyTypes_(80, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'CurveRadius', None,vaObject
			, vaPoint, vaIndex)

	def CurveSeam(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""CurveSeam"""
		return self._ApplyTypes_(527, 1, (12, 0), ((12, 0), (12, 0)), 'CurveSeam', None,vaObject
			, vaParam)

	def CurveStartPoint(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveStartPoint"""
		return self._ApplyTypes_(99, 1, (12, 0), ((12, 0), (12, 16)), 'CurveStartPoint', None,vaObject
			, vaIndex)

	def CurveSurfaceIntersection(self, vaCrv=defaultNamedNotOptArg, vaSrf=defaultNamedNotOptArg, vaTol=defaultNamedOptArg, vaAngleTol=defaultNamedOptArg):
		"""CurveSurfaceIntersection"""
		return self._ApplyTypes_(424, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), 'CurveSurfaceIntersection', None,vaCrv
			, vaSrf, vaTol, vaAngleTol)

	def CurveTangent(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveTangent"""
		return self._ApplyTypes_(363, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'CurveTangent', None,vaObject
			, vaParam, vaIndex)

	def CurveWeights(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""CurveWeights"""
		return self._ApplyTypes_(314, 1, (12, 0), ((12, 0), (12, 16)), 'CurveWeights', None,vaObject
			, vaIndex)

	def DefaultRenderer(self, vaRenderer=defaultNamedOptArg):
		"""DefaultRenderer"""
		return self._ApplyTypes_(316, 1, (12, 0), ((12, 16),), 'DefaultRenderer', None,vaRenderer
			)

	def DeleteAlias(self, vaName=defaultNamedNotOptArg):
		"""DeleteAlias"""
		return self._ApplyTypes_(710, 1, (12, 0), ((12, 0),), 'DeleteAlias', None,vaName
			)

	def DeleteAttributeData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""DeleteAttributeData"""
		return self._ApplyTypes_(684, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'DeleteAttributeData', None,vaObject
			, vaApp, vaKey)

	def DeleteBlock(self, vaName=defaultNamedNotOptArg):
		"""DeleteBlock"""
		return self._ApplyTypes_(418, 1, (12, 0), ((12, 0),), 'DeleteBlock', None,vaName
			)

	def DeleteDimStyle(self, vaStyle=defaultNamedNotOptArg):
		"""DeleteDimStyle"""
		return self._ApplyTypes_(456, 1, (12, 0), ((12, 0),), 'DeleteDimStyle', None,vaStyle
			)

	def DeleteDocumentData(self, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""DeleteDocumentData"""
		return self._ApplyTypes_(237, 1, (12, 0), ((12, 16), (12, 16)), 'DeleteDocumentData', None,vaApp
			, vaKey)

	def DeleteGroup(self, vaName=defaultNamedNotOptArg):
		"""DeleteGroup"""
		return self._ApplyTypes_(136, 1, (12, 0), ((12, 0),), 'DeleteGroup', None,vaName
			)

	def DeleteLayer(self, vaName=defaultNamedNotOptArg):
		"""DeleteLayer"""
		return self._ApplyTypes_(4, 1, (12, 0), ((12, 0),), 'DeleteLayer', None,vaName
			)

	def DeleteNamedCPlane(self, vaName=defaultNamedNotOptArg):
		"""DeleteNamedCPlane"""
		return self._ApplyTypes_(284, 1, (12, 0), ((12, 0),), 'DeleteNamedCPlane', None,vaName
			)

	def DeleteNamedView(self, vaName=defaultNamedNotOptArg):
		"""DeleteNamedView"""
		return self._ApplyTypes_(285, 1, (12, 0), ((12, 0),), 'DeleteNamedView', None,vaName
			)

	def DeleteObject(self, vaObject=defaultNamedNotOptArg):
		"""DeleteObject"""
		return self._ApplyTypes_(185, 1, (12, 0), ((12, 0),), 'DeleteObject', None,vaObject
			)

	def DeleteObjectData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""DeleteObjectData"""
		return self._ApplyTypes_(238, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'DeleteObjectData', None,vaObject
			, vaApp, vaKey)

	def DeleteObjects(self, vaObjects=defaultNamedNotOptArg):
		"""DeleteObjects"""
		return self._ApplyTypes_(186, 1, (12, 0), ((12, 0),), 'DeleteObjects', None,vaObjects
			)

	def DeleteSearchPath(self, vaFolder=defaultNamedNotOptArg):
		"""DeleteSearchPath"""
		return self._ApplyTypes_(512, 1, (12, 0), ((12, 0),), 'DeleteSearchPath', None,vaFolder
			)

	def DeleteStartupScript(self, vaScript=defaultNamedNotOptArg):
		"""DeleteStartupScript"""
		return self._ApplyTypes_(715, 1, (12, 0), ((12, 0),), 'DeleteStartupScript', None,vaScript
			)

	def DeleteToolBar(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""DeleteToolBar"""
		return self._ApplyTypes_(223, 1, (12, 0), ((12, 0), (12, 0)), 'DeleteToolBar', None,vaAlias
			, vaName)

	def DimScale(self, vaScale=defaultNamedNotOptArg):
		"""DimScale"""
		return self._ApplyTypes_(460, 1, (12, 0), ((12, 0),), 'DimScale', None,vaScale
			)

	def DimStyleAnglePrecision(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleAnglePrecision"""
		return self._ApplyTypes_(464, 1, (12, 0), ((12, 0), (12, 16)), 'DimStyleAnglePrecision', None,vaStyle
			, vaValue)

	def DimStyleArrowSize(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleArrowSize"""
		return self._ApplyTypes_(468, 1, (12, 0), ((12, 0), (12, 16)), 'DimStyleArrowSize', None,vaStyle
			, vaValue)

	def DimStyleCount(self):
		"""DimStyleCount"""
		return self._ApplyTypes_(451, 1, (12, 0), (), 'DimStyleCount', None,)

	def DimStyleExtension(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleExtension"""
		return self._ApplyTypes_(466, 1, (12, 0), ((12, 0), (12, 16)), 'DimStyleExtension', None,vaStyle
			, vaValue)

	def DimStyleFont(self, vaStyle=defaultNamedNotOptArg, vaFont=defaultNamedOptArg):
		"""DimStyleFont"""
		return self._ApplyTypes_(462, 1, (12, 0), ((12, 0), (12, 16)), 'DimStyleFont', None,vaStyle
			, vaFont)

	def DimStyleLeaderArrowSize(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleLeaderArrowSize"""
		return self._ApplyTypes_(704, 1, (12, 0), ((12, 0), (12, 16)), 'DimStyleLeaderArrowSize', None,vaStyle
			, vaValue)

	def DimStyleLinearPrecision(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleLinearPrecision"""
		return self._ApplyTypes_(463, 1, (12, 0), ((12, 0), (12, 16)), 'DimStyleLinearPrecision', None,vaStyle
			, vaValue)

	def DimStyleNames(self, vaSort=defaultNamedOptArg):
		"""DimStyleNames"""
		return self._ApplyTypes_(452, 1, (12, 0), ((12, 16),), 'DimStyleNames', None,vaSort
			)

	def DimStyleNumberFormat(self, vaStyle=defaultNamedNotOptArg, vaFormat=defaultNamedOptArg):
		"""DimStyleNumberFormat"""
		return self._ApplyTypes_(459, 1, (12, 0), ((12, 0), (12, 16)), 'DimStyleNumberFormat', None,vaStyle
			, vaFormat)

	def DimStyleOffset(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleOffset"""
		return self._ApplyTypes_(467, 1, (12, 0), ((12, 0), (12, 16)), 'DimStyleOffset', None,vaStyle
			, vaValue)

	def DimStyleTextAlignment(self, vaStyle=defaultNamedNotOptArg, vaAlignment=defaultNamedOptArg):
		"""DimStyleTextAlignment"""
		return self._ApplyTypes_(461, 1, (12, 0), ((12, 0), (12, 16)), 'DimStyleTextAlignment', None,vaStyle
			, vaAlignment)

	def DimStyleTextHeight(self, vaStyle=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""DimStyleTextHeight"""
		return self._ApplyTypes_(465, 1, (12, 0), ((12, 0), (12, 16)), 'DimStyleTextHeight', None,vaStyle
			, vaValue)

	def DimensionStyle(self, vaObject=defaultNamedNotOptArg, vaStyle=defaultNamedOptArg):
		"""DimensionStyle"""
		return self._ApplyTypes_(703, 1, (12, 0), ((12, 0), (12, 16)), 'DimensionStyle', None,vaObject
			, vaStyle)

	def DimensionText(self, vaObject=defaultNamedNotOptArg):
		"""DimensionText"""
		return self._ApplyTypes_(469, 1, (12, 0), ((12, 0),), 'DimensionText', None,vaObject
			)

	def DimensionUserText(self, vaObject=defaultNamedNotOptArg, vaText=defaultNamedOptArg):
		"""DimensionUserText"""
		return self._ApplyTypes_(563, 1, (12, 0), ((12, 0), (12, 16)), 'DimensionUserText', None,vaObject
			, vaText)

	def DimensionValue(self, vaObject=defaultNamedNotOptArg):
		"""DimensionValue"""
		return self._ApplyTypes_(568, 1, (12, 0), ((12, 0),), 'DimensionValue', None,vaObject
			)

	def DisjointMeshCount(self, vaMesh=defaultNamedNotOptArg):
		"""DisjointMeshCount"""
		return self._ApplyTypes_(721, 1, (12, 0), ((12, 0),), 'DisjointMeshCount', None,vaMesh
			)

	def Distance(self, vaFrom=defaultNamedNotOptArg, vaTo=defaultNamedNotOptArg):
		"""Distance"""
		return self._ApplyTypes_(118, 1, (12, 0), ((12, 0), (12, 0)), 'Distance', None,vaFrom
			, vaTo)

	def DistanceToPlane(self, vaPlane=defaultNamedNotOptArg, vaPt=defaultNamedNotOptArg):
		"""DistanceToPlane"""
		return self._ApplyTypes_(628, 1, (12, 0), ((12, 0), (12, 0)), 'DistanceToPlane', None,vaPlane
			, vaPt)

	def DivideCurve(self, vaObject=defaultNamedNotOptArg, vaCount=defaultNamedNotOptArg, vaCreate=defaultNamedNotOptArg):
		"""DivideCurve"""
		return self._ApplyTypes_(78, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'DivideCurve', None,vaObject
			, vaCount, vaCreate)

	def DivideCurveLength(self, vaObject=defaultNamedNotOptArg, vaLength=defaultNamedNotOptArg, vaCreate=defaultNamedOptArg):
		"""DivideCurveLength"""
		return self._ApplyTypes_(374, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'DivideCurveLength', None,vaObject
			, vaLength, vaCreate)

	def DocumentDataCount(self):
		"""DocumentDataCount"""
		return self._ApplyTypes_(239, 1, (12, 0), (), 'DocumentDataCount', None,)

	def DocumentModified(self, vaModified=defaultNamedOptArg):
		"""DocumentModified"""
		return self._ApplyTypes_(323, 1, (12, 0), ((12, 16),), 'DocumentModified', None,vaModified
			)

	def DocumentName(self):
		"""DocumentName"""
		return self._ApplyTypes_(113, 1, (12, 0), (), 'DocumentName', None,)

	def DocumentPath(self):
		"""DocumentPath"""
		return self._ApplyTypes_(301, 1, (12, 0), (), 'DocumentPath', None,)

	def DocumentURL(self, vaURL=defaultNamedOptArg):
		"""DocumentURL"""
		return self._ApplyTypes_(275, 1, (12, 0), ((12, 16),), 'DocumentURL', None,vaURL
			)

	def DuplicateEdgeCurves(self, vaObject=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg):
		"""DuplicateEdgeCurves"""
		return self._ApplyTypes_(657, 1, (12, 0), ((12, 0), (12, 16)), 'DuplicateEdgeCurves', None,vaObject
			, vaSelect)

	def EdgeAnalysisColor(self, vaColor=defaultNamedOptArg):
		"""EdgeAnalysisColor"""
		return self._ApplyTypes_(449, 1, (12, 0), ((12, 16),), 'EdgeAnalysisColor', None,vaColor
			)

	def EdgeAnalysisMode(self, vaMode=defaultNamedOptArg):
		"""EdgeAnalysisMode"""
		return self._ApplyTypes_(448, 1, (12, 0), ((12, 16),), 'EdgeAnalysisMode', None,vaMode
			)

	def EditBox(self, vaString=defaultNamedOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""EditBox"""
		return self._ApplyTypes_(54, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'EditBox', None,vaString
			, vaPrompt, vaTitle)

	def EllipseCenterPoint(self, vaObject=defaultNamedNotOptArg):
		"""EllipseCenterPoint"""
		return self._ApplyTypes_(524, 1, (12, 0), ((12, 0),), 'EllipseCenterPoint', None,vaObject
			)

	def EllipseQuadPoints(self, vaObject=defaultNamedNotOptArg):
		"""EllipseQuadPoints"""
		return self._ApplyTypes_(525, 1, (12, 0), ((12, 0),), 'EllipseQuadPoints', None,vaObject
			)

	def EnableAutosave(self, vaEnable=defaultNamedOptArg):
		"""EnableAutosave"""
		return self._ApplyTypes_(430, 1, (12, 0), ((12, 16),), 'EnableAutosave', None,vaEnable
			)

	def EnableLight(self, vaLight=defaultNamedNotOptArg, vaBool=defaultNamedOptArg):
		"""EnableLight"""
		return self._ApplyTypes_(158, 1, (12, 0), ((12, 0), (12, 16)), 'EnableLight', None,vaLight
			, vaBool)

	def EnableObjectGrips(self, vaObject=defaultNamedNotOptArg, vaEnable=defaultNamedOptArg):
		"""EnableObjectGrips"""
		return self._ApplyTypes_(499, 1, (12, 0), ((12, 0), (12, 16)), 'EnableObjectGrips', None,vaObject
			, vaEnable)

	def EnableRedraw(self, vaRedraw=defaultNamedOptArg):
		"""EnableRedraw"""
		return self._ApplyTypes_(317, 1, (12, 0), ((12, 16),), 'EnableRedraw', None,vaRedraw
			)

	def EvaluateCurve(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""EvaluateCurve"""
		return self._ApplyTypes_(100, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'EvaluateCurve', None,vaObject
			, vaParam, vaIndex)

	def EvaluateSurface(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""EvaluateSurface"""
		return self._ApplyTypes_(205, 1, (12, 0), ((12, 0), (12, 0)), 'EvaluateSurface', None,vaObject
			, vaParam)

	def ExeFolder(self):
		"""ExeFolder"""
		return self._ApplyTypes_(21, 1, (12, 0), (), 'ExeFolder', None,)

	def Exit(self):
		"""Exit"""
		return self._ApplyTypes_(537, 1, (12, 0), (), 'Exit', None,)

	def ExpandLayer(self, vaName=defaultNamedNotOptArg, vaExpand=defaultNamedNotOptArg):
		"""ExpandLayer"""
		return self._ApplyTypes_(690, 1, (12, 0), ((12, 0), (12, 0)), 'ExpandLayer', None,vaName
			, vaExpand)

	def ExplodeBlockInstance(self, vaObject=defaultNamedNotOptArg):
		"""ExplodeBlockInstance"""
		return self._ApplyTypes_(419, 1, (12, 0), ((12, 0),), 'ExplodeBlockInstance', None,vaObject
			)

	def ExplodeCurves(self, vaObject=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""ExplodeCurves"""
		return self._ApplyTypes_(446, 1, (12, 0), ((12, 0), (12, 16)), 'ExplodeCurves', None,vaObject
			, vaDelete)

	def ExplodePolysurfaces(self, vaObjects=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""ExplodePolysurfaces"""
		return self._ApplyTypes_(447, 1, (12, 0), ((12, 0), (12, 16)), 'ExplodePolysurfaces', None,vaObjects
			, vaDelete)

	def ExtendCurve(self, vaObject=defaultNamedNotOptArg, vaType=defaultNamedNotOptArg, vaSide=defaultNamedNotOptArg, vaObjects=defaultNamedNotOptArg):
		"""ExtendCurve"""
		return self._ApplyTypes_(438, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), 'ExtendCurve', None,vaObject
			, vaType, vaSide, vaObjects)

	def ExtendCurveLength(self, vaObject=defaultNamedNotOptArg, vaType=defaultNamedNotOptArg, vaSide=defaultNamedNotOptArg, vaLength=defaultNamedNotOptArg):
		"""ExtendCurveLength"""
		return self._ApplyTypes_(436, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), 'ExtendCurveLength', None,vaObject
			, vaType, vaSide, vaLength)

	def ExtendCurvePoint(self, vaObject=defaultNamedNotOptArg, vaSize=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""ExtendCurvePoint"""
		return self._ApplyTypes_(437, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'ExtendCurvePoint', None,vaObject
			, vaSize, vaPoint)

	def ExtractIsoCurve(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg):
		"""ExtractIsoCurve"""
		return self._ApplyTypes_(488, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'ExtractIsoCurve', None,vaObject
			, vaParam, vaDir)

	def ExtractPreviewImage(self, vaFileName=defaultNamedNotOptArg, vaModelName=defaultNamedOptArg):
		"""ExtractPreviewImage"""
		return self._ApplyTypes_(389, 1, (12, 0), ((12, 0), (12, 16)), 'ExtractPreviewImage', None,vaFileName
			, vaModelName)

	def ExtrudeCurve(self, vaCurve=defaultNamedNotOptArg, vaPath=defaultNamedNotOptArg):
		"""ExtrudeCurve"""
		return self._ApplyTypes_(538, 1, (12, 0), ((12, 0), (12, 0)), 'ExtrudeCurve', None,vaCurve
			, vaPath)

	def ExtrudeCurvePoint(self, vaCurve=defaultNamedNotOptArg, vaApex=defaultNamedNotOptArg):
		"""ExtrudeCurvePoint"""
		return self._ApplyTypes_(540, 1, (12, 0), ((12, 0), (12, 0)), 'ExtrudeCurvePoint', None,vaCurve
			, vaApex)

	def ExtrudeCurveStraight(self, vaCurve=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg):
		"""ExtrudeCurveStraight"""
		return self._ApplyTypes_(539, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'ExtrudeCurveStraight', None,vaCurve
			, vaStart, vaEnd)

	def ExtrudeSurface(self, vaSurface=defaultNamedNotOptArg, vaCurve=defaultNamedNotOptArg, vaCap=defaultNamedOptArg):
		"""ExtrudeSurface"""
		return self._ApplyTypes_(541, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'ExtrudeSurface', None,vaSurface
			, vaCurve, vaCap)

	def FairCurve(self, vaObject=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""FairCurve"""
		return self._ApplyTypes_(599, 1, (12, 0), ((12, 0), (12, 16)), 'FairCurve', None,vaObject
			, vaTolerance)

	def FindFile(self, vaFile=defaultNamedNotOptArg):
		"""FindFile"""
		return self._ApplyTypes_(81, 1, (12, 0), ((12, 0),), 'FindFile', None,vaFile
			)

	def FirstObject(self, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""FirstObject"""
		return self._ApplyTypes_(31, 1, (12, 0), ((12, 16), (12, 16)), 'FirstObject', None,vaSelect
			, vaIncludeLights)

	def FlipSurface(self, vaObject=defaultNamedNotOptArg, vaReverse=defaultNamedOptArg):
		"""FlipSurface"""
		return self._ApplyTypes_(718, 1, (12, 0), ((12, 0), (12, 16)), 'FlipSurface', None,vaObject
			, vaReverse)

	def GetAngle(self, vaPoint=defaultNamedOptArg, vaRef=defaultNamedOptArg, vaDefault=defaultNamedOptArg, vaPrompt=defaultNamedOptArg):
		"""GetAngle"""
		return self._ApplyTypes_(277, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), 'GetAngle', None,vaPoint
			, vaRef, vaDefault, vaPrompt)

	def GetAttributeData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""GetAttributeData"""
		return self._ApplyTypes_(682, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'GetAttributeData', None,vaObject
			, vaApp, vaKey)

	def GetBoolean(self, vaPrompt=defaultNamedNotOptArg, vaItems=defaultNamedNotOptArg, vaDefaults=defaultNamedNotOptArg):
		"""GetBoolean"""
		return self._ApplyTypes_(622, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'GetBoolean', None,vaPrompt
			, vaItems, vaDefaults)

	def GetBox(self, vaMode=defaultNamedOptArg, vaPoint=defaultNamedOptArg, vaPrompt1=defaultNamedOptArg, vaPrompt2=defaultNamedOptArg
			, vaPrompt3=defaultNamedOptArg):
		"""GetBox"""
		return self._ApplyTypes_(342, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'GetBox', None,vaMode
			, vaPoint, vaPrompt1, vaPrompt2, vaPrompt3)

	def GetColor(self, vaColor=defaultNamedOptArg):
		"""GetColor"""
		return self._ApplyTypes_(65, 1, (12, 0), ((12, 16),), 'GetColor', None,vaColor
			)

	def GetCurveObject(self, vaPrompt=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg, vaSelect=defaultNamedOptArg):
		"""GetCurveObject"""
		return self._ApplyTypes_(575, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'GetCurveObject', None,vaPrompt
			, vaPreSelect, vaSelect)

	def GetDistance(self, vaPoint=defaultNamedOptArg, vaDefault=defaultNamedOptArg, vaPrompt1=defaultNamedOptArg, vaPrompt2=defaultNamedOptArg):
		"""GetDistance"""
		return self._ApplyTypes_(66, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), 'GetDistance', None,vaPoint
			, vaDefault, vaPrompt1, vaPrompt2)

	def GetDocumentData(self, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""GetDocumentData"""
		return self._ApplyTypes_(240, 1, (12, 0), ((12, 16), (12, 16)), 'GetDocumentData', None,vaApp
			, vaKey)

	def GetInteger(self, vaPrompt=defaultNamedOptArg, vaDefault=defaultNamedOptArg, vaMin=defaultNamedOptArg, vaMax=defaultNamedOptArg):
		"""GetInteger"""
		return self._ApplyTypes_(64, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), 'GetInteger', None,vaPrompt
			, vaDefault, vaMin, vaMax)

	def GetLayer(self, vaPrompt=defaultNamedOptArg, vaLayer=defaultNamedOptArg, vaNewButton=defaultNamedOptArg, vaCurrentButton=defaultNamedOptArg):
		"""GetLayer"""
		return self._ApplyTypes_(672, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), 'GetLayer', None,vaPrompt
			, vaLayer, vaNewButton, vaCurrentButton)

	def GetLinetype(self, vaLinetype=defaultNamedOptArg):
		"""GetLinetype"""
		return self._ApplyTypes_(673, 1, (12, 0), ((12, 16),), 'GetLinetype', None,vaLinetype
			)

	def GetObject(self, vaPrompt=defaultNamedOptArg, vaType=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg, vaSelect=defaultNamedOptArg
			, vaObjects=defaultNamedOptArg):
		"""GetObject"""
		return self._ApplyTypes_(32, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'GetObject', None,vaPrompt
			, vaType, vaPreSelect, vaSelect, vaObjects)

	def GetObjectData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""GetObjectData"""
		return self._ApplyTypes_(241, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'GetObjectData', None,vaObject
			, vaApp, vaKey)

	def GetObjectGrip(self, vaPrompt=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg, vaSelect=defaultNamedOptArg):
		"""GetObjectGrip"""
		return self._ApplyTypes_(561, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'GetObjectGrip', None,vaPrompt
			, vaPreSelect, vaSelect)

	def GetObjectGrips(self, vaPrompt=defaultNamedNotOptArg, vaPreSelect=defaultNamedNotOptArg, vaSelect=defaultNamedNotOptArg):
		"""GetObjectGrips"""
		return self._ApplyTypes_(562, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'GetObjectGrips', None,vaPrompt
			, vaPreSelect, vaSelect)

	def GetObjects(self, vaPrompt=defaultNamedOptArg, vaType=defaultNamedOptArg, vaGroup=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg
			, vaSelect=defaultNamedOptArg, vaObjects=defaultNamedOptArg):
		"""GetObjects"""
		return self._ApplyTypes_(33, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'GetObjects', None,vaPrompt
			, vaType, vaGroup, vaPreSelect, vaSelect, vaObjects
			)

	def GetPlugInObject(self, vaName=defaultNamedNotOptArg):
		"""GetPlugInObject"""
		return self._ApplyTypes_(636, 1, (12, 0), ((12, 0),), 'GetPlugInObject', None,vaName
			)

	def GetPoint(self, vaPrompt=defaultNamedOptArg, vaPoint=defaultNamedOptArg, vaDistance=defaultNamedOptArg, vaPlane=defaultNamedOptArg):
		"""GetPoint"""
		return self._ApplyTypes_(61, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), 'GetPoint', None,vaPrompt
			, vaPoint, vaDistance, vaPlane)

	def GetPointCoordinates(self, vaPrompt=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg):
		"""GetPointCoordinates"""
		return self._ApplyTypes_(645, 1, (12, 0), ((12, 16), (12, 16)), 'GetPointCoordinates', None,vaPrompt
			, vaPreSelect)

	def GetPointOnCurve(self, vaObject=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg):
		"""GetPointOnCurve"""
		return self._ApplyTypes_(147, 1, (12, 0), ((12, 0), (12, 16)), 'GetPointOnCurve', None,vaObject
			, vaPrompt)

	def GetPointOnMesh(self, vaObject=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg):
		"""GetPointOnMesh"""
		return self._ApplyTypes_(401, 1, (12, 0), ((12, 0), (12, 16)), 'GetPointOnMesh', None,vaObject
			, vaPrompt)

	def GetPointOnSurface(self, vaObject=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg):
		"""GetPointOnSurface"""
		return self._ApplyTypes_(148, 1, (12, 0), ((12, 0), (12, 16)), 'GetPointOnSurface', None,vaObject
			, vaPrompt)

	def GetPoints(self, vaDraw=defaultNamedOptArg, vaPlane=defaultNamedOptArg, vaPrompt1=defaultNamedOptArg, vaPrompt2=defaultNamedOptArg
			, vaMax=defaultNamedOptArg):
		"""GetPoints"""
		return self._ApplyTypes_(67, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'GetPoints', None,vaDraw
			, vaPlane, vaPrompt1, vaPrompt2, vaMax)

	def GetPrintWidth(self, vaPrintWidth=defaultNamedOptArg):
		"""GetPrintWidth"""
		return self._ApplyTypes_(674, 1, (12, 0), ((12, 16),), 'GetPrintWidth', None,vaPrintWidth
			)

	def GetReal(self, vaPrompt=defaultNamedOptArg, vaDefault=defaultNamedOptArg, vaMin=defaultNamedOptArg, vaMax=defaultNamedOptArg):
		"""GetReal"""
		return self._ApplyTypes_(63, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), 'GetReal', None,vaPrompt
			, vaDefault, vaMin, vaMax)

	def GetRectangle(self, vaMode=defaultNamedOptArg, vaPoint=defaultNamedOptArg, vaPrompt1=defaultNamedOptArg, vaPrompt2=defaultNamedOptArg
			, vaPrompt3=defaultNamedOptArg):
		"""GetRectangle"""
		return self._ApplyTypes_(341, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'GetRectangle', None,vaMode
			, vaPoint, vaPrompt1, vaPrompt2, vaPrompt3)

	def GetSettings(self, vaFile=defaultNamedNotOptArg, vaSection=defaultNamedOptArg, vaKey=defaultNamedOptArg):
		"""GetSettings"""
		return self._ApplyTypes_(246, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'GetSettings', None,vaFile
			, vaSection, vaKey)

	def GetString(self, vaPrompt=defaultNamedOptArg, vaDefault=defaultNamedOptArg, vaStrings=defaultNamedOptArg):
		"""GetString"""
		return self._ApplyTypes_(62, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'GetString', None,vaPrompt
			, vaDefault, vaStrings)

	def GetSurfaceObject(self, vaPrompt=defaultNamedOptArg, vaPreSelect=defaultNamedOptArg, vaSelect=defaultNamedOptArg):
		"""GetSurfaceObject"""
		return self._ApplyTypes_(576, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'GetSurfaceObject', None,vaPrompt
			, vaPreSelect, vaSelect)

	def GroupCount(self):
		"""GroupCount"""
		return self._ApplyTypes_(137, 1, (12, 0), (), 'GroupCount', None,)

	def GroupNames(self):
		"""GroupNames"""
		return self._ApplyTypes_(138, 1, (12, 0), (), 'GroupNames', None,)

	def Help(self, vaTopic=defaultNamedOptArg):
		"""Help"""
		return self._ApplyTypes_(22, 1, (12, 0), ((12, 16),), 'Help', None,vaTopic
			)

	def HiddenObjects(self, vaIncludeLights=defaultNamedOptArg):
		"""HiddenObjects"""
		return self._ApplyTypes_(366, 1, (12, 0), ((12, 16),), 'HiddenObjects', None,vaIncludeLights
			)

	def HideObject(self, vaObject=defaultNamedNotOptArg):
		"""HideObject"""
		return self._ApplyTypes_(187, 1, (12, 0), ((12, 0),), 'HideObject', None,vaObject
			)

	def HideObjects(self, vaObjects=defaultNamedNotOptArg):
		"""HideObjects"""
		return self._ApplyTypes_(303, 1, (12, 0), ((12, 0),), 'HideObjects', None,vaObjects
			)

	def HideToolBar(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""HideToolBar"""
		return self._ApplyTypes_(224, 1, (12, 0), ((12, 0), (12, 0)), 'HideToolBar', None,vaAlias
			, vaName)

	def HtmlBox(self, vaFile=defaultNamedNotOptArg, vaArgs=defaultNamedOptArg, vaOptions=defaultNamedOptArg):
		"""HtmlBox"""
		return self._ApplyTypes_(276, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'HtmlBox', None,vaFile
			, vaArgs, vaOptions)

	def InCommand(self, vaScript=defaultNamedOptArg):
		"""InCommand"""
		return self._ApplyTypes_(596, 1, (12, 0), ((12, 16),), 'InCommand', None,vaScript
			)

	def InsertBlock(self, vaName=defaultNamedNotOptArg, vaPt=defaultNamedNotOptArg, vaScale=defaultNamedOptArg, vaAngle=defaultNamedOptArg
			, vaRotate=defaultNamedOptArg):
		"""InsertBlock"""
		return self._ApplyTypes_(633, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16), (12, 16)), 'InsertBlock', None,vaName
			, vaPt, vaScale, vaAngle, vaRotate)

	def InsertCurveKnot(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaSym=defaultNamedOptArg):
		"""InsertCurveKnot"""
		return self._ApplyTypes_(515, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'InsertCurveKnot', None,vaObject
			, vaParam, vaSym)

	def InsertSurfaceKnot(self, vaSrf=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg, vaSym=defaultNamedOptArg):
		"""InsertSurfaceKnot"""
		return self._ApplyTypes_(516, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), 'InsertSurfaceKnot', None,vaSrf
			, vaParam, vaDir, vaSym)

	def InstallFolder(self):
		"""InstallFolder"""
		return self._ApplyTypes_(23, 1, (12, 0), (), 'InstallFolder', None,)

	def IntegerBox(self, vaPrompt=defaultNamedOptArg, vaInteger=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""IntegerBox"""
		return self._ApplyTypes_(55, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'IntegerBox', None,vaPrompt
			, vaInteger, vaTitle)

	def IntersectBreps(self, vaBrep0=defaultNamedNotOptArg, vaBrep1=defaultNamedNotOptArg, vaTol=defaultNamedOptArg):
		"""IntersectBreps"""
		return self._ApplyTypes_(544, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'IntersectBreps', None,vaBrep0
			, vaBrep1, vaTol)

	def InvertSelectedObjects(self, vaIncludeLights=defaultNamedOptArg):
		"""InvertSelectedObjects"""
		return self._ApplyTypes_(34, 1, (12, 0), ((12, 16),), 'InvertSelectedObjects', None,vaIncludeLights
			)

	def IsAlias(self, vaName=defaultNamedNotOptArg):
		"""IsAlias"""
		return self._ApplyTypes_(711, 1, (12, 0), ((12, 0),), 'IsAlias', None,vaName
			)

	def IsAlignedDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsAlignedDimension"""
		return self._ApplyTypes_(566, 1, (12, 0), ((12, 0),), 'IsAlignedDimension', None,vaObject
			)

	def IsAngularDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsAngularDimension"""
		return self._ApplyTypes_(338, 1, (12, 0), ((12, 0),), 'IsAngularDimension', None,vaObject
			)

	def IsArc(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsArc"""
		return self._ApplyTypes_(101, 1, (12, 0), ((12, 0), (12, 16)), 'IsArc', None,vaObject
			, vaIndex)

	def IsAttributeData(self, vaObject=defaultNamedNotOptArg):
		"""IsAttributeData"""
		return self._ApplyTypes_(686, 1, (12, 0), ((12, 0),), 'IsAttributeData', None,vaObject
			)

	def IsBlock(self, vaName=defaultNamedNotOptArg):
		"""IsBlock"""
		return self._ApplyTypes_(398, 1, (12, 0), ((12, 0),), 'IsBlock', None,vaName
			)

	def IsBlockEmbedded(self, vaName=defaultNamedNotOptArg):
		"""IsBlockEmbedded"""
		return self._ApplyTypes_(405, 1, (12, 0), ((12, 0),), 'IsBlockEmbedded', None,vaName
			)

	def IsBlockInUse(self, vaName=defaultNamedNotOptArg, vaWhere=defaultNamedOptArg):
		"""IsBlockInUse"""
		return self._ApplyTypes_(406, 1, (12, 0), ((12, 0), (12, 16)), 'IsBlockInUse', None,vaName
			, vaWhere)

	def IsBlockInstance(self, vaObject=defaultNamedNotOptArg):
		"""IsBlockInstance"""
		return self._ApplyTypes_(420, 1, (12, 0), ((12, 0),), 'IsBlockInstance', None,vaObject
			)

	def IsBlockReference(self, vaName=defaultNamedNotOptArg):
		"""IsBlockReference"""
		return self._ApplyTypes_(407, 1, (12, 0), ((12, 0),), 'IsBlockReference', None,vaName
			)

	def IsBrep(self, vaObject=defaultNamedNotOptArg):
		"""IsBrep"""
		return self._ApplyTypes_(206, 1, (12, 0), ((12, 0),), 'IsBrep', None,vaObject
			)

	def IsCircle(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCircle"""
		return self._ApplyTypes_(102, 1, (12, 0), ((12, 0), (12, 16)), 'IsCircle', None,vaObject
			, vaIndex)

	def IsCommand(self, vaName=defaultNamedNotOptArg):
		"""IsCommand"""
		return self._ApplyTypes_(530, 1, (12, 0), ((12, 0),), 'IsCommand', None,vaName
			)

	def IsCurve(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCurve"""
		return self._ApplyTypes_(103, 1, (12, 0), ((12, 0), (12, 16)), 'IsCurve', None,vaObject
			, vaIndex)

	def IsCurveClosable(self, vaObject=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""IsCurveClosable"""
		return self._ApplyTypes_(441, 1, (12, 0), ((12, 0), (12, 16)), 'IsCurveClosable', None,vaObject
			, vaTolerance)

	def IsCurveClosed(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCurveClosed"""
		return self._ApplyTypes_(104, 1, (12, 0), ((12, 0), (12, 16)), 'IsCurveClosed', None,vaObject
			, vaIndex)

	def IsCurveInPlane(self, vaObject=defaultNamedNotOptArg, vaPlane=defaultNamedOptArg):
		"""IsCurveInPlane"""
		return self._ApplyTypes_(483, 1, (12, 0), ((12, 0), (12, 16)), 'IsCurveInPlane', None,vaObject
			, vaPlane)

	def IsCurveLinear(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCurveLinear"""
		return self._ApplyTypes_(105, 1, (12, 0), ((12, 0), (12, 16)), 'IsCurveLinear', None,vaObject
			, vaIndex)

	def IsCurvePeriodic(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCurvePeriodic"""
		return self._ApplyTypes_(106, 1, (12, 0), ((12, 0), (12, 16)), 'IsCurvePeriodic', None,vaObject
			, vaIndex)

	def IsCurvePlanar(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsCurvePlanar"""
		return self._ApplyTypes_(107, 1, (12, 0), ((12, 0), (12, 16)), 'IsCurvePlanar', None,vaObject
			, vaIndex)

	def IsCurveRational(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg):
		"""IsCurveRational"""
		return self._ApplyTypes_(380, 1, (12, 0), ((12, 0), (12, 0)), 'IsCurveRational', None,vaObject
			, vaIndex)

	def IsDiameterDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsDiameterDimension"""
		return self._ApplyTypes_(565, 1, (12, 0), ((12, 0),), 'IsDiameterDimension', None,vaObject
			)

	def IsDimStyle(self, vaStyle=defaultNamedNotOptArg):
		"""IsDimStyle"""
		return self._ApplyTypes_(454, 1, (12, 0), ((12, 0),), 'IsDimStyle', None,vaStyle
			)

	def IsDimStyleReference(self, vaStyle=defaultNamedNotOptArg):
		"""IsDimStyleReference"""
		return self._ApplyTypes_(457, 1, (12, 0), ((12, 0),), 'IsDimStyleReference', None,vaStyle
			)

	def IsDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsDimension"""
		return self._ApplyTypes_(564, 1, (12, 0), ((12, 0),), 'IsDimension', None,vaObject
			)

	def IsDirectionalLight(self, vaLight=defaultNamedNotOptArg):
		"""IsDirectionalLight"""
		return self._ApplyTypes_(159, 1, (12, 0), ((12, 0),), 'IsDirectionalLight', None,vaLight
			)

	def IsDocumentData(self):
		"""IsDocumentData"""
		return self._ApplyTypes_(278, 1, (12, 0), (), 'IsDocumentData', None,)

	def IsDocumentModified(self):
		"""IsDocumentModified"""
		return self._ApplyTypes_(273, 1, (12, 0), (), 'IsDocumentModified', None,)

	def IsEllipse(self, vaObject=defaultNamedNotOptArg):
		"""IsEllipse"""
		return self._ApplyTypes_(523, 1, (12, 0), ((12, 0),), 'IsEllipse', None,vaObject
			)

	def IsGroup(self, vaName=defaultNamedNotOptArg):
		"""IsGroup"""
		return self._ApplyTypes_(139, 1, (12, 0), ((12, 0),), 'IsGroup', None,vaName
			)

	def IsGroupEmpty(self, vaName=defaultNamedNotOptArg):
		"""IsGroupEmpty"""
		return self._ApplyTypes_(140, 1, (12, 0), ((12, 0),), 'IsGroupEmpty', None,vaName
			)

	def IsLayer(self, vaName=defaultNamedNotOptArg):
		"""IsLayer"""
		return self._ApplyTypes_(6, 1, (12, 0), ((12, 0),), 'IsLayer', None,vaName
			)

	def IsLayerChangeable(self, vaName=defaultNamedNotOptArg):
		"""IsLayerChangeable"""
		return self._ApplyTypes_(18, 1, (12, 0), ((12, 0),), 'IsLayerChangeable', None,vaName
			)

	def IsLayerChildOf(self, vaName=defaultNamedNotOptArg, vaParent=defaultNamedNotOptArg):
		"""IsLayerChildOf"""
		return self._ApplyTypes_(692, 1, (12, 0), ((12, 0), (12, 0)), 'IsLayerChildOf', None,vaName
			, vaParent)

	def IsLayerCurrent(self, vaName=defaultNamedNotOptArg):
		"""IsLayerCurrent"""
		return self._ApplyTypes_(313, 1, (12, 0), ((12, 0),), 'IsLayerCurrent', None,vaName
			)

	def IsLayerEmpty(self, vaName=defaultNamedNotOptArg):
		"""IsLayerEmpty"""
		return self._ApplyTypes_(7, 1, (12, 0), ((12, 0),), 'IsLayerEmpty', None,vaName
			)

	def IsLayerExpanded(self, vaName=defaultNamedNotOptArg):
		"""IsLayerExpanded"""
		return self._ApplyTypes_(689, 1, (12, 0), ((12, 0),), 'IsLayerExpanded', None,vaName
			)

	def IsLayerLocked(self, vaName=defaultNamedNotOptArg):
		"""IsLayerLocked"""
		return self._ApplyTypes_(8, 1, (12, 0), ((12, 0),), 'IsLayerLocked', None,vaName
			)

	def IsLayerOn(self, vaName=defaultNamedNotOptArg):
		"""IsLayerOn"""
		return self._ApplyTypes_(9, 1, (12, 0), ((12, 0),), 'IsLayerOn', None,vaName
			)

	def IsLayerParentOf(self, vaName=defaultNamedNotOptArg, vaParent=defaultNamedNotOptArg):
		"""IsLayerParentOf"""
		return self._ApplyTypes_(693, 1, (12, 0), ((12, 0), (12, 0)), 'IsLayerParentOf', None,vaName
			, vaParent)

	def IsLayerReference(self, vaName=defaultNamedNotOptArg):
		"""IsLayerReference"""
		return self._ApplyTypes_(10, 1, (12, 0), ((12, 0),), 'IsLayerReference', None,vaName
			)

	def IsLayerSelectable(self, vaName=defaultNamedNotOptArg):
		"""IsLayerSelectable"""
		return self._ApplyTypes_(19, 1, (12, 0), ((12, 0),), 'IsLayerSelectable', None,vaName
			)

	def IsLayerVisible(self, vaName=defaultNamedNotOptArg):
		"""IsLayerVisible"""
		return self._ApplyTypes_(20, 1, (12, 0), ((12, 0),), 'IsLayerVisible', None,vaName
			)

	def IsLeader(self, vaObject=defaultNamedNotOptArg):
		"""IsLeader"""
		return self._ApplyTypes_(337, 1, (12, 0), ((12, 0),), 'IsLeader', None,vaObject
			)

	def IsLight(self, vaLight=defaultNamedNotOptArg):
		"""IsLight"""
		return self._ApplyTypes_(160, 1, (12, 0), ((12, 0),), 'IsLight', None,vaLight
			)

	def IsLightEnabled(self, vaLight=defaultNamedNotOptArg):
		"""IsLightEnabled"""
		return self._ApplyTypes_(161, 1, (12, 0), ((12, 0),), 'IsLightEnabled', None,vaLight
			)

	def IsLightReference(self, vaLight=defaultNamedNotOptArg):
		"""IsLightReference"""
		return self._ApplyTypes_(162, 1, (12, 0), ((12, 0),), 'IsLightReference', None,vaLight
			)

	def IsLine(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsLine"""
		return self._ApplyTypes_(108, 1, (12, 0), ((12, 0), (12, 16)), 'IsLine', None,vaObject
			, vaIndex)

	def IsLinearDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsLinearDimension"""
		return self._ApplyTypes_(339, 1, (12, 0), ((12, 0),), 'IsLinearDimension', None,vaObject
			)

	def IsLinearLight(self, vaLight=defaultNamedNotOptArg):
		"""IsLinearLight"""
		return self._ApplyTypes_(163, 1, (12, 0), ((12, 0),), 'IsLinearLight', None,vaLight
			)

	def IsLinetype(self, vaName=defaultNamedNotOptArg):
		"""IsLinetype"""
		return self._ApplyTypes_(607, 1, (12, 0), ((12, 0),), 'IsLinetype', None,vaName
			)

	def IsLinetypeReference(self, vaName=defaultNamedNotOptArg):
		"""IsLinetypeReference"""
		return self._ApplyTypes_(608, 1, (12, 0), ((12, 0),), 'IsLinetypeReference', None,vaName
			)

	def IsMaterialDefault(self, vaIndex=defaultNamedNotOptArg):
		"""IsMaterialDefault"""
		return self._ApplyTypes_(175, 1, (12, 0), ((12, 0),), 'IsMaterialDefault', None,vaIndex
			)

	def IsMaterialReference(self, vaIndex=defaultNamedNotOptArg):
		"""IsMaterialReference"""
		return self._ApplyTypes_(176, 1, (12, 0), ((12, 0),), 'IsMaterialReference', None,vaIndex
			)

	def IsMesh(self, vaObject=defaultNamedNotOptArg):
		"""IsMesh"""
		return self._ApplyTypes_(119, 1, (12, 0), ((12, 0),), 'IsMesh', None,vaObject
			)

	def IsMeshClosed(self, vaObject=defaultNamedNotOptArg):
		"""IsMeshClosed"""
		return self._ApplyTypes_(355, 1, (12, 0), ((12, 0),), 'IsMeshClosed', None,vaObject
			)

	def IsNurbsCurve(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsNurbsCurve"""
		return self._ApplyTypes_(109, 1, (12, 0), ((12, 0), (12, 16)), 'IsNurbsCurve', None,vaObject
			, vaIndex)

	def IsObject(self, vaObject=defaultNamedNotOptArg):
		"""IsObject"""
		return self._ApplyTypes_(46, 1, (12, 0), ((12, 0),), 'IsObject', None,vaObject
			)

	def IsObjectData(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectData"""
		return self._ApplyTypes_(279, 1, (12, 0), ((12, 0),), 'IsObjectData', None,vaObject
			)

	def IsObjectHidden(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectHidden"""
		return self._ApplyTypes_(47, 1, (12, 0), ((12, 0),), 'IsObjectHidden', None,vaObject
			)

	def IsObjectInGroup(self, vaObject=defaultNamedNotOptArg, vaGroup=defaultNamedNotOptArg):
		"""IsObjectInGroup"""
		return self._ApplyTypes_(188, 1, (12, 0), ((12, 0), (12, 0)), 'IsObjectInGroup', None,vaObject
			, vaGroup)

	def IsObjectLocked(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectLocked"""
		return self._ApplyTypes_(48, 1, (12, 0), ((12, 0),), 'IsObjectLocked', None,vaObject
			)

	def IsObjectNormal(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectNormal"""
		return self._ApplyTypes_(49, 1, (12, 0), ((12, 0),), 'IsObjectNormal', None,vaObject
			)

	def IsObjectReference(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectReference"""
		return self._ApplyTypes_(271, 1, (12, 0), ((12, 0),), 'IsObjectReference', None,vaObject
			)

	def IsObjectSelectable(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectSelectable"""
		return self._ApplyTypes_(307, 1, (12, 0), ((12, 0),), 'IsObjectSelectable', None,vaObject
			)

	def IsObjectSelected(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectSelected"""
		return self._ApplyTypes_(50, 1, (12, 0), ((12, 0),), 'IsObjectSelected', None,vaObject
			)

	def IsObjectSolid(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectSolid"""
		return self._ApplyTypes_(189, 1, (12, 0), ((12, 0),), 'IsObjectSolid', None,vaObject
			)

	def IsObjectValid(self, vaObject=defaultNamedNotOptArg):
		"""IsObjectValid"""
		return self._ApplyTypes_(522, 1, (12, 0), ((12, 0),), 'IsObjectValid', None,vaObject
			)

	def IsOrdinateDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsOrdinateDimension"""
		return self._ApplyTypes_(659, 1, (12, 0), ((12, 0),), 'IsOrdinateDimension', None,vaObject
			)

	def IsPlaneSurface(self, vaObject=defaultNamedNotOptArg):
		"""IsPlaneSurface"""
		return self._ApplyTypes_(638, 1, (12, 0), ((12, 0),), 'IsPlaneSurface', None,vaObject
			)

	def IsPoint(self, vaObject=defaultNamedNotOptArg):
		"""IsPoint"""
		return self._ApplyTypes_(120, 1, (12, 0), ((12, 0),), 'IsPoint', None,vaObject
			)

	def IsPointCloud(self, vaObject=defaultNamedNotOptArg):
		"""IsPointCloud"""
		return self._ApplyTypes_(121, 1, (12, 0), ((12, 0),), 'IsPointCloud', None,vaObject
			)

	def IsPointInSurface(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""IsPointInSurface"""
		return self._ApplyTypes_(443, 1, (12, 0), ((12, 0), (12, 0)), 'IsPointInSurface', None,vaObject
			, vaPoint)

	def IsPointLight(self, vaLight=defaultNamedNotOptArg):
		"""IsPointLight"""
		return self._ApplyTypes_(164, 1, (12, 0), ((12, 0),), 'IsPointLight', None,vaLight
			)

	def IsPointOnCurve(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsPointOnCurve"""
		return self._ApplyTypes_(318, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'IsPointOnCurve', None,vaObject
			, vaPoint, vaIndex)

	def IsPointOnSurface(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""IsPointOnSurface"""
		return self._ApplyTypes_(319, 1, (12, 0), ((12, 0), (12, 0)), 'IsPointOnSurface', None,vaObject
			, vaPoint)

	def IsPolyCurve(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsPolyCurve"""
		return self._ApplyTypes_(368, 1, (12, 0), ((12, 0), (12, 16)), 'IsPolyCurve', None,vaObject
			, vaIndex)

	def IsPolySurface(self, vaObject=defaultNamedNotOptArg):
		"""IsPolySurface"""
		return self._ApplyTypes_(207, 1, (12, 0), ((12, 0),), 'IsPolySurface', None,vaObject
			)

	def IsPolySurfaceClosed(self, vaObject=defaultNamedNotOptArg):
		"""IsPolySurfaceClosed"""
		return self._ApplyTypes_(208, 1, (12, 0), ((12, 0),), 'IsPolySurfaceClosed', None,vaObject
			)

	def IsPolySurfacePlanar(self, vaObject=defaultNamedNotOptArg):
		"""IsPolySurfacePlanar"""
		return self._ApplyTypes_(209, 1, (12, 0), ((12, 0),), 'IsPolySurfacePlanar', None,vaObject
			)

	def IsPolyline(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""IsPolyline"""
		return self._ApplyTypes_(110, 1, (12, 0), ((12, 0), (12, 16)), 'IsPolyline', None,vaObject
			, vaIndex)

	def IsProcedure(self, vaName=defaultNamedNotOptArg):
		"""IsProcedure"""
		return self._ApplyTypes_(287, 1, (12, 0), ((12, 0),), 'IsProcedure', None,vaName
			)

	def IsRadialDimension(self, vaObject=defaultNamedNotOptArg):
		"""IsRadialDimension"""
		return self._ApplyTypes_(340, 1, (12, 0), ((12, 0),), 'IsRadialDimension', None,vaObject
			)

	def IsRectangularLight(self, vaLight=defaultNamedNotOptArg):
		"""IsRectangularLight"""
		return self._ApplyTypes_(165, 1, (12, 0), ((12, 0),), 'IsRectangularLight', None,vaLight
			)

	def IsSpotLight(self, vaLight=defaultNamedNotOptArg):
		"""IsSpotLight"""
		return self._ApplyTypes_(166, 1, (12, 0), ((12, 0),), 'IsSpotLight', None,vaLight
			)

	def IsSurface(self, vaObject=defaultNamedNotOptArg):
		"""IsSurface"""
		return self._ApplyTypes_(210, 1, (12, 0), ((12, 0),), 'IsSurface', None,vaObject
			)

	def IsSurfaceClosed(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""IsSurfaceClosed"""
		return self._ApplyTypes_(211, 1, (12, 0), ((12, 0), (12, 0)), 'IsSurfaceClosed', None,vaObject
			, vaValue)

	def IsSurfacePeriodic(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""IsSurfacePeriodic"""
		return self._ApplyTypes_(212, 1, (12, 0), ((12, 0), (12, 0)), 'IsSurfacePeriodic', None,vaObject
			, vaValue)

	def IsSurfacePlanar(self, vaObject=defaultNamedNotOptArg, vaTol=defaultNamedOptArg):
		"""IsSurfacePlanar"""
		return self._ApplyTypes_(213, 1, (12, 0), ((12, 0), (12, 16)), 'IsSurfacePlanar', None,vaObject
			, vaTol)

	def IsSurfaceRational(self, vaObject=defaultNamedNotOptArg):
		"""IsSurfaceRational"""
		return self._ApplyTypes_(434, 1, (12, 0), ((12, 0),), 'IsSurfaceRational', None,vaObject
			)

	def IsSurfaceSingular(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""IsSurfaceSingular"""
		return self._ApplyTypes_(214, 1, (12, 0), ((12, 0), (12, 0)), 'IsSurfaceSingular', None,vaObject
			, vaValue)

	def IsSurfaceTrimmed(self, vaObject=defaultNamedNotOptArg):
		"""IsSurfaceTrimmed"""
		return self._ApplyTypes_(269, 1, (12, 0), ((12, 0),), 'IsSurfaceTrimmed', None,vaObject
			)

	def IsText(self, vaObject=defaultNamedNotOptArg):
		"""IsText"""
		return self._ApplyTypes_(122, 1, (12, 0), ((12, 0),), 'IsText', None,vaObject
			)

	def IsTextDot(self, vaObject=defaultNamedNotOptArg):
		"""IsTextDot"""
		return self._ApplyTypes_(336, 1, (12, 0), ((12, 0),), 'IsTextDot', None,vaObject
			)

	def IsToolBar(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""IsToolBar"""
		return self._ApplyTypes_(225, 1, (12, 0), ((12, 0), (12, 0)), 'IsToolBar', None,vaAlias
			, vaName)

	def IsToolBarCollection(self, vaFile=defaultNamedNotOptArg):
		"""IsToolBarCollection"""
		return self._ApplyTypes_(226, 1, (12, 0), ((12, 0),), 'IsToolBarCollection', None,vaFile
			)

	def IsToolBarVisible(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""IsToolBarVisible"""
		return self._ApplyTypes_(227, 1, (12, 0), ((12, 0), (12, 0)), 'IsToolBarVisible', None,vaAlias
			, vaName)

	def IsToolbarDocked(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""IsToolbarDocked"""
		return self._ApplyTypes_(724, 1, (12, 0), ((12, 0), (12, 0)), 'IsToolbarDocked', None,vaAlias
			, vaName)

	def IsVectorParallelTo(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""IsVectorParallelTo"""
		return self._ApplyTypes_(660, 1, (12, 0), ((12, 0), (12, 0)), 'IsVectorParallelTo', None,vaVec0
			, vaVec1)

	def IsVectorPerpendicularTo(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""IsVectorPerpendicularTo"""
		return self._ApplyTypes_(661, 1, (12, 0), ((12, 0), (12, 0)), 'IsVectorPerpendicularTo', None,vaVec0
			, vaVec1)

	def IsVectorTiny(self, vaVec=defaultNamedNotOptArg):
		"""IsVectorTiny"""
		return self._ApplyTypes_(610, 1, (12, 0), ((12, 0),), 'IsVectorTiny', None,vaVec
			)

	def IsVectorZero(self, vaVec=defaultNamedNotOptArg):
		"""IsVectorZero"""
		return self._ApplyTypes_(611, 1, (12, 0), ((12, 0),), 'IsVectorZero', None,vaVec
			)

	def IsView(self, vaView=defaultNamedNotOptArg):
		"""IsView"""
		return self._ApplyTypes_(252, 1, (12, 0), ((12, 0),), 'IsView', None,vaView
			)

	def IsViewCurrent(self, vaView=defaultNamedNotOptArg):
		"""IsViewCurrent"""
		return self._ApplyTypes_(253, 1, (12, 0), ((12, 0),), 'IsViewCurrent', None,vaView
			)

	def IsViewMaximized(self, vaView=defaultNamedOptArg):
		"""IsViewMaximized"""
		return self._ApplyTypes_(254, 1, (12, 0), ((12, 16),), 'IsViewMaximized', None,vaView
			)

	def IsViewPerspective(self, vaView=defaultNamedOptArg):
		"""IsViewPerspective"""
		return self._ApplyTypes_(255, 1, (12, 0), ((12, 16),), 'IsViewPerspective', None,vaView
			)

	def IsViewTitleVisible(self, vaView=defaultNamedOptArg):
		"""IsViewTitleVisible"""
		return self._ApplyTypes_(256, 1, (12, 0), ((12, 16),), 'IsViewTitleVisible', None,vaView
			)

	def IsVisibleInView(self, vaObject=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""IsVisibleInView"""
		return self._ApplyTypes_(727, 1, (12, 0), ((12, 0), (12, 16)), 'IsVisibleInView', None,vaObject
			, vaView)

	def IsWallpaper(self, vaView=defaultNamedOptArg):
		"""IsWallpaper"""
		return self._ApplyTypes_(531, 1, (12, 0), ((12, 16),), 'IsWallpaper', None,vaView
			)

	def JoinArrays(self, vaFirst=defaultNamedNotOptArg, vaSecond=defaultNamedNotOptArg):
		"""JoinArrays"""
		return self._ApplyTypes_(547, 1, (12, 0), ((12, 0), (12, 0)), 'JoinArrays', None,vaFirst
			, vaSecond)

	def JoinCurves(self, vaObjects=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""JoinCurves"""
		return self._ApplyTypes_(111, 1, (12, 0), ((12, 0), (12, 16)), 'JoinCurves', None,vaObjects
			, vaDelete)

	def JoinSurfaces(self, vaObjects=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""JoinSurfaces"""
		return self._ApplyTypes_(487, 1, (12, 0), ((12, 0), (12, 16)), 'JoinSurfaces', None,vaObjects
			, vaDelete)

	def LastCommandName(self):
		"""LastCommandName"""
		return self._ApplyTypes_(594, 1, (12, 0), (), 'LastCommandName', None,)

	def LastCommandResult(self):
		"""LastCommandResult"""
		return self._ApplyTypes_(292, 1, (12, 0), (), 'LastCommandResult', None,)

	def LastCreatedObjects(self, vaSelect=defaultNamedOptArg):
		"""LastCreatedObjects"""
		return self._ApplyTypes_(485, 1, (12, 0), ((12, 16),), 'LastCreatedObjects', None,vaSelect
			)

	def LastLoadedScriptFile(self):
		"""LastLoadedScriptFile"""
		return self._ApplyTypes_(373, 1, (12, 0), (), 'LastLoadedScriptFile', None,)

	def LastObject(self, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""LastObject"""
		return self._ApplyTypes_(35, 1, (12, 0), ((12, 16), (12, 16)), 'LastObject', None,vaSelect
			, vaIncludeLights)

	def LayerChildCount(self, vaName=defaultNamedNotOptArg):
		"""LayerChildCount"""
		return self._ApplyTypes_(694, 1, (12, 0), ((12, 0),), 'LayerChildCount', None,vaName
			)

	def LayerChildren(self, vaName=defaultNamedNotOptArg):
		"""LayerChildren"""
		return self._ApplyTypes_(691, 1, (12, 0), ((12, 0),), 'LayerChildren', None,vaName
			)

	def LayerColor(self, vaName=defaultNamedNotOptArg, vaColor=defaultNamedOptArg):
		"""LayerColor"""
		return self._ApplyTypes_(11, 1, (12, 0), ((12, 0), (12, 16)), 'LayerColor', None,vaName
			, vaColor)

	def LayerCount(self):
		"""LayerCount"""
		return self._ApplyTypes_(12, 1, (12, 0), (), 'LayerCount', None,)

	def LayerLinetype(self, vaLayer=defaultNamedNotOptArg, vaLinetype=defaultNamedOptArg):
		"""LayerLinetype"""
		return self._ApplyTypes_(602, 1, (12, 0), ((12, 0), (12, 16)), 'LayerLinetype', None,vaLayer
			, vaLinetype)

	def LayerLocked(self, vaLayer=defaultNamedNotOptArg, vaLocked=defaultNamedOptArg):
		"""LayerLocked"""
		return self._ApplyTypes_(601, 1, (12, 0), ((12, 0), (12, 16)), 'LayerLocked', None,vaLayer
			, vaLocked)

	def LayerMaterialIndex(self, vaName=defaultNamedNotOptArg):
		"""LayerMaterialIndex"""
		return self._ApplyTypes_(13, 1, (12, 0), ((12, 0),), 'LayerMaterialIndex', None,vaName
			)

	def LayerMode(self, vaName=defaultNamedNotOptArg, vaMode=defaultNamedOptArg):
		"""LayerMode"""
		return self._ApplyTypes_(14, 1, (12, 0), ((12, 0), (12, 16)), 'LayerMode', None,vaName
			, vaMode)

	def LayerNames(self, vaSort=defaultNamedOptArg):
		"""LayerNames"""
		return self._ApplyTypes_(15, 1, (12, 0), ((12, 16),), 'LayerNames', None,vaSort
			)

	def LayerOrder(self, vaName=defaultNamedNotOptArg):
		"""LayerOrder"""
		return self._ApplyTypes_(17, 1, (12, 0), ((12, 0),), 'LayerOrder', None,vaName
			)

	def LayerPrintColor(self, vaLayer=defaultNamedNotOptArg, vaPrintColor=defaultNamedOptArg):
		"""LayerPrintColor"""
		return self._ApplyTypes_(603, 1, (12, 0), ((12, 0), (12, 16)), 'LayerPrintColor', None,vaLayer
			, vaPrintColor)

	def LayerPrintWidth(self, vaLayer=defaultNamedNotOptArg, vaPrintWidth=defaultNamedOptArg):
		"""LayerPrintWidth"""
		return self._ApplyTypes_(604, 1, (12, 0), ((12, 0), (12, 16)), 'LayerPrintWidth', None,vaLayer
			, vaPrintWidth)

	def LayerVisible(self, vaLayer=defaultNamedNotOptArg, vaVisible=defaultNamedOptArg):
		"""LayerVisible"""
		return self._ApplyTypes_(600, 1, (12, 0), ((12, 0), (12, 16)), 'LayerVisible', None,vaLayer
			, vaVisible)

	def LightColor(self, vaLight=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""LightColor"""
		return self._ApplyTypes_(167, 1, (12, 0), ((12, 0), (12, 16)), 'LightColor', None,vaLight
			, vaValue)

	def LightCount(self):
		"""LightCount"""
		return self._ApplyTypes_(168, 1, (12, 0), (), 'LightCount', None,)

	def LightDirection(self, vaLight=defaultNamedNotOptArg, vaPoint=defaultNamedOptArg):
		"""LightDirection"""
		return self._ApplyTypes_(491, 1, (12, 0), ((12, 0), (12, 16)), 'LightDirection', None,vaLight
			, vaPoint)

	def LightLocation(self, vaLight=defaultNamedNotOptArg, vaPoint=defaultNamedOptArg):
		"""LightLocation"""
		return self._ApplyTypes_(490, 1, (12, 0), ((12, 0), (12, 16)), 'LightLocation', None,vaLight
			, vaPoint)

	def LightName(self, vaLight=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""LightName"""
		return self._ApplyTypes_(169, 1, (12, 0), ((12, 0), (12, 16)), 'LightName', None,vaLight
			, vaValue)

	def LightObjects(self):
		"""LightObjects"""
		return self._ApplyTypes_(170, 1, (12, 0), (), 'LightObjects', None,)

	def LineFitFromPoints(self, vaPoints=defaultNamedNotOptArg):
		"""LineFitFromPoints"""
		return self._ApplyTypes_(726, 1, (12, 0), ((8197, 0),), 'LineFitFromPoints', None,RhinoUtils.FlattenOnce(vaPoints)
			)

	def LinetypeCount(self):
		"""LinetypeCount"""
		return self._ApplyTypes_(605, 1, (12, 0), (), 'LinetypeCount', None,)

	def LinetypeNames(self, vaSort=defaultNamedNotOptArg):
		"""LinetypeNames"""
		return self._ApplyTypes_(606, 1, (12, 0), ((12, 0),), 'LinetypeNames', None,vaSort
			)

	def ListBox(self, vaList=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""ListBox"""
		return self._ApplyTypes_(56, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'ListBox', None,vaList
			, vaPrompt, vaTitle)

	def LocaleID(self):
		"""LocaleID"""
		return self._ApplyTypes_(450, 1, (12, 0), (), 'LocaleID', None,)

	def LockObject(self, vaObject=defaultNamedNotOptArg):
		"""LockObject"""
		return self._ApplyTypes_(190, 1, (12, 0), ((12, 0),), 'LockObject', None,vaObject
			)

	def LockObjects(self, vaObjects=defaultNamedNotOptArg):
		"""LockObjects"""
		return self._ApplyTypes_(304, 1, (12, 0), ((12, 0),), 'LockObjects', None,vaObjects
			)

	def LockedObjects(self, vaIncludeLights=defaultNamedOptArg):
		"""LockedObjects"""
		return self._ApplyTypes_(365, 1, (12, 0), ((12, 16),), 'LockedObjects', None,vaIncludeLights
			)

	def MakeCurvePeriodic(self, vaObject=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""MakeCurvePeriodic"""
		return self._ApplyTypes_(444, 1, (12, 0), ((12, 0), (12, 16)), 'MakeCurvePeriodic', None,vaObject
			, vaDelete)

	def MakeSurfacePeriodic(self, vaObject=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""MakeSurfacePeriodic"""
		return self._ApplyTypes_(445, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'MakeSurfacePeriodic', None,vaObject
			, vaDir, vaDelete)

	def MatchMaterial(self, vaSrc=defaultNamedNotOptArg, vaDest=defaultNamedNotOptArg):
		"""MatchMaterial"""
		return self._ApplyTypes_(322, 1, (12, 0), ((12, 0), (12, 0)), 'MatchMaterial', None,vaSrc
			, vaDest)

	def MaterialBump(self, vaIndex=defaultNamedNotOptArg, vaBump=defaultNamedOptArg):
		"""MaterialBump"""
		return self._ApplyTypes_(177, 1, (12, 0), ((12, 0), (12, 16)), 'MaterialBump', None,vaIndex
			, vaBump)

	def MaterialColor(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialColor"""
		return self._ApplyTypes_(178, 1, (12, 0), ((12, 0), (12, 16)), 'MaterialColor', None,vaIndex
			, vaValue)

	def MaterialName(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialName"""
		return self._ApplyTypes_(179, 1, (12, 0), ((12, 0), (12, 16)), 'MaterialName', None,vaIndex
			, vaValue)

	def MaterialReflectiveColor(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialReflectiveColor"""
		return self._ApplyTypes_(180, 1, (12, 0), ((12, 0), (12, 16)), 'MaterialReflectiveColor', None,vaIndex
			, vaValue)

	def MaterialShine(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialShine"""
		return self._ApplyTypes_(181, 1, (12, 0), ((12, 0), (12, 16)), 'MaterialShine', None,vaIndex
			, vaValue)

	def MaterialTexture(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialTexture"""
		return self._ApplyTypes_(182, 1, (12, 0), ((12, 0), (12, 16)), 'MaterialTexture', None,vaIndex
			, vaValue)

	def MaterialTransparency(self, vaIndex=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""MaterialTransparency"""
		return self._ApplyTypes_(183, 1, (12, 0), ((12, 0), (12, 16)), 'MaterialTransparency', None,vaIndex
			, vaValue)

	def MaximizeRestoreView(self, vaView=defaultNamedOptArg):
		"""MaximizeRestoreView"""
		return self._ApplyTypes_(257, 1, (12, 0), ((12, 16),), 'MaximizeRestoreView', None,vaView
			)

	def MeshArea(self, vaObject=defaultNamedNotOptArg):
		"""MeshArea"""
		return self._ApplyTypes_(353, 1, (12, 0), ((12, 0),), 'MeshArea', None,vaObject
			)

	def MeshAreaCentroid(self, vaObject=defaultNamedNotOptArg):
		"""MeshAreaCentroid"""
		return self._ApplyTypes_(477, 1, (12, 0), ((12, 0),), 'MeshAreaCentroid', None,vaObject
			)

	def MeshContourPoints(self, vaObject=defaultNamedNotOptArg, vaBase=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaInterval=defaultNamedOptArg
			, vaConcident=defaultNamedOptArg):
		"""MeshContourPoints"""
		return self._ApplyTypes_(123, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16), (12, 16)), 'MeshContourPoints', None,vaObject
			, vaBase, vaEnd, vaInterval, vaConcident)

	def MeshFaceCenters(self, vaObject=defaultNamedNotOptArg):
		"""MeshFaceCenters"""
		return self._ApplyTypes_(570, 1, (12, 0), ((12, 0),), 'MeshFaceCenters', None,vaObject
			)

	def MeshFaceCount(self, vaObject=defaultNamedNotOptArg):
		"""MeshFaceCount"""
		return self._ApplyTypes_(124, 1, (12, 0), ((12, 0),), 'MeshFaceCount', None,vaObject
			)

	def MeshFaceNormals(self, vaObject=defaultNamedNotOptArg):
		"""MeshFaceNormals"""
		return self._ApplyTypes_(569, 1, (12, 0), ((12, 0),), 'MeshFaceNormals', None,vaObject
			)

	def MeshFaceVertices(self, vaObject=defaultNamedNotOptArg):
		"""MeshFaceVertices"""
		return self._ApplyTypes_(495, 1, (12, 0), ((12, 0),), 'MeshFaceVertices', None,vaObject
			)

	def MeshFaces(self, vaObject=defaultNamedNotOptArg, vaQuads=defaultNamedOptArg):
		"""MeshFaces"""
		return self._ApplyTypes_(125, 1, (12, 0), ((12, 0), (12, 16)), 'MeshFaces', None,vaObject
			, vaQuads)

	def MeshHasFaceNormals(self, vaObject=defaultNamedNotOptArg):
		"""MeshHasFaceNormals"""
		return self._ApplyTypes_(696, 1, (12, 0), ((12, 0),), 'MeshHasFaceNormals', None,vaObject
			)

	def MeshHasTextureCoordinates(self, vaObject=defaultNamedNotOptArg):
		"""MeshHasTextureCoordinates"""
		return self._ApplyTypes_(697, 1, (12, 0), ((12, 0),), 'MeshHasTextureCoordinates', None,vaObject
			)

	def MeshHasVertexColors(self, vaObject=defaultNamedNotOptArg):
		"""MeshHasVertexColors"""
		return self._ApplyTypes_(698, 1, (12, 0), ((12, 0),), 'MeshHasVertexColors', None,vaObject
			)

	def MeshHasVertexNormals(self, vaObject=defaultNamedNotOptArg):
		"""MeshHasVertexNormals"""
		return self._ApplyTypes_(695, 1, (12, 0), ((12, 0),), 'MeshHasVertexNormals', None,vaObject
			)

	def MeshNakedEdgePoints(self, vaObject=defaultNamedNotOptArg):
		"""MeshNakedEdgePoints"""
		return self._ApplyTypes_(580, 1, (12, 0), ((12, 0),), 'MeshNakedEdgePoints', None,vaObject
			)

	def MeshOffset(self, vaMesh=defaultNamedNotOptArg, vaDistance=defaultNamedNotOptArg):
		"""MeshOffset"""
		return self._ApplyTypes_(720, 1, (12, 0), ((12, 0), (12, 0)), 'MeshOffset', None,vaMesh
			, vaDistance)

	def MeshPolyline(self, vaCrv=defaultNamedNotOptArg):
		"""MeshPolyline"""
		return self._ApplyTypes_(546, 1, (12, 0), ((12, 0),), 'MeshPolyline', None,vaCrv
			)

	def MeshQuadCount(self, vaObject=defaultNamedNotOptArg):
		"""MeshQuadCount"""
		return self._ApplyTypes_(350, 1, (12, 0), ((12, 0),), 'MeshQuadCount', None,vaObject
			)

	def MeshQuadsToTriangles(self, vaObject=defaultNamedNotOptArg):
		"""MeshQuadsToTriangles"""
		return self._ApplyTypes_(352, 1, (12, 0), ((12, 0),), 'MeshQuadsToTriangles', None,vaObject
			)

	def MeshTextureCoordinates(self, vaObject=defaultNamedNotOptArg):
		"""MeshTextureCoordinates"""
		return self._ApplyTypes_(425, 1, (12, 0), ((12, 0),), 'MeshTextureCoordinates', None,vaObject
			)

	def MeshTriangleCount(self, vaObject=defaultNamedNotOptArg):
		"""MeshTriangleCount"""
		return self._ApplyTypes_(351, 1, (12, 0), ((12, 0),), 'MeshTriangleCount', None,vaObject
			)

	def MeshVertexColors(self, vaObject=defaultNamedNotOptArg, vaColors=defaultNamedOptArg):
		"""MeshVertexColors"""
		return self._ApplyTypes_(699, 1, (12, 0), ((12, 0), (12, 16)), 'MeshVertexColors', None,vaObject
			, vaColors)

	def MeshVertexCount(self, vaObject=defaultNamedNotOptArg):
		"""MeshVertexCount"""
		return self._ApplyTypes_(126, 1, (12, 0), ((12, 0),), 'MeshVertexCount', None,vaObject
			)

	def MeshVertexNormals(self, vaObject=defaultNamedNotOptArg):
		"""MeshVertexNormals"""
		return self._ApplyTypes_(426, 1, (12, 0), ((12, 0),), 'MeshVertexNormals', None,vaObject
			)

	def MeshVertices(self, vaObject=defaultNamedNotOptArg):
		"""MeshVertices"""
		return self._ApplyTypes_(127, 1, (12, 0), ((12, 0),), 'MeshVertices', None,vaObject
			)

	def MeshVolume(self, vaObject=defaultNamedNotOptArg):
		"""MeshVolume"""
		return self._ApplyTypes_(354, 1, (12, 0), ((12, 0),), 'MeshVolume', None,vaObject
			)

	def MeshVolumeCentroid(self, vaObject=defaultNamedNotOptArg):
		"""MeshVolumeCentroid"""
		return self._ApplyTypes_(478, 1, (12, 0), ((12, 0),), 'MeshVolumeCentroid', None,vaObject
			)

	def MessageBeep(self, vaType=defaultNamedOptArg):
		"""MessageBeep"""
		return self._ApplyTypes_(149, 1, (12, 0), ((12, 16),), 'MessageBeep', None,vaType
			)

	def MessageBox(self, vaText=defaultNamedNotOptArg, vaType=defaultNamedOptArg, vaCaption=defaultNamedOptArg):
		"""MessageBox"""
		return self._ApplyTypes_(150, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'MessageBox', None,vaText
			, vaType, vaCaption)

	def MirrorObject(self, vaObject=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""MirrorObject"""
		return self._ApplyTypes_(589, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), 'MirrorObject', None,vaObject
			, vaStart, vaEnd, vaCopy)

	def MirrorObjects(self, vaObjects=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""MirrorObjects"""
		return self._ApplyTypes_(590, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), 'MirrorObjects', None,vaObjects
			, vaStart, vaEnd, vaCopy)

	def MoveObject(self, vaObject=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg):
		"""MoveObject"""
		return self._ApplyTypes_(270, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'MoveObject', None,vaObject
			, vaStart, vaEnd)

	def MoveObjects(self, vaObjects=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg):
		"""MoveObjects"""
		return self._ApplyTypes_(296, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'MoveObjects', None,vaObjects
			, vaStart, vaEnd)

	def MovePlane(self, vaPlane=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg):
		"""MovePlane"""
		return self._ApplyTypes_(631, 1, (12, 0), ((12, 0), (12, 0)), 'MovePlane', None,vaPlane
			, vaOrigin)

	def MultiListBox(self, vaList=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""MultiListBox"""
		return self._ApplyTypes_(57, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'MultiListBox', None,vaList
			, vaPrompt, vaTitle)

	def NamedCPlane(self, vaName=defaultNamedNotOptArg):
		"""NamedCPlane"""
		return self._ApplyTypes_(286, 1, (12, 0), ((12, 0),), 'NamedCPlane', None,vaName
			)

	def NamedCPlanes(self):
		"""NamedCPlanes"""
		return self._ApplyTypes_(258, 1, (12, 0), (), 'NamedCPlanes', None,)

	def NamedViews(self):
		"""NamedViews"""
		return self._ApplyTypes_(259, 1, (12, 0), (), 'NamedViews', None,)

	def NextObject(self, vaObject=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""NextObject"""
		return self._ApplyTypes_(36, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'NextObject', None,vaObject
			, vaSelect, vaIncludeLights)

	def NextObjectGrip(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg, vaDir=defaultNamedOptArg, vaSelect=defaultNamedOptArg):
		"""NextObjectGrip"""
		return self._ApplyTypes_(558, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), 'NextObjectGrip', None,vaObject
			, vaIndex, vaDir, vaSelect)

	def NormalObjects(self, vaIncludeLights=defaultNamedOptArg):
		"""NormalObjects"""
		return self._ApplyTypes_(364, 1, (12, 0), ((12, 16),), 'NormalObjects', None,vaIncludeLights
			)

	def Notes(self, vaNotes=defaultNamedOptArg):
		"""Notes"""
		return self._ApplyTypes_(274, 1, (12, 0), ((12, 16),), 'Notes', None,vaNotes
			)

	def ObjectColor(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ObjectColor"""
		return self._ApplyTypes_(191, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectColor', None,vaObject
			, vaValue)

	def ObjectColorSource(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ObjectColorSource"""
		return self._ApplyTypes_(192, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectColorSource', None,vaObject
			, vaValue)

	def ObjectDataCount(self, vaObject=defaultNamedNotOptArg):
		"""ObjectDataCount"""
		return self._ApplyTypes_(242, 1, (12, 0), ((12, 0),), 'ObjectDataCount', None,vaObject
			)

	def ObjectDescription(self, vaObject=defaultNamedNotOptArg):
		"""ObjectDescription"""
		return self._ApplyTypes_(470, 1, (12, 0), ((12, 0),), 'ObjectDescription', None,vaObject
			)

	def ObjectDump(self, vaObject=defaultNamedNotOptArg, vaType=defaultNamedOptArg):
		"""ObjectDump"""
		return self._ApplyTypes_(705, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectDump', None,vaObject
			, vaType)

	def ObjectGripCount(self, vaObject=defaultNamedNotOptArg):
		"""ObjectGripCount"""
		return self._ApplyTypes_(500, 1, (12, 0), ((12, 0),), 'ObjectGripCount', None,vaObject
			)

	def ObjectGripLocation(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg, vaPt=defaultNamedOptArg):
		"""ObjectGripLocation"""
		return self._ApplyTypes_(556, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'ObjectGripLocation', None,vaObject
			, vaIndex, vaPt)

	def ObjectGripLocations(self, vaObject=defaultNamedNotOptArg, vaPoints=defaultNamedOptArg):
		"""ObjectGripLocations"""
		return self._ApplyTypes_(557, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectGripLocations', None,vaObject
			, vaPoints)

	def ObjectGripsOn(self, vaObject=defaultNamedNotOptArg):
		"""ObjectGripsOn"""
		return self._ApplyTypes_(497, 1, (12, 0), ((12, 0),), 'ObjectGripsOn', None,vaObject
			)

	def ObjectGripsSelected(self, vaObject=defaultNamedNotOptArg):
		"""ObjectGripsSelected"""
		return self._ApplyTypes_(498, 1, (12, 0), ((12, 0),), 'ObjectGripsSelected', None,vaObject
			)

	def ObjectGroups(self, vaObject=defaultNamedNotOptArg):
		"""ObjectGroups"""
		return self._ApplyTypes_(193, 1, (12, 0), ((12, 0),), 'ObjectGroups', None,vaObject
			)

	def ObjectLayer(self, vaObject=defaultNamedNotOptArg, vaLayer=defaultNamedOptArg):
		"""ObjectLayer"""
		return self._ApplyTypes_(51, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectLayer', None,vaObject
			, vaLayer)

	def ObjectLinetype(self, vaObject=defaultNamedNotOptArg, vaLinetype=defaultNamedOptArg):
		"""ObjectLinetype"""
		return self._ApplyTypes_(646, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectLinetype', None,vaObject
			, vaLinetype)

	def ObjectLinetypeSource(self, vaObject=defaultNamedNotOptArg, vaSource=defaultNamedOptArg):
		"""ObjectLinetypeSource"""
		return self._ApplyTypes_(647, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectLinetypeSource', None,vaObject
			, vaSource)

	def ObjectMaterialIndex(self, vaObject=defaultNamedNotOptArg):
		"""ObjectMaterialIndex"""
		return self._ApplyTypes_(194, 1, (12, 0), ((12, 0),), 'ObjectMaterialIndex', None,vaObject
			)

	def ObjectMaterialSource(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ObjectMaterialSource"""
		return self._ApplyTypes_(195, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectMaterialSource', None,vaObject
			, vaValue)

	def ObjectName(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ObjectName"""
		return self._ApplyTypes_(196, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectName', None,vaObject
			, vaValue)

	def ObjectNames(self, vaObjects=defaultNamedNotOptArg, vaNames=defaultNamedOptArg):
		"""ObjectNames"""
		return self._ApplyTypes_(639, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectNames', None,vaObjects
			, vaNames)

	def ObjectTopGroup(self, vaObject=defaultNamedNotOptArg):
		"""ObjectTopGroup"""
		return self._ApplyTypes_(197, 1, (12, 0), ((12, 0),), 'ObjectTopGroup', None,vaObject
			)

	def ObjectType(self, vaObject=defaultNamedNotOptArg):
		"""ObjectType"""
		return self._ApplyTypes_(198, 1, (12, 0), ((12, 0),), 'ObjectType', None,vaObject
			)

	def ObjectURL(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""ObjectURL"""
		return self._ApplyTypes_(199, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectURL', None,vaObject
			, vaValue)

	def ObjectsByColor(self, vaColor=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""ObjectsByColor"""
		return self._ApplyTypes_(37, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'ObjectsByColor', None,vaColor
			, vaSelect, vaIncludeLights)

	def ObjectsByGroup(self, vaGroup=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg):
		"""ObjectsByGroup"""
		return self._ApplyTypes_(38, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectsByGroup', None,vaGroup
			, vaSelect)

	def ObjectsByLayer(self, vaLayer=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg):
		"""ObjectsByLayer"""
		return self._ApplyTypes_(39, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectsByLayer', None,vaLayer
			, vaSelect)

	def ObjectsByName(self, vaName=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""ObjectsByName"""
		return self._ApplyTypes_(40, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'ObjectsByName', None,vaName
			, vaSelect, vaIncludeLights)

	def ObjectsByType(self, vaType=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg):
		"""ObjectsByType"""
		return self._ApplyTypes_(41, 1, (12, 0), ((12, 0), (12, 16)), 'ObjectsByType', None,vaType
			, vaSelect)

	def ObjectsByURL(self, vaURL=defaultNamedNotOptArg, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""ObjectsByURL"""
		return self._ApplyTypes_(42, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'ObjectsByURL', None,vaURL
			, vaSelect, vaIncludeLights)

	def OffsetCurve(self, vaObject=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg, vaDistance=defaultNamedNotOptArg, vaNormal=defaultNamedOptArg
			, vaCorner=defaultNamedOptArg):
		"""OffsetCurve"""
		return self._ApplyTypes_(634, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16), (12, 16)), 'OffsetCurve', None,vaObject
			, vaOrigin, vaDistance, vaNormal, vaCorner)

	def OffsetSurface(self, vaObject=defaultNamedNotOptArg, vaDistance=defaultNamedNotOptArg):
		"""OffsetSurface"""
		return self._ApplyTypes_(635, 1, (12, 0), ((12, 0), (12, 0)), 'OffsetSurface', None,vaObject
			, vaDistance)

	def OpenFileName(self, vaTitle=defaultNamedOptArg, vaFilter=defaultNamedOptArg, vaPath=defaultNamedOptArg, vaFile=defaultNamedOptArg
			, vaExt=defaultNamedOptArg):
		"""OpenFileName"""
		return self._ApplyTypes_(151, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'OpenFileName', None,vaTitle
			, vaFilter, vaPath, vaFile, vaExt)

	def OpenToolBarCollection(self, vaFile=defaultNamedNotOptArg):
		"""OpenToolBarCollection"""
		return self._ApplyTypes_(228, 1, (12, 0), ((12, 0),), 'OpenToolBarCollection', None,vaFile
			)

	def OrientObject(self, vaObject=defaultNamedNotOptArg, vaFrom=defaultNamedNotOptArg, vaTo=defaultNamedNotOptArg, vaFlags=defaultNamedOptArg):
		"""OrientObject"""
		return self._ApplyTypes_(390, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), 'OrientObject', None,vaObject
			, vaFrom, vaTo, vaFlags)

	def OrientObjects(self, vaObjects=defaultNamedNotOptArg, vaFrom=defaultNamedNotOptArg, vaTo=defaultNamedNotOptArg, vaFlags=defaultNamedOptArg):
		"""OrientObjects"""
		return self._ApplyTypes_(391, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), 'OrientObjects', None,vaObjects
			, vaFrom, vaTo, vaFlags)

	def Ortho(self, vaMode=defaultNamedOptArg):
		"""Ortho"""
		return self._ApplyTypes_(345, 1, (12, 0), ((12, 16),), 'Ortho', None,vaMode
			)

	def Osnap(self, vaMode=defaultNamedOptArg):
		"""Osnap"""
		return self._ApplyTypes_(347, 1, (12, 0), ((12, 16),), 'Osnap', None,vaMode
			)

	def OsnapDialog(self, vaMode=defaultNamedOptArg):
		"""OsnapDialog"""
		return self._ApplyTypes_(349, 1, (12, 0), ((12, 16),), 'OsnapDialog', None,vaMode
			)

	def OsnapMode(self, vaModes=defaultNamedOptArg):
		"""OsnapMode"""
		return self._ApplyTypes_(343, 1, (12, 0), ((12, 16),), 'OsnapMode', None,vaModes
			)

	def PI(self):
		"""PI"""
		return self._ApplyTypes_(663, 1, (12, 0), (), 'PI', None,)

	def ParentLayer(self, vaName=defaultNamedNotOptArg, vaParent=defaultNamedOptArg):
		"""ParentLayer"""
		return self._ApplyTypes_(688, 1, (12, 0), ((12, 0), (12, 16)), 'ParentLayer', None,vaName
			, vaParent)

	def Planar(self, vaMode=defaultNamedOptArg):
		"""Planar"""
		return self._ApplyTypes_(346, 1, (12, 0), ((12, 16),), 'Planar', None,vaMode
			)

	def PlanarClosedCurveContainment(self, vaCrv1=defaultNamedNotOptArg, vaCrv2=defaultNamedNotOptArg, vaPlane=defaultNamedOptArg, vaTol=defaultNamedOptArg):
		"""PlanarClosedCurveContainment"""
		return self._ApplyTypes_(480, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), 'PlanarClosedCurveContainment', None,vaCrv1
			, vaCrv2, vaPlane, vaTol)

	def PlanarCurveCollision(self, vaCrv1=defaultNamedNotOptArg, vaCrv2=defaultNamedNotOptArg, vaPlane=defaultNamedOptArg, vaTol=defaultNamedOptArg):
		"""PlanarCurveCollision"""
		return self._ApplyTypes_(481, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), 'PlanarCurveCollision', None,vaCrv1
			, vaCrv2, vaPlane, vaTol)

	def PlaneClosestPoint(self, vaPlane=defaultNamedNotOptArg, vaPt=defaultNamedNotOptArg):
		"""PlaneClosestPoint"""
		return self._ApplyTypes_(629, 1, (12, 0), ((12, 0), (12, 0)), 'PlaneClosestPoint', None,vaPlane
			, vaPt)

	def PlaneEquation(self, vaPlane=defaultNamedNotOptArg):
		"""PlaneEquation"""
		return self._ApplyTypes_(642, 1, (12, 0), ((12, 0),), 'PlaneEquation', None,vaPlane
			)

	def PlaneFitFromPoints(self, vaPoints=defaultNamedNotOptArg):
		"""PlaneFitFromPoints"""
		return self._ApplyTypes_(725, 1, (12, 0), ((12, 0),), 'PlaneFitFromPoints', None,vaPoints
			)

	def PlaneFromFrame(self, vaOrigin=defaultNamedNotOptArg, vaX=defaultNamedNotOptArg, vaY=defaultNamedNotOptArg):
		"""PlaneFromFrame"""
		return self._ApplyTypes_(627, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'PlaneFromFrame', None,vaOrigin
			, vaX, vaY)

	def PlaneFromNormal(self, vaOrigin=defaultNamedNotOptArg, vaNormal=defaultNamedNotOptArg):
		"""PlaneFromNormal"""
		return self._ApplyTypes_(626, 1, (12, 0), ((12, 0), (12, 0)), 'PlaneFromNormal', None,vaOrigin
			, vaNormal)

	def PlaneFromPoints(self, vaOrigin=defaultNamedNotOptArg, vaX=defaultNamedNotOptArg, vaY=defaultNamedNotOptArg):
		"""PlaneFromPoints"""
		return self._ApplyTypes_(649, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'PlaneFromPoints', None,vaOrigin
			, vaX, vaY)

	def PlugIns(self, vaTypes=defaultNamedOptArg, vaLoaded=defaultNamedOptArg):
		"""PlugIns"""
		return self._ApplyTypes_(315, 1, (12, 0), ((12, 16), (12, 16)), 'PlugIns', None,vaTypes
			, vaLoaded)

	def PointAdd(self, vaPt0=defaultNamedNotOptArg, vaPt1=defaultNamedNotOptArg):
		"""PointAdd"""
		return self._ApplyTypes_(666, 1, (12, 0), ((12, 0), (12, 0)), 'PointAdd', None,vaPt0
			, vaPt1)

	def PointCloudCount(self, vaObject=defaultNamedNotOptArg):
		"""PointCloudCount"""
		return self._ApplyTypes_(128, 1, (12, 0), ((12, 0),), 'PointCloudCount', None,vaObject
			)

	def PointCloudPoints(self, vaObject=defaultNamedNotOptArg):
		"""PointCloudPoints"""
		return self._ApplyTypes_(129, 1, (12, 0), ((12, 0),), 'PointCloudPoints', None,vaObject
			)

	def PointCompare(self, vaPt0=defaultNamedNotOptArg, vaPt1=defaultNamedNotOptArg, vaTol=defaultNamedOptArg):
		"""PointCompare"""
		return self._ApplyTypes_(667, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'PointCompare', None,vaPt0
			, vaPt1, vaTol)

	def PointCoordinates(self, vaObject=defaultNamedNotOptArg, vaNewPt=defaultNamedOptArg):
		"""PointCoordinates"""
		return self._ApplyTypes_(130, 1, (12, 0), ((12, 0), (12, 16)), 'PointCoordinates', None,vaObject
			, vaNewPt)

	def PointDivide(self, vaPt=defaultNamedNotOptArg, vaDivide=defaultNamedNotOptArg):
		"""PointDivide"""
		return self._ApplyTypes_(668, 1, (12, 0), ((12, 0), (12, 0)), 'PointDivide', None,vaPt
			, vaDivide)

	def PointInPlanarClosedCurve(self, vaPt=defaultNamedNotOptArg, vaCrv=defaultNamedNotOptArg, vaPlane=defaultNamedOptArg, vaTol=defaultNamedOptArg):
		"""PointInPlanarClosedCurve"""
		return self._ApplyTypes_(482, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), 'PointInPlanarClosedCurve', None,vaPt
			, vaCrv, vaPlane, vaTol)

	def PointScale(self, vaPt=defaultNamedNotOptArg, vaScale=defaultNamedNotOptArg):
		"""PointScale"""
		return self._ApplyTypes_(669, 1, (12, 0), ((12, 0), (12, 0)), 'PointScale', None,vaPt
			, vaScale)

	def PointSubtract(self, vaPt0=defaultNamedNotOptArg, vaPt1=defaultNamedNotOptArg):
		"""PointSubtract"""
		return self._ApplyTypes_(670, 1, (12, 0), ((12, 0), (12, 0)), 'PointSubtract', None,vaPt0
			, vaPt1)

	def PointTransform(self, vaPt=defaultNamedNotOptArg, vaXform=defaultNamedNotOptArg):
		"""PointTransform"""
		return self._ApplyTypes_(671, 1, (12, 0), ((12, 0), (12, 0)), 'PointTransform', None,vaPt
			, vaXform)

	def PointsAreCoplanar(self, vaPoints=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""PointsAreCoplanar"""
		return self._ApplyTypes_(593, 1, (12, 0), ((12, 0), (12, 16)), 'PointsAreCoplanar', None,vaPoints
			, vaTolerance)

	def Polar(self, vaPoint=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg, vaDistance=defaultNamedNotOptArg, vaPlane=defaultNamedNotOptArg):
		"""Polar"""
		return self._ApplyTypes_(662, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), 'Polar', None,vaPoint
			, vaAngle, vaDistance, vaPlane)

	def PolyCurveCount(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""PolyCurveCount"""
		return self._ApplyTypes_(369, 1, (12, 0), ((12, 0), (12, 16)), 'PolyCurveCount', None,vaObject
			, vaIndex)

	def PolylineVertices(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedOptArg):
		"""PolylineVertices"""
		return self._ApplyTypes_(112, 1, (12, 0), ((12, 0), (12, 16)), 'PolylineVertices', None,vaObject
			, vaIndex)

	def PopupMenu(self, vaItems=defaultNamedNotOptArg, vaModes=defaultNamedOptArg, vaPoint=defaultNamedOptArg, vaView=defaultNamedOptArg):
		"""PopupMenu"""
		return self._ApplyTypes_(595, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), 'PopupMenu', None,vaItems
			, vaModes, vaPoint, vaView)

	def PrevObjectGrip(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg, vaDir=defaultNamedOptArg, vaSelect=defaultNamedOptArg):
		"""PrevObjectGrip"""
		return self._ApplyTypes_(559, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), 'PrevObjectGrip', None,vaObject
			, vaIndex, vaDir, vaSelect)

	def PrevSelectedObjects(self, vaSelect=defaultNamedOptArg):
		"""PrevSelectedObjects"""
		return self._ApplyTypes_(486, 1, (12, 0), ((12, 16),), 'PrevSelectedObjects', None,vaSelect
			)

	def Print(self, vaCmd=defaultNamedOptArg):
		"""Print"""
		return self._ApplyTypes_(2, 1, (12, 0), ((12, 16),), 'Print', None,vaCmd
			)

	def PrintEx(self, vaText=defaultNamedOptArg):
		"""PrintEx"""
		return self._ApplyTypes_(370, 1, (12, 0), ((12, 16),), 'PrintEx', None,vaText
			)

	def PrinterNames(self):
		"""PrinterNames"""
		return self._ApplyTypes_(356, 1, (12, 0), (), 'PrinterNames', None,)

	def ProjectOsnaps(self, vaMode=defaultNamedOptArg):
		"""ProjectOsnaps"""
		return self._ApplyTypes_(348, 1, (12, 0), ((12, 16),), 'ProjectOsnaps', None,vaMode
			)

	def Prompt(self, vaPrompt=defaultNamedOptArg):
		"""Prompt"""
		return self._ApplyTypes_(24, 1, (12, 0), ((12, 16),), 'Prompt', None,vaPrompt
			)

	def PropertyListBox(self, vaList=defaultNamedNotOptArg, vaValues=defaultNamedNotOptArg, vaPrompt=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""PropertyListBox"""
		return self._ApplyTypes_(58, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), 'PropertyListBox', None,vaList
			, vaValues, vaPrompt, vaTitle)

	def Pt2Str(self, vaPoint=defaultNamedNotOptArg, vaPrecision=defaultNamedOptArg, vaSpace=defaultNamedOptArg):
		"""Pt2Str"""
		return self._ApplyTypes_(297, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'Pt2Str', None,vaPoint
			, vaPrecision, vaSpace)

	def PullCurve(self, vaObject=defaultNamedNotOptArg, vaCurve=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""PullCurve"""
		return self._ApplyTypes_(493, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'PullCurve', None,vaObject
			, vaCurve, vaDelete)

	def PullCurveToMesh(self, vaMesh=defaultNamedNotOptArg, vaCurve=defaultNamedNotOptArg):
		"""PullCurveToMesh"""
		return self._ApplyTypes_(719, 1, (12, 0), ((12, 0), (12, 0)), 'PullCurveToMesh', None,vaMesh
			, vaCurve)

	def PullPoints(self, vaObject=defaultNamedNotOptArg, vaPoints=defaultNamedNotOptArg):
		"""PullPoints"""
		return self._ApplyTypes_(716, 1, (12, 0), ((12, 0), (12, 0)), 'PullPoints', None,vaObject
			, vaPoints)

	def PurgeLayer(self, vaLayer=defaultNamedNotOptArg):
		"""PurgeLayer"""
		return self._ApplyTypes_(291, 1, (12, 0), ((12, 0),), 'PurgeLayer', None,vaLayer
			)

	def RealBox(self, vaPrompt=defaultNamedOptArg, vaReal=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""RealBox"""
		return self._ApplyTypes_(59, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'RealBox', None,vaPrompt
			, vaReal, vaTitle)

	def Redraw(self):
		"""Redraw"""
		return self._ApplyTypes_(114, 1, (12, 0), (), 'Redraw', None,)

	def ReferenceObjects(self, vaIncludeLights=defaultNamedOptArg):
		"""ReferenceObjects"""
		return self._ApplyTypes_(367, 1, (12, 0), ((12, 16),), 'ReferenceObjects', None,vaIncludeLights
			)

	def RegistryKey(self):
		"""RegistryKey"""
		return self._ApplyTypes_(25, 1, (12, 0), (), 'RegistryKey', None,)

	def RemapObject(self, vaObject=defaultNamedNotOptArg, vaSrcPlane=defaultNamedNotOptArg, vaDstPlane=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""RemapObject"""
		return self._ApplyTypes_(655, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), 'RemapObject', None,vaObject
			, vaSrcPlane, vaDstPlane, vaCopy)

	def RemapObjects(self, vaObjects=defaultNamedNotOptArg, vaSrcPlane=defaultNamedNotOptArg, vaDstPlane=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""RemapObjects"""
		return self._ApplyTypes_(656, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), 'RemapObjects', None,vaObjects
			, vaSrcPlane, vaDstPlane, vaCopy)

	def RemoveObjectFromAllGroups(self, vaObject=defaultNamedNotOptArg):
		"""RemoveObjectFromAllGroups"""
		return self._ApplyTypes_(141, 1, (12, 0), ((12, 0),), 'RemoveObjectFromAllGroups', None,vaObject
			)

	def RemoveObjectFromGroup(self, vaObject=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""RemoveObjectFromGroup"""
		return self._ApplyTypes_(142, 1, (12, 0), ((12, 0), (12, 0)), 'RemoveObjectFromGroup', None,vaObject
			, vaName)

	def RemoveObjectFromTopGroup(self, vaObject=defaultNamedNotOptArg):
		"""RemoveObjectFromTopGroup"""
		return self._ApplyTypes_(143, 1, (12, 0), ((12, 0),), 'RemoveObjectFromTopGroup', None,vaObject
			)

	def RemoveObjectsFromGroup(self, vaObjects=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""RemoveObjectsFromGroup"""
		return self._ApplyTypes_(144, 1, (12, 0), ((12, 0), (12, 0)), 'RemoveObjectsFromGroup', None,vaObjects
			, vaName)

	def RenameBlock(self, vaOld=defaultNamedNotOptArg, vaNew=defaultNamedNotOptArg):
		"""RenameBlock"""
		return self._ApplyTypes_(399, 1, (12, 0), ((12, 0), (12, 0)), 'RenameBlock', None,vaOld
			, vaNew)

	def RenameDimStyle(self, vaOld=defaultNamedNotOptArg, vaNew=defaultNamedNotOptArg):
		"""RenameDimStyle"""
		return self._ApplyTypes_(458, 1, (12, 0), ((12, 0), (12, 0)), 'RenameDimStyle', None,vaOld
			, vaNew)

	def RenameGroup(self, vaOld=defaultNamedNotOptArg, vaNew=defaultNamedNotOptArg):
		"""RenameGroup"""
		return self._ApplyTypes_(145, 1, (12, 0), ((12, 0), (12, 0)), 'RenameGroup', None,vaOld
			, vaNew)

	def RenameLayer(self, vaOld=defaultNamedNotOptArg, vaNew=defaultNamedNotOptArg):
		"""RenameLayer"""
		return self._ApplyTypes_(16, 1, (12, 0), ((12, 0), (12, 0)), 'RenameLayer', None,vaOld
			, vaNew)

	def RenameView(self, vaOld=defaultNamedNotOptArg, vaNew=defaultNamedNotOptArg):
		"""RenameView"""
		return self._ApplyTypes_(260, 1, (12, 0), ((12, 0), (12, 0)), 'RenameView', None,vaOld
			, vaNew)

	def RenderAntialias(self, vaValue=defaultNamedOptArg):
		"""RenderAntialias"""
		return self._ApplyTypes_(333, 1, (12, 0), ((12, 16),), 'RenderAntialias', None,vaValue
			)

	def RenderColor(self, vaItem=defaultNamedNotOptArg, vaColor=defaultNamedOptArg):
		"""RenderColor"""
		return self._ApplyTypes_(331, 1, (12, 0), ((12, 0), (12, 16)), 'RenderColor', None,vaItem
			, vaColor)

	def RenderResolution(self, vaSizes=defaultNamedOptArg):
		"""RenderResolution"""
		return self._ApplyTypes_(332, 1, (12, 0), ((12, 16),), 'RenderResolution', None,vaSizes
			)

	def RenderSettings(self, vaSetting=defaultNamedOptArg):
		"""RenderSettings"""
		return self._ApplyTypes_(334, 1, (12, 0), ((12, 16),), 'RenderSettings', None,vaSetting
			)

	def RestoreNamedCPlane(self, vaName=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""RestoreNamedCPlane"""
		return self._ApplyTypes_(282, 1, (12, 0), ((12, 0), (12, 16)), 'RestoreNamedCPlane', None,vaName
			, vaView)

	def RestoreNamedView(self, vaName=defaultNamedNotOptArg, vaView=defaultNamedOptArg):
		"""RestoreNamedView"""
		return self._ApplyTypes_(283, 1, (12, 0), ((12, 0), (12, 16)), 'RestoreNamedView', None,vaName
			, vaView)

	def ReverseCurve(self, vaObject=defaultNamedNotOptArg):
		"""ReverseCurve"""
		return self._ApplyTypes_(542, 1, (12, 0), ((12, 0),), 'ReverseCurve', None,vaObject
			)

	def RotateCamera(self, vaView=defaultNamedOptArg, vaDir=defaultNamedOptArg, vaAngle=defaultNamedOptArg):
		"""RotateCamera"""
		return self._ApplyTypes_(519, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'RotateCamera', None,vaView
			, vaDir, vaAngle)

	def RotateObject(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg, vaAxis=defaultNamedOptArg
			, vaCopy=defaultNamedOptArg):
		"""RotateObject"""
		return self._ApplyTypes_(392, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16), (12, 16)), 'RotateObject', None,vaObject
			, vaPoint, vaAngle, vaAxis, vaCopy)

	def RotateObjects(self, vaObjects=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg, vaAxis=defaultNamedOptArg
			, vaCopy=defaultNamedOptArg):
		"""RotateObjects"""
		return self._ApplyTypes_(393, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16), (12, 16)), 'RotateObjects', None,vaObjects
			, vaPoint, vaAngle, vaAxis, vaCopy)

	def RotatePlane(self, vaPlane=defaultNamedNotOptArg, vaDegrees=defaultNamedNotOptArg, vaX=defaultNamedNotOptArg):
		"""RotatePlane"""
		return self._ApplyTypes_(630, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'RotatePlane', None,vaPlane
			, vaDegrees, vaX)

	def RotateView(self, vaView=defaultNamedNotOptArg, vaDir=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg):
		"""RotateView"""
		return self._ApplyTypes_(650, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'RotateView', None,vaView
			, vaDir, vaAngle)

	def SaveFileName(self, vaTitle=defaultNamedOptArg, vaFilter=defaultNamedOptArg, vaPath=defaultNamedOptArg, vaFile=defaultNamedOptArg
			, vaExt=defaultNamedOptArg):
		"""SaveFileName"""
		return self._ApplyTypes_(152, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'SaveFileName', None,vaTitle
			, vaFilter, vaPath, vaFile, vaExt)

	def SaveSettings(self, vaFile=defaultNamedNotOptArg, vaSection=defaultNamedOptArg, vaKey=defaultNamedOptArg, vaValue=defaultNamedOptArg):
		"""SaveSettings"""
		return self._ApplyTypes_(247, 1, (12, 0), ((12, 0), (12, 16), (12, 16), (12, 16)), 'SaveSettings', None,vaFile
			, vaSection, vaKey, vaValue)

	def SaveToolBarCollection(self, vaAlias=defaultNamedNotOptArg):
		"""SaveToolBarCollection"""
		return self._ApplyTypes_(229, 1, (12, 0), ((12, 0),), 'SaveToolBarCollection', None,vaAlias
			)

	def SaveToolBarCollectionAs(self, vaAlias=defaultNamedNotOptArg, vaFile=defaultNamedOptArg):
		"""SaveToolBarCollectionAs"""
		return self._ApplyTypes_(230, 1, (12, 0), ((12, 0), (12, 16)), 'SaveToolBarCollectionAs', None,vaAlias
			, vaFile)

	def ScaleObject(self, vaObject=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg, vaScale=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""ScaleObject"""
		return self._ApplyTypes_(585, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), 'ScaleObject', None,vaObject
			, vaOrigin, vaScale, vaCopy)

	def ScaleObjects(self, vaObjects=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg, vaScale=defaultNamedNotOptArg, vaCopy=defaultNamedOptArg):
		"""ScaleObjects"""
		return self._ApplyTypes_(586, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16)), 'ScaleObjects', None,vaObjects
			, vaOrigin, vaScale, vaCopy)

	def ScreenSize(self):
		"""ScreenSize"""
		return self._ApplyTypes_(553, 1, (12, 0), (), 'ScreenSize', None,)

	def SdkVersion(self):
		"""SdkVersion"""
		return self._ApplyTypes_(359, 1, (12, 0), (), 'SdkVersion', None,)

	def SearchPathCount(self):
		"""SearchPathCount"""
		return self._ApplyTypes_(509, 1, (12, 0), (), 'SearchPathCount', None,)

	def SearchPathList(self):
		"""SearchPathList"""
		return self._ApplyTypes_(510, 1, (12, 0), (), 'SearchPathList', None,)

	def SelectObject(self, vaObject=defaultNamedNotOptArg):
		"""SelectObject"""
		return self._ApplyTypes_(200, 1, (12, 0), ((12, 0),), 'SelectObject', None,vaObject
			)

	def SelectObjectGrip(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg):
		"""SelectObjectGrip"""
		return self._ApplyTypes_(554, 1, (12, 0), ((12, 0), (12, 0)), 'SelectObjectGrip', None,vaObject
			, vaIndex)

	def SelectObjectGrips(self, vaObject=defaultNamedNotOptArg):
		"""SelectObjectGrips"""
		return self._ApplyTypes_(501, 1, (12, 0), ((12, 0),), 'SelectObjectGrips', None,vaObject
			)

	def SelectObjects(self, vaObjects=defaultNamedNotOptArg):
		"""SelectObjects"""
		return self._ApplyTypes_(298, 1, (12, 0), ((12, 0),), 'SelectObjects', None,vaObjects
			)

	def SelectedObjectGrips(self, vaObject=defaultNamedNotOptArg):
		"""SelectedObjectGrips"""
		return self._ApplyTypes_(560, 1, (12, 0), ((12, 0),), 'SelectedObjectGrips', None,vaObject
			)

	def SelectedObjects(self, vaIncludeLights=defaultNamedOptArg):
		"""SelectedObjects"""
		return self._ApplyTypes_(43, 1, (12, 0), ((12, 16),), 'SelectedObjects', None,vaIncludeLights
			)

	def SendKeystrokes(self, vaStr=defaultNamedOptArg, vaReturn=defaultNamedOptArg):
		"""SendKeystrokes"""
		return self._ApplyTypes_(496, 1, (12, 0), ((12, 16), (12, 16)), 'SendKeystrokes', None,vaStr
			, vaReturn)

	def SetAttributeData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedNotOptArg, vaKey=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""SetAttributeData"""
		return self._ApplyTypes_(683, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), 'SetAttributeData', None,vaObject
			, vaApp, vaKey, vaValue)

	def SetDocumentData(self, vaApp=defaultNamedNotOptArg, vaKey=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""SetDocumentData"""
		return self._ApplyTypes_(243, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'SetDocumentData', None,vaApp
			, vaKey, vaValue)

	def SetObjectData(self, vaObject=defaultNamedNotOptArg, vaApp=defaultNamedNotOptArg, vaKey=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""SetObjectData"""
		return self._ApplyTypes_(244, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), 'SetObjectData', None,vaObject
			, vaApp, vaKey, vaValue)

	def ShearObject(self, vaObject=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg, vaRefPt=defaultNamedNotOptArg, vaDegrees=defaultNamedNotOptArg
			, vaCopy=defaultNamedOptArg):
		"""ShearObject"""
		return self._ApplyTypes_(587, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 16)), 'ShearObject', None,vaObject
			, vaOrigin, vaRefPt, vaDegrees, vaCopy)

	def ShearObjects(self, vaObjects=defaultNamedNotOptArg, vaOrigin=defaultNamedNotOptArg, vaRefPt=defaultNamedNotOptArg, vaDegrees=defaultNamedNotOptArg
			, vaCopy=defaultNamedOptArg):
		"""ShearObjects"""
		return self._ApplyTypes_(588, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 16)), 'ShearObjects', None,vaObjects
			, vaOrigin, vaRefPt, vaDegrees, vaCopy)

	def ShortPath(self, vaObject=defaultNamedNotOptArg, vaStart=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg):
		"""ShortPath"""
		return self._ApplyTypes_(702, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'ShortPath', None,vaObject
			, vaStart, vaEnd)

	def ShowObject(self, vaObject=defaultNamedNotOptArg):
		"""ShowObject"""
		return self._ApplyTypes_(201, 1, (12, 0), ((12, 0),), 'ShowObject', None,vaObject
			)

	def ShowObjects(self, vaObjects=defaultNamedNotOptArg):
		"""ShowObjects"""
		return self._ApplyTypes_(305, 1, (12, 0), ((12, 0),), 'ShowObjects', None,vaObjects
			)

	def ShowToolBar(self, vaAlias=defaultNamedNotOptArg, vaName=defaultNamedNotOptArg):
		"""ShowToolBar"""
		return self._ApplyTypes_(231, 1, (12, 0), ((12, 0), (12, 0)), 'ShowToolBar', None,vaAlias
			, vaName)

	def ShowViewTitle(self, vaView=defaultNamedOptArg, vaValue=defaultNamedOptArg):
		"""ShowViewTitle"""
		return self._ApplyTypes_(261, 1, (12, 0), ((12, 16), (12, 16)), 'ShowViewTitle', None,vaView
			, vaValue)

	def ShrinkTrimmedSurface(self, vaObject=defaultNamedNotOptArg):
		"""ShrinkTrimmedSurface"""
		return self._ApplyTypes_(700, 1, (12, 0), ((12, 0),), 'ShrinkTrimmedSurface', None,vaObject
			)

	def SimplifyArray(self, vaArray=defaultNamedNotOptArg):
		"""SimplifyArray"""
		return self._ApplyTypes_(597, 1, (12, 0), ((12, 0),), 'SimplifyArray', None,vaArray
			)

	def SimplifyCurve(self, vaObject=defaultNamedNotOptArg, vaFlags=defaultNamedOptArg):
		"""SimplifyCurve"""
		return self._ApplyTypes_(573, 1, (12, 0), ((12, 0), (12, 16)), 'SimplifyCurve', None,vaObject
			, vaFlags)

	def Sleep(self, vaTime=defaultNamedNotOptArg):
		"""Sleep"""
		return self._ApplyTypes_(248, 1, (12, 0), ((12, 0),), 'Sleep', None,vaTime
			)

	def Snap(self, vaMode=defaultNamedOptArg):
		"""Snap"""
		return self._ApplyTypes_(344, 1, (12, 0), ((12, 16),), 'Snap', None,vaMode
			)

	def Sort(self, vaStrings=defaultNamedNotOptArg, vaMode=defaultNamedOptArg):
		"""Sort"""
		return self._ApplyTypes_(249, 1, (12, 0), ((12, 0), (12, 16)), 'Sort', None,vaStrings
			, vaMode)

	def SortNumbers(self, vaNumbers=defaultNamedNotOptArg, vaAscending=defaultNamedOptArg):
		"""SortNumbers"""
		return self._ApplyTypes_(552, 1, (12, 0), ((12, 0), (12, 16)), 'SortNumbers', None,vaNumbers
			, vaAscending)

	def SortPointList(self, vaPoints=defaultNamedNotOptArg, vaTolerance=defaultNamedOptArg):
		"""SortPointList"""
		return self._ApplyTypes_(644, 1, (12, 0), ((12, 0), (12, 16)), 'SortPointList', None,vaPoints
			, vaTolerance)

	def SortPoints(self, vaPoints=defaultNamedNotOptArg, vaAscending=defaultNamedOptArg):
		"""SortPoints"""
		return self._ApplyTypes_(551, 1, (12, 0), ((12, 0), (12, 16)), 'SortPoints', None,vaPoints
			, vaAscending)

	def SortStrings(self, vaStrings=defaultNamedNotOptArg, vaMode=defaultNamedOptArg):
		"""SortStrings"""
		return self._ApplyTypes_(640, 1, (12, 0), ((12, 0), (12, 16)), 'SortStrings', None,vaStrings
			, vaMode)

	def SplitBrep(self, vaObject=defaultNamedNotOptArg, vaCutter=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""SplitBrep"""
		return self._ApplyTypes_(637, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'SplitBrep', None,vaObject
			, vaCutter, vaDelete)

	def SplitCurve(self, vaCrv=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""SplitCurve"""
		return self._ApplyTypes_(504, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'SplitCurve', None,vaCrv
			, vaParam, vaDelete)

	def SplitDisjointMesh(self, vaMesh=defaultNamedNotOptArg, vaDelete=defaultNamedNotOptArg):
		"""SplitDisjointMesh"""
		return self._ApplyTypes_(722, 1, (12, 0), ((12, 0), (12, 0)), 'SplitDisjointMesh', None,vaMesh
			, vaDelete)

	def SpoolToPrinter(self, vaFile=defaultNamedNotOptArg, vaPrinter=defaultNamedNotOptArg):
		"""SpoolToPrinter"""
		return self._ApplyTypes_(357, 1, (12, 0), ((12, 0), (12, 0)), 'SpoolToPrinter', None,vaFile
			, vaPrinter)

	def SpotLightHardness(self, vaLight=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""SpotLightHardness"""
		return self._ApplyTypes_(171, 1, (12, 0), ((12, 0), (12, 16)), 'SpotLightHardness', None,vaLight
			, vaValue)

	def SpotLightRadius(self, vaLight=defaultNamedNotOptArg, vaRadius=defaultNamedOptArg):
		"""SpotLightRadius"""
		return self._ApplyTypes_(584, 1, (12, 0), ((12, 0), (12, 16)), 'SpotLightRadius', None,vaLight
			, vaRadius)

	def SpotLightShadowIntensity(self, vaLight=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""SpotLightShadowIntensity"""
		return self._ApplyTypes_(172, 1, (12, 0), ((12, 0), (12, 16)), 'SpotLightShadowIntensity', None,vaLight
			, vaValue)

	def StartupScriptCount(self):
		"""StartupScriptCount"""
		return self._ApplyTypes_(712, 1, (12, 0), (), 'StartupScriptCount', None,)

	def StartupScriptList(self):
		"""StartupScriptList"""
		return self._ApplyTypes_(713, 1, (12, 0), (), 'StartupScriptList', None,)

	def StatusBarDistance(self, vaDistance=defaultNamedOptArg):
		"""StatusBarDistance"""
		return self._ApplyTypes_(26, 1, (12, 0), ((12, 16),), 'StatusBarDistance', None,vaDistance
			)

	def StatusBarMessage(self, vaText=defaultNamedOptArg):
		"""StatusBarMessage"""
		return self._ApplyTypes_(28, 1, (12, 0), ((12, 16),), 'StatusBarMessage', None,vaText
			)

	def StatusBarNumber(self, vaNumber=defaultNamedOptArg):
		"""StatusBarNumber"""
		return self._ApplyTypes_(312, 1, (12, 0), ((12, 16),), 'StatusBarNumber', None,vaNumber
			)

	def StatusBarPoint(self, vaPoint=defaultNamedOptArg):
		"""StatusBarPoint"""
		return self._ApplyTypes_(27, 1, (12, 0), ((12, 16),), 'StatusBarPoint', None,vaPoint
			)

	def Str2Pt(self, vaStr=defaultNamedNotOptArg):
		"""Str2Pt"""
		return self._ApplyTypes_(409, 1, (12, 0), ((12, 0),), 'Str2Pt', None,vaStr
			)

	def Str2PtArray(self, vaStr=defaultNamedNotOptArg):
		"""Str2PtArray"""
		return self._ApplyTypes_(410, 1, (12, 0), ((12, 0),), 'Str2PtArray', None,vaStr
			)

	def StringBox(self, vaPrompt=defaultNamedOptArg, vaString=defaultNamedOptArg, vaTitle=defaultNamedOptArg):
		"""StringBox"""
		return self._ApplyTypes_(60, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'StringBox', None,vaPrompt
			, vaString, vaTitle)

	def Strtok(self, vaString=defaultNamedNotOptArg, vaSeps=defaultNamedOptArg):
		"""Strtok"""
		return self._ApplyTypes_(250, 1, (12, 0), ((12, 0), (12, 16)), 'Strtok', None,vaString
			, vaSeps)

	def SurfaceArea(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceArea"""
		return self._ApplyTypes_(382, 1, (12, 0), ((12, 0),), 'SurfaceArea', None,vaObject
			)

	def SurfaceAreaCentroid(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceAreaCentroid"""
		return self._ApplyTypes_(384, 1, (12, 0), ((12, 0),), 'SurfaceAreaCentroid', None,vaObject
			)

	def SurfaceAreaMoments(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceAreaMoments"""
		return self._ApplyTypes_(386, 1, (12, 0), ((12, 0),), 'SurfaceAreaMoments', None,vaObject
			)

	def SurfaceClosestPoint(self, vaObject=defaultNamedNotOptArg, vaPt=defaultNamedNotOptArg):
		"""SurfaceClosestPoint"""
		return self._ApplyTypes_(215, 1, (12, 0), ((12, 0), (12, 0)), 'SurfaceClosestPoint', None,vaObject
			, vaPt)

	def SurfaceContourPoints(self, vaObject=defaultNamedNotOptArg, vaBase=defaultNamedNotOptArg, vaEnd=defaultNamedNotOptArg, vaInterval=defaultNamedOptArg
			, vaAngle=defaultNamedOptArg):
		"""SurfaceContourPoints"""
		return self._ApplyTypes_(79, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 16), (12, 16)), 'SurfaceContourPoints', None,vaObject
			, vaBase, vaEnd, vaInterval, vaAngle)

	def SurfaceCurvature(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""SurfaceCurvature"""
		return self._ApplyTypes_(378, 1, (12, 0), ((12, 0), (12, 0)), 'SurfaceCurvature', None,vaObject
			, vaParam)

	def SurfaceCurvatureAnalysis(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceCurvatureAnalysis"""
		return self._ApplyTypes_(632, 1, (12, 0), ((12, 0),), 'SurfaceCurvatureAnalysis', None,vaObject
			)

	def SurfaceDegree(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedOptArg):
		"""SurfaceDegree"""
		return self._ApplyTypes_(216, 1, (12, 0), ((12, 0), (12, 16)), 'SurfaceDegree', None,vaObject
			, vaValue)

	def SurfaceDomain(self, vaObject=defaultNamedNotOptArg, vaValue=defaultNamedNotOptArg):
		"""SurfaceDomain"""
		return self._ApplyTypes_(217, 1, (12, 0), ((12, 0), (12, 0)), 'SurfaceDomain', None,vaObject
			, vaValue)

	def SurfaceEditPoints(self, vaObject=defaultNamedNotOptArg, vaReturnParameters=defaultNamedOptArg, vaReturnAll=defaultNamedOptArg):
		"""SurfaceEditPoints"""
		return self._ApplyTypes_(427, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'SurfaceEditPoints', None,vaObject
			, vaReturnParameters, vaReturnAll)

	def SurfaceEvaluate(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg, vaDerCount=defaultNamedNotOptArg):
		"""SurfaceEvaluate"""
		return self._ApplyTypes_(583, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'SurfaceEvaluate', None,vaObject
			, vaParam, vaDerCount)

	def SurfaceFrame(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""SurfaceFrame"""
		return self._ApplyTypes_(623, 1, (12, 0), ((12, 0), (12, 0)), 'SurfaceFrame', None,vaObject
			, vaParam)

	def SurfaceIsocurveDensity(self, vaObject=defaultNamedNotOptArg, vaDensity=defaultNamedOptArg):
		"""SurfaceIsocurveDensity"""
		return self._ApplyTypes_(361, 1, (12, 0), ((12, 0), (12, 16)), 'SurfaceIsocurveDensity', None,vaObject
			, vaDensity)

	def SurfaceKnotCount(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceKnotCount"""
		return self._ApplyTypes_(431, 1, (12, 0), ((12, 0),), 'SurfaceKnotCount', None,vaObject
			)

	def SurfaceKnots(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceKnots"""
		return self._ApplyTypes_(432, 1, (12, 0), ((12, 0),), 'SurfaceKnots', None,vaObject
			)

	def SurfaceNormal(self, vaObject=defaultNamedNotOptArg, vaParam=defaultNamedNotOptArg):
		"""SurfaceNormal"""
		return self._ApplyTypes_(362, 1, (12, 0), ((12, 0), (12, 0)), 'SurfaceNormal', None,vaObject
			, vaParam)

	def SurfacePointCount(self, vaObject=defaultNamedNotOptArg):
		"""SurfacePointCount"""
		return self._ApplyTypes_(218, 1, (12, 0), ((12, 0),), 'SurfacePointCount', None,vaObject
			)

	def SurfacePoints(self, vaObject=defaultNamedNotOptArg, vaReturnAll=defaultNamedOptArg):
		"""SurfacePoints"""
		return self._ApplyTypes_(372, 1, (12, 0), ((12, 0), (12, 16)), 'SurfacePoints', None,vaObject
			, vaReturnAll)

	def SurfacePrincipalCurvature(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedNotOptArg):
		"""SurfacePrincipalCurvature"""
		return self._ApplyTypes_(717, 1, (12, 0), ((12, 0), (12, 0)), 'SurfacePrincipalCurvature', None,vaObject
			, vaPoint)

	def SurfaceSurfaceIntersection(self, vaSrfA=defaultNamedNotOptArg, vaSrfB=defaultNamedNotOptArg, vaTol=defaultNamedOptArg, vaCreate=defaultNamedOptArg):
		"""SurfaceSurfaceIntersection"""
		return self._ApplyTypes_(484, 1, (12, 0), ((12, 0), (12, 0), (12, 16), (12, 16)), 'SurfaceSurfaceIntersection', None,vaSrfA
			, vaSrfB, vaTol, vaCreate)

	def SurfaceVolume(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceVolume"""
		return self._ApplyTypes_(383, 1, (12, 0), ((12, 0),), 'SurfaceVolume', None,vaObject
			)

	def SurfaceVolumeCentroid(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceVolumeCentroid"""
		return self._ApplyTypes_(385, 1, (12, 0), ((12, 0),), 'SurfaceVolumeCentroid', None,vaObject
			)

	def SurfaceVolumeMoments(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceVolumeMoments"""
		return self._ApplyTypes_(387, 1, (12, 0), ((12, 0),), 'SurfaceVolumeMoments', None,vaObject
			)

	def SurfaceWeights(self, vaObject=defaultNamedNotOptArg):
		"""SurfaceWeights"""
		return self._ApplyTypes_(433, 1, (12, 0), ((12, 0),), 'SurfaceWeights', None,vaObject
			)

	def SynchronizeCPlanes(self, vaView=defaultNamedOptArg):
		"""SynchronizeCPlanes"""
		return self._ApplyTypes_(289, 1, (12, 0), ((12, 16),), 'SynchronizeCPlanes', None,vaView
			)

	def TemplateFile(self, vaFile=defaultNamedOptArg):
		"""TemplateFile"""
		return self._ApplyTypes_(529, 1, (12, 0), ((12, 16),), 'TemplateFile', None,vaFile
			)

	def TemplateFolder(self, vaFolder=defaultNamedOptArg):
		"""TemplateFolder"""
		return self._ApplyTypes_(528, 1, (12, 0), ((12, 16),), 'TemplateFolder', None,vaFolder
			)

	def TextDotPoint(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedOptArg):
		"""TextDotPoint"""
		return self._ApplyTypes_(422, 1, (12, 0), ((12, 0), (12, 16)), 'TextDotPoint', None,vaObject
			, vaPoint)

	def TextDotText(self, vaObject=defaultNamedNotOptArg, vaText=defaultNamedOptArg):
		"""TextDotText"""
		return self._ApplyTypes_(421, 1, (12, 0), ((12, 0), (12, 16)), 'TextDotText', None,vaObject
			, vaText)

	def TextObjectFont(self, vaObject=defaultNamedNotOptArg, vaFont=defaultNamedOptArg):
		"""TextObjectFont"""
		return self._ApplyTypes_(474, 1, (12, 0), ((12, 0), (12, 16)), 'TextObjectFont', None,vaObject
			, vaFont)

	def TextObjectHeight(self, vaObject=defaultNamedNotOptArg, vaSize=defaultNamedOptArg):
		"""TextObjectHeight"""
		return self._ApplyTypes_(473, 1, (12, 0), ((12, 0), (12, 16)), 'TextObjectHeight', None,vaObject
			, vaSize)

	def TextObjectPlane(self, vaObject=defaultNamedNotOptArg, vaPlane=defaultNamedOptArg):
		"""TextObjectPlane"""
		return self._ApplyTypes_(476, 1, (12, 0), ((12, 0), (12, 16)), 'TextObjectPlane', None,vaObject
			, vaPlane)

	def TextObjectPoint(self, vaObject=defaultNamedNotOptArg, vaPoint=defaultNamedOptArg):
		"""TextObjectPoint"""
		return self._ApplyTypes_(471, 1, (12, 0), ((12, 0), (12, 16)), 'TextObjectPoint', None,vaObject
			, vaPoint)

	def TextObjectStyle(self, vaObject=defaultNamedNotOptArg, vaStyle=defaultNamedOptArg):
		"""TextObjectStyle"""
		return self._ApplyTypes_(475, 1, (12, 0), ((12, 0), (12, 16)), 'TextObjectStyle', None,vaObject
			, vaStyle)

	def TextObjectText(self, vaObject=defaultNamedNotOptArg, vaText=defaultNamedOptArg):
		"""TextObjectText"""
		return self._ApplyTypes_(472, 1, (12, 0), ((12, 0), (12, 16)), 'TextObjectText', None,vaObject
			, vaText)

	def TiltView(self, vaView=defaultNamedOptArg, vaDir=defaultNamedOptArg, vaAngle=defaultNamedOptArg):
		"""TiltView"""
		return self._ApplyTypes_(518, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'TiltView', None,vaView
			, vaDir, vaAngle)

	def ToDegrees(self, vaRadians=defaultNamedNotOptArg):
		"""ToDegrees"""
		return self._ApplyTypes_(664, 1, (12, 0), ((12, 0),), 'ToDegrees', None,vaRadians
			)

	def ToRadians(self, vaDegrees=defaultNamedNotOptArg):
		"""ToRadians"""
		return self._ApplyTypes_(665, 1, (12, 0), ((12, 0),), 'ToRadians', None,vaDegrees
			)

	def ToolBarCollectionCount(self):
		"""ToolBarCollectionCount"""
		return self._ApplyTypes_(232, 1, (12, 0), (), 'ToolBarCollectionCount', None,)

	def ToolBarCollectionNames(self, vaPath=defaultNamedOptArg):
		"""ToolBarCollectionNames"""
		return self._ApplyTypes_(234, 1, (12, 0), ((12, 16),), 'ToolBarCollectionNames', None,vaPath
			)

	def ToolBarCollectionPath(self, vaAlias=defaultNamedNotOptArg):
		"""ToolBarCollectionPath"""
		return self._ApplyTypes_(233, 1, (12, 0), ((12, 0),), 'ToolBarCollectionPath', None,vaAlias
			)

	def ToolBarCount(self, vaAlias=defaultNamedNotOptArg):
		"""ToolBarCount"""
		return self._ApplyTypes_(235, 1, (12, 0), ((12, 0),), 'ToolBarCount', None,vaAlias
			)

	def ToolBarNames(self, vaAlias=defaultNamedNotOptArg):
		"""ToolBarNames"""
		return self._ApplyTypes_(236, 1, (12, 0), ((12, 0),), 'ToolBarNames', None,vaAlias
			)

	def TransformObject(self, vaObject=defaultNamedNotOptArg, vaXform=defaultNamedNotOptArg):
		"""TransformObject"""
		return self._ApplyTypes_(272, 1, (12, 0), ((12, 0), (12, 0)), 'TransformObject', None,vaObject
			, vaXform)

	def TransformObjects(self, vaObjects=defaultNamedNotOptArg, vaXform=defaultNamedNotOptArg):
		"""TransformObjects"""
		return self._ApplyTypes_(302, 1, (12, 0), ((12, 0), (12, 0)), 'TransformObjects', None,vaObjects
			, vaXform)

	def TrimCurve(self, vaCrv=defaultNamedNotOptArg, vaInterval=defaultNamedNotOptArg, vaDelete=defaultNamedOptArg):
		"""TrimCurve"""
		return self._ApplyTypes_(505, 1, (12, 0), ((12, 0), (12, 0), (12, 16)), 'TrimCurve', None,vaCrv
			, vaInterval, vaDelete)

	def UnifyMeshNormals(self, vaMesh=defaultNamedNotOptArg):
		"""UnifyMeshNormals"""
		return self._ApplyTypes_(723, 1, (12, 0), ((12, 0),), 'UnifyMeshNormals', None,vaMesh
			)

	def UnitAbsoluteTolerance(self, vaTol=defaultNamedOptArg):
		"""UnitAbsoluteTolerance"""
		return self._ApplyTypes_(324, 1, (12, 0), ((12, 16),), 'UnitAbsoluteTolerance', None,vaTol
			)

	def UnitAngleTolerance(self, vaTol=defaultNamedOptArg):
		"""UnitAngleTolerance"""
		return self._ApplyTypes_(325, 1, (12, 0), ((12, 16),), 'UnitAngleTolerance', None,vaTol
			)

	def UnitCustomUnitSystem(self, vaValue=defaultNamedNotOptArg, vaScale=defaultNamedOptArg, vaName=defaultNamedOptArg):
		"""UnitCustomUnitSystem"""
		return self._ApplyTypes_(326, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'UnitCustomUnitSystem', None,vaValue
			, vaScale, vaName)

	def UnitDistanceDisplayMode(self, vaMode=defaultNamedOptArg):
		"""UnitDistanceDisplayMode"""
		return self._ApplyTypes_(327, 1, (12, 0), ((12, 16),), 'UnitDistanceDisplayMode', None,vaMode
			)

	def UnitDistanceDisplayPrecision(self, vaPrecision=defaultNamedOptArg):
		"""UnitDistanceDisplayPrecision"""
		return self._ApplyTypes_(328, 1, (12, 0), ((12, 16),), 'UnitDistanceDisplayPrecision', None,vaPrecision
			)

	def UnitRelativeTolerance(self, vaTol=defaultNamedOptArg):
		"""UnitRelativeTolerance"""
		return self._ApplyTypes_(329, 1, (12, 0), ((12, 16),), 'UnitRelativeTolerance', None,vaTol
			)

	def UnitSystem(self, vaSystem=defaultNamedOptArg, vaScale=defaultNamedOptArg):
		"""UnitSystem"""
		return self._ApplyTypes_(330, 1, (12, 0), ((12, 16), (12, 16)), 'UnitSystem', None,vaSystem
			, vaScale)

	def UnitSystemName(self, vaCapitalize=defaultNamedOptArg, vaSingular=defaultNamedOptArg, vaAbbreviate=defaultNamedOptArg):
		"""UnitSystemName"""
		return self._ApplyTypes_(492, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'UnitSystemName', None,vaCapitalize
			, vaSingular, vaAbbreviate)

	def UnlockObject(self, vaObject=defaultNamedNotOptArg):
		"""UnlockObject"""
		return self._ApplyTypes_(202, 1, (12, 0), ((12, 0),), 'UnlockObject', None,vaObject
			)

	def UnlockObjects(self, vaObjects=defaultNamedNotOptArg):
		"""UnlockObjects"""
		return self._ApplyTypes_(306, 1, (12, 0), ((12, 0),), 'UnlockObjects', None,vaObjects
			)

	def UnselectAllObjects(self):
		"""UnselectAllObjects"""
		return self._ApplyTypes_(44, 1, (12, 0), (), 'UnselectAllObjects', None,)

	def UnselectObject(self, vaObject=defaultNamedNotOptArg):
		"""UnselectObject"""
		return self._ApplyTypes_(299, 1, (12, 0), ((12, 0),), 'UnselectObject', None,vaObject
			)

	def UnselectObjectGrip(self, vaObject=defaultNamedNotOptArg, vaIndex=defaultNamedNotOptArg):
		"""UnselectObjectGrip"""
		return self._ApplyTypes_(555, 1, (12, 0), ((12, 0), (12, 0)), 'UnselectObjectGrip', None,vaObject
			, vaIndex)

	def UnselectObjectGrips(self, vaObject=defaultNamedNotOptArg):
		"""UnselectObjectGrips"""
		return self._ApplyTypes_(502, 1, (12, 0), ((12, 0),), 'UnselectObjectGrips', None,vaObject
			)

	def UnselectObjects(self, vaObjects=defaultNamedNotOptArg):
		"""UnselectObjects"""
		return self._ApplyTypes_(300, 1, (12, 0), ((12, 0),), 'UnselectObjects', None,vaObjects
			)

	def UnselectedObjects(self, vaSelect=defaultNamedOptArg, vaIncludeLights=defaultNamedOptArg):
		"""UnselectedObjects"""
		return self._ApplyTypes_(45, 1, (12, 0), ((12, 16), (12, 16)), 'UnselectedObjects', None,vaSelect
			, vaIncludeLights)

	def VectorAdd(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorAdd"""
		return self._ApplyTypes_(612, 1, (12, 0), ((12, 0), (12, 0)), 'VectorAdd', None,vaVec0
			, vaVec1)

	def VectorCompare(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorCompare"""
		return self._ApplyTypes_(613, 1, (12, 0), ((12, 0), (12, 0)), 'VectorCompare', None,vaVec0
			, vaVec1)

	def VectorCreate(self, vaPt0=defaultNamedNotOptArg, vaPt1=defaultNamedNotOptArg):
		"""VectorCreate"""
		return self._ApplyTypes_(614, 1, (12, 0), ((12, 0), (12, 0)), 'VectorCreate', None,vaPt0
			, vaPt1)

	def VectorCrossProduct(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorCrossProduct"""
		return self._ApplyTypes_(615, 1, (12, 0), ((12, 0), (12, 0)), 'VectorCrossProduct', None,vaVec0
			, vaVec1)

	def VectorDivide(self, vaVec=defaultNamedNotOptArg, vaScale=defaultNamedNotOptArg):
		"""VectorDivide"""
		return self._ApplyTypes_(625, 1, (12, 0), ((12, 0), (12, 0)), 'VectorDivide', None,vaVec
			, vaScale)

	def VectorDotProduct(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorDotProduct"""
		return self._ApplyTypes_(616, 1, (12, 0), ((12, 0), (12, 0)), 'VectorDotProduct', None,vaVec0
			, vaVec1)

	def VectorLength(self, vaVec=defaultNamedNotOptArg):
		"""VectorLength"""
		return self._ApplyTypes_(617, 1, (12, 0), ((12, 0),), 'VectorLength', None,vaVec
			)

	def VectorMultiply(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorMultiply"""
		return self._ApplyTypes_(624, 1, (12, 0), ((12, 0), (12, 0)), 'VectorMultiply', None,vaVec0
			, vaVec1)

	def VectorReverse(self, vaVec=defaultNamedNotOptArg):
		"""VectorReverse"""
		return self._ApplyTypes_(618, 1, (12, 0), ((12, 0),), 'VectorReverse', None,vaVec
			)

	def VectorRotate(self, vaVec=defaultNamedNotOptArg, vaAngle=defaultNamedNotOptArg, vaAxis=defaultNamedNotOptArg):
		"""VectorRotate"""
		return self._ApplyTypes_(678, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), 'VectorRotate', None,vaVec
			, vaAngle, vaAxis)

	def VectorScale(self, vaVec=defaultNamedNotOptArg, vaScale=defaultNamedNotOptArg):
		"""VectorScale"""
		return self._ApplyTypes_(619, 1, (12, 0), ((12, 0), (12, 0)), 'VectorScale', None,vaVec
			, vaScale)

	def VectorSubtract(self, vaVec0=defaultNamedNotOptArg, vaVec1=defaultNamedNotOptArg):
		"""VectorSubtract"""
		return self._ApplyTypes_(620, 1, (12, 0), ((12, 0), (12, 0)), 'VectorSubtract', None,vaVec0
			, vaVec1)

	def VectorUnitize(self, vaVec=defaultNamedNotOptArg):
		"""VectorUnitize"""
		return self._ApplyTypes_(621, 1, (12, 0), ((12, 0),), 'VectorUnitize', None,vaVec
			)

	def Version(self):
		"""Version"""
		return self._ApplyTypes_(288, 1, (12, 0), (), 'Version', None,)

	def ViewCPlane(self, vaView=defaultNamedOptArg, vaValue=defaultNamedOptArg):
		"""ViewCPlane"""
		return self._ApplyTypes_(264, 1, (12, 0), ((12, 16), (8197, 16)), 'ViewCPlane', None,vaView
			, RhinoUtils.FlattenOnce(vaValue))

	def ViewCamera(self, vaView=defaultNamedOptArg, vaCamera=defaultNamedOptArg):
		"""ViewCamera"""
		return self._ApplyTypes_(394, 1, (12, 0), ((12, 16), (12, 16)), 'ViewCamera', None,vaView
			, vaCamera)

	def ViewCameraLens(self, vaView=defaultNamedOptArg, vaValue=defaultNamedOptArg):
		"""ViewCameraLens"""
		return self._ApplyTypes_(262, 1, (12, 0), ((12, 16), (12, 16)), 'ViewCameraLens', None,vaView
			, vaValue)

	def ViewCameraTarget(self, vaView=defaultNamedOptArg, vaCamera=defaultNamedOptArg, vaTarget=defaultNamedOptArg):
		"""ViewCameraTarget"""
		return self._ApplyTypes_(263, 1, (12, 0), ((12, 16), (12, 16), (12, 16)), 'ViewCameraTarget', None,vaView
			, vaCamera, vaTarget)

	def ViewCameraUp(self, vaView=defaultNamedOptArg, vaUp=defaultNamedOptArg):
		"""ViewCameraUp"""
		return self._ApplyTypes_(517, 1, (12, 0), ((12, 16), (12, 16)), 'ViewCameraUp', None,vaView
			, vaUp)

	def ViewDisplayMode(self, vaView=defaultNamedOptArg, vaMode=defaultNamedOptArg):
		"""ViewDisplayMode"""
		return self._ApplyTypes_(290, 1, (12, 0), ((12, 16), (12, 16)), 'ViewDisplayMode', None,vaView
			, vaMode)

	def ViewNames(self):
		"""ViewNames"""
		return self._ApplyTypes_(265, 1, (12, 0), (), 'ViewNames', None,)

	def ViewProjection(self, vaView=defaultNamedOptArg, vaValue=defaultNamedOptArg):
		"""ViewProjection"""
		return self._ApplyTypes_(266, 1, (12, 0), ((12, 16), (12, 16)), 'ViewProjection', None,vaView
			, vaValue)

	def ViewSize(self, vaView=defaultNamedOptArg):
		"""ViewSize"""
		return self._ApplyTypes_(267, 1, (12, 0), ((12, 16),), 'ViewSize', None,vaView
			)

	def ViewTarget(self, vaView=defaultNamedOptArg, vaTarget=defaultNamedOptArg):
		"""ViewTarget"""
		return self._ApplyTypes_(395, 1, (12, 0), ((12, 16), (12, 16)), 'ViewTarget', None,vaView
			, vaTarget)

	def Wallpaper(self, vaView=defaultNamedOptArg, vaFileName=defaultNamedOptArg, vaHidden=defaultNamedOptArg, vaGrayscale=defaultNamedOptArg):
		"""Wallpaper"""
		return self._ApplyTypes_(532, 1, (12, 0), ((12, 16), (12, 16), (12, 16), (12, 16)), 'Wallpaper', None,vaView
			, vaFileName, vaHidden, vaGrayscale)

	def WallpaperGrayScale(self, vaView=defaultNamedOptArg, vaGrayscale=defaultNamedOptArg):
		"""WallpaperGrayScale"""
		return self._ApplyTypes_(534, 1, (12, 0), ((12, 16), (12, 16)), 'WallpaperGrayScale', None,vaView
			, vaGrayscale)

	def WallpaperHidden(self, vaView=defaultNamedOptArg, vaHidden=defaultNamedOptArg):
		"""WallpaperHidden"""
		return self._ApplyTypes_(533, 1, (12, 0), ((12, 16), (12, 16)), 'WallpaperHidden', None,vaView
			, vaHidden)

	def WindowHandle(self):
		"""WindowHandle"""
		return self._ApplyTypes_(29, 1, (12, 0), (), 'WindowHandle', None,)

	def WorkingFolder(self, vaFolder=defaultNamedOptArg):
		"""WorkingFolder"""
		return self._ApplyTypes_(439, 1, (12, 0), ((12, 16),), 'WorkingFolder', None,vaFolder
			)

	def WorldXYPlane(self):
		"""WorldXYPlane"""
		return self._ApplyTypes_(652, 1, (12, 0), (), 'WorldXYPlane', None,)

	def WorldYZPlane(self):
		"""WorldYZPlane"""
		return self._ApplyTypes_(653, 1, (12, 0), (), 'WorldYZPlane', None,)

	def WorldZXPlane(self):
		"""WorldZXPlane"""
		return self._ApplyTypes_(654, 1, (12, 0), (), 'WorldZXPlane', None,)

	def XFormCPlaneToWorld(self, vaPoint=defaultNamedNotOptArg, vaPlane=defaultNamedNotOptArg):
		"""XFormCPlaneToWorld"""
		return self._ApplyTypes_(131, 1, (12, 0), ((12, 0), (12, 0)), 'XFormCPlaneToWorld', None,vaPoint
			, vaPlane)

	def XFormScreenToWorld(self, vaPoint=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaScreenToClient=defaultNamedOptArg):
		"""XFormScreenToWorld"""
		return self._ApplyTypes_(581, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'XFormScreenToWorld', None,vaPoint
			, vaView, vaScreenToClient)

	def XFormWorldToCPlane(self, vaPoint=defaultNamedNotOptArg, vaPlane=defaultNamedNotOptArg):
		"""XFormWorldToCPlane"""
		return self._ApplyTypes_(132, 1, (12, 0), ((12, 0), (12, 0)), 'XFormWorldToCPlane', None,vaPoint
			, vaPlane)

	def XFormWorldToScreen(self, vaPoint=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaClientToScreen=defaultNamedOptArg):
		"""XFormWorldToScreen"""
		return self._ApplyTypes_(582, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'XFormWorldToScreen', None,vaPoint
			, vaView, vaClientToScreen)

	def ZoomBoundingBox(self, vaCorners=defaultNamedNotOptArg, vaView=defaultNamedOptArg, vaAll=defaultNamedOptArg):
		"""ZoomBoundingBox"""
		return self._ApplyTypes_(479, 1, (12, 0), ((12, 0), (12, 16), (12, 16)), 'ZoomBoundingBox', None,vaCorners
			, vaView, vaAll)

	def ZoomExtents(self, vaView=defaultNamedOptArg, vaAll=defaultNamedOptArg):
		"""ZoomExtents"""
		return self._ApplyTypes_(375, 1, (12, 0), ((12, 16), (12, 16)), 'ZoomExtents', None,vaView
			, vaAll)

	def ZoomSelected(self, vaView=defaultNamedOptArg, vaAll=defaultNamedOptArg):
		"""ZoomSelected"""
		return self._ApplyTypes_(376, 1, (12, 0), ((12, 16), (12, 16)), 'ZoomSelected', None,vaView
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


