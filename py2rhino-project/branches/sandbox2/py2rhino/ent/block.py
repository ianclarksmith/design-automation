import pythoncom
from py2rhino import _base

class _BlockModf(object):
    
    def delete(self):
        """
        
        Deletes a block definition and all of it's inserted instances.

        Parameters
        ==========
        None

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DeleteBlock
    
        """
        return _base._rsf.delete_block(self._block._name)
    
class _BlockTest(object):
    
    def is_embedded(self):
        """
        
        Verifies that a block definition is embedded, or linked, from an external file.

        Parameters
        ==========
        None

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsBlockEmbedded
    
        """
        return _base._rsf.is_block_embedded(self._block._name)
    
    def is_in_use(self, where=pythoncom.Empty):
        """
        
        Verifies that a block definition is being used by an inserted instance.

        Parameters
        ==========
        where  (integer, Optional) - Where to look, where:
        0 (Default)
        Check for top level references in active document
        1
        Check for top level and nested references in active document
        2

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsBlockInUse
    
        """
        return _base._rsf.is_block_in_use(self._block._name, where)
    
    def is_reference(self):
        """
        
        Verifies that a block definition is from a reference file.

        Parameters
        ==========
        None

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsBlockReference
    
        """
        return _base._rsf.is_block_reference(self._block._name)


class _BlockProp(object):

    def description(self, text=pythoncom.Empty):
        """
        
        Returns or sets the description of a block definition.

        Parameters
        ==========
        text  (string, Optional) - The new description.  If omitted, the current description is returned.

        Returns
        =======
        string - If a description is not specified,  the current description if successful.
        string - If a description is specified, the previous description if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockDescription
    
        """
        return _base._rsf.block_description(self._block._name, text)
    
    def instance_count(self):
        """
        
        Counts the number of instances of the block in the document.  Nested instances are not included in the count.

        Parameters
        ==========
        None

        Returns
        =======
        number - The number of instances of the block in the document if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockInstanceCount
    
        """
        return _base._rsf.block_instance_count(self._block._name)
    
    def instances(self):
        """
        
        Returns the identifiers of the inserted instances of a block.

        Parameters
        ==========
        None

        Returns
        =======
        list - A list of strings identifying the instances of a block if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockInstances
    
        """
        instance_ids = _base._rsf.block_instances(self._block._name)
        if instance_ids:
            instances = []
            for instance_id in instance_ids:
                instances.append(BlockInstance(instance_id))
            return instances
        else:
            return None
        

    
    def path(self):
        """
        
        Returns the path to the source of a linked or embedded block definition.  A linked or embedded block definition is a block definition that was inserted from an external file.

        Parameters
        ==========
        None

        Returns
        =======
        string - The path to the linked block file is successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockPath
    
        """
        return _base._rsf.block_path(self._block._name)
    
    def url(self, url=pythoncom.Empty):
        """
        
        Returns or sets the URL of a block definition.

        Parameters
        ==========
        url  (string, Optional) - The new URL.  If omitted, the current URL is returned.

        Returns
        =======
        string - If a URL is not specified,  the current URL if successful.
        string - If a URL is specified, the previous URL if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockURL
    
        """
        return _base._rsf.block_u_r_l(self._block._name, url)
    
    def url_tag(self, url=pythoncom.Empty):
        """
        
        Returns or sets the URL tag, or description, of a block definition.

        Parameters
        ==========
        url  (string, Optional) - The new URL tag.  If omitted, the current URL tag is returned.

        Returns
        =======
        string - If a URL tag is not specified,  the current URL tag if successful.
        string - If a URL tag is specified, the previous URL tag if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockURLTag
    
        """
        return _base._rsf.block_u_r_l_tag(self._block._name, url)
    
class _BlockObjs(object):
    
    def rename(self, new_block_name):
        """
        
        Renames an existing block definition.

        Parameters
        ==========
        new_block_name  (string, Required) - The new block definition name.

        Returns
        =======
        string - The new block definition name if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RenameBlock

        """
        name = _base._rsf.rename_block(self._block._name, new_block_name)
        if name:
            self._name = name
            return name
        else:
            return None


    def object_count(self):
        """
        
        Returns the number of objects that make up a block definition.

        Parameters
        ==========
        None

        Returns
        =======
        number - The number of objects that make up the block definition if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockObjectCount
    
        """
        return _base._rsf.block_object_count(self._block._name)
    
    def objects(self):
        """
        
        Returns the identifiers of the objects that make up a block definition.

        Parameters
        ==========
        None

        Returns
        =======
        list - A list of strings identifying the objects that make up a block definition if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockObjects
    
        """
        #TODO: convert these ids to objects
        return _base._rsf.block_objects(self._block._name)

    
