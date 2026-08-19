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

rgmb_region_2 = openmc.Material(name="rgmb_region_2")
rgmb_region_2.add_nuclide('U235', 0.03)
rgmb_region_2.add_nuclide('U238', 0.97)
rgmb_region_2.add_nuclide('O16', 2.0)
rgmb_region_2.set_density('g/cm3', 10.0)

rgmb_region_20 = openmc.Material(name="rgmb_region_20")
rgmb_region_20.add_nuclide('U235', 0.03)
rgmb_region_20.add_nuclide('U238', 0.97)
rgmb_region_20.add_nuclide('O16', 2.0)
rgmb_region_20.set_density('g/cm3', 10.0)

rgmb_region_3 = openmc.Material(name="rgmb_region_3")
rgmb_region_3.add_nuclide('U235', 0.03)
rgmb_region_3.add_nuclide('U238', 0.97)
rgmb_region_3.add_nuclide('O16', 2.0)
rgmb_region_3.set_density('g/cm3', 10.0)

rgmb_region_30 = openmc.Material(name="rgmb_region_30")
rgmb_region_30.add_nuclide('U235', 0.03)
rgmb_region_30.add_nuclide('U238', 0.97)
rgmb_region_30.add_nuclide('O16', 2.0)
rgmb_region_30.set_density('g/cm3', 10.0)

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

openmc_mats = openmc.Materials([rgmb_region_1, rgmb_region_10, rgmb_region_2, rgmb_region_20, rgmb_region_3, rgmb_region_30, rgmb_region_4, rgmb_region_5])
openmc_mats.export_to_xml()

# Define surfaces
cmg_radial_boundary = openmc.ZCylinder(r=15, y0=0, x0=0, boundary_type='vacuum')
pin1_ducted_pin_unit_pin_unit_radial_ring_0 = openmc.ZCylinder(r=0.2, y0=0, x0=0)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 = openmc.Plane(d=0.68, b=0, c=0, a=1)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 = openmc.Plane(d=0.68, b=0.866025, c=0, a=0.5)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 = openmc.Plane(d=0.68, b=0.866025, c=0, a=-0.5)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 = openmc.Plane(d=0.68, b=1.22465e-16, c=0, a=-1)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 = openmc.Plane(d=0.68, b=-0.866025, c=0, a=-0.5)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5 = openmc.Plane(d=0.68, b=-0.866025, c=0, a=0.5)
pin3_ducted_pin_unit_pin_unit_radial_ring_0 = openmc.ZCylinder(r=0.3818, y0=0, x0=0)
rgmb_axial_plane_bottom_boundary = openmc.Plane(d=0, b=0, c=1, a=0, boundary_type='vacuum')
rgmb_axial_plane_top_boundary = openmc.Plane(d=1, b=0, c=1, a=0, boundary_type='vacuum')

