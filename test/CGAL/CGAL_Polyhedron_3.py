# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""SWIG wrapper for the CGAL 3D Polyhedron package provided under the GPL-3.0+ license"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
# import CGAL_Polyhedron_3PYTHON_wrap.cxx
# from Release import CGAL_Polyhedron_3
if __package__ or "." in __name__:
    from . import _CGAL_Polyhedron_3
else:
    import _CGAL_Polyhedron_3

import builtins as __builtin__
# try:
#     import builtins as __builtin__
# except ImportError:
#     import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import CGAL.CGAL_Kernel
class Polyhedron_3_Modifier_base(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Modifier_base_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Modifier_base())
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Modifier_base

# Register Polyhedron_3_Modifier_base in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Modifier_base_swigregister(Polyhedron_3_Modifier_base)

class Polyhedron_3_Modifier_1(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def get_modifier(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Modifier_1_get_modifier(self)

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Modifier_1_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Modifier_1())
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Modifier_1

# Register Polyhedron_3_Modifier_1 in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Modifier_1_swigregister(Polyhedron_3_Modifier_1)

class Polyhedron_3_Modifier_2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def get_modifier(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Modifier_2_get_modifier(self)

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Modifier_2_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Modifier_2())
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Modifier_2

# Register Polyhedron_3_Modifier_2 in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Modifier_2_swigregister(Polyhedron_3_Modifier_2)

RELATIVE_INDEXING = _CGAL_Polyhedron_3.RELATIVE_INDEXING
ABSOLUTE_INDEXING = _CGAL_Polyhedron_3.ABSOLUTE_INDEXING
class Polyhedron_3_Halfedge_handle(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Halfedge_handle())

    def opposite(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_opposite(self, *args)

    def next(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_next(self, *args)

    def prev(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_prev(self, *args)

    def next_on_vertex(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_next_on_vertex(self, *args)

    def prev_on_vertex(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_prev_on_vertex(self, *args)

    def is_border(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_is_border(self)

    def is_border_edge(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_is_border_edge(self)

    def vertex_begin(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_vertex_begin(self)

    def facet_begin(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_facet_begin(self)

    def vertex_degree(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_vertex_degree(self)

    def is_bivalent(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_is_bivalent(self)

    def is_trivalent(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_is_trivalent(self)

    def facet_degree(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_facet_degree(self)

    def is_triangle(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_is_triangle(self)

    def is_quad(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_is_quad(self)

    def vertex(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_vertex(self, *args)

    def facet(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_facet(self, *args)

    def __lt__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle___lt__(self, p)

    def __gt__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle___gt__(self, p)

    def __le__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle___le__(self, p)

    def __ge__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle___ge__(self, p)

    def __eq__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle___ne__(self, p)

    def __hash__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle___hash__(self)

    def id(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_id(self)

    def set_id(self, i):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_set_id(self, i)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_deepcopy(self, *args)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Halfedge_handle

# Register Polyhedron_3_Halfedge_handle in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Halfedge_handle_swigregister(Polyhedron_3_Halfedge_handle)

class Polyhedron_3_Vertex_handle(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Vertex_handle())

    def point(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_point(self, *args)

    def halfedge(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_halfedge(self, *args)

    def vertex_begin(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_vertex_begin(self)

    def set_halfedge(self, c):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_set_halfedge(self, c)

    def vertex_degree(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_vertex_degree(self)

    def is_bivalent(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_is_bivalent(self)

    def is_trivalent(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_is_trivalent(self)

    def __lt__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle___lt__(self, p)

    def __gt__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle___gt__(self, p)

    def __le__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle___le__(self, p)

    def __ge__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle___ge__(self, p)

    def __eq__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle___ne__(self, p)

    def __hash__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle___hash__(self)

    def id(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_id(self)

    def set_id(self, i):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_set_id(self, i)

    def set_point(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_set_point(self, p)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_deepcopy(self, *args)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Vertex_handle

# Register Polyhedron_3_Vertex_handle in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Vertex_handle_swigregister(Polyhedron_3_Vertex_handle)

class Polyhedron_3_Facet_handle(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Facet_handle())

    def halfedge(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_halfedge(self, *args)

    def facet_begin(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_facet_begin(self)

    def set_halfedge(self, c):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_set_halfedge(self, c)

    def facet_degree(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_facet_degree(self)

    def is_triangle(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_is_triangle(self)

    def is_quad(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_is_quad(self)

    def __lt__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle___lt__(self, p)

    def __gt__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle___gt__(self, p)

    def __le__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle___le__(self, p)

    def __ge__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle___ge__(self, p)

    def __eq__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle___ne__(self, p)

    def __hash__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle___hash__(self)

    def id(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_id(self)

    def set_id(self, i):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_set_id(self, i)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_deepcopy(self, *args)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Facet_handle

# Register Polyhedron_3_Facet_handle in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Facet_handle_swigregister(Polyhedron_3_Facet_handle)

class Polyhedron_3(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _CGAL_Polyhedron_3.Polyhedron_3_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3(*args))

    def reserve(self, c1, c2, c3):
        return _CGAL_Polyhedron_3.Polyhedron_3_reserve(self, c1, c2, c3)

    def make_tetrahedron(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_make_tetrahedron(self, *args)

    def make_triangle(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_make_triangle(self, *args)

    def empty(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_empty(self)

    def size_of_vertices(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_size_of_vertices(self)

    def size_of_halfedges(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_size_of_halfedges(self)

    def size_of_facets(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_size_of_facets(self)

    def capacity_of_vertices(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_capacity_of_vertices(self)

    def capacity_of_halfedges(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_capacity_of_halfedges(self)

    def capacity_of_facets(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_capacity_of_facets(self)

    def bytes(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_bytes(self)

    def bytes_reserved(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_bytes_reserved(self)

    def vertices(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_vertices(self)

    def halfedges(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_halfedges(self)

    def facets(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_facets(self)

    def edges(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_edges(self)

    def points(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_points(self)

    def is_closed(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_is_closed(self)

    def is_pure_bivalent(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_is_pure_bivalent(self)

    def is_pure_trivalent(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_is_pure_trivalent(self)

    def is_pure_triangle(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_is_pure_triangle(self)

    def is_pure_quad(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_is_pure_quad(self)

    def is_triangle(self, c):
        return _CGAL_Polyhedron_3.Polyhedron_3_is_triangle(self, c)

    def is_tetrahedron(self, c):
        return _CGAL_Polyhedron_3.Polyhedron_3_is_tetrahedron(self, c)

    def split_facet(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_split_facet(self, *args)

    def join_facet(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_join_facet(self, *args)

    def split_vertex(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_split_vertex(self, *args)

    def join_vertex(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_join_vertex(self, *args)

    def split_edge(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_split_edge(self, *args)

    def flip_edge(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_flip_edge(self, *args)

    def create_center_vertex(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_create_center_vertex(self, *args)

    def erase_center_vertex(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_erase_center_vertex(self, *args)

    def split_loop(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_split_loop(self, *args)

    def join_loop(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_join_loop(self, *args)

    def make_hole(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_make_hole(self, *args)

    def fill_hole(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_fill_hole(self, *args)

    def add_vertex_and_facet_to_border(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_add_vertex_and_facet_to_border(self, *args)

    def add_facet_to_border(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_add_facet_to_border(self, *args)

    def erase_facet(self, c):
        return _CGAL_Polyhedron_3.Polyhedron_3_erase_facet(self, c)

    def erase_connected_component(self, c):
        return _CGAL_Polyhedron_3.Polyhedron_3_erase_connected_component(self, c)

    def keep_largest_connected_components(self, c):
        return _CGAL_Polyhedron_3.Polyhedron_3_keep_largest_connected_components(self, c)

    def clear(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_clear(self)

    def normalize_border(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_normalize_border(self)

    def size_of_border_halfedges(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_size_of_border_halfedges(self)

    def size_of_border_edges(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_size_of_border_edges(self)

    def border_halfedges(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_border_halfedges(self)

    def non_border_halfedges(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_non_border_halfedges(self)

    def border_edges(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_border_edges(self)

    def non_border_edges(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_non_border_edges(self)

    def inside_out(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_inside_out(self)

    def is_valid(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_is_valid(self)

    def normalized_border_is_valid(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_normalized_border_is_valid(self)

    def delegate(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_delegate(self, *args)

    def write_to_file(self, off_filename, prec=5):
        return _CGAL_Polyhedron_3.Polyhedron_3_write_to_file(self, off_filename, prec)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_deepcopy(self, *args)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3

# Register Polyhedron_3 in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_swigregister(Polyhedron_3)

class Polyhedron_modifier(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_modifier_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_modifier())

    def begin_surface(self, v, f, h=0, mode=RELATIVE_INDEXING):
        return _CGAL_Polyhedron_3.Polyhedron_modifier_begin_surface(self, v, f, h, mode)

    def end_surface(self):
        return _CGAL_Polyhedron_3.Polyhedron_modifier_end_surface(self)

    def add_vertex(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_modifier_add_vertex(self, p)

    def begin_facet(self):
        return _CGAL_Polyhedron_3.Polyhedron_modifier_begin_facet(self)

    def end_facet(self):
        return _CGAL_Polyhedron_3.Polyhedron_modifier_end_facet(self)

    def add_vertex_to_facet(self, i):
        return _CGAL_Polyhedron_3.Polyhedron_modifier_add_vertex_to_facet(self, i)

    def rollback(self):
        return _CGAL_Polyhedron_3.Polyhedron_modifier_rollback(self)

    def clear(self):
        return _CGAL_Polyhedron_3.Polyhedron_modifier_clear(self)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_modifier

# Register Polyhedron_modifier in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_modifier_swigregister(Polyhedron_modifier)

class Polyhedron_3_Halfedge_iterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_iterator_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Halfedge_iterator())

    def __iter__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_iterator___iter__(self)

    def __next__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_iterator___next__(self)

    def next(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_iterator_next(self, *args)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_iterator_deepcopy(self, *args)

    def hasNext(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_iterator_hasNext(self)

    def __eq__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_iterator___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_iterator___ne__(self, p)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Halfedge_iterator

# Register Polyhedron_3_Halfedge_iterator in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Halfedge_iterator_swigregister(Polyhedron_3_Halfedge_iterator)

class Polyhedron_3_Edge_iterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Edge_iterator_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Edge_iterator())

    def __iter__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Edge_iterator___iter__(self)

    def __next__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Edge_iterator___next__(self)

    def next(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Edge_iterator_next(self, *args)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Edge_iterator_deepcopy(self, *args)

    def hasNext(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Edge_iterator_hasNext(self)

    def __eq__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Edge_iterator___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Edge_iterator___ne__(self, p)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Edge_iterator

# Register Polyhedron_3_Edge_iterator in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Edge_iterator_swigregister(Polyhedron_3_Edge_iterator)

class Polyhedron_3_Vertex_iterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Vertex_iterator_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Vertex_iterator())

    def __iter__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_iterator___iter__(self)

    def __next__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_iterator___next__(self)

    def next(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_iterator_next(self, *args)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_iterator_deepcopy(self, *args)

    def hasNext(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_iterator_hasNext(self)

    def __eq__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_iterator___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Vertex_iterator___ne__(self, p)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Vertex_iterator

# Register Polyhedron_3_Vertex_iterator in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Vertex_iterator_swigregister(Polyhedron_3_Vertex_iterator)

class Polyhedron_3_Facet_iterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Facet_iterator_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Facet_iterator())

    def __iter__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_iterator___iter__(self)

    def __next__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_iterator___next__(self)

    def next(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_iterator_next(self, *args)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_iterator_deepcopy(self, *args)

    def hasNext(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_iterator_hasNext(self)

    def __eq__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_iterator___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Facet_iterator___ne__(self, p)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Facet_iterator

# Register Polyhedron_3_Facet_iterator in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Facet_iterator_swigregister(Polyhedron_3_Facet_iterator)

class Polyhedron_3_Point_iterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Point_iterator_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Point_iterator())

    def __iter__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Point_iterator___iter__(self)

    def __next__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Point_iterator___next__(self)

    def next(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Point_iterator_next(self, *args)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Point_iterator_deepcopy(self, *args)

    def hasNext(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Point_iterator_hasNext(self)

    def __eq__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Point_iterator___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Point_iterator___ne__(self, p)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Point_iterator

# Register Polyhedron_3_Point_iterator in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Point_iterator_swigregister(Polyhedron_3_Point_iterator)

class Polyhedron_3_Halfedge_around_vertex_circulator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_vertex_circulator_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Halfedge_around_vertex_circulator())

    def __iter__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_vertex_circulator___iter__(self)

    def next(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_vertex_circulator_next(self)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_vertex_circulator_deepcopy(self, *args)

    def prev(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_vertex_circulator_prev(self)

    def hasNext(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_vertex_circulator_hasNext(self)

    def __eq__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_vertex_circulator___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_vertex_circulator___ne__(self, p)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Halfedge_around_vertex_circulator

# Register Polyhedron_3_Halfedge_around_vertex_circulator in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_vertex_circulator_swigregister(Polyhedron_3_Halfedge_around_vertex_circulator)

class Polyhedron_3_Halfedge_around_facet_circulator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_facet_circulator_swiginit(self, _CGAL_Polyhedron_3.new_Polyhedron_3_Halfedge_around_facet_circulator())

    def __iter__(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_facet_circulator___iter__(self)

    def next(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_facet_circulator_next(self)

    def deepcopy(self, *args):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_facet_circulator_deepcopy(self, *args)

    def prev(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_facet_circulator_prev(self)

    def hasNext(self):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_facet_circulator_hasNext(self)

    def __eq__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_facet_circulator___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_facet_circulator___ne__(self, p)
    __swig_destroy__ = _CGAL_Polyhedron_3.delete_Polyhedron_3_Halfedge_around_facet_circulator

# Register Polyhedron_3_Halfedge_around_facet_circulator in _CGAL_Polyhedron_3:
_CGAL_Polyhedron_3.Polyhedron_3_Halfedge_around_facet_circulator_swigregister(Polyhedron_3_Halfedge_around_facet_circulator)



