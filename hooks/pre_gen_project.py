
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

import subprocess
import sys
from re import search, match
from subprocess import run, PIPE


def get_omnet_version():
    major = 0
    try:
        result = run(['opp_run', '-v'], stdout=PIPE)
        if not result.returncode == 0:
            err("Cannot check for OMNeT++ version. Is opp_run in your PATH?")
            exit(1)
        version = search("Version: (.*?),", result.stdout.decode())
        if version:
            version_string = version.group(1)
            version_parts = version_string.split(".")
            major = int(version_parts[0])
    except FileNotFoundError:
        err("Cannot check for OMNeT++ version. Is opp_run in your PATH?")
        exit(1)
    return major


project_name_as_file_name = '{{ cookiecutter.project_name_as_file_name }}'
project_name_as_macro_name = '{{ cookiecutter.project_name_as_macro_name }}'
use_hetnet = '{{ cookiecutter.use_hetnet }}'

print('Cookiecutter checks starting.')

print('Making sure we can run git')
subprocess.check_call(['git', '--version'])

if not match(r'^[a-z0-9_]+$', project_name_as_file_name):
    print('ERROR: project_name_as_file_name "%s" does not solely consist of characters a-z, 0-9, and underscore.' % project_name_as_file_name)
    sys.exit(1)

if not match(r'^[A-Z0-9_]+$', project_name_as_macro_name):
    print('ERROR: project_name_as_macro_name "%s" does not solely consist of characters A-Z, 0-9, and underscore.' % project_name_as_macro_name)
    sys.exit(1)

if use_hetnet == "yes" and get_omnet_version() >= 6:
    print('ERROR: OMNeT++ version 6 is not supported by some of the frameworks required for Plexe with heterogenous interfaces. Please use OMNeT++ version 5.7.')
    sys.exit(1)

print('Cookiecutter checks successful.')
