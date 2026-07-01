//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#include "PolygonDomainEngUnit.h"
#include "CSGNPolygonUnit.h"

namespace CSG
{

PolygonDomainEngUnit::PolygonDomainEngUnit(const std::string & name, unsigned int n_sides, Real apothem, const std::string & fill_mat, const std::string & insert_name)
  : CSGCellEngUnit(name, MooseUtils::prettyCppType<PolygonDomainEngUnit>()),
    _n_sides(n_sides),
    _apothem(apothem),
    _fill_mat(fill_mat),
    _insert_name(insert_name)
{
  if (_n_sides < 3)
    mooseError("Polygon domain engineering unit " + name + " must have 3 or more sides.");
  if (_apothem <= 0.0)
    mooseError("Polygon domain engineering unit " + name + " must have apothem that is positive.");
  if (_fill_mat.empty())
    mooseError("Fill material for polygon domain engineering unit must be specified");
  // TODO error checking on insert name, that it exists in CSGBase?
}

std::unordered_map<std::string, AttributeVariant>
PolygonDomainEngUnit::getAttributes() const
{
  return {{"num_sides", _n_sides}, {"apothem", _apothem}, {"fill_mat", _fill_mat}, {"insert_name", _insert_name}};
}

std::unique_ptr<CSGCellEngUnit>
PolygonDomainEngUnit::clone() const
{
  return std::make_unique<PolygonDomainEngUnit>(_name, _n_sides, _apothem, _fill_mat, _insert_name);
}

void
PolygonDomainEngUnit::expandUnit()
{
  // TODO handle insert_name
  if (!_insert_name.empty())
  {
    const auto & insert_root_cell = _internal_base->getCellByName(_insert_name + "_root_cell");
  }
  std::unique_ptr<CSG::CSGNPolygonUnit> polygon_ptr =
      std::make_unique<CSG::CSGNPolygonUnit>(_name + "_polygon_unit", _n_sides, _apothem);
  const auto & polygon_surf = _internal_base->addEngUnit(std::move(polygon_ptr));

  _internal_base->createCell(_name + "_cell", _fill_mat, -polygon_surf);
}

} // namespace CSG
