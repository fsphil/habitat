# Copyright 2011 (C) Adam Greig
#
# This file is part of habitat.
#
# habitat is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# habitat is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with habitat.  If not, see <http://www.gnu.org/licenses/>.

"""
Parser parses received telemetry into useful data.

.. autosummary::
    :toctree: habitat

    habitat.parser.parser
    habitat.parser.sensor_manager
    habitat.parser.parser_modules
    habitat.parser.sensors
"""

__all__ = ["parser", "sensor_manager", "parser_modules", "sensors"]

from . import parser