class Block(object):
    #--------------------------------------------------------------------------
    # nested classes to hold methods
    
    class objs(_BlockObjs):
        def __init__(self, _block):
            self._block = _block
    class modf(_BlockModf):
        def __init__(self, _block):
            self._block = _block
    class test(_BlockTest):
        def __init__(self, _block):
            self._block = _block            
    class prop(_BlockProp):
        def __init__(self, _block):
            self._block = _block
    #--------------------------------------------------------------------------
    # Class constructor
    def __init__(self, name):
        if name==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._name = name
        
        #create instances of the nested classes
        self.objs = Block.objs(self)
        self.modf = Block.modf(self)
        self.test = Block.test(self)        
        self.prop = Block.prop(self)

class _BlockInstanceFunc(object):
    def explode_instance(self):
    
        """
        
        Explodes a block instance into it's geometric components.  The exploded objects are added to the document.

        Parameters
        ==========
        None

        Returns
        =======
        list - A list of strings identifying the newly exploded objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExplodeBlockInstance
    
        """
        return _base._rsf.explode_block_instance(self._block_instance._rhino_id)  
    
class _BlockInstanceProp(object):
    def instance_insert_point(self):
    
        """
        
        Returns the insertion point of a block instance.

        Parameters
        ==========
        None

        Returns
        =======
        list - A 3-D point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockInstanceInsertPoint
    
        """
        return _base._rsf.block_instance_insert_point(self._block_instance._rhino_id)
    
    def instance_name(self):
    
        """
        
        Returns the block name of a block instance.

        Parameters
        ==========
        None

        Returns
        =======
        string - The block name if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockInstanceName
    
        """
        return _base._rsf.block_instance_name(self._block_instance._rhino_id)
    
    def instance_xform(self):
    
        """
        
        Returns the location of a block instance relative to the world coordinate system origin (0,0,0).  The position is returned as a 4x4 transformation matrix

        Parameters
        ==========
        None

        Returns
        =======
        list - A transformation matrix (4x4 list of numbers) if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockInstanceXform
    
        """
        return _base._rsf.block_instance_xform(self._block_instance._rhino_id)
    
class BlockInstance(object):    
    #TODO: should a block instance be part of the object hierarchy????
    
    #--------------------------------------------------------------------------
    # nested classes to hold methods
          
    class prop(_BlockInstanceProp):
        def __init__(self, _block_instance):
            self._block_instance = _block_instance
    class func(_BlockInstanceFunc):
        def __init__(self, _block_instance):
            self._block_instance = _block_instance
    
    #--------------------------------------------------------------------------
    # Class constructor
    def __init__(self, rhino_id):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = rhino_id

        #create instances of the nested classes
        self.prop = BlockInstance.prop(self)
        self.func = BlockInstance.func(self)        
    #--------------------------------------------------------------------------
    @staticmethod
    def create(block, insertion_point, scale=pythoncom.Empty, angle=pythoncom.Empty, normal=pythoncom.Empty):
    
        """
        
        Inserts a block whose definition already exists in the document.

        Parameters
        ==========
        block_name  (string, Required) - The name of the block definition to insert.
        insertion_point  (List of float, Required) - The 3-D insertion point of the block.
        scale  (List of float, Optional) - An list of three numbers that identify the x,y,z scale factors. If omitted, the block is not scaled.
        angle  (float, Optional) - The rotation angle in degrees. If omitted, the block is not rotated.
        normal  (List of float, Optional) - A 3-D vector identifying the axis of rotation. If omitted and dblAngle is specified, the world Z axis is used.

        Returns
        =======
        string - The newly inserted block instance, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: InsertBlock
    
        """
        block_id = _base._rsf.insert_block(block._name, insertion_point, scale, angle, normal)
        return BlockInstance(block_id)
    
    @staticmethod
    def create_by_xform(block, xform):
    
        """
        
        Inserts a block whose definition already exists in the document.

        Parameters
        ==========
        block_name  (string, Required) - The name of the block definition to insert.
        xform  (List of float, Required) - 4x4 transformation matrix to apply.

        Returns
        =======
        string - The newly inserted block instance, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: InsertBlock
    
        """
        block_id = _base._rsf.insert_block_2(block._name, xform)
        return BlockInstance(block_id)
    

    
 