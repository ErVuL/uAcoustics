# uAcoustics
Python/Linux underwater acoustics propagation models and toolbox using ***pyat***, ***pyram***, ***arlpy*** and the ***OALIB acoustic toolbox***.

## Installation

The following installation process is written for a debian based Linux OS. Tested under Debian 12 with built-in python 3.11.2.

### LaTeX

Install LaTeX with the following command:
    
    sudo apt install texlive-base

### OALIB AT

*OPTIONAL : Modify the ***at/MakeFile*** in order to set your own compilation settings (add Krakel, use LLAPACK, configure CPU, ...).*\
The acoustic toolbox from OALIB is in fortran, the code must be build and installed with the following commands:

    mkdir /opt/build
    cp -r oalib/at /opt/build
    cd /opt/build/at
    make clean
    make all
    make install

Add ***bin*** folder to your $PATH by editing your ***./profile***, ***./bashprofile*** or ***./bashrc*** ... and adding the following line:

    export PATH="/opt/build/at/bin:$PATH"

This allow python modules to find fortran executable files.

### PYTHON

Install some dependencies:

    sudo apt install python3-numpy python3-scipy python3-matplotlib python3-pandas
or:

    pip3 install numpy scipy matplotlib pandas

Copy the ***pyat***, ***pyram*** and ***arlpy*** directories into your python project.\
In Spyder or some other IDEs you may have to add:

    os.environ['PATH'] = os.environ['PATH'].replace(':/opt/build/at/bin', '')+":/opt/build/at/bin"
    
at the beginning of your code to import the fortran binaries to your IDE's environment.

## About

### PYRAM

Range dependant Acoustic Model is a Parabolic Equation solver.\
Python adaptation of RAM v1.5.\
Fork from https://github.com/marcuskd/pyram the 04/11/2023.

### OALIB AT

OALIB source code (fortran) written in the 80's and 90's. Contains:
  - BELLHOP: Beam/ray trace code
  - KRAKEN: Normal mode code
  - SCOOTER: Finite element FFP code
  - SPARC: Time domain FFP code

Fork from https://github.com/oalib-acoustics/Acoustics-Toolbox/tree/main the 04/11/2023.
See also:\
http://oalib.hlsresearch.com/AcousticsToolbox \
https://oalib-acoustics.org/models-and-software/acoustics-toolbox/ 

### PYAT

Python module used to interact with OALIB executable files.\
Fork from https://github.com/hunterakins/pyat the 04/11/2023.

### ARLPY

Python project also able to interact with bellhop.\
It contains a lot of useful functions for underwater acoustic processing.\
Fork from https://github.com/org-arl/arlpy the 05/11/2023.

## Linked resources

  - https://oalib-acoustics.org: OALIB website.
  - https://github.com/A-New-Bellhope/bellhopcuda: Faster version of Bellhop in C++ that can use cuda and seems to be fully compatible with the python code by just replacing files.
  - https://github.com/org-arl/UnderwaterAcoustics.jl: Julia underwater acoustic toolbox with Bellhop, Kraken, another Ray model and a Pekeris solver.
