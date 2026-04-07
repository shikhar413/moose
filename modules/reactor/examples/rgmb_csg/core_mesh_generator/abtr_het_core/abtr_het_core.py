import openmc

# Define material fills as materials
rgmb_region_1 = openmc.Material(name="rgmb_region_1")
rgmb_region_1.add_nuclide('U235', 0.03)
rgmb_region_1.add_nuclide('U238', 0.97)
rgmb_region_1.add_nuclide('O16', 2.0)
rgmb_region_1.set_density('g/cm3', 10.0)

rgmb_region_10 = openmc.Material(name="rgmb_region_10")
rgmb_region_10.add_nuclide('U235', 0.03)
rgmb_region_10.add_nuclide('U238', 0.97)
rgmb_region_10.add_nuclide('O16', 2.0)
rgmb_region_10.set_density('g/cm3', 10.0)

rgmb_region_11 = openmc.Material(name="rgmb_region_11")
rgmb_region_11.add_nuclide('U235', 0.03)
rgmb_region_11.add_nuclide('U238', 0.97)
rgmb_region_11.add_nuclide('O16', 2.0)
rgmb_region_11.set_density('g/cm3', 10.0)

rgmb_region_12 = openmc.Material(name="rgmb_region_12")
rgmb_region_12.add_nuclide('U235', 0.03)
rgmb_region_12.add_nuclide('U238', 0.97)
rgmb_region_12.add_nuclide('O16', 2.0)
rgmb_region_12.set_density('g/cm3', 10.0)

rgmb_region_2 = openmc.Material(name="rgmb_region_2")
rgmb_region_2.add_nuclide('U235', 0.03)
rgmb_region_2.add_nuclide('U238', 0.97)
rgmb_region_2.add_nuclide('O16', 2.0)
rgmb_region_2.set_density('g/cm3', 10.0)

rgmb_region_3 = openmc.Material(name="rgmb_region_3")
rgmb_region_3.add_nuclide('U235', 0.03)
rgmb_region_3.add_nuclide('U238', 0.97)
rgmb_region_3.add_nuclide('O16', 2.0)
rgmb_region_3.set_density('g/cm3', 10.0)

rgmb_region_4 = openmc.Material(name="rgmb_region_4")
rgmb_region_4.add_nuclide('U235', 0.03)
rgmb_region_4.add_nuclide('U238', 0.97)
rgmb_region_4.add_nuclide('O16', 2.0)
rgmb_region_4.set_density('g/cm3', 10.0)

rgmb_region_5 = openmc.Material(name="rgmb_region_5")
rgmb_region_5.add_nuclide('U235', 0.03)
rgmb_region_5.add_nuclide('U238', 0.97)
rgmb_region_5.add_nuclide('O16', 2.0)
rgmb_region_5.set_density('g/cm3', 10.0)

rgmb_region_6 = openmc.Material(name="rgmb_region_6")
rgmb_region_6.add_nuclide('U235', 0.03)
rgmb_region_6.add_nuclide('U238', 0.97)
rgmb_region_6.add_nuclide('O16', 2.0)
rgmb_region_6.set_density('g/cm3', 10.0)

rgmb_region_7 = openmc.Material(name="rgmb_region_7")
rgmb_region_7.add_nuclide('U235', 0.03)
rgmb_region_7.add_nuclide('U238', 0.97)
rgmb_region_7.add_nuclide('O16', 2.0)
rgmb_region_7.set_density('g/cm3', 10.0)

rgmb_region_8 = openmc.Material(name="rgmb_region_8")
rgmb_region_8.add_nuclide('U235', 0.03)
rgmb_region_8.add_nuclide('U238', 0.97)
rgmb_region_8.add_nuclide('O16', 2.0)
rgmb_region_8.set_density('g/cm3', 10.0)

rgmb_region_9 = openmc.Material(name="rgmb_region_9")
rgmb_region_9.add_nuclide('U235', 0.03)
rgmb_region_9.add_nuclide('U238', 0.97)
rgmb_region_9.add_nuclide('O16', 2.0)
rgmb_region_9.set_density('g/cm3', 10.0)

openmc_mats = openmc.Materials([rgmb_region_1, rgmb_region_10, rgmb_region_11, rgmb_region_12, rgmb_region_2, rgmb_region_3, rgmb_region_4, rgmb_region_5, rgmb_region_6, rgmb_region_7, rgmb_region_8, rgmb_region_9])
openmc_mats.export_to_xml()

