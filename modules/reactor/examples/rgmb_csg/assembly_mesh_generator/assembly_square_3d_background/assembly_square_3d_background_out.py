import openmc

# Define material fills as materials
rgmb_region_1 = openmc.Material(name="rgmb_region_1")
rgmb_region_1.add_nuclide('U235', 0.03)
rgmb_region_1.add_nuclide('U238', 0.97)
rgmb_region_1.add_nuclide('O16', 2.0)
rgmb_region_1.set_density('g/cm3', 10.0)

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

rgmb_region_13 = openmc.Material(name="rgmb_region_13")
rgmb_region_13.add_nuclide('U235', 0.03)
rgmb_region_13.add_nuclide('U238', 0.97)
rgmb_region_13.add_nuclide('O16', 2.0)
rgmb_region_13.set_density('g/cm3', 10.0)

rgmb_region_15 = openmc.Material(name="rgmb_region_15")
rgmb_region_15.add_nuclide('U235', 0.03)
rgmb_region_15.add_nuclide('U238', 0.97)
rgmb_region_15.add_nuclide('O16', 2.0)
rgmb_region_15.set_density('g/cm3', 10.0)

rgmb_region_16 = openmc.Material(name="rgmb_region_16")
rgmb_region_16.add_nuclide('U235', 0.03)
rgmb_region_16.add_nuclide('U238', 0.97)
rgmb_region_16.add_nuclide('O16', 2.0)
rgmb_region_16.set_density('g/cm3', 10.0)

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

openmc_mats = openmc.Materials([rgmb_region_1, rgmb_region_11, rgmb_region_12, rgmb_region_13, rgmb_region_15, rgmb_region_16, rgmb_region_2, rgmb_region_3, rgmb_region_5, rgmb_region_6])
openmc_mats.export_to_xml()

# Define surfaces
amg_radial_boundary_expanded_surf_0 = openmc.Plane(d=1.42063, b=0, c=0, a=1, boundary_type='vacuum')
amg_radial_boundary_expanded_surf_1 = openmc.Plane(d=1.42063, b=1, c=0, a=6.12323e-17, boundary_type='vacuum')
amg_radial_boundary_expanded_surf_2 = openmc.Plane(d=1.42063, b=1.22465e-16, c=0, a=-1, boundary_type='vacuum')
amg_radial_boundary_expanded_surf_3 = openmc.Plane(d=1.42063, b=-1, c=0, a=-1.83697e-16, boundary_type='vacuum')
pin1_ducted_pin_unit_pin_unit_axial_0_radial_ring_0 = openmc.ZCylinder(r=0.2, y0=0, x0=0)
pin1_ducted_pin_unit_pin_unit_axial_1_radial_ring_0 = openmc.ZCylinder(r=0.2, y0=0, x0=0)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 = openmc.Plane(d=0.58, b=0, c=0, a=1)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 = openmc.Plane(d=0.58, b=1, c=0, a=6.12323e-17)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 = openmc.Plane(d=0.58, b=1.22465e-16, c=0, a=-1)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 = openmc.Plane(d=0.58, b=-1, c=0, a=-1.83697e-16)
rgmb_axial_plane_0 = openmc.Plane(d=1, b=0, c=1, a=0)
rgmb_axial_plane_bottom_boundary = openmc.Plane(d=0, b=0, c=1, a=0, boundary_type='vacuum')
rgmb_axial_plane_top_boundary = openmc.Plane(d=2, b=0, c=1, a=0, boundary_type='vacuum')

