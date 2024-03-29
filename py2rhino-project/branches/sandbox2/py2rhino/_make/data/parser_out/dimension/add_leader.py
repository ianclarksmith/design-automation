add_leader = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "AddLeader",
    "output_package_name": "dimension",
    "output_module_name": "add_leader",

    "doc_html": """
        Adds an annotation leader to the document. Leader objects are planar. The array of 3-D points passed to this member should be co-planar.
    """,

    "syntax_html": {
        0: ("arrPoints", "strView", "strText"),
    },

    "params_html": {
        0: {
            "name": "arrPoints",
            "py_name": "points",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array of 3-D points.  The array must contain at least two points.
            """
        },
        1: {
            "name": "strView",
            "py_name": "view",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        The title of the view.  If a view title is specified,  arrPoints will be constrained to the view's construction plane. If a view title is not specified, arrPoints will be constrained to a plane fit through the array of points.
            """
        },
        2: {
            "name": "strText",
            "py_name": "text",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Text",
            "doc": """
        The leader's text string.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 321,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaText",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