# Define cells, universes, and lattices
amg2_lattice_outer_axial_0 = openmc.Cell(fill=rgmb_region_20)
amg2_lattice_outer_univ = openmc.Universe(cells=[amg2_lattice_outer_axial_0])
pin1_ducted_pin_unit_cell_radial_1 = openmc.Cell(fill=rgmb_region_5, region=(~(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5)))
pin1_ducted_pin_unit_pin_unit_cell_radial_1 = openmc.Cell(fill=rgmb_region_2, region=(~(-pin1_ducted_pin_unit_pin_unit_radial_ring_0)))
pin1_ducted_pin_unit_pin_unit_cell_radial_0 = openmc.Cell(fill=rgmb_region_1, region=(-pin1_ducted_pin_unit_pin_unit_radial_ring_0))
pin1_ducted_pin_unit_pin_unit_expanded_root = openmc.Universe(cells=[pin1_ducted_pin_unit_pin_unit_cell_radial_0, pin1_ducted_pin_unit_pin_unit_cell_radial_1])
pin1_ducted_pin_unit_cell_radial_0 = openmc.Cell(fill=pin1_ducted_pin_unit_pin_unit_expanded_root, region=(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5))
pin1_ducted_pin_unit_expanded_root = openmc.Universe(cells=[pin1_ducted_pin_unit_cell_radial_0, pin1_ducted_pin_unit_cell_radial_1])
pin3_ducted_pin_unit_pin_unit_cell_radial_1 = openmc.Cell(fill=rgmb_region_4, region=(~(-pin3_ducted_pin_unit_pin_unit_radial_ring_0)))
pin3_ducted_pin_unit_pin_unit_cell_radial_0 = openmc.Cell(fill=rgmb_region_3, region=(-pin3_ducted_pin_unit_pin_unit_radial_ring_0))
pin3_ducted_pin_unit_pin_unit_expanded_root = openmc.Universe(cells=[pin3_ducted_pin_unit_pin_unit_cell_radial_0, pin3_ducted_pin_unit_pin_unit_cell_radial_1])
pin3_ducted_pin_unit_cell_radial_0 = openmc.Cell(fill=pin3_ducted_pin_unit_pin_unit_expanded_root)
pin3_ducted_pin_unit_expanded_root = openmc.Universe(cells=[pin3_ducted_pin_unit_cell_radial_0])
amg2_lattice_unrotated = openmc.HexLattice()
amg2_lattice_unrotated.orientation = 'x'
amg2_lattice_unrotated.pitch = (1.42063,)
amg2_lattice_unrotated.center = (0, 0)
amg2_lattice_unrotated.outer = amg2_lattice_outer_univ
amg2_lattice_unrotated.universes = [
  [pin1_ducted_pin_unit_expanded_root, pin1_ducted_pin_unit_expanded_root, pin3_ducted_pin_unit_expanded_root, pin1_ducted_pin_unit_expanded_root, pin1_ducted_pin_unit_expanded_root, pin1_ducted_pin_unit_expanded_root],
  [pin3_ducted_pin_unit_expanded_root]
]
amg2_lattice_cell = openmc.Cell(fill=amg2_lattice_unrotated)
amg2_lattice_cell.rotation = (0, 0, 90)
amg2_lattice = openmc.Universe(cells=[amg2_lattice_cell])
amg2_lattice_cell = openmc.Cell(fill=amg2_lattice)
amg2_univ = openmc.Universe(cells=[amg2_lattice_cell])
amg1_lattice_outer_axial_0 = openmc.Cell(fill=rgmb_region_10)
amg1_lattice_outer_univ = openmc.Universe(cells=[amg1_lattice_outer_axial_0])
pin2_ducted_pin_unit_cell_radial_0 = openmc.Cell(fill=rgmb_region_2)
pin2_ducted_pin_unit_expanded_root = openmc.Universe(cells=[pin2_ducted_pin_unit_cell_radial_0])
amg1_lattice_unrotated = openmc.HexLattice()
amg1_lattice_unrotated.orientation = 'x'
amg1_lattice_unrotated.pitch = (1.42063,)
amg1_lattice_unrotated.center = (0, 0)
amg1_lattice_unrotated.outer = amg1_lattice_outer_univ
amg1_lattice_unrotated.universes = [
  [pin2_ducted_pin_unit_expanded_root, pin2_ducted_pin_unit_expanded_root, pin2_ducted_pin_unit_expanded_root, pin2_ducted_pin_unit_expanded_root, pin2_ducted_pin_unit_expanded_root, pin2_ducted_pin_unit_expanded_root],
  [pin2_ducted_pin_unit_expanded_root]
]
amg1_lattice_cell = openmc.Cell(fill=amg1_lattice_unrotated)
amg1_lattice_cell.rotation = (0, 0, 90)
amg1_lattice = openmc.Universe(cells=[amg1_lattice_cell])
amg1_lattice_cell = openmc.Cell(fill=amg1_lattice)
amg1_univ = openmc.Universe(cells=[amg1_lattice_cell])
rgmb_region_30_cell = openmc.Cell(fill=rgmb_region_30)
rgmb_region_30_univ = openmc.Universe(cells=[rgmb_region_30_cell])
cmg_lattice = openmc.HexLattice()
cmg_lattice.orientation = 'x'
cmg_lattice.pitch = (7.10315,)
cmg_lattice.center = (0, 0)
cmg_lattice.outer = rgmb_region_30_univ
cmg_lattice.universes = [
  [amg2_univ, amg2_univ, amg2_univ, amg2_univ, amg2_univ, amg2_univ],
  [amg1_univ]
]
cmg_lattice_cell = openmc.Cell(fill=cmg_lattice, region=(-cmg_radial_boundary & +rgmb_axial_plane_bottom_boundary & -rgmb_axial_plane_top_boundary))
root_universe = openmc.Universe(cells=[cmg_lattice_cell])
geom = openmc.Geometry(root_universe)
geom.export_to_xml()

# Define settings
point = openmc.stats.Point((0, 0, 0.5))
src = openmc.Source(space=point)
settings = openmc.Settings()
settings.source = src
settings.batches = 100
settings.inactive = 10
settings.particles = 1000
settings.export_to_xml()

xy_plot = openmc.Plot()
xy_plot.filename = 'xyplot'
xy_plot.width = (30, 30)
xy_plot.pixels = (1000, 1000)
xy_plot.color_by = 'material'
xy_plot.origin = (0, 0, 0.5)

yz_plot = openmc.Plot()
yz_plot.filename = 'yzplot'
yz_plot.width = (30, 30)
yz_plot.pixels = (1000, 1000)
yz_plot.color_by = 'material'
yz_plot.basis = 'yz'
yz_plot.origin = (0, 0, 0.5)

plots = openmc.Plots([xy_plot, yz_plot])
plots.export_to_xml()

openmc.run(threads=1)
openmc.plot_geometry()