# Define cells, universes, and lattices
amg_lattice_outer_axial_1 = openmc.Cell(fill=rgmb_region_16, region=(+rgmb_axial_plane_0))
amg_lattice_outer_axial_0 = openmc.Cell(fill=rgmb_region_6, region=(-rgmb_axial_plane_0))
amg_lattice_outer_univ = openmc.Universe(cells=[amg_lattice_outer_axial_0, amg_lattice_outer_axial_1])
pin2_ducted_pin_unit_cell_radial_0_axial_1 = openmc.Cell(fill=rgmb_region_13, region=(+rgmb_axial_plane_0))
pin2_ducted_pin_unit_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_3, region=(-rgmb_axial_plane_0))
pin2_ducted_pin_unit_expanded_root = openmc.Universe(cells=[pin2_ducted_pin_unit_cell_radial_0_axial_0, pin2_ducted_pin_unit_cell_radial_0_axial_1])
pin1_ducted_pin_unit_cell_radial_1_axial_1 = openmc.Cell(fill=rgmb_region_15, region=(~(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3) & +rgmb_axial_plane_0))
pin1_ducted_pin_unit_cell_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_5, region=(~(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3) & -rgmb_axial_plane_0))
pin1_ducted_pin_unit_pin_unit_axial_1_cell_radial_1 = openmc.Cell(fill=rgmb_region_12, region=(~(-pin1_ducted_pin_unit_pin_unit_axial_1_radial_ring_0)))
pin1_ducted_pin_unit_pin_unit_axial_1_cell_radial_0 = openmc.Cell(fill=rgmb_region_11, region=(-pin1_ducted_pin_unit_pin_unit_axial_1_radial_ring_0))
pin1_ducted_pin_unit_pin_unit_axial_1_expanded_root = openmc.Universe(cells=[pin1_ducted_pin_unit_pin_unit_axial_1_cell_radial_0, pin1_ducted_pin_unit_pin_unit_axial_1_cell_radial_1])
pin1_ducted_pin_unit_cell_radial_0_axial_1 = openmc.Cell(fill=pin1_ducted_pin_unit_pin_unit_axial_1_expanded_root, region=(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 & +rgmb_axial_plane_0))
pin1_ducted_pin_unit_pin_unit_axial_0_cell_radial_1 = openmc.Cell(fill=rgmb_region_2, region=(~(-pin1_ducted_pin_unit_pin_unit_axial_0_radial_ring_0)))
pin1_ducted_pin_unit_pin_unit_axial_0_cell_radial_0 = openmc.Cell(fill=rgmb_region_1, region=(-pin1_ducted_pin_unit_pin_unit_axial_0_radial_ring_0))
pin1_ducted_pin_unit_pin_unit_axial_0_expanded_root = openmc.Universe(cells=[pin1_ducted_pin_unit_pin_unit_axial_0_cell_radial_0, pin1_ducted_pin_unit_pin_unit_axial_0_cell_radial_1])
pin1_ducted_pin_unit_cell_radial_0_axial_0 = openmc.Cell(fill=pin1_ducted_pin_unit_pin_unit_axial_0_expanded_root, region=(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -rgmb_axial_plane_0))
pin1_ducted_pin_unit_expanded_root = openmc.Universe(cells=[pin1_ducted_pin_unit_cell_radial_0_axial_0, pin1_ducted_pin_unit_cell_radial_0_axial_1, pin1_ducted_pin_unit_cell_radial_1_axial_0, pin1_ducted_pin_unit_cell_radial_1_axial_1])
amg_lattice = openmc.RectLattice()
amg_lattice.pitch = (1.25, 1.25)
amg_lattice.lower_left = (-1.25, -1.25)
amg_lattice.outer = amg_lattice_outer_univ
amg_lattice.universes = [
  [pin1_ducted_pin_unit_expanded_root, pin1_ducted_pin_unit_expanded_root],
  [pin1_ducted_pin_unit_expanded_root, pin2_ducted_pin_unit_expanded_root]
]
amg_lattice_cell = openmc.Cell(fill=amg_lattice)
amg_univ = openmc.Universe(cells=[amg_lattice_cell])
amg_root_cell = openmc.Cell(fill=amg_univ, region=(-amg_radial_boundary_expanded_surf_0 & -amg_radial_boundary_expanded_surf_1 & -amg_radial_boundary_expanded_surf_2 & -amg_radial_boundary_expanded_surf_3 & +rgmb_axial_plane_bottom_boundary & -rgmb_axial_plane_top_boundary))
root_universe = openmc.Universe(cells=[amg_root_cell])
geom = openmc.Geometry(root_universe)
geom.export_to_xml()

# Define settings
point = openmc.stats.Point((0, 0, 1))
src = openmc.Source(space=point)
settings = openmc.Settings()
settings.source = src
settings.batches = 100
settings.inactive = 10
settings.particles = 1000
settings.export_to_xml()

xy_plot = openmc.Plot()
xy_plot.filename = 'xyplot'
xy_plot.width = (3, 3)
xy_plot.pixels = (1000, 1000)
xy_plot.color_by = 'material'
xy_plot.origin = (0, 0, 1)

yz_plot = openmc.Plot()
yz_plot.filename = 'yzplot'
yz_plot.width = (3, 3)
yz_plot.pixels = (1000, 1000)
yz_plot.color_by = 'material'
yz_plot.basis = 'yz'
yz_plot.origin = (0, 0, 1)

plots = openmc.Plots([xy_plot, yz_plot])
plots.export_to_xml()

openmc.run(threads=1)
openmc.plot_geometry()
