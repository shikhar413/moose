import openmc

# Define material fills as materials
rgmb_region_2 = openmc.Material(name="rgmb_region_2")
rgmb_region_2.add_nuclide('U235', 0.03)
rgmb_region_2.add_nuclide('U238', 0.97)
rgmb_region_2.add_nuclide('O16', 2.0)
rgmb_region_2.set_density('g/cm3', 10.0)

openmc_mats = openmc.Materials([rgmb_region_2])
openmc_mats.export_to_xml()

# Define surfaces
cmg_radial_ring = openmc.ZCylinder(r=3.55158, y0=0, x0=0, boundary_type='vacuum')
rgmb_axial_plane_0 = openmc.Plane(d=0, b=0, c=1, a=0, boundary_type='vacuum')
rgmb_axial_plane_1 = openmc.Plane(d=1, b=0, c=1, a=0, boundary_type='vacuum')

# Define cells, universes, and lattices
empty_cell = openmc.Cell()
empty_univ = openmc.Universe(cells=[empty_cell])
pin2_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_2)
pin2_univ = openmc.Universe(cells=[pin2_cell_radial_0_axial_0])
pin1_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_2)
pin1_univ = openmc.Universe(cells=[pin1_cell_radial_0_axial_0])
cmg_lattice = openmc.HexLattice()
cmg_lattice.orientation = 'x'
cmg_lattice.pitch = (1.42063,)
cmg_lattice.center = (0, 0)
cmg_lattice.outer = empty_univ
cmg_lattice.universes = [
  [empty_univ, pin2_univ, empty_univ, pin2_univ, empty_univ, pin2_univ],
  [pin1_univ]
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