# Define surfaces
control_assembly_radial_duct_0_surf_0 = openmc.Plane(d=-6.099, b=-0.866025, c=2.76035e-18, a=-0.5)
control_assembly_radial_duct_0_surf_1 = openmc.Plane(d=-6.099, b=-0.866025, c=1.76348e-17, a=0.5)
control_assembly_radial_duct_0_surf_2 = openmc.Plane(d=-6.099, b=-2.52233e-16, c=0, a=1)
control_assembly_radial_duct_0_surf_3 = openmc.Plane(d=-6.099, b=0.866025, c=-8.0615e-18, a=0.5)
control_assembly_radial_duct_0_surf_4 = openmc.Plane(d=-6.099, b=0.866025, c=4.81505e-18, a=-0.5)
control_assembly_radial_duct_0_surf_5 = openmc.Plane(d=-6.099, b=6.30583e-16, c=-1.4803e-17, a=-1)
control_assembly_radial_duct_1_surf_0 = openmc.Plane(d=-6.399, b=-0.866025, c=3.11788e-18, a=-0.5)
control_assembly_radial_duct_1_surf_1 = openmc.Plane(d=-6.399, b=-0.866025, c=-2.33341e-17, a=0.5)
control_assembly_radial_duct_1_surf_2 = openmc.Plane(d=-6.399, b=-3.60612e-16, c=-1.4803e-17, a=1)
control_assembly_radial_duct_1_surf_3 = openmc.Plane(d=-6.399, b=0.866025, c=-8.4549e-20, a=0.5)
control_assembly_radial_duct_1_surf_4 = openmc.Plane(d=-6.399, b=0.866025, c=2.3104e-18, a=-0.5)
control_assembly_radial_duct_1_surf_5 = openmc.Plane(d=-6.399, b=6.0102e-16, c=-1.4803e-17, a=-1)
control_assembly_radial_duct_2_surf_0 = openmc.Plane(d=-6.799, b=-0.866025, c=3.16305e-18, a=-0.5)
control_assembly_radial_duct_2_surf_1 = openmc.Plane(d=-6.799, b=-0.866025, c=4.90345e-18, a=0.5)
control_assembly_radial_duct_2_surf_2 = openmc.Plane(d=-6.799, b=-3.39396e-16, c=-1.4803e-17, a=1)
control_assembly_radial_duct_2_surf_3 = openmc.Plane(d=-6.799, b=0.866025, c=-9.82301e-19, a=0.5)
control_assembly_radial_duct_2_surf_4 = openmc.Plane(d=-6.799, b=0.866025, c=-7.9163e-18, a=-0.5)
control_assembly_radial_duct_2_surf_5 = openmc.Plane(d=-6.799, b=6.78793e-16, c=6.69877e-33, a=-1)
control_assembly_radial_duct_3_surf_0 = openmc.Plane(d=-7.099, b=-0.866025, c=-1.72184e-18, a=-0.5)
control_assembly_radial_duct_3_surf_1 = openmc.Plane(d=-7.099, b=-0.866025, c=-6.39476e-18, a=0.5)
control_assembly_radial_duct_3_surf_2 = openmc.Plane(d=-7.099, b=-3.25054e-16, c=1.4803e-17, a=1)
control_assembly_radial_duct_3_surf_3 = openmc.Plane(d=-7.099, b=0.866025, c=-1.45416e-17, a=0.5)
control_assembly_radial_duct_3_surf_4 = openmc.Plane(d=-7.099, b=0.866025, c=2.45572e-18, a=-0.5)
control_assembly_radial_duct_3_surf_5 = openmc.Plane(d=-7.099, b=6.50107e-16, c=0, a=-1)
control_pin_radial_ring_0 = openmc.ZCylinder(r=0.485, y0=0, x0=0)
control_pin_radial_ring_1 = openmc.ZCylinder(r=0.55904, y0=0, x0=0)
fuel_assembly_1_radial_duct_0_surf_0 = openmc.Plane(d=-6.799, b=-0.866025, c=3.16305e-18, a=-0.5)
fuel_assembly_1_radial_duct_0_surf_1 = openmc.Plane(d=-6.799, b=-0.866025, c=4.90345e-18, a=0.5)
fuel_assembly_1_radial_duct_0_surf_2 = openmc.Plane(d=-6.799, b=-3.39396e-16, c=-1.4803e-17, a=1)
fuel_assembly_1_radial_duct_0_surf_3 = openmc.Plane(d=-6.799, b=0.866025, c=-9.82301e-19, a=0.5)
fuel_assembly_1_radial_duct_0_surf_4 = openmc.Plane(d=-6.799, b=0.866025, c=-7.9163e-18, a=-0.5)
fuel_assembly_1_radial_duct_0_surf_5 = openmc.Plane(d=-6.799, b=6.78793e-16, c=6.69877e-33, a=-1)
fuel_assembly_1_radial_duct_1_surf_0 = openmc.Plane(d=-7.099, b=-0.866025, c=-1.72184e-18, a=-0.5)
fuel_assembly_1_radial_duct_1_surf_1 = openmc.Plane(d=-7.099, b=-0.866025, c=-6.39476e-18, a=0.5)
fuel_assembly_1_radial_duct_1_surf_2 = openmc.Plane(d=-7.099, b=-3.25054e-16, c=1.4803e-17, a=1)
fuel_assembly_1_radial_duct_1_surf_3 = openmc.Plane(d=-7.099, b=0.866025, c=-1.45416e-17, a=0.5)
fuel_assembly_1_radial_duct_1_surf_4 = openmc.Plane(d=-7.099, b=0.866025, c=2.45572e-18, a=-0.5)
fuel_assembly_1_radial_duct_1_surf_5 = openmc.Plane(d=-7.099, b=6.50107e-16, c=0, a=-1)
fuel_assembly_2_radial_duct_0_surf_0 = openmc.Plane(d=-6.799, b=-0.866025, c=3.16305e-18, a=-0.5)
fuel_assembly_2_radial_duct_0_surf_1 = openmc.Plane(d=-6.799, b=-0.866025, c=4.90345e-18, a=0.5)
fuel_assembly_2_radial_duct_0_surf_2 = openmc.Plane(d=-6.799, b=-3.39396e-16, c=-1.4803e-17, a=1)
fuel_assembly_2_radial_duct_0_surf_3 = openmc.Plane(d=-6.799, b=0.866025, c=-9.82301e-19, a=0.5)
fuel_assembly_2_radial_duct_0_surf_4 = openmc.Plane(d=-6.799, b=0.866025, c=-7.9163e-18, a=-0.5)
fuel_assembly_2_radial_duct_0_surf_5 = openmc.Plane(d=-6.799, b=6.78793e-16, c=6.69877e-33, a=-1)
fuel_assembly_2_radial_duct_1_surf_0 = openmc.Plane(d=-7.099, b=-0.866025, c=-1.72184e-18, a=-0.5)
fuel_assembly_2_radial_duct_1_surf_1 = openmc.Plane(d=-7.099, b=-0.866025, c=-6.39476e-18, a=0.5)
fuel_assembly_2_radial_duct_1_surf_2 = openmc.Plane(d=-7.099, b=-3.25054e-16, c=1.4803e-17, a=1)
fuel_assembly_2_radial_duct_1_surf_3 = openmc.Plane(d=-7.099, b=0.866025, c=-1.45416e-17, a=0.5)
fuel_assembly_2_radial_duct_1_surf_4 = openmc.Plane(d=-7.099, b=0.866025, c=2.45572e-18, a=-0.5)
fuel_assembly_2_radial_duct_1_surf_5 = openmc.Plane(d=-7.099, b=6.50107e-16, c=0, a=-1)
fuel_assembly_3_radial_duct_0_surf_0 = openmc.Plane(d=-6.799, b=-0.866025, c=3.16305e-18, a=-0.5)
fuel_assembly_3_radial_duct_0_surf_1 = openmc.Plane(d=-6.799, b=-0.866025, c=4.90345e-18, a=0.5)
fuel_assembly_3_radial_duct_0_surf_2 = openmc.Plane(d=-6.799, b=-3.39396e-16, c=-1.4803e-17, a=1)
fuel_assembly_3_radial_duct_0_surf_3 = openmc.Plane(d=-6.799, b=0.866025, c=-9.82301e-19, a=0.5)
fuel_assembly_3_radial_duct_0_surf_4 = openmc.Plane(d=-6.799, b=0.866025, c=-7.9163e-18, a=-0.5)
fuel_assembly_3_radial_duct_0_surf_5 = openmc.Plane(d=-6.799, b=6.78793e-16, c=6.69877e-33, a=-1)
fuel_assembly_3_radial_duct_1_surf_0 = openmc.Plane(d=-7.099, b=-0.866025, c=-1.72184e-18, a=-0.5)
fuel_assembly_3_radial_duct_1_surf_1 = openmc.Plane(d=-7.099, b=-0.866025, c=-6.39476e-18, a=0.5)
fuel_assembly_3_radial_duct_1_surf_2 = openmc.Plane(d=-7.099, b=-3.25054e-16, c=1.4803e-17, a=1)
fuel_assembly_3_radial_duct_1_surf_3 = openmc.Plane(d=-7.099, b=0.866025, c=-1.45416e-17, a=0.5)
fuel_assembly_3_radial_duct_1_surf_4 = openmc.Plane(d=-7.099, b=0.866025, c=2.45572e-18, a=-0.5)
fuel_assembly_3_radial_duct_1_surf_5 = openmc.Plane(d=-7.099, b=6.50107e-16, c=0, a=-1)
fuel_pin_1_radial_ring_0 = openmc.ZCylinder(r=0.348, y0=0, x0=0)
fuel_pin_1_radial_ring_1 = openmc.ZCylinder(r=0.40333, y0=0, x0=0)
fuel_pin_2_radial_ring_0 = openmc.ZCylinder(r=0.348, y0=0, x0=0)
fuel_pin_2_radial_ring_1 = openmc.ZCylinder(r=0.40333, y0=0, x0=0)
fuel_pin_3_radial_ring_0 = openmc.ZCylinder(r=0.348, y0=0, x0=0)
fuel_pin_3_radial_ring_1 = openmc.ZCylinder(r=0.40333, y0=0, x0=0)
het_core_radial_ring = openmc.ZCylinder(r=138.681, y0=0, x0=0, boundary_type='vacuum')
rgmb_axial_plane_0 = openmc.Plane(d=0, b=0, c=1, a=0, boundary_type='vacuum')
rgmb_axial_plane_1 = openmc.Plane(d=60, b=0, c=1, a=0)
rgmb_axial_plane_2 = openmc.Plane(d=140, b=0, c=1, a=0)
rgmb_axial_plane_3 = openmc.Plane(d=160, b=0, c=1, a=0)
rgmb_axial_plane_4 = openmc.Plane(d=260, b=0, c=1, a=0, boundary_type='vacuum')

