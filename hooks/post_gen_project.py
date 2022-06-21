
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
import os
import subprocess

print('Cookiecutter successful. Running git commands to set up repository.')
subprocess.check_call(['git', 'init'])
subprocess.check_call(['git', 'config', 'user.name', 'Michele Segata'])
subprocess.check_call(['git', 'config', 'user.email', 'segata@ccs-labs.org'])
subprocess.check_call(['git', 'commit', '--allow-empty', '--message', 'Initial commit'])

{%- if cookiecutter.use_hetnet == "yes" %}

# INET
subprocess.check_call(['git', 'subtree', 'add', '--prefix=inet', '--message', 'Merge INET 4.2.1', 'https://github.com/inet-framework/inet', 'v4.2.1'])

# SimuLTE
subprocess.check_call(['git', 'subtree', 'add', '--prefix=simulte', '--message', 'Merge SimuLTE 1.2.0', 'https://github.com/inet-framework/simulte.git', 'v1.2.0'])
# add simulte as remote to cherry-pick important fixes
subprocess.check_call(['git', 'remote', 'add', 'simulte_remote', 'https://github.com/inet-framework/simulte.git'])
subprocess.check_call(['git', 'fetch', 'simulte_remote'])
subprocess.check_call(['git', 'cherry-pick', '23c0936^..7ed450c'])
subprocess.check_call(['git', 'remote', 'remove', 'simulte_remote'])


# Veins VLC
subprocess.check_call(['git', 'subtree', 'add', '--prefix=veins_vlc', '--message', 'Merge Veins VLC 1.0', 'https://github.com/veins/veins_vlc', 'veins-vlc-1.0'])
# add veins_vlc as remote to cherry-pick important fixes
subprocess.check_call(['git', 'remote', 'add', 'veinsvlc_remote', 'https://github.com/veins/veins_vlc.git'])
subprocess.check_call(['git', 'fetch', 'veinsvlc_remote'])
subprocess.check_call(['git', 'cherry-pick', 'a88d62^..0547a9'])
subprocess.check_call(['git', 'remote', 'remove', 'veinsvlc_remote'])
# patch configure file to support veins 5.2
with open(os.getcwd() + "/veins_vlc/configure", "r") as file:
    data = file.readlines()
data[57] ="    expect_version = ['5.0', '5.1', '5.2']\n"
with open(os.getcwd() + "/veins_vlc/configure", "w") as file:
    file.writelines(data)
subprocess.check_call(['git', 'add', '-u'])
subprocess.check_call(['git', 'commit', '-m', 'veins_vlc: allow veins 5.2'])

# '.project' file
with open(os.getcwd() + "/simulte/.project", "r") as file:
    data = file.readlines()
data[5] ="\t\t<project>inet</project>\n\t\t<project>veins</project>\n\t\t<project>veins_inet</project>\n"
with open(os.getcwd() + "/simulte/.project", "w") as file:
    file.writelines(data)

# Makefile
with open(os.getcwd() + "/simulte/Makefile", "r") as file:
    data = file.readlines()
data[15] = "\t@cd src && opp_makemake --make-so -f --deep -o lte -pSIMULTE -O out -KINET_PROJ=../../inet -DINET_IMPORT -I. -I$$\(INET_PROJ\)/src -L$$\(INET_PROJ\)/src -lINET$$\(D\)\n"
with open(os.getcwd() + "/simulte/Makefile", "w") as file:
    file.writelines(data)

# src/run_lte
with open(os.getcwd() + "/simulte/src/run_lte", "r") as file:
    data = file.readlines()
data[3] = "INET_DIR=$(cd $DIR/../../inet/src ; pwd)\n"
with open(os.getcwd() + "/simulte/src/run_lte", "w") as file:
    file.writelines(data)

subprocess.check_call(['git', 'add', '-u'])
subprocess.check_call(['git', 'commit', '-m', 'edit omnet project files'])


{%- endif %}

# Plexe
subprocess.check_call(['git', 'subtree', 'add', '--prefix=plexe', '--message', 'Merge Plexe 3.1', 'https://github.com/michele-segata/plexe', 'plexe-3.1'])

# Veins
subprocess.check_call(['git', 'subtree', 'add', '--prefix=veins', '--message', 'Merge Veins 5.2', 'https://github.com/sommer/veins', 'veins-5.2'])

print('Repository set up successful. Running git commands to clean up.')
subprocess.check_call(['git', 'config', '--unset', 'user.name'])
subprocess.check_call(['git', 'config', '--unset', 'user.email'])

print('Cookiecutter successful.')
