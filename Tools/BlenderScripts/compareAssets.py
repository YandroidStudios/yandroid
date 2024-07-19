import bpy
import bmesh

# Author: Squirrel Modeller
# Tools utilized: ChatGPT 4
# Able to check nodes like RGB, principled BSDF. Fails upon checking sockets same type like multiple color sockets.

def is_iterable(value):
    """Check if the value is iterable but not a string."""
    try:
        iter(value)
        return not isinstance(value, str)
    except TypeError:
        return False

def calculate_vertex_similarity(obj1, obj2):
    """Calculate the similarity between vertices of two objects based on their local coordinates."""
    bm1 = bmesh.new()
    bm2 = bmesh.new()
    bm1.from_mesh(obj1.data)
    bm2.from_mesh(obj2.data)
    bm1.verts.ensure_lookup_table()
    bm2.verts.ensure_lookup_table()

    verts1_local = [v.co for v in bm1.verts]
    verts2_local = [v.co for v in bm2.verts]
    matching_verts_count = sum(1 for v1 in verts1_local if v1 in verts2_local)
    total_verts = len(verts1_local) + len(verts2_local)
    similarity_percentage = (matching_verts_count * 2) / total_verts * 100 if total_verts > 0 else 0

    bm1.free()
    bm2.free()
    return similarity_percentage

def compare_materials(obj1, obj2):
    """Compare materials of two objects for similarity."""
    if len(obj1.data.materials) != len(obj2.data.materials):
        print("Number of materials does not match.")
        return False

    for mat1, mat2 in zip(obj1.data.materials, obj2.data.materials):
        if mat1.use_nodes != mat2.use_nodes or not compare_nodes(mat1.node_tree.nodes, mat2.node_tree.nodes):
            print(f"Material '{mat1.name}' and '{mat2.name}' nodes do not match.")
            return False
    return True

def compare_nodes(nodes1, nodes2):
    """Compare nodes of two materials for similarity."""
    differences_found = False
    if len(nodes1) != len(nodes2):
        print("Node count does not match.")
        differences_found = True

    for node1, node2 in zip(sorted(nodes1, key=lambda x: x.type), sorted(nodes2, key=lambda x: x.type)):
        if node1.type != node2.type:
            print(f"Node type mismatch: {node1.type} vs {node2.type}")
            differences_found = True
            continue

        for input1, input2 in zip(node1.inputs, node2.inputs):
            if input1.type != input2.type or not compare_socket_values(input1, input2):
                differences_found = True

    return not differences_found

def compare_socket_values(input1, input2):
    """Compare values of two sockets for similarity."""
    if hasattr(input1, 'default_value') and hasattr(input2, 'default_value'):
        value1 = input1.default_value
        value2 = input2.default_value
        if is_iterable(value1) and is_iterable(value2):
            if tuple(value1) != tuple(value2):
                print(f"Difference found in '{input1.name}' values: {tuple(value1)} vs {tuple(value2)}")
                return False
        else:
            if value1 != value2:
                print(f"Difference found in '{input1.name}' values: {value1} vs {value2}")
                return False
    return True

def compare_selected_objects():
    """Compare selected objects for vertex similarity and material properties."""
    selected_objects = bpy.context.selected_objects
    if len(selected_objects) != 2:
        print("Please select exactly two objects.")
        return

    obj1, obj2 = selected_objects
    similarity = calculate_vertex_similarity(obj1, obj2)
    print(f"Vertex similarity percentage: {similarity:.2f}%")

    if compare_materials(obj1, obj2):
        print("Materials match in terms of nodes and properties.")
    else:
        print("Materials do not match.")

# Run the comparison
compare_selected_objects()
