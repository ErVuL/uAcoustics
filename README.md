# uAcoustics
Python/Linux underwater acoustic propagation models and toolbox using ***pyat***, ***pyram***, ***arlpy*** and the ***OALIB acoustic toolbox***.\
\
This project aims to develop a simple to use, maintain and install python module for underwater acoustics. It will mainly use common python modules such as ***numpy***, ***scipy***, ***matplotlib*** and ***pandas***. ***arlpy*** seems to be one of the best suited projects for such application, it will be the starting point of this one. The main objectives are to integrate more acoustic models into ***arlpy***, replace ***bokeh*** by ***matplotlib*** (at least at the beginning) and develop further utilities. (Maybe, if the quality of the code is sufficient, we will consider to contribute to ***arlpy*** project..)

## Installation

The following installation process is written for a debian based Linux OS. Tested under Debian 12 with built-in python 3.11.2.

### Required APT

Install some applications with the following command:
    
    sudo apt install texlive-base gfortran cmake 

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

you may have to "sudo" some commands but avoid it if not necessary.
Add binaries to your ***$PATH*** by editing your ***./bashrc*** (or ***./profile*** or ***./bashprofile***) and adding the following line:

    export PATH="/opt/build/at/bin:$PATH"

This allows your shell to find fortran executable files.\
*In Spyder or some other IDEs you may have to add:*

    os.environ['PATH'] = os.environ['PATH'].replace(':/opt/build/at/bin', '')+":/opt/build/at/bin"
    
*at the beginning of your code to import the fortran binaries to your IDE's environment.*

### Python

Install some dependencies:

    sudo apt install python3-numpy python3-scipy python3-matplotlib python3-pandas
or:

    pip3 install numpy scipy matplotlib pandas

Add the ***pyat***, ***pyram***, ***utm*** and ***arlpy*** directories to your ***$PYTHONPATH*** by adding:

    export PYTHONPATH="<installationPath>/uAcoustics/python/arlpy:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/pyram:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/pyat:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/utm:$PYTHONPATH"

to the end of your ***./bashrc*** (or ***./profile*** or ***./bashprofile***).\
*For Spyder or IDEs you may have to add them to the IDE's ***$PYTHONPATH***.*

## Roadmap

| TODO                                             | Status      |
|--------------------------------------------------|-------------|
| Make oalib installation works properly           | Done        |
| Update deprecated pyram types                    | Done        |
| Simplify acoustic env() in arlpy                 | Done        |
| Make a simple installation process               | Done        |
| Compatibility with Spyder                        | Done        |
| Use matplotlib for plots                         | In progress |
| Add usefull plots                                | In progress |
| Add pyram to arlpy                               | In progress |
| Feed the signal processing and uwa modules       | Not started |
| Add kraken to arlpy                              | Not started |
| ...                                              | ...         |
| Add scooter to arlpy                             | Not started |
| Add sparc to arlpy                               | Not started |
| Add krakel to arlpy                              | Not started |


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
