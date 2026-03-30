[Mesh]
  [rmp]
    type = ReactorMeshParams
    dim = 3
    geom = "Hex"
    assembly_pitch = 7.10315
    axial_regions = 1
    axial_mesh_intervals = 1
    top_boundary_id = 201
    bottom_boundary_id = 202
  []

  [pin1]
    type = PinMeshGenerator
    reactor_params = rmp
    pin_type = 2
    pitch = 1.42063
    region_ids='1'
    quad_center_elements = true
    homogenized = true
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
    extra_element_ids_to_output = 'region_id pin_type_id'
  []
[]

[Executioner]
  type = Steady
[]
