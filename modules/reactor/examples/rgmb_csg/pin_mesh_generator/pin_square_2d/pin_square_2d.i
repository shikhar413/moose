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
    pitch = 1.42063
    quad_center_elements = false
    num_sectors = 4
    ring_radii = '0.3385 0.3705 0.4665'
    mesh_intervals = '1 1 1 1'
    region_ids='1 2 3 4'
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
