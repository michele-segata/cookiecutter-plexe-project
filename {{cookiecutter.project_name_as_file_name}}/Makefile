
#
# Copyright (C) 2019 Christoph Sommer <sommer@ccs-labs.org>
#
# Documentation for these modules is at http://veins.car2x.org/
#
# SPDX-License-Identifier: GPL-2.0-or-later
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

.PHONY: all clean

all:
	$(MAKE) -C veins all
	$(MAKE) -C plexe all

{%- if cookiecutter.use_hetnet == "yes" %}
ifdef MODE
	$(MAKE) -C inet all
else
	$(MAKE) -C inet all MODE=release
	$(MAKE) -C inet all MODE=debug
endif
	$(MAKE) -C veins/subprojects/veins_inet all
	$(MAKE) -C veins_vlc all

ifdef MODE
	$(MAKE) -C simulte all
else
	$(MAKE) -C simulte all MODE=release
	$(MAKE) -C simulte all MODE=debug
endif

	$(MAKE) -C plexe/subprojects/plexe_vlc all
	$(MAKE) -C plexe/subprojects/plexe_lte all
	$(MAKE) -C plexe/subprojects/plexe_hetnet all
{%- endif %}

clean:
	$(MAKE) -C veins clean
	$(MAKE) -C plexe clean
{%- if cookiecutter.use_hetnet == "yes" %}
	$(MAKE) -C inet clean
	$(MAKE) -C veins/subprojects/veins_inet clean
	$(MAKE) -C veins_vlc clean
	$(MAKE) -C simulte clean
	$(MAKE) -C plexe/subprojects/plexe_vlc clean
	$(MAKE) -C plexe/subprojects/plexe_lte clean
	$(MAKE) -C plexe/subprojects/plexe_hetnet clean
{%- endif %}
