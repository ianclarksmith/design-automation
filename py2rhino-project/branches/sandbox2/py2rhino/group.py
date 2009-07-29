# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Group(p2r._OtherType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_group(cls, ):

        return p2r_f.add_group(self.rhino_id)


    def add_objects(self, objects):

        return p2r_f.add_objects_to_group(objects, self.rhino_id)


    def delete(self, ):

        return p2r_f.delete_group(self.rhino_id)


    def count(self):

        return p2r_f.group_count()


    def names(self):

        return p2r_f.group_names()


    def hide(self, ):

        return p2r_f.hide_group(self.rhino_id)


    def is_empty(self, ):

        return p2r_f.is_group_empty(self.rhino_id)


    def lock(self, ):

        return p2r_f.lock_group(self.rhino_id)


    def remove_object_from_top_group(self, ):

        return p2r_f.remove_object_from_top_group(self.rhino_id)


    def remove_objects(self, objects):

        return p2r_f.remove_objects_from_group(objects, self.rhino_id)


    def rename(self, old_group, new_group):

        return p2r_f.rename_group(old_group, new_group)


    def show(self, ):

        return p2r_f.show_group(self.rhino_id)


    def unlock(self, ):

        return p2r_f.unlock_group(self.rhino_id)

