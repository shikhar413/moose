//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#pragma once

#include "CSGCellEngUnit.h"
#include "CSGBase.h"

namespace CSG
{

/**
 * PolygonDomainEngUnit is a CSGCellEngUnit that represents a regular N-sided polygon
 * (prismatic region) with its axis aligned with the z-axis. The polygon can have an
 * optional insert, which represents another CSGCellEngUnit that is inserted into
 * the polygon domain
 *
 * The polygon is defined by N infinite planes, one per side, each oriented so that
 * its inward normal points toward the center. The interior of the polygon is the
 * intersection of the N negative half-spaces of those planes.
 *
 * Implements:
 *   - expandUnit(): creates N CSGPlane surfaces in _internal_base, one per side
 *   - clone(): returns a deep copy
 *   - getAttributes(): returns n_sides, apothem, fill material, and name of insert
 */
class PolygonDomainEngUnit : public CSGCellEngUnit
{
public:
  /**
   * @brief Constructor for PolygonDomainEngUnit
   *
   * @param name unique name of the unit
   * @param n_sides number of sides of the regular polygon (must be >= 3)
   * @param apothem distance from the center to the midpoint of each side
   * @param fill_mat name of fill material in polygon domain
   * @param insert_name name of CSGCellEngUnit that is inserted into polygon domain
   */
  PolygonDomainEngUnit(const std::string & name, unsigned int n_sides, Real apothem, const std::string & fill_mat, const std::string & insert_name);

  /**
   * @brief Return the polygon domain attributes for this object.
   *
   * @return map containing: n_sides (unsigned int), apothem (Real), fill_mat (std::string), and insert_name (std::string)
   */
  std::unordered_map<std::string, AttributeVariant> getAttributes() const override;

protected:
  /**
   * @brief Return a deep copy of this unit.
   *
   * @return unique_ptr to a new PolygonDomainEngUnit with identical parameters
   */
  std::unique_ptr<CSGCellEngUnit> clone() const override;

  /**
   * @brief Represent the polygon domain as a universe filled with the linked insert name
   */
  void expandUnit() override;

private:
  /// Number of sides of the regular polygon
  const int _n_sides;

  /// Distance from the polygon center to the midpoint of each side
  const Real _apothem;

  /// Distance from the polygon center to the midpoint of each side
  const std::string _fill_mat;

  /// Name of insert linked to unit
  std::string _insert_name;
};

} // namespace CSG
