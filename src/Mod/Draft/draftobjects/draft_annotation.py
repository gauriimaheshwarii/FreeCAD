# ***************************************************************************
# *   (c) 2020 Carlo Pavan                                                  *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

"""This module provides the object code for Draft DimensionStyle.
"""
## @package style_dimension
# \ingroup DRAFT
# \brief This module provides the object code for Draft DimensionStyle.

import FreeCAD as App
from PySide.QtCore import QT_TRANSLATE_NOOP
from draftutils import gui_utils

class DraftAnnotation:
    """The Draft Annotation Base object"""
    def __init__(self,obj,tp="Unknown"):
        if obj:
            obj.Proxy = self
        self.Type = tp

    def __getstate__(self):
        return self.Type

    def __setstate__(self,state):
        if state:
            self.Type = state

    def execute(self,obj):
        pass

    def onChanged(self, obj, prop):
        pass



class DimensionBase(DraftAnnotation):
    """The Draft Dimension Base object"""

    def __init__(self, obj, tp = "Dimension"):
        "Initialize common properties for dimension objects"
        DraftAnnotation.__init__(self,obj, tp)
        
        # Annotation
        obj.addProperty("App::PropertyLink","DimensionStyle",
                        "Annotation",
                        QT_TRANSLATE_NOOP("App::Property",
                                          "Link dimension style"))

    def onChanged(self,obj,prop):
        
        if prop == "DimensionStyle":
            if hasattr(obj, "DimensionStyle"):
                gui_utils.format_object(target = obj, origin = obj.DimensionStyle)


    def execute(self, obj):
        
        return
