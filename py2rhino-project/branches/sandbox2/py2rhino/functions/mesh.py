# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_mesh(vertices, face_vertices, vertex_normals=pythoncom.Empty, texture_coordinates=pythoncom.Empty, vertex_colors=pythoncom.Empty):

    return _rsf.add_mesh(vertices, face_vertices, vertex_normals, texture_coordinates, vertex_colors)

def add_planar_mesh(object, delete):

    return _rsf.add_planar_mesh(object, delete)

def curve_mesh_intersection(curve, mesh, return_faces=pythoncom.Empty):

    return _rsf.curve_mesh_intersection(curve, mesh, return_faces)

def disjoint_mesh_count(object):

    return _rsf.disjoint_mesh_count(object)

def duplicate_mesh_border(object):

    return _rsf.duplicate_mesh_border(object)

def explode_meshes(objects, delete=pythoncom.Empty):

    return _rsf.explode_meshes(objects, delete)

def is_mesh(object):

    return _rsf.is_mesh(object)

def is_mesh_closed(object):

    return _rsf.is_mesh_closed(object)

def is_mesh_manifold(object):

    return _rsf.is_mesh_manifold(object)

def mesh_area(objects):

    return _rsf.mesh_area(objects)

def mesh_area_centroid(object):

    return _rsf.mesh_area_centroid(object)

def mesh_boolean_difference(input_0, input_1, delete=pythoncom.Empty):

    return _rsf.mesh_boolean_difference(input_0, input_1, delete)

def mesh_boolean_intersection(input_0, input_1, delete=pythoncom.Empty):

    return _rsf.mesh_boolean_intersection(input_0, input_1, delete)

def mesh_boolean_split(input_0, input_1, delete=pythoncom.Empty):

    return _rsf.mesh_boolean_split(input_0, input_1, delete)

def mesh_boolean_union(input, delete=pythoncom.Empty):

    return _rsf.mesh_boolean_union(input, delete)

def mesh_closest_point(object, point, tolerance=pythoncom.Empty):

    return _rsf.mesh_closest_point(object, point, tolerance)

def mesh_contour_points(object, start_point, end_point, interval=pythoncom.Empty, remove_coincident_points=pythoncom.Empty):

    return _rsf.mesh_contour_points(object, start_point, end_point, interval, remove_coincident_points)

def mesh_face_centers(object):

    return _rsf.mesh_face_centers(object)

def mesh_face_count(object):

    return _rsf.mesh_face_count(object)

def mesh_face_normals(object):

    return _rsf.mesh_face_normals(object)

def mesh_face_vertices(object):

    return _rsf.mesh_face_vertices(object)

def mesh_faces(object, face_type=pythoncom.Empty):

    return _rsf.mesh_faces(object, face_type)

def mesh_has_face_normals(object):

    return _rsf.mesh_has_face_normals(object)

def mesh_has_texture_coordinates(object):

    return _rsf.mesh_has_texture_coordinates(object)

def mesh_has_vertex_colors(object):

    return _rsf.mesh_has_vertex_colors(object)

def mesh_has_vertex_normals(object):

    return _rsf.mesh_has_vertex_normals(object)

def mesh_mesh_intersection(mesh_1, mesh_2, tolerance=pythoncom.Empty):

    return _rsf.mesh_mesh_intersection(mesh_1, mesh_2, tolerance)

def mesh_naked_edge_points(object):

    return _rsf.mesh_naked_edge_points(object)

def mesh_offset(mesh, distance):

    return _rsf.mesh_offset(mesh, distance)

def mesh_quad_count(object):

    return _rsf.mesh_quad_count(object)

def mesh_quads_to_triangles(object):

    return _rsf.mesh_quads_to_triangles(object)

def mesh_texture_coordinates(object):

    return _rsf.mesh_texture_coordinates(object)

def mesh_triangle_count(object):

    return _rsf.mesh_triangle_count(object)

def mesh_vertex_colors(object, vertex_colors=pythoncom.Empty):

    return _rsf.mesh_vertex_colors(object, vertex_colors)

def mesh_vertex_count(object):

    return _rsf.mesh_vertex_count(object)

def mesh_vertex_normals(object):

    return _rsf.mesh_vertex_normals(object)

def mesh_vertices(object):

    return _rsf.mesh_vertices(object)

def mesh_volume(objects):

    return _rsf.mesh_volume(objects)

def mesh_volume_centroid(object):

    return _rsf.mesh_volume_centroid(object)

def pull_curve_to_mesh(mesh, curve):

    return _rsf.pull_curve_to_mesh(mesh, curve)

def split_disjoint_mesh(object, delete=pythoncom.Empty):

    return _rsf.split_disjoint_mesh(object, delete)

def unify_mesh_normals(object):

    return _rsf.unify_mesh_normals(object)

