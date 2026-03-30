[Mesh]
  [rmp]
    type = ReactorMeshParams
    dim = 3
    geom = "Hex"
    assembly_pitch = 7.10315
    axial_regions = '1 1'
    axial_mesh_intervals = '1 1'
    top_boundary_id = 201
    bottom_boundary_id = 202
  []

  [pin1]
    type = PinMeshGenerator
    reactor_params = rmp
    pin_type = 1
    pitch = 1.42063
    region_ids='11 12 13; 11 12 13'
    quad_center_elements = false
    num_sectors = 2
    ring_radii = 0.4665
    duct_halfpitch = 0.68
    mesh_intervals = '1 1 1'
    extrude = true
  []
[]

[Problem]
  solve = false
[]

[Outputs]
  [out]
    type = Exodus
    execute_on = timestep_end
    output_extra_element_ids = true
    extra_element_ids_to_output = 'region_id'
  []
[]

[Executioner]
  type = Steady
[]
