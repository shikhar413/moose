# ==============================================================================
# Global Variables
# ==============================================================================
# These global variables control geometrical parameters of the heterogeneous mesh
fuel_pin_pitch = 0.908             # Pin pitch of fuel pin
fuel_clad_r_i = 0.348              # Inner radius of fuel pin cladding
fuel_clad_r_o = 0.40333            # Outer radius of fuel pin cladding
duct_pitch_inner = 13.598          # Inner pitch of fuel assembly duct region
duct_pitch_outer = 14.198          # Outer pitch of fuel assembly duct region
assembly_pitch = 14.598            # Assembly pitch

# These global variables control the placement of axial levels in the extruded mesh
z_active_core_lower = 60
z_active_core_upper = 140
z_sodium_gp_upper = 160
z_gp_upper = 260

# These global variables control the size of each axial layer
dz_active_core_lower = '${fparse z_active_core_lower - 0}'
dz_active_core_upper = '${fparse z_active_core_upper - z_active_core_lower}'
dz_sodium_gp_upper = '${fparse z_sodium_gp_upper - z_active_core_upper}'
dz_gp_upper = '${fparse z_gp_upper - z_sodium_gp_upper}'

# These global variables control how many intervals are in each axial layer. Here, a
# maximum axial mesh size of 20cm is assumed for each axial subinterval
max_axial_mesh_size = 20
naxial_active_core_lower = '${fparse ceil(dz_active_core_lower / max_axial_mesh_size)}'
naxial_active_core_upper = '${fparse ceil(dz_active_core_upper / max_axial_mesh_size)}'
naxial_sodium_gp_upper = '${fparse ceil(dz_sodium_gp_upper / max_axial_mesh_size)}'
naxial_gp_upper = '${fparse ceil(dz_gp_upper / max_axial_mesh_size)}'

# These global variables assign a region ID to each region in the core
# RGMB uses these region IDs to assign the `region_id` extra element integer
mid_fuel_1 = 1           # Fuel region of fuel_pin_1
mid_ht9 = 5              # HT-9 steel region of cladding
mid_sodium = 6           # Sodium region of background
mid_lower_refl = 9       # Lower reflector region
mid_upper_na_plen = 10   # Sodium plenum region
mid_upper_gas_plen = 11  # Gas plenum region

[Mesh]
  [rmp]
    type = ReactorMeshParams
    dim = 3                               # Dimensionality of output mesh (2 or 3)
    geom = "Hex"                          # Geometry type (Hex or Square)
    assembly_pitch = ${assembly_pitch}    # # Size of assembly flat-to-flat pitch

    axial_regions = '${dz_active_core_lower}
                     ${dz_active_core_upper}
                     ${dz_sodium_gp_upper}
                     ${dz_gp_upper}'                    # Size of each axial zone
    axial_mesh_intervals = '${naxial_active_core_lower}
                            ${naxial_active_core_upper}
                            ${naxial_sodium_gp_upper}
                            ${naxial_gp_upper}'         # Number of subintervals per axial zone
    top_boundary_id = 201                               # Boundary ID assigned to top surface
    bottom_boundary_id = 202                            # Boundary ID assigned to bottom surface
    radial_boundary_id = 203                            # Boundary ID assigned to radial surface
    flexible_assembly_stitching = true                  # Set to true to stitch dissimilar assembly types together,
                                                        # i.e. homogeneous and heterogeneous assemblies
  []

  ### Step 1. Define pin mesh structures to stitch into fuel / control assemblies
  [fuel_pin_1]
    type = PinMeshGenerator
    reactor_params = rmp                              # Name of ReactorMeshParams object
    pin_type = 1                                      # Unique identifier for pin type
    pitch = ${fuel_pin_pitch}                         # Pin pitch
    num_sectors = 2                                   # Number of azimuthal sectors per hexagonal side
    quad_center_elements = false                      # Whether central mesh elements in inner ring should use
                                                      # quad elements (true) or tri elements (false)
    ring_radii = '${fuel_clad_r_i} ${fuel_clad_r_o}'  # Radii for each ring
    mesh_intervals = '1 1 1'                          # Number of radial intervals for each radial region
                                                      # (inner ring, outer ring, background)
    region_ids = '${mid_lower_refl}     ${mid_lower_refl}     ${mid_lower_refl};
                  ${mid_fuel_1}         ${mid_ht9}            ${mid_sodium};
                  ${mid_upper_na_plen}  ${mid_upper_na_plen}  ${mid_upper_na_plen};
                  ${mid_upper_gas_plen} ${mid_upper_gas_plen} ${mid_upper_gas_plen}' # Region IDs for each radial region (inner ring, outer ring, background),
                                                                                     # provided for each axial layer from bottom to top
  []
  ### Step 2. Define assembly mesh structures for fuel and control assemblies
  [fuel_assembly_1]
    type = AssemblyMeshGenerator
    assembly_type = 1                              # Unique identifier for pin type

    background_intervals = 1                       # Number of radial intervals in background region
    background_region_id = '${mid_lower_refl}
                            ${mid_sodium}
                            ${mid_upper_na_plen}
                            ${mid_upper_gas_plen}'    # Region ID corresponding to background region,
                                                      # defined for each axial layer from bottom to top
    duct_halfpitch = '${fparse duct_pitch_inner / 2}
                      ${fparse duct_pitch_outer / 2}' # Halfpitches for assembly inner and outer duct regions
    duct_intervals = '1 1'                            # Number of radial intervals for each assembly duct region
    duct_region_ids = ' ${mid_lower_refl}     ${mid_lower_refl};
                        ${mid_ht9}            ${mid_sodium};
                        ${mid_upper_na_plen}  ${mid_upper_na_plen};
                        ${mid_upper_gas_plen} ${mid_upper_gas_plen}' # Region IDs corresponding to inner and outer duct regions,
                                                                     # defined for each axial layer from bottom to top

    inputs = 'fuel_pin_1'                    # Name of contituent pin mesh structures
    pattern = '0 0 0 0 0 0 0 0 0;
              0 0 0 0 0 0 0 0 0 0;
             0 0 0 0 0 0 0 0 0 0 0;
            0 0 0 0 0 0 0 0 0 0 0 0;
           0 0 0 0 0 0 0 0 0 0 0 0 0;
          0 0 0 0 0 0 0 0 0 0 0 0 0 0;
         0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
        0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
       0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
        0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
         0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
          0 0 0 0 0 0 0 0 0 0 0 0 0 0;
           0 0 0 0 0 0 0 0 0 0 0 0 0;
            0 0 0 0 0 0 0 0 0 0 0 0;
             0 0 0 0 0 0 0 0 0 0 0;
              0 0 0 0 0 0 0 0 0 0;
               0 0 0 0 0 0 0 0 0'            # Lattice pattern of constituent pins
    extrude = true
  []
[]