# Define cells, universes, and lattices
dummy_cell = openmc.Cell()
dummy_univ = openmc.Universe(cells=[dummy_cell])
shielding_assembly_cell_radial_0_axial_3 = openmc.Cell(fill=rgmb_region_8, region=(+rgmb_axial_plane_3))
shielding_assembly_cell_radial_0_axial_2 = openmc.Cell(fill=rgmb_region_8, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
shielding_assembly_cell_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_8, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
shielding_assembly_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_8, region=(-rgmb_axial_plane_1))
shielding_assembly_univ = openmc.Universe(cells=[shielding_assembly_cell_radial_0_axial_0, shielding_assembly_cell_radial_0_axial_1, shielding_assembly_cell_radial_0_axial_2, shielding_assembly_cell_radial_0_axial_3])
reflector_assembly_cell_radial_0_axial_3 = openmc.Cell(fill=rgmb_region_7, region=(+rgmb_axial_plane_3))
reflector_assembly_cell_radial_0_axial_2 = openmc.Cell(fill=rgmb_region_7, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
reflector_assembly_cell_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_7, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
reflector_assembly_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_7, region=(-rgmb_axial_plane_1))
reflector_assembly_univ = openmc.Universe(cells=[reflector_assembly_cell_radial_0_axial_0, reflector_assembly_cell_radial_0_axial_1, reflector_assembly_cell_radial_0_axial_2, reflector_assembly_cell_radial_0_axial_3])
fuel_assembly_2_duct_radial_1_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(+rgmb_axial_plane_3))
fuel_assembly_2_duct_radial_1_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_assembly_2_duct_radial_1_axial_1 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_assembly_2_duct_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-rgmb_axial_plane_1))
fuel_assembly_2_duct_radial_1_univ = openmc.Universe(cells=[fuel_assembly_2_duct_radial_1_axial_0, fuel_assembly_2_duct_radial_1_axial_1, fuel_assembly_2_duct_radial_1_axial_2, fuel_assembly_2_duct_radial_1_axial_3])
fuel_assembly_2_duct_cell_radial_1 = openmc.Cell(fill=fuel_assembly_2_duct_radial_1_univ, region=(~(+fuel_assembly_2_radial_duct_1_surf_0 & +fuel_assembly_2_radial_duct_1_surf_1 & +fuel_assembly_2_radial_duct_1_surf_2 & +fuel_assembly_2_radial_duct_1_surf_3 & +fuel_assembly_2_radial_duct_1_surf_4 & +fuel_assembly_2_radial_duct_1_surf_5)))
fuel_assembly_2_duct_radial_0_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(+rgmb_axial_plane_3))
fuel_assembly_2_duct_radial_0_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_assembly_2_duct_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_5, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_assembly_2_duct_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-rgmb_axial_plane_1))
fuel_assembly_2_duct_radial_0_univ = openmc.Universe(cells=[fuel_assembly_2_duct_radial_0_axial_0, fuel_assembly_2_duct_radial_0_axial_1, fuel_assembly_2_duct_radial_0_axial_2, fuel_assembly_2_duct_radial_0_axial_3])
fuel_assembly_2_duct_cell_radial_0 = openmc.Cell(fill=fuel_assembly_2_duct_radial_0_univ, region=(~(+fuel_assembly_2_radial_duct_0_surf_0 & +fuel_assembly_2_radial_duct_0_surf_1 & +fuel_assembly_2_radial_duct_0_surf_2 & +fuel_assembly_2_radial_duct_0_surf_3 & +fuel_assembly_2_radial_duct_0_surf_4 & +fuel_assembly_2_radial_duct_0_surf_5) & +fuel_assembly_2_radial_duct_1_surf_0 & +fuel_assembly_2_radial_duct_1_surf_1 & +fuel_assembly_2_radial_duct_1_surf_2 & +fuel_assembly_2_radial_duct_1_surf_3 & +fuel_assembly_2_radial_duct_1_surf_4 & +fuel_assembly_2_radial_duct_1_surf_5))
fuel_assembly_2_lattice_outer_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(+rgmb_axial_plane_3))
fuel_assembly_2_lattice_outer_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_assembly_2_lattice_outer_axial_1 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_assembly_2_lattice_outer_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-rgmb_axial_plane_1))
fuel_assembly_2_lattice_outer_univ = openmc.Universe(cells=[fuel_assembly_2_lattice_outer_axial_0, fuel_assembly_2_lattice_outer_axial_1, fuel_assembly_2_lattice_outer_axial_2, fuel_assembly_2_lattice_outer_axial_3])
fuel_pin_2_cell_radial_2_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(~(-fuel_pin_2_radial_ring_1) & +rgmb_axial_plane_3))
fuel_pin_2_cell_radial_2_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(~(-fuel_pin_2_radial_ring_1) & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_pin_2_cell_radial_2_axial_1 = openmc.Cell(fill=rgmb_region_6, region=(~(-fuel_pin_2_radial_ring_1) & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_pin_2_cell_radial_2_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(~(-fuel_pin_2_radial_ring_1) & -rgmb_axial_plane_1))
fuel_pin_2_cell_radial_1_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(-fuel_pin_2_radial_ring_1 & ~(-fuel_pin_2_radial_ring_0) & +rgmb_axial_plane_3))
fuel_pin_2_cell_radial_1_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(-fuel_pin_2_radial_ring_1 & ~(-fuel_pin_2_radial_ring_0) & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_pin_2_cell_radial_1_axial_1 = openmc.Cell(fill=rgmb_region_5, region=(-fuel_pin_2_radial_ring_1 & ~(-fuel_pin_2_radial_ring_0) & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_pin_2_cell_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-fuel_pin_2_radial_ring_1 & ~(-fuel_pin_2_radial_ring_0) & -rgmb_axial_plane_1))
fuel_pin_2_cell_radial_0_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(-fuel_pin_2_radial_ring_0 & +rgmb_axial_plane_3))
fuel_pin_2_cell_radial_0_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(-fuel_pin_2_radial_ring_0 & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_pin_2_cell_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_2, region=(-fuel_pin_2_radial_ring_0 & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_pin_2_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-fuel_pin_2_radial_ring_0 & -rgmb_axial_plane_1))
fuel_pin_2_univ = openmc.Universe(cells=[fuel_pin_2_cell_radial_0_axial_0, fuel_pin_2_cell_radial_0_axial_1, fuel_pin_2_cell_radial_0_axial_2, fuel_pin_2_cell_radial_0_axial_3, fuel_pin_2_cell_radial_1_axial_0, fuel_pin_2_cell_radial_1_axial_1, fuel_pin_2_cell_radial_1_axial_2, fuel_pin_2_cell_radial_1_axial_3, fuel_pin_2_cell_radial_2_axial_0, fuel_pin_2_cell_radial_2_axial_1, fuel_pin_2_cell_radial_2_axial_2, fuel_pin_2_cell_radial_2_axial_3])
fuel_assembly_2_lattice_unrotated = openmc.HexLattice()
fuel_assembly_2_lattice_unrotated.orientation = 'x'
fuel_assembly_2_lattice_unrotated.pitch = (0.908,)
fuel_assembly_2_lattice_unrotated.center = (0, 0)
fuel_assembly_2_lattice_unrotated.outer = fuel_assembly_2_lattice_outer_univ
fuel_assembly_2_lattice_unrotated.universes = [
  [fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ],
  [fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ],
  [fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ],
  [fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ],
  [fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ],
  [fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ],
  [fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ],
  [fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ, fuel_pin_2_univ],
  [fuel_pin_2_univ]
]
fuel_assembly_2_lattice_cell = openmc.Cell(fill=fuel_assembly_2_lattice_unrotated)
fuel_assembly_2_lattice_cell.rotation = (0, 0, 90)
fuel_assembly_2_lattice = openmc.Universe(cells=[fuel_assembly_2_lattice_cell])
fuel_assembly_2_lattice_cell = openmc.Cell(fill=fuel_assembly_2_lattice, region=(+fuel_assembly_2_radial_duct_0_surf_0 & +fuel_assembly_2_radial_duct_0_surf_1 & +fuel_assembly_2_radial_duct_0_surf_2 & +fuel_assembly_2_radial_duct_0_surf_3 & +fuel_assembly_2_radial_duct_0_surf_4 & +fuel_assembly_2_radial_duct_0_surf_5))
fuel_assembly_2_univ = openmc.Universe(cells=[fuel_assembly_2_lattice_cell, fuel_assembly_2_duct_cell_radial_0, fuel_assembly_2_duct_cell_radial_1])
control_assembly_duct_radial_3_axial_3 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_3))
control_assembly_duct_radial_3_axial_2 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
control_assembly_duct_radial_3_axial_1 = openmc.Cell(fill=rgmb_region_12, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
control_assembly_duct_radial_3_axial_0 = openmc.Cell(fill=rgmb_region_12, region=(-rgmb_axial_plane_1))
control_assembly_duct_radial_3_univ = openmc.Universe(cells=[control_assembly_duct_radial_3_axial_0, control_assembly_duct_radial_3_axial_1, control_assembly_duct_radial_3_axial_2, control_assembly_duct_radial_3_axial_3])
control_assembly_duct_cell_radial_3 = openmc.Cell(fill=control_assembly_duct_radial_3_univ, region=(~(+control_assembly_radial_duct_3_surf_0 & +control_assembly_radial_duct_3_surf_1 & +control_assembly_radial_duct_3_surf_2 & +control_assembly_radial_duct_3_surf_3 & +control_assembly_radial_duct_3_surf_4 & +control_assembly_radial_duct_3_surf_5)))
control_assembly_duct_radial_2_axial_3 = openmc.Cell(fill=rgmb_region_5, region=(+rgmb_axial_plane_3))
control_assembly_duct_radial_2_axial_2 = openmc.Cell(fill=rgmb_region_5, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
control_assembly_duct_radial_2_axial_1 = openmc.Cell(fill=rgmb_region_12, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
control_assembly_duct_radial_2_axial_0 = openmc.Cell(fill=rgmb_region_12, region=(-rgmb_axial_plane_1))
control_assembly_duct_radial_2_univ = openmc.Universe(cells=[control_assembly_duct_radial_2_axial_0, control_assembly_duct_radial_2_axial_1, control_assembly_duct_radial_2_axial_2, control_assembly_duct_radial_2_axial_3])
control_assembly_duct_cell_radial_2 = openmc.Cell(fill=control_assembly_duct_radial_2_univ, region=(~(+control_assembly_radial_duct_2_surf_0 & +control_assembly_radial_duct_2_surf_1 & +control_assembly_radial_duct_2_surf_2 & +control_assembly_radial_duct_2_surf_3 & +control_assembly_radial_duct_2_surf_4 & +control_assembly_radial_duct_2_surf_5) & +control_assembly_radial_duct_3_surf_0 & +control_assembly_radial_duct_3_surf_1 & +control_assembly_radial_duct_3_surf_2 & +control_assembly_radial_duct_3_surf_3 & +control_assembly_radial_duct_3_surf_4 & +control_assembly_radial_duct_3_surf_5))
control_assembly_duct_radial_1_axial_3 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_3))
control_assembly_duct_radial_1_axial_2 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
control_assembly_duct_radial_1_axial_1 = openmc.Cell(fill=rgmb_region_12, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
control_assembly_duct_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_12, region=(-rgmb_axial_plane_1))
control_assembly_duct_radial_1_univ = openmc.Universe(cells=[control_assembly_duct_radial_1_axial_0, control_assembly_duct_radial_1_axial_1, control_assembly_duct_radial_1_axial_2, control_assembly_duct_radial_1_axial_3])
control_assembly_duct_cell_radial_1 = openmc.Cell(fill=control_assembly_duct_radial_1_univ, region=(~(+control_assembly_radial_duct_1_surf_0 & +control_assembly_radial_duct_1_surf_1 & +control_assembly_radial_duct_1_surf_2 & +control_assembly_radial_duct_1_surf_3 & +control_assembly_radial_duct_1_surf_4 & +control_assembly_radial_duct_1_surf_5) & +control_assembly_radial_duct_2_surf_0 & +control_assembly_radial_duct_2_surf_1 & +control_assembly_radial_duct_2_surf_2 & +control_assembly_radial_duct_2_surf_3 & +control_assembly_radial_duct_2_surf_4 & +control_assembly_radial_duct_2_surf_5))
control_assembly_duct_radial_0_axial_3 = openmc.Cell(fill=rgmb_region_5, region=(+rgmb_axial_plane_3))
control_assembly_duct_radial_0_axial_2 = openmc.Cell(fill=rgmb_region_5, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
control_assembly_duct_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_12, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
control_assembly_duct_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_12, region=(-rgmb_axial_plane_1))
control_assembly_duct_radial_0_univ = openmc.Universe(cells=[control_assembly_duct_radial_0_axial_0, control_assembly_duct_radial_0_axial_1, control_assembly_duct_radial_0_axial_2, control_assembly_duct_radial_0_axial_3])
control_assembly_duct_cell_radial_0 = openmc.Cell(fill=control_assembly_duct_radial_0_univ, region=(~(+control_assembly_radial_duct_0_surf_0 & +control_assembly_radial_duct_0_surf_1 & +control_assembly_radial_duct_0_surf_2 & +control_assembly_radial_duct_0_surf_3 & +control_assembly_radial_duct_0_surf_4 & +control_assembly_radial_duct_0_surf_5) & +control_assembly_radial_duct_1_surf_0 & +control_assembly_radial_duct_1_surf_1 & +control_assembly_radial_duct_1_surf_2 & +control_assembly_radial_duct_1_surf_3 & +control_assembly_radial_duct_1_surf_4 & +control_assembly_radial_duct_1_surf_5))
control_assembly_lattice_outer_axial_3 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_3))
control_assembly_lattice_outer_axial_2 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
control_assembly_lattice_outer_axial_1 = openmc.Cell(fill=rgmb_region_12, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
control_assembly_lattice_outer_axial_0 = openmc.Cell(fill=rgmb_region_12, region=(-rgmb_axial_plane_1))
control_assembly_lattice_outer_univ = openmc.Universe(cells=[control_assembly_lattice_outer_axial_0, control_assembly_lattice_outer_axial_1, control_assembly_lattice_outer_axial_2, control_assembly_lattice_outer_axial_3])
control_pin_cell_radial_2_axial_3 = openmc.Cell(fill=rgmb_region_6, region=(~(-control_pin_radial_ring_1) & +rgmb_axial_plane_3))
control_pin_cell_radial_2_axial_2 = openmc.Cell(fill=rgmb_region_6, region=(~(-control_pin_radial_ring_1) & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
control_pin_cell_radial_2_axial_1 = openmc.Cell(fill=rgmb_region_12, region=(~(-control_pin_radial_ring_1) & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
control_pin_cell_radial_2_axial_0 = openmc.Cell(fill=rgmb_region_12, region=(~(-control_pin_radial_ring_1) & -rgmb_axial_plane_1))
control_pin_cell_radial_1_axial_3 = openmc.Cell(fill=rgmb_region_5, region=(-control_pin_radial_ring_1 & ~(-control_pin_radial_ring_0) & +rgmb_axial_plane_3))
control_pin_cell_radial_1_axial_2 = openmc.Cell(fill=rgmb_region_5, region=(-control_pin_radial_ring_1 & ~(-control_pin_radial_ring_0) & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
control_pin_cell_radial_1_axial_1 = openmc.Cell(fill=rgmb_region_12, region=(-control_pin_radial_ring_1 & ~(-control_pin_radial_ring_0) & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
control_pin_cell_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_12, region=(-control_pin_radial_ring_1 & ~(-control_pin_radial_ring_0) & -rgmb_axial_plane_1))
control_pin_cell_radial_0_axial_3 = openmc.Cell(fill=rgmb_region_4, region=(-control_pin_radial_ring_0 & +rgmb_axial_plane_3))
control_pin_cell_radial_0_axial_2 = openmc.Cell(fill=rgmb_region_4, region=(-control_pin_radial_ring_0 & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
control_pin_cell_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_12, region=(-control_pin_radial_ring_0 & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
control_pin_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_12, region=(-control_pin_radial_ring_0 & -rgmb_axial_plane_1))
control_pin_univ = openmc.Universe(cells=[control_pin_cell_radial_0_axial_0, control_pin_cell_radial_0_axial_1, control_pin_cell_radial_0_axial_2, control_pin_cell_radial_0_axial_3, control_pin_cell_radial_1_axial_0, control_pin_cell_radial_1_axial_1, control_pin_cell_radial_1_axial_2, control_pin_cell_radial_1_axial_3, control_pin_cell_radial_2_axial_0, control_pin_cell_radial_2_axial_1, control_pin_cell_radial_2_axial_2, control_pin_cell_radial_2_axial_3])
control_assembly_lattice_unrotated = openmc.HexLattice()
control_assembly_lattice_unrotated.orientation = 'x'
control_assembly_lattice_unrotated.pitch = (1.243,)
control_assembly_lattice_unrotated.center = (0, 0)
control_assembly_lattice_unrotated.outer = control_assembly_lattice_outer_univ
control_assembly_lattice_unrotated.universes = [
  [control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ],
  [control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ],
  [control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ],
  [control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ],
  [control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ, control_pin_univ],
  [control_pin_univ]
]
control_assembly_lattice_cell = openmc.Cell(fill=control_assembly_lattice_unrotated)
control_assembly_lattice_cell.rotation = (0, 0, 90)
control_assembly_lattice = openmc.Universe(cells=[control_assembly_lattice_cell])
control_assembly_lattice_cell = openmc.Cell(fill=control_assembly_lattice, region=(+control_assembly_radial_duct_0_surf_0 & +control_assembly_radial_duct_0_surf_1 & +control_assembly_radial_duct_0_surf_2 & +control_assembly_radial_duct_0_surf_3 & +control_assembly_radial_duct_0_surf_4 & +control_assembly_radial_duct_0_surf_5))
control_assembly_univ = openmc.Universe(cells=[control_assembly_lattice_cell, control_assembly_duct_cell_radial_0, control_assembly_duct_cell_radial_1, control_assembly_duct_cell_radial_2, control_assembly_duct_cell_radial_3])
fuel_assembly_1_duct_radial_1_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(+rgmb_axial_plane_3))
fuel_assembly_1_duct_radial_1_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_assembly_1_duct_radial_1_axial_1 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_assembly_1_duct_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-rgmb_axial_plane_1))
fuel_assembly_1_duct_radial_1_univ = openmc.Universe(cells=[fuel_assembly_1_duct_radial_1_axial_0, fuel_assembly_1_duct_radial_1_axial_1, fuel_assembly_1_duct_radial_1_axial_2, fuel_assembly_1_duct_radial_1_axial_3])
fuel_assembly_1_duct_cell_radial_1 = openmc.Cell(fill=fuel_assembly_1_duct_radial_1_univ, region=(~(+fuel_assembly_1_radial_duct_1_surf_0 & +fuel_assembly_1_radial_duct_1_surf_1 & +fuel_assembly_1_radial_duct_1_surf_2 & +fuel_assembly_1_radial_duct_1_surf_3 & +fuel_assembly_1_radial_duct_1_surf_4 & +fuel_assembly_1_radial_duct_1_surf_5)))
fuel_assembly_1_duct_radial_0_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(+rgmb_axial_plane_3))
fuel_assembly_1_duct_radial_0_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_assembly_1_duct_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_5, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_assembly_1_duct_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-rgmb_axial_plane_1))
fuel_assembly_1_duct_radial_0_univ = openmc.Universe(cells=[fuel_assembly_1_duct_radial_0_axial_0, fuel_assembly_1_duct_radial_0_axial_1, fuel_assembly_1_duct_radial_0_axial_2, fuel_assembly_1_duct_radial_0_axial_3])
fuel_assembly_1_duct_cell_radial_0 = openmc.Cell(fill=fuel_assembly_1_duct_radial_0_univ, region=(~(+fuel_assembly_1_radial_duct_0_surf_0 & +fuel_assembly_1_radial_duct_0_surf_1 & +fuel_assembly_1_radial_duct_0_surf_2 & +fuel_assembly_1_radial_duct_0_surf_3 & +fuel_assembly_1_radial_duct_0_surf_4 & +fuel_assembly_1_radial_duct_0_surf_5) & +fuel_assembly_1_radial_duct_1_surf_0 & +fuel_assembly_1_radial_duct_1_surf_1 & +fuel_assembly_1_radial_duct_1_surf_2 & +fuel_assembly_1_radial_duct_1_surf_3 & +fuel_assembly_1_radial_duct_1_surf_4 & +fuel_assembly_1_radial_duct_1_surf_5))
fuel_assembly_1_lattice_outer_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(+rgmb_axial_plane_3))
fuel_assembly_1_lattice_outer_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_assembly_1_lattice_outer_axial_1 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_assembly_1_lattice_outer_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-rgmb_axial_plane_1))
fuel_assembly_1_lattice_outer_univ = openmc.Universe(cells=[fuel_assembly_1_lattice_outer_axial_0, fuel_assembly_1_lattice_outer_axial_1, fuel_assembly_1_lattice_outer_axial_2, fuel_assembly_1_lattice_outer_axial_3])
fuel_pin_1_cell_radial_2_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(~(-fuel_pin_1_radial_ring_1) & +rgmb_axial_plane_3))
fuel_pin_1_cell_radial_2_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(~(-fuel_pin_1_radial_ring_1) & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_pin_1_cell_radial_2_axial_1 = openmc.Cell(fill=rgmb_region_6, region=(~(-fuel_pin_1_radial_ring_1) & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_pin_1_cell_radial_2_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(~(-fuel_pin_1_radial_ring_1) & -rgmb_axial_plane_1))
fuel_pin_1_cell_radial_1_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(-fuel_pin_1_radial_ring_1 & ~(-fuel_pin_1_radial_ring_0) & +rgmb_axial_plane_3))
fuel_pin_1_cell_radial_1_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(-fuel_pin_1_radial_ring_1 & ~(-fuel_pin_1_radial_ring_0) & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_pin_1_cell_radial_1_axial_1 = openmc.Cell(fill=rgmb_region_5, region=(-fuel_pin_1_radial_ring_1 & ~(-fuel_pin_1_radial_ring_0) & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_pin_1_cell_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-fuel_pin_1_radial_ring_1 & ~(-fuel_pin_1_radial_ring_0) & -rgmb_axial_plane_1))
fuel_pin_1_cell_radial_0_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(-fuel_pin_1_radial_ring_0 & +rgmb_axial_plane_3))
fuel_pin_1_cell_radial_0_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(-fuel_pin_1_radial_ring_0 & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_pin_1_cell_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_1, region=(-fuel_pin_1_radial_ring_0 & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_pin_1_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-fuel_pin_1_radial_ring_0 & -rgmb_axial_plane_1))
fuel_pin_1_univ = openmc.Universe(cells=[fuel_pin_1_cell_radial_0_axial_0, fuel_pin_1_cell_radial_0_axial_1, fuel_pin_1_cell_radial_0_axial_2, fuel_pin_1_cell_radial_0_axial_3, fuel_pin_1_cell_radial_1_axial_0, fuel_pin_1_cell_radial_1_axial_1, fuel_pin_1_cell_radial_1_axial_2, fuel_pin_1_cell_radial_1_axial_3, fuel_pin_1_cell_radial_2_axial_0, fuel_pin_1_cell_radial_2_axial_1, fuel_pin_1_cell_radial_2_axial_2, fuel_pin_1_cell_radial_2_axial_3])
fuel_assembly_1_lattice_unrotated = openmc.HexLattice()
fuel_assembly_1_lattice_unrotated.orientation = 'x'
fuel_assembly_1_lattice_unrotated.pitch = (0.908,)
fuel_assembly_1_lattice_unrotated.center = (0, 0)
fuel_assembly_1_lattice_unrotated.outer = fuel_assembly_1_lattice_outer_univ
fuel_assembly_1_lattice_unrotated.universes = [
  [fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ],
  [fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ],
  [fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ],
  [fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ],
  [fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ],
  [fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ],
  [fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ],
  [fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ, fuel_pin_1_univ],
  [fuel_pin_1_univ]
]
fuel_assembly_1_lattice_cell = openmc.Cell(fill=fuel_assembly_1_lattice_unrotated)
fuel_assembly_1_lattice_cell.rotation = (0, 0, 90)
fuel_assembly_1_lattice = openmc.Universe(cells=[fuel_assembly_1_lattice_cell])
fuel_assembly_1_lattice_cell = openmc.Cell(fill=fuel_assembly_1_lattice, region=(+fuel_assembly_1_radial_duct_0_surf_0 & +fuel_assembly_1_radial_duct_0_surf_1 & +fuel_assembly_1_radial_duct_0_surf_2 & +fuel_assembly_1_radial_duct_0_surf_3 & +fuel_assembly_1_radial_duct_0_surf_4 & +fuel_assembly_1_radial_duct_0_surf_5))
fuel_assembly_1_univ = openmc.Universe(cells=[fuel_assembly_1_lattice_cell, fuel_assembly_1_duct_cell_radial_0, fuel_assembly_1_duct_cell_radial_1])
fuel_assembly_3_duct_radial_1_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(+rgmb_axial_plane_3))
fuel_assembly_3_duct_radial_1_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_assembly_3_duct_radial_1_axial_1 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_assembly_3_duct_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-rgmb_axial_plane_1))
fuel_assembly_3_duct_radial_1_univ = openmc.Universe(cells=[fuel_assembly_3_duct_radial_1_axial_0, fuel_assembly_3_duct_radial_1_axial_1, fuel_assembly_3_duct_radial_1_axial_2, fuel_assembly_3_duct_radial_1_axial_3])
fuel_assembly_3_duct_cell_radial_1 = openmc.Cell(fill=fuel_assembly_3_duct_radial_1_univ, region=(~(+fuel_assembly_3_radial_duct_1_surf_0 & +fuel_assembly_3_radial_duct_1_surf_1 & +fuel_assembly_3_radial_duct_1_surf_2 & +fuel_assembly_3_radial_duct_1_surf_3 & +fuel_assembly_3_radial_duct_1_surf_4 & +fuel_assembly_3_radial_duct_1_surf_5)))
fuel_assembly_3_duct_radial_0_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(+rgmb_axial_plane_3))
fuel_assembly_3_duct_radial_0_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_assembly_3_duct_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_5, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_assembly_3_duct_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-rgmb_axial_plane_1))
fuel_assembly_3_duct_radial_0_univ = openmc.Universe(cells=[fuel_assembly_3_duct_radial_0_axial_0, fuel_assembly_3_duct_radial_0_axial_1, fuel_assembly_3_duct_radial_0_axial_2, fuel_assembly_3_duct_radial_0_axial_3])
fuel_assembly_3_duct_cell_radial_0 = openmc.Cell(fill=fuel_assembly_3_duct_radial_0_univ, region=(~(+fuel_assembly_3_radial_duct_0_surf_0 & +fuel_assembly_3_radial_duct_0_surf_1 & +fuel_assembly_3_radial_duct_0_surf_2 & +fuel_assembly_3_radial_duct_0_surf_3 & +fuel_assembly_3_radial_duct_0_surf_4 & +fuel_assembly_3_radial_duct_0_surf_5) & +fuel_assembly_3_radial_duct_1_surf_0 & +fuel_assembly_3_radial_duct_1_surf_1 & +fuel_assembly_3_radial_duct_1_surf_2 & +fuel_assembly_3_radial_duct_1_surf_3 & +fuel_assembly_3_radial_duct_1_surf_4 & +fuel_assembly_3_radial_duct_1_surf_5))
fuel_assembly_3_lattice_outer_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(+rgmb_axial_plane_3))
fuel_assembly_3_lattice_outer_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(+rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_assembly_3_lattice_outer_axial_1 = openmc.Cell(fill=rgmb_region_6, region=(+rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_assembly_3_lattice_outer_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-rgmb_axial_plane_1))
fuel_assembly_3_lattice_outer_univ = openmc.Universe(cells=[fuel_assembly_3_lattice_outer_axial_0, fuel_assembly_3_lattice_outer_axial_1, fuel_assembly_3_lattice_outer_axial_2, fuel_assembly_3_lattice_outer_axial_3])
fuel_pin_3_cell_radial_2_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(~(-fuel_pin_3_radial_ring_1) & +rgmb_axial_plane_3))
fuel_pin_3_cell_radial_2_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(~(-fuel_pin_3_radial_ring_1) & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_pin_3_cell_radial_2_axial_1 = openmc.Cell(fill=rgmb_region_6, region=(~(-fuel_pin_3_radial_ring_1) & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_pin_3_cell_radial_2_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(~(-fuel_pin_3_radial_ring_1) & -rgmb_axial_plane_1))
fuel_pin_3_cell_radial_1_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(-fuel_pin_3_radial_ring_1 & ~(-fuel_pin_3_radial_ring_0) & +rgmb_axial_plane_3))
fuel_pin_3_cell_radial_1_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(-fuel_pin_3_radial_ring_1 & ~(-fuel_pin_3_radial_ring_0) & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_pin_3_cell_radial_1_axial_1 = openmc.Cell(fill=rgmb_region_5, region=(-fuel_pin_3_radial_ring_1 & ~(-fuel_pin_3_radial_ring_0) & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_pin_3_cell_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-fuel_pin_3_radial_ring_1 & ~(-fuel_pin_3_radial_ring_0) & -rgmb_axial_plane_1))
fuel_pin_3_cell_radial_0_axial_3 = openmc.Cell(fill=rgmb_region_11, region=(-fuel_pin_3_radial_ring_0 & +rgmb_axial_plane_3))
fuel_pin_3_cell_radial_0_axial_2 = openmc.Cell(fill=rgmb_region_10, region=(-fuel_pin_3_radial_ring_0 & +rgmb_axial_plane_2 & -rgmb_axial_plane_3))
fuel_pin_3_cell_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_3, region=(-fuel_pin_3_radial_ring_0 & +rgmb_axial_plane_1 & -rgmb_axial_plane_2))
fuel_pin_3_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_9, region=(-fuel_pin_3_radial_ring_0 & -rgmb_axial_plane_1))
fuel_pin_3_univ = openmc.Universe(cells=[fuel_pin_3_cell_radial_0_axial_0, fuel_pin_3_cell_radial_0_axial_1, fuel_pin_3_cell_radial_0_axial_2, fuel_pin_3_cell_radial_0_axial_3, fuel_pin_3_cell_radial_1_axial_0, fuel_pin_3_cell_radial_1_axial_1, fuel_pin_3_cell_radial_1_axial_2, fuel_pin_3_cell_radial_1_axial_3, fuel_pin_3_cell_radial_2_axial_0, fuel_pin_3_cell_radial_2_axial_1, fuel_pin_3_cell_radial_2_axial_2, fuel_pin_3_cell_radial_2_axial_3])
fuel_assembly_3_lattice_unrotated = openmc.HexLattice()
fuel_assembly_3_lattice_unrotated.orientation = 'x'
fuel_assembly_3_lattice_unrotated.pitch = (0.908,)
fuel_assembly_3_lattice_unrotated.center = (0, 0)
fuel_assembly_3_lattice_unrotated.outer = fuel_assembly_3_lattice_outer_univ
fuel_assembly_3_lattice_unrotated.universes = [
  [fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ],
  [fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ],
  [fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ],
  [fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ],
  [fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ],
  [fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ],
  [fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ],
  [fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ, fuel_pin_3_univ],
  [fuel_pin_3_univ]
]
fuel_assembly_3_lattice_cell = openmc.Cell(fill=fuel_assembly_3_lattice_unrotated)
fuel_assembly_3_lattice_cell.rotation = (0, 0, 90)
fuel_assembly_3_lattice = openmc.Universe(cells=[fuel_assembly_3_lattice_cell])
fuel_assembly_3_lattice_cell = openmc.Cell(fill=fuel_assembly_3_lattice, region=(+fuel_assembly_3_radial_duct_0_surf_0 & +fuel_assembly_3_radial_duct_0_surf_1 & +fuel_assembly_3_radial_duct_0_surf_2 & +fuel_assembly_3_radial_duct_0_surf_3 & +fuel_assembly_3_radial_duct_0_surf_4 & +fuel_assembly_3_radial_duct_0_surf_5))
fuel_assembly_3_univ = openmc.Universe(cells=[fuel_assembly_3_lattice_cell, fuel_assembly_3_duct_cell_radial_0, fuel_assembly_3_duct_cell_radial_1])
het_core_lattice = openmc.HexLattice()
het_core_lattice.orientation = 'x'
het_core_lattice.pitch = (14.598,)
het_core_lattice.center = (0, 0)
het_core_lattice.outer = dummy_univ
het_core_lattice.universes = [
  [dummy_univ, dummy_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, dummy_univ, dummy_univ, dummy_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, dummy_univ, dummy_univ, dummy_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, dummy_univ, dummy_univ, dummy_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, dummy_univ, dummy_univ, dummy_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, dummy_univ, dummy_univ, dummy_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, dummy_univ],
  [shielding_assembly_univ, shielding_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, shielding_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, shielding_assembly_univ],
  [reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ],
  [reflector_assembly_univ, reflector_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, reflector_assembly_univ, reflector_assembly_univ, reflector_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, reflector_assembly_univ],
  [fuel_assembly_2_univ, fuel_assembly_2_univ, control_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, control_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, control_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, control_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, control_assembly_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, fuel_assembly_2_univ, control_assembly_univ, fuel_assembly_2_univ],
  [fuel_assembly_3_univ, fuel_assembly_1_univ, fuel_assembly_1_univ, reflector_assembly_univ, fuel_assembly_1_univ, fuel_assembly_1_univ, fuel_assembly_3_univ, fuel_assembly_1_univ, fuel_assembly_1_univ, reflector_assembly_univ, fuel_assembly_1_univ, fuel_assembly_1_univ, fuel_assembly_3_univ, fuel_assembly_1_univ, fuel_assembly_1_univ, reflector_assembly_univ, fuel_assembly_1_univ, fuel_assembly_1_univ],
  [fuel_assembly_1_univ, fuel_assembly_3_univ, fuel_assembly_1_univ, control_assembly_univ, fuel_assembly_1_univ, fuel_assembly_3_univ, fuel_assembly_1_univ, control_assembly_univ, fuel_assembly_1_univ, fuel_assembly_3_univ, fuel_assembly_1_univ, control_assembly_univ],
  [fuel_assembly_1_univ, fuel_assembly_1_univ, fuel_assembly_1_univ, fuel_assembly_1_univ, fuel_assembly_1_univ, fuel_assembly_1_univ],
  [control_assembly_univ]
]
het_core_lattice_cell = openmc.Cell(fill=het_core_lattice, region=(-het_core_radial_ring & +rgmb_axial_plane_0 & -rgmb_axial_plane_4))
root_universe = openmc.Universe(cells=[het_core_lattice_cell])
geom = openmc.Geometry(root_universe)
geom.export_to_xml()

# Define settings
point = openmc.stats.Point((0, 0, 130))
src = openmc.Source(space=point)
settings = openmc.Settings()
settings.source = src
settings.batches = 100
settings.inactive = 10
settings.particles = 1000
settings.export_to_xml()

xy_plot = openmc.Plot()
xy_plot.filename = 'xyplot'
xy_plot.width = (280, 280)
xy_plot.pixels = (1000, 1000)
xy_plot.color_by = 'material'
xy_plot.origin = (0, 0, 130)

yz_plot = openmc.Plot()
yz_plot.filename = 'yzplot'
yz_plot.width = (280, 280)
yz_plot.pixels = (1000, 1000)
yz_plot.color_by = 'material'
yz_plot.basis = 'yz'
yz_plot.origin = (0, 0, 130)

plots = openmc.Plots([xy_plot, yz_plot])
plots.export_to_xml()

openmc.run(threads=1)
openmc.plot_geometry()
