add_cut_plane = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddCutPlane",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_cut_plane",

    "doc_html": """
        Adds a planar surface through objects at a designated location.  For more information, see the Rhino help file for the CutPlane command.
    """,

    "syntax_html": """
        Rhino.AddCutPlane (arrObjects, arrStartPoint, arrEndPoint [, arrNormal])
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_str",
            "doc": """
        The identifiers of objects that the cutting planes will pass through.
            """
        },
        1: {
            "name": "StartPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The start of the line that defines the cutting plane.
            """
        },
        2: {
            "name": "EndPoint",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "arr_of_dbl",
            "doc": """
        The end of the line that defines the cutting plane.
            """
        },
        3: {
            "name": "Normal",
            "opt_or_req": "Optional",
            "type": "A vector that will be contained in the returned planar surface",
            "type_string": "arr_of_dbl",
            "doc": """
        In the case of Rhino's CutPlane command, this is the normal to, or Z axis of, the active view's construction plane.  If omitted, the world Z axis is used.
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

    "id_com": 822,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStart",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaEnd",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

