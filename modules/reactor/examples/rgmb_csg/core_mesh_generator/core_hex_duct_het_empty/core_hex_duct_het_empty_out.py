import openmc

# Define material fills as materials
rgmb_region_1 = openmc.Material(name="rgmb_region_1")
rgmb_region_1.add_nuclide('U235', 0.03)
rgmb_region_1.add_nuclide('U238', 0.97)
rgmb_region_1.add_nuclide('O16', 2.0)
rgmb_region_1.set_density('g/cm3', 10.0)

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

openmc_mats = openmc.Materials([rgmb_region_1, rgmb_region_2, rgmb_region_3, rgmb_region_4])
openmc_mats.export_to_xml()

# Define surfaces
cmg_radial_boundary = openmc.ZCylinder(r=3.55158, y0=0, x0=0, boundary_type='vacuum')
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 = openmc.Plane(d=0.5, b=0, c=0, a=1)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 = openmc.Plane(d=0.5, b=0.866025, c=0, a=0.5)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 = openmc.Plane(d=0.5, b=0.866025, c=0, a=-0.5)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 = openmc.Plane(d=0.5, b=1.22465e-16, c=0, a=-1)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 = openmc.Plane(d=0.5, b=-0.866025, c=0, a=-0.5)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5 = openmc.Plane(d=0.5, b=-0.866025, c=0, a=0.5)
pin2_ducted_pin_unit_radial_duct_0_expanded_surf_0 = openmc.Plane(d=0.6, b=0, c=0, a=1)
pin2_ducted_pin_unit_radial_duct_0_expanded_surf_1 = openmc.Plane(d=0.6, b=0.866025, c=0, a=0.5)
pin2_ducted_pin_unit_radial_duct_0_expanded_surf_2 = openmc.Plane(d=0.6, b=0.866025, c=0, a=-0.5)
pin2_ducted_pin_unit_radial_duct_0_expanded_surf_3 = openmc.Plane(d=0.6, b=1.22465e-16, c=0, a=-1)
pin2_ducted_pin_unit_radial_duct_0_expanded_surf_4 = openmc.Plane(d=0.6, b=-0.866025, c=0, a=-0.5)
pin2_ducted_pin_unit_radial_duct_0_expanded_surf_5 = openmc.Plane(d=0.6, b=-0.866025, c=0, a=0.5)
rgmb_axial_plane_bottom_boundary = openmc.Plane(d=0, b=0, c=1, a=0, boundary_type='vacuum')
rgmb_axial_plane_top_boundary = openmc.Plane(d=1, b=0, c=1, a=0, boundary_type='vacuum')

# Define cells, universes, and lattices
empty_cell = openmc.Cell()
empty_univ = openmc.Universe(cells=[empty_cell])
pin2_ducted_pin_unit_cell_radial_1 = openmc.Cell(fill=rgmb_region_4, region=(~(-pin2_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin2_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin2_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin2_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -pin2_ducted_pin_unit_radial_duct_0_expanded_surf_4 & -pin2_ducted_pin_unit_radial_duct_0_expanded_surf_5)))
pin2_ducted_pin_unit_cell_radial_0 = openmc.Cell(fill=rgmb_region_3, region=(-pin2_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin2_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin2_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin2_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -pin2_ducted_pin_unit_radial_duct_0_expanded_surf_4 & -pin2_ducted_pin_unit_radial_duct_0_expanded_surf_5))
pin2_ducted_pin_unit_expanded_root = openmc.Universe(cells=[pin2_ducted_pin_unit_cell_radial_0, pin2_ducted_pin_unit_cell_radial_1])
pin1_ducted_pin_unit_cell_radial_1 = openmc.Cell(fill=rgmb_region_2, region=(~(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5)))
pin1_ducted_pin_unit_cell_radial_0 = openmc.Cell(fill=rgmb_region_1, region=(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5))
pin1_ducted_pin_unit_expanded_root = openmc.Universe(cells=[pin1_ducted_pin_unit_cell_radial_0, pin1_ducted_pin_unit_cell_radial_1])
cmg_lattice = openmc.HexLattice()
cmg_lattice.orientation = 'x'
cmg_lattice.pitch = (1.42063,)
cmg_lattice.center = (0, 0)
cmg_lattice.outer = empty_univ
cmg_lattice.universes = [
  [empty_univ, pin2_ducted_pin_unit_expanded_root, empty_univ, pin2_ducted_pin_unit_expanded_root, empty_univ, pin2_ducted_pin_unit_expanded_root],
  [pin1_ducted_pin_unit_expanded_root]
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
xy_plot.width = (5, 5)
xy_plot.pixels = (1000, 1000)
xy_plot.color_by = 'material'
xy_plot.origin = (0, 0, 0.5)

yz_plot = openmc.Plot()
yz_plot.filename = 'yzplot'
yz_plot.width = (5, 5)
yz_plot.pixels = (1000, 1000)
yz_plot.color_by = 'material'
yz_plot.basis = 'yz'
yz_plot.origin = (0, 0, 0.5)

plots = openmc.Plots([xy_plot, yz_plot])
plots.export_to_xml()

openmc.run(threads=1)
openmc.plot_geometry()
