import exceptions
from util import to_array

class Line(object):
    
    def __init__(self, id):
        self.id = id

    def ArrayPolar(self, NumberOfObjects, AngleToFill, CenterPoint):
        """Creates an array of selected objects in a polar pattern."""
        raise exceptions.NotImplementedError()
    
    def ArrayRectangular(self, NumberOfRows, NumberOfColumns, NumberOfLevels, DistBetweenRows, DistBetweenCols, DistBetweenLevels):
        """Creates an array of selected objects in a rectangular pattern."""
        raise exceptions.NotImplementedError()

    def Copy(self, point1, point2):
        """Copies the entity object."""
        return Line(id.Copy(to_array(point1), to_array(point2)))

    def Delete(self):
        """Deletes a specified object"""
        id.Delete()

    def Erase(self):
        """Erases all the objects in a selection set"""
        return None

    def GetBoundingBox(self):
        """Returns the min and max point of the bounding box of the entity object."""
        return None

    def GetExtensionDictionary(self):
        """Gets the extension dictionary associated with an object"""
        return None

    def GetXData(self, AppName):
        """Gets the extended data (XData) associated with an object"""
        return None

    def Highlight(self, HighlightFlag):
        """Highlights the entity object."""
        return None

    def IntersectWith(self, IntersectObject, option):
        """Intersects with the input entity object."""
        raise exceptions.NotImplementedError()

    def Mirror(self, Point1, Point2):
        """Mirrors selected objects about a line."""
        return None

    def Mirror3D(self, Point1, Point2, point3):
        """Mirrors selected objects about a plane defined by three points."""
        return None

    def Move(self, FromPoint, ToPoint):
        """Moves the entity object from source to destination."""
        return None

    def Offset(self, Distance):
        """Creates a new line by offsetting the current line by a specified distance"""
        return None

    def Rotate(self, BasePoint, RotationAngle):
        """Rotates the entity object about a point."""
        return None

    def Rotate3D(self, Point1, Point2, RotationAngle):
        """Rotates the entity object about a 3D line."""
        return None

    def ScaleEntity(self, BasePoint, ScaleFactor):
        """Scale the entity object with respect to the base point and the scale factor."""
        return None

    def SetXData(self, XDataType, XDataValue):
        """Sets the extended data (XData) associated with an object"""
        return None

    def TransformBy(self, TransformationMatrix):
        """Performs the specified transformation on the entity object."""
        return None

    def Update(self):
        """Updates the graphics of the entity object."""
        return None