[Mesh]
  [rmp]
    type = ReactorMeshParams
    dim = 2
    geom = "Square"
    assembly_pitch = 7.10315
  []

  [pin1]
    type = PinMeshGenerator
    reactor_params = rmp
    pin_type = 2
    pitch = 7.10315
    region_ids='1 2 3'
    quad_center_elements = true
    homogenized = false
    use_as_assembly = true
    num_sectors = 2
    ring_radii = 2
    duct_halfpitch = 3
    mesh_intervals = '1 1 1'
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
    extra_element_ids_to_output = 'region_id pin_type_id assembly_type_id'
  []
[]

[Executioner]
  type = Steady
[]
