[Mesh]
  [rmp]
    type = ReactorMeshParams
    dim = 3
    geom = "Square"
    assembly_pitch = 7.10315
    axial_regions = '1 1'
    axial_mesh_intervals = '1 1'
    top_boundary_id = 201
    bottom_boundary_id = 202
  []

  [pin1]
    type = PinMeshGenerator
    reactor_params = rmp
    pin_type = 2
    pitch = 1.42063
    region_ids='1 2 3 4; 5 6 7 8'
    quad_center_elements = false
    num_sectors = 2
    mesh_intervals = '1 1 1 1'
    ring_radii = '0.3385 0.3705 0.4665'
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
