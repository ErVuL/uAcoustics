# uAcoustics
Python/Linux underwater acoustic propagation models and toolbox using ***pyat***, ***pyram***, ***arlpy*** and the ***OALIB acoustic toolbox***.\
\
This project aims to develop a simple to use, maintain and install python module for underwater acoustics. It will mainly use common python modules such as ***numpy***, ***scipy***, ***matplotlib*** and ***pandas***. ***arlpy*** seems to be one of the best suited python projects for such application, it will be the starting point of this one. The main objectives are to integrate more acoustic models into ***arlpy*** using a single environment definition for all models, replace ***bokeh*** by ***matplotlib*** (at least at the beginning) and develop further utilities. If the quality of the code is sufficient, we will consider to contribute to one or more of the forked projects.

## Installation

The following installation process is written for a debian based Linux OS. Tested under Debian 12 with built-in python 3.11.2.

### Required APT

Install some applications with the following command:
    
    sudo apt install git texlive-base gfortran cmake 

### Download

Make an installation directory with :

    mkdir <installationPath>
    cd <installationPath>
    
it will contains a local copy of the main python modules, and the source code of the oalib toolbox.
Then download the entire project with:

    git clone --recurse-submodules -j8 git@github.com:ErVuL/uAcoustics.git
    cd uAcoustics

### OALIB

*OPTIONAL : Modify the ***at/MakeFile*** in order to set your own compilation settings (add Krakel, use LLAPACK, configure CPU, ...).*
The acoustic toolbox from OALIB is in fortran, the installation is done in ***/opt/build*** with the following commands:

    mkdir /opt/build
    cp -r oalib/at /opt/build
    cd /opt/build/at
    make clean
    make all
    make install

you may have to "sudo" some commands but avoid it if not necessary. If you choose to install the acoustic toolbox somewhere else, you will have to modify ***uAcoustics/python/arlpy/arlpy/uwapm.py*** specifying your installation path by editing the line:

    # Add acoustic toolbox path to Python path
    os.environ['PATH'] = os.environ['PATH'].replace(':/opt/build/at/bin', '')+":/opt/build/at/bin"

Add binaries to your ***$PATH*** by editing your ***./bashrc*** (or ***./profile*** or ***./bashprofile***) and adding the following line:

    export PATH="/opt/build/at/bin:$PATH"

This allows your shell to find fortran executable files.

### Python

Install some dependencies:

    sudo apt install python3-numpy python3-scipy python3-matplotlib python3-pandas
    
or if you use a ***venv***:

    pip3 install numpy scipy matplotlib pandas

Add the ***pyat***, ***pyram***, ***utm*** and ***arlpy*** directories to your ***$PYTHONPATH*** by adding:

    export PYTHONPATH="<installationPath>/uAcoustics/python/arlpy:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/pyram:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/pyat:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/utm:$PYTHONPATH"

to the end of your ***./bashrc*** (or ***./profile*** or ***./bashprofile***).\
*For Spyder or IDEs you may have to add them to the IDE's ***$PYTHONPATH***.*

## Update
  
Update the git project and submodules with:

    cd <installationPath>/uAcoustics
    git pull
    git pull --recurse-submodules

Or, erase and re-download the full project with:

    cd <installationPath>
    rm -rf uAcoustics
    git clone --recurse-submodules -j8 git@github.com:ErVuL/uAcoustics.git

Then if necessary, update and compile the oalib source code with:

    rm -rf /opt/build/at
    cp -r <installationPath>/uAcoustics/oalib/at /opt/build
    cd /opt/build/at
    make clean
    make all
    make install

## Uninstall

Remove main folders and dependencies:

    rm -rf <installationPath>/uAcoustics
    rm -rf /opt/build/at
    sudo apt remove -y git texlive-base gfortran cmake
    
Then clean the ***$PATH*** and ***$PYTHONPATH*** by editing your ***./bashrc*** (or ***./profile*** or ***./bashprofile***) and removing the following line:

    export PATH="/opt/build/at/bin:$PATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/arlpy:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/pyram:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/pyat:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/utm:$PYTHONPATH"

To remove python modules use:

    sudo apt remove -y python3-numpy python3-scipy python3-matplotlib python3-pandas 

Or:

    pip3 uninstall numpy scipy matplotlib pandas
    
## Roadmap

| TODO                                                 | Status      |
|------------------------------------------------------|-------------|
| Make oalib installation works properly               | Done        |
| Update deprecated pyram types                        | Done        |
| Simplify acoustic env() in arlpy                     | Done        |
| Make a simple installation process                   | Done        |
| Compatibility with Spyder                            | Done        |
| Add BSD 3 license                                    | Done        |
| Add basic plots                                      | Done        |
| Add Wenz curves simulator                            | Done        |
| Add plot PSD func in dB re 1uPa/vHz for rec signals  | Done        |
| Use matplotlib for uwapm plots                       | Done        |
| Add pyram to arlpy                                   | Done (beta) |
| Redefine class for simpler call and separate env     | Done        |
| Add kraken to arlpy                                  | Done (beta) |
| Handle source range and left propagation             | Done        |
| Create Jupyter notebooks tutorials for each model    | In progress |
| Totally remove pandas                                | Not started |
| Make a simple installation process for venv          | Not started |
| Add requirements.txt file for pip                    | Not started |
| Remove pyat from the project                         | Not started |
| Add common sound profile plot                        | Done        |
| Add spectro func in dB re 1uPa/vHz for rec signals   | Not started |
| Add statistical spectrogram in dB re 1uPa/vHz        | Not started |
| Add channel simulator filter using IR ?              | Not started |
| Manage all options for Bellhop, Kraken and RAM       | In progress |
| Add Krakenc to arlpy                                 | Not started |
| Maintain up to date unittest and assert in arlpy     | In progress |
| Maintain up to date function and class comments      | In progress |
| Add earthquakes and explosions to Wenz model         | Not started |
| Consider Windows compatibility                       | Not started |
| ...                                                  | ...         |
| Add scooter to arlpy                                 | Not started |
| Add sparc to arlpy                                   | Not started |
| Consider using c++ version of bellhop                | Not started |

## Some results

Some results are availables in the jupyter notebooks located in ***/python***.

## About

### PYRAM

Range dependant Acoustic Model is a Parabolic Equation solver.\
Python adaptation of RAM v1.5.\
Fork from https://github.com/marcuskd/pyram.

### OALIB AT

OALIB source code (fortran) written in the 80's and 90's. Contains:
  - BELLHOP: Beam/ray trace code
  - KRAKEN: Normal mode code
  - SCOOTER: Finite element FFP code
  - SPARC: Time domain FFP code

Fork from https://github.com/oalib-acoustics/Acoustics-Toolbox/tree/main.

### PYAT

Python module used to interact with OALIB executable files.\
Fork from https://github.com/hunterakins/pyat.

### ARLPY

Python project with some signal processing, underwater acoustics utilities and also able to interact with bellhop.\
Fork from https://github.com/org-arl/arlpy.

### UTM

Bidirectional UTM-WGS84 converter for python.\
Fork from https://github.com/Turbo87/utm.git.

## Linked resources

  - https://oalib-acoustics.org: OALIB website.
  - https://github.com/A-New-Bellhope/bellhopcuda: Faster version of Bellhop in C++ that can use cuda and seems to be fully compatible with the python code by just replacing files.
  - https://github.com/org-arl/UnderwaterAcoustics.jl: Julia underwater acoustic toolbox with Bellhop, Kraken, another Ray model and a Pekeris solver.
