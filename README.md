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
    
or if you use a ***venv***:

    pip3 install numpy scipy matplotlib pandas

Add the ***pyat***, ***pyram***, ***utm*** and ***arlpy*** directories to your ***$PYTHONPATH*** by adding:

    export PYTHONPATH="<installationPath>/uAcoustics/python/arlpy:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/pyram:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/pyat:$PYTHONPATH"
    export PYTHONPATH="<installationPath>/uAcoustics/python/utm:$PYTHONPATH"

to the end of your ***./bashrc*** (or ***./profile*** or ***./bashprofile***).\
*For Spyder or IDEs you may have to add them to the IDE's ***$PYTHONPATH***.*\

### Update
  
Update the git project and submodules with:

    cd <installationPath>/uAcoustics
    git pull
    git pull --recurse-submodules

Or, erase and re-download the full project with:

    cd <installationPath>
    rm -rf uAcoustics
    git clone --recurse-submodules -j8 git@github.com:ErVuL/uAcoustics.git

Then if necessary, update and compile the oalib source code with:

    cp -rf <installationPath>/uAcoustics/oalib/at /opt/build
    cd /opt/build/at
    make clean
    make all
    make install

### Uninstall

Remove main folders and dependencies:

    rm -rf <installationPath>/uAcoustics/
    rm -rf /opt/build/at
    sudo apt remove -y git texlive-base gfortran cmake
    
Then clean the ***$PATH*** by editing your ***./bashrc*** (or ***./profile*** or ***./bashprofile***) and removing the following line:

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
| Add basic plots                                      | Done        |
| Add Wenz curves simulator                            | Done        |
| Add plot PSD func in dB re 1uPa/vHz for rec signals  | Done        |
| Use matplotlib for uwapm plots                       | Done        |
| Add pyram to arlpy                                   | Done (beta) |
| Add kraken to arlpy                                  | In progress |
| Add spectro func in dB re 1uPa/vHz for rec signals   | Not started |
| Add channel simulator filter using IR ?              | Not started |
| Add earthquakes and explosions to Wenz model         | Not started |
| Maintain up to date unittest and assert in arlpy     | Not started |           
| ...                                                  | ...         |
| Add scooter to arlpy                                 | Not started |
| Add sparc to arlpy                                   | Not started |
| Add krakel to arlpy                                  | Not started |
| Consider using c++ version of bellhop                | Not started |

## Some results

Results obtain with examples available in the ***/python*** directory.

![wenz](https://github.com/ErVuL/uAcoustics/assets/45111151/e805cca7-38ec-4d3d-90be-acb5233cf026)
![ssp](https://github.com/ErVuL/uAcoustics/assets/45111151/9f8a9d6c-974b-4273-a5a8-6383a5d7c0f9)
![ray](https://github.com/ErVuL/uAcoustics/assets/45111151/4f4ea814-f96d-4786-a976-214a6176e040)
![ram](https://github.com/ErVuL/uAcoustics/assets/45111151/5ab3c9d0-b4ce-4754-a7be-d953259d53e5)
![polar](https://github.com/ErVuL/uAcoustics/assets/45111151/8c9b0d44-f417-4b05-84c7-13dfb0edd3b2)
![mod](https://github.com/ErVuL/uAcoustics/assets/45111151/e8cc6c27-2aeb-4afa-8839-b55d4fcdb9d1)
![kraken](https://github.com/ErVuL/uAcoustics/assets/45111151/d8336307-ce87-46f5-85ce-1a9e58307b0a)
![ir](https://github.com/ErVuL/uAcoustics/assets/45111151/1fdf2738-8048-4201-8a10-3fffbc7819fe)
![density](https://github.com/ErVuL/uAcoustics/assets/45111151/e561baf9-ec67-4d4d-aa54-feb5b12660fb)
![bellhop](https://github.com/ErVuL/uAcoustics/assets/45111151/56e2462e-b0f3-4754-b208-2bf3e4684e7d)
![attn](https://github.com/ErVuL/uAcoustics/assets/45111151/1576fad2-35cc-48de-95f0-4fe8d8d7a2d9)
![arrivals](https://github.com/ErVuL/uAcoustics/assets/45111151/55c363f4-d8d4-4860-a6cc-8d51c55afd32)


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
