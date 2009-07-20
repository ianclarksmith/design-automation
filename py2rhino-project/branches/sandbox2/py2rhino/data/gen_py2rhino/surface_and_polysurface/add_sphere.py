add_sphere = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "add_sphere",

    "doc_html": """
        Adds a spherical surface to the document.
    """,

    "syntax_html": """
        Rhino.AddSphere (arrCenter, dblRadius)
    """,

    "params_html": {
        0: {
            "name": "Center",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The center point of the sphere.
            """
        },
        1: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An equatorial plane.  The origin of the plane will be the center point of the sphere.
            """
        },
        2: {
            "name": "Radius",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The radius of the sphere in current model units.
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

    "id_com": 71,

    "params_com": {
        0: {
            "name": "vaCenter",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRadius",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

