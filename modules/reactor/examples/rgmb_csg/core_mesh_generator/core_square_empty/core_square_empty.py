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

rgmb_region_5 = openmc.Material(name="rgmb_region_5")
rgmb_region_5.add_nuclide('U235', 0.03)
rgmb_region_5.add_nuclide('U238', 0.97)
rgmb_region_5.add_nuclide('O16', 2.0)
rgmb_region_5.set_density('g/cm3', 10.0)

openmc_mats = openmc.Materials([rgmb_region_1, rgmb_region_2, rgmb_region_3, rgmb_region_4, rgmb_region_5])
openmc_mats.export_to_xml()

# Define surfaces
cmg_radial_ring = openmc.ZCylinder(r=5.68252, y0=0, x0=0, boundary_type='vacuum')
pin1_radial_duct_1_surf_0 = openmc.Plane(d=-0.68, b=-1, c=-1.23358e-18, a=-8.1634e-17)
pin1_radial_duct_1_surf_1 = openmc.Plane(d=-0.68, b=-1.63268e-16, c=0, a=1)
pin1_radial_duct_1_surf_2 = openmc.Plane(d=-0.68, b=1, c=0, a=1.63268e-16)
pin1_radial_duct_1_surf_3 = openmc.Plane(d=-0.68, b=2.44902e-16, c=-1.23358e-18, a=-1)
pin1_radial_ring_0 = openmc.ZCylinder(r=0.2, y0=0, x0=0)
pin3_radial_ring_0 = openmc.ZCylinder(r=0.3818, y0=0, x0=0)
rgmb_axial_plane_0 = openmc.Plane(d=0, b=0, c=1, a=0, boundary_type='vacuum')
rgmb_axial_plane_1 = openmc.Plane(d=1, b=0, c=1, a=0, boundary_type='vacuum')

# Define cells, universes, and lattices
empty_cell = openmc.Cell()
empty_univ = openmc.Universe(cells=[empty_cell])
pin2_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_2)
pin2_univ = openmc.Universe(cells=[pin2_cell_radial_0_axial_0])
pin1_cell_radial_2_axial_0 = openmc.Cell(fill=rgmb_region_5, region=(~(+pin1_radial_duct_1_surf_0 & +pin1_radial_duct_1_surf_1 & +pin1_radial_duct_1_surf_2 & +pin1_radial_duct_1_surf_3)))
pin1_cell_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_2, region=((+pin1_radial_duct_1_surf_0 & +pin1_radial_duct_1_surf_1 & +pin1_radial_duct_1_surf_2 & +pin1_radial_duct_1_surf_3) & ~(-pin1_radial_ring_0)))
pin1_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_1, region=(-pin1_radial_ring_0))
pin1_univ = openmc.Universe(cells=[pin1_cell_radial_0_axial_0, pin1_cell_radial_1_axial_0, pin1_cell_radial_2_axial_0])
pin3_cell_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_4, region=(~(-pin3_radial_ring_0)))
pin3_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_3, region=(-pin3_radial_ring_0))
pin3_univ = openmc.Universe(cells=[pin3_cell_radial_0_axial_0, pin3_cell_radial_1_axial_0])
amg2_lattice = openmc.RectLattice()
amg2_lattice.pitch = (1.42063, 1.42063)
amg2_lattice.lower_left = (-1.42063, -1.42063)
amg2_lattice.universes = [
  [pin3_univ, pin1_univ],
  [pin1_univ, pin2_univ]
]
amg2_lattice_cell = openmc.Cell(fill=amg2_lattice)
amg2_univ = openmc.Universe(cells=[amg2_lattice_cell])
amg1_lattice = openmc.RectLattice()
amg1_lattice.pitch = (1.42063, 1.42063)
amg1_lattice.lower_left = (-1.42063, -1.42063)
amg1_lattice.universes = [
  [pin2_univ, pin2_univ],
  [pin2_univ, pin2_univ]
]
amg1_lattice_cell = openmc.Cell(fill=amg1_lattice)
amg1_univ = openmc.Universe(cells=[amg1_lattice_cell])
cmg_lattice = openmc.RectLattice()
cmg_lattice.pitch = (2.84126, 2.84126)
cmg_lattice.lower_left = (-2.84126, -2.84126)
cmg_lattice.outer = empty_univ
cmg_lattice.universes = [
  [empty_univ, amg1_univ],
  [amg1_univ, amg2_univ]
]
cmg_lattice_cell = openmc.Cell(fill=cmg_lattice, region=(-cmg_radial_ring & +rgmb_axial_plane_0 & -rgmb_axial_plane_1))
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
xy_plot.width = (6, 6)
xy_plot.pixels = (1000, 1000)
xy_plot.color_by = 'material'
xy_plot.origin = (0, 0, 0.5)

yz_plot = openmc.Plot()
yz_plot.filename = 'yzplot'
yz_plot.width = (6, 6)
yz_plot.pixels = (1000, 1000)
yz_plot.color_by = 'material'
yz_plot.basis = 'yz'
yz_plot.origin = (0, 0, 0.5)

plots = openmc.Plots([xy_plot, yz_plot])
plots.export_to_xml()

openmc.run(threads=1)
openmc.plot_geometry()
