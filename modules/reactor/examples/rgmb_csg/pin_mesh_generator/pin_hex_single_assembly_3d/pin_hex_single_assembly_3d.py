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

openmc_mats = openmc.Materials([rgmb_region_1, rgmb_region_2, rgmb_region_3])
openmc_mats.export_to_xml()

# Define surfaces
pin1_radial_duct_1_surf_0 = openmc.Plane(d=-3, b=-0.866025, c=-1.06831e-18, a=-0.5)
pin1_radial_duct_1_surf_1 = openmc.Plane(d=-3, b=-0.866025, c=8.0507e-18, a=0.5)
pin1_radial_duct_1_surf_2 = openmc.Plane(d=-3, b=-3.84593e-16, c=7.40149e-18, a=1)
pin1_radial_duct_1_surf_3 = openmc.Plane(d=-3, b=0.866025, c=1.06831e-18, a=0.5)
pin1_radial_duct_1_surf_4 = openmc.Plane(d=-3, b=0.866025, c=1.64082e-18, a=-0.5)
pin1_radial_duct_1_surf_5 = openmc.Plane(d=-3, b=7.69185e-16, c=0, a=-1)
pin1_radial_duct_2_surf_0 = openmc.Plane(d=-3.55157, b=-0.866025, c=-5.25613e-18, a=-0.5, boundary_type='vacuum')
pin1_radial_duct_2_surf_1 = openmc.Plane(d=-3.55158, b=-0.866025, c=-9.64573e-18, a=0.5, boundary_type='vacuum')
pin1_radial_duct_2_surf_2 = openmc.Plane(d=-3.55157, b=-3.24864e-16, c=-7.40149e-18, a=1, boundary_type='vacuum')
pin1_radial_duct_2_surf_3 = openmc.Plane(d=-3.55157, b=0.866025, c=-8.37219e-19, a=0.5, boundary_type='vacuum')
pin1_radial_duct_2_surf_4 = openmc.Plane(d=-3.55157, b=0.866025, c=-5.22682e-18, a=-0.5, boundary_type='vacuum')
pin1_radial_duct_2_surf_5 = openmc.Plane(d=-3.55158, b=6.49727e-16, c=0, a=-1, boundary_type='vacuum')
pin1_radial_ring_0 = openmc.ZCylinder(r=2, y0=0, x0=0)
rgmb_axial_plane_0 = openmc.Plane(d=0, b=0, c=1, a=0, boundary_type='vacuum')
rgmb_axial_plane_1 = openmc.Plane(d=1, b=0, c=1, a=0, boundary_type='vacuum')

# Define cells, universes, and lattices
pin1_cell_radial_2_axial_0 = openmc.Cell(fill=rgmb_region_3, region=(~(+pin1_radial_duct_1_surf_0 & +pin1_radial_duct_1_surf_1 & +pin1_radial_duct_1_surf_2 & +pin1_radial_duct_1_surf_3 & +pin1_radial_duct_1_surf_4 & +pin1_radial_duct_1_surf_5)))
pin1_cell_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_2, region=((+pin1_radial_duct_1_surf_0 & +pin1_radial_duct_1_surf_1 & +pin1_radial_duct_1_surf_2 & +pin1_radial_duct_1_surf_3 & +pin1_radial_duct_1_surf_4 & +pin1_radial_duct_1_surf_5) & ~(-pin1_radial_ring_0)))
pin1_cell_radial_0_axial_0 = openmc.Cell(fill=rgmb_region_1, region=(-pin1_radial_ring_0))
pin1_univ = openmc.Universe(cells=[pin1_cell_radial_0_axial_0, pin1_cell_radial_1_axial_0, pin1_cell_radial_2_axial_0])
pin1_root_cell = openmc.Cell(fill=pin1_univ, region=(+pin1_radial_duct_2_surf_0 & +pin1_radial_duct_2_surf_1 & +pin1_radial_duct_2_surf_2 & +pin1_radial_duct_2_surf_3 & +pin1_radial_duct_2_surf_4 & +pin1_radial_duct_2_surf_5 & +rgmb_axial_plane_0 & -rgmb_axial_plane_1))
root_universe = openmc.Universe(cells=[pin1_root_cell])
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
xy_plot.width = (10, 10)
xy_plot.pixels = (1000, 1000)
xy_plot.color_by = 'material'
xy_plot.origin = (0, 0, 0.5)

yz_plot = openmc.Plot()
yz_plot.filename = 'yzplot'
yz_plot.width = (10, 10)
yz_plot.pixels = (1000, 1000)
yz_plot.color_by = 'material'
yz_plot.basis = 'yz'
yz_plot.origin = (0, 0, 0.5)

plots = openmc.Plots([xy_plot, yz_plot])
plots.export_to_xml()

openmc.run(threads=1)
openmc.plot_geometry()
