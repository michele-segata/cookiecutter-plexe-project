# cookiecutter-veins-project #

Cookiecutter project template for quickly setting up a simulation model library using Plexe.

## Supported Program Versions ##

- Cookiecutter 1.6.0 (see <https://github.com/cookiecutter/cookiecutter>)
- git 2.23.0 (see <https://git-scm.com/>)

## Running ##

Save the contents of this repository to disk, e.g., in `~/src/cookiecutter-plexe-project` (that is, this file resides in `~/src/cookiecutter-plexe-project/README.md`).

Open a terminal and switch to a directory that should contain your new project, e.g., `~/src`.

Run cookiecutter, e.g., as `cookiecutter ~/src/cookiecutter-plexe-project`.
You will be prompted for a number of configuration variables (each with a default value, which you can accept by pressing the `enter` key).
After finishing, cookiecutter will have created a directory named after your `project_name_as_file_name` directory.

## Detailed procedure ##

First install cookiecutter for python via `pip`
```
pip install --user cookiecutter
```
Then download the `cookiecutter-plexe-project` via `git`
```
cd ~/src
git clone https://github.com/michele-segata/cookiecutter-plexe-project.git
```
and automatically download all the required source code by running
```
cd ~/src
cookiecutter -v cookiecutter-plexe-project
```
Cookiecutter will prompt about some basic information, such as project name, project download folder, etc.
You can simply leave all the default values besides the last one.
The first prompt will ask you whether you want to use the heterogeneous networking extension or not (`use_hetnet`).
If you type no, then standard Plexe (802.11p only) will be downloaded, otherwise cookiecutter will take care of downloading all the required extensions.
**Be aware that the HetNet version is not compatible with OMNeT++ 6** but only with 5.7.
If will find all the required software under the `plexe_proj` folder and every framework (Veins, Plexe, INET, etc.) will be located in a subfolder.
To build all the software simply type
```
cd ~/src/plexe_proj
./configure
make
```

## More Information ##

See the Plexe website <http://plexe.car2x.org/> for a tutorial, documentation,
and publications.

## License ##

Veins is composed of many parts. See the version control log for a full list of
contributors and modifications. Each part is protected by its own, individual
copyright(s), but can be redistributed and/or modified under an open source
license. License terms are available at the top of each file. Parts that do not
explicitly include license text shall be assumed to be governed by the "GNU
General Public License" as published by the Free Software Foundation -- either
version 2 of the License, or (at your option) any later version
(SPDX-License-Identifier: GPL-2.0-or-later). Parts that are not source code and
do not include license text shall be assumed to allow the Creative Commons
"Attribution-ShareAlike 4.0 International License" as an additional option
(SPDX-License-Identifier: GPL-2.0-or-later OR CC-BY-SA-4.0). Full license texts
are available with the source distribution.

