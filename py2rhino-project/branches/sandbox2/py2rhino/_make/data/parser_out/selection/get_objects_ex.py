get_objects_ex = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "GetObjectsEx",
    "output_package_name": "selection",
    "output_module_name": "get_objects_ex",

    "doc_html": """
        Prompts the user to pick or select one or more objects.
    """,

    "syntax_html": {
        0: ("strMessage", "intType", "blnGroup", "blnPreSelect", "blnSelect", "arrObjects"),
    },

    "params_html": {
        0: {
            "name": "strMessage",
            "py_name": "message",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "intType",
            "py_name": "type",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Type",
            "doc": """
        The type(s) of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
		Value
		Description
		0
		All objects (default)
		1
		Point
		2
		Point cloud
		4
		Curve
		8
		Surface or single-face brep
		16
		Polysurface or multiple-face
		32
		Mesh
		256
		Light
		512
		Annotation
		4096
		Instance or block reference
		8192
		Text dot object
		16384
		Grip object
		32768
		Detail
		65536
		Hatch
		131072
		Morph control
		134217728
		Cage
		268435456
		Phantom
		536870912
            """
        },
        2: {
            "name": "blnGroup",
            "py_name": "group",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Group",
            "doc": """
        Honor object grouping.  If omitted and the user picks a group, the entire group will be picked (True). Note, if intType is set to a value other than 0 (All objects), then group selection will be disabled.
            """
        },
        3: {
            "name": "blnPreSelect",
            "py_name": "pre_select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "PreSelect",
            "doc": """
        Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
            """
        },
        4: {
            "name": "blnSelect",
            "py_name": "select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Select",
            "doc": """
        Specifies whether or not the picked objects will remain selected when the function ends.  If omitted, objects that were pre-picked will remain selected and the objects that were post-picked will not be selected.
            """
        },
        5: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects that are allowed to be selected.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array that contains arrays of selection information if successful. The array of selection information will contain the following:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 820,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaType",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaGroup",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPreSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        5: {
            "name": "vaObjects",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

