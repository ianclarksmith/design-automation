get_box = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetBox",
    "output_package_name": "user_interface",
    "output_module_name": "get_box",

    "doc_html": """
        Pauses for user input of a box.
    """,

    "syntax_html": {
        0: ("intMode", "arrPoint", "strPrompt1", "strPrompt2", "strPrompt3"),
    },

    "params_html": {
        0: {
            "name": "intMode",
            "py_name": "mode",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Mode",
            "doc": """
        The box selection mode.  If not specified, all modes (0) are available.  The box selection modes are as follows:
		Value
		Description
		0
		All modes.
		1
		Corner.  The base rectangle is created by picking two corner points.
		2
		3-Point.  The base rectangle is created by picking three points
		3
		Vertical.  The base vertical rectangle is created by picking three points.
		4
            """
        },
        1: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D base point.
            """
        },
        2: {
            "name": "strPrompt1",
            "py_name": "prompt1",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Prompt1",
            "doc": """
        The first prompt or message.
            """
        },
        3: {
            "name": "strPrompt2",
            "py_name": "prompt2",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Prompt2",
            "doc": """
        The second prompt or message.
            """
        },
        4: {
            "name": "strPrompt3",
            "py_name": "prompt3",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Prompt3",
            "doc": """
        The third prompt or message.  The third prompt used only with 3Point and Vertical modes.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of eight 3-D points that define the corners of the box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 342,

    "params_com": {
        0: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPrompt1",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPrompt2",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaPrompt3",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

