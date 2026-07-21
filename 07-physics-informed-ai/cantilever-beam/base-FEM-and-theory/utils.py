from pathlib import Path
import numpy as np
from mpi4py import MPI
import dolfinx
from dolfinx.io import gmsh as dgmsh
import gmsh

def extract_boundary_conditions(onelab_vars):
    dirichlet_bcs = {}
    neumann_loads = {}
    
    for var in onelab_vars:
        if var.startswith("BC/"):
            parts = var.split("/")
            if len(parts) >= 3:
                group_name = parts[1]
                comp = parts[2]  # "u_x" or "u_y"
                val = gmsh.onelab.getNumber(var)[0]
                if group_name not in dirichlet_bcs:
                    dirichlet_bcs[group_name] = [None, None]
                if comp == "u_x":
                    dirichlet_bcs[group_name][0] = val
                elif comp == "u_y":
                    dirichlet_bcs[group_name][1] = val
                    
        elif var.startswith("Load/"):
            parts = var.split("/")
            if len(parts) >= 3:
                group_name = parts[1]
                comp = parts[2]  # "t_x" or "t_y"
                val = gmsh.onelab.getNumber(var)[0]
                if group_name not in neumann_loads:
                    neumann_loads[group_name] = [0.0, 0.0]
                if comp == "t_x":
                    neumann_loads[group_name][0] = val
                elif comp == "t_y":
                    neumann_loads[group_name][1] = val
                    
    return dirichlet_bcs, neumann_loads

def load_gmsh_cantilever(geo_path: Path, comm=MPI.COMM_SELF):
    """
    Loads cantilever.geo, parses parameters from ONELAB, generates the mesh,
    and returns (mesh, cell_tags, facet_tags, physical_groups, params, dirichlet_bcs, neumann_loads).
    """
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)
    gmsh.open(str(geo_path))
    
    onelab_vars = gmsh.onelab.getNames()
    params = {}
    
    # Extract material parameters
    for key in ["Material/E", "Material/nu", "Material/mu", "Material/lambda"]:
        if key in onelab_vars:
            params[key.split("/")[-1]] = gmsh.onelab.getNumber(key)[0]
            
    # Extract geometry parameters
    for key in ["Geometry/L", "Geometry/H"]:
        if key in onelab_vars:
            params[key.split("/")[-1]] = gmsh.onelab.getNumber(key)[0]
            
    # Extract BCs
    dirichlet_bcs, neumann_loads = extract_boundary_conditions(onelab_vars)
    
    # Generate 2D mesh
    gmsh.model.mesh.generate(2)
    
    # Import into DOLFINx
    mesh_data = dgmsh.model_to_mesh(gmsh.model, comm, rank=0, gdim=2)
    gmsh.finalize()
    
    return (
        mesh_data.mesh,
        mesh_data.cell_tags,
        mesh_data.facet_tags,
        mesh_data.physical_groups,
        params,
        dirichlet_bcs,
        neumann_loads
    )
