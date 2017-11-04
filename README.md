
# Genome-Network-Analysis
<p>The research program is conducted as a part of the Loyola Summer Research Program 2017. The network analysis is progarmmed and analysed with Python 2.7 using the SNAP (Stanford Network Analysis Platform) library. <p>
  
# Analysis and Conclusions
<p>The genome network analysis project is about creating a tool that aids in analyzing complex genome networks. A genome is the set of genetic material in an organism. The problems with analyzing such complex genome network is that in an absence of any computational tool it is always error prone and tedious. The homologous complex component in a cluster of network is difficult to detect manually.<p>
  
<p>The purpose of this research is to design a similarity metric so researchers would be able to efficiently compare and contrast genes shared among genomes. Specifically, for comparing large genome networks like viral communities. This study use SNAP and Python in order to identify relationships between homologous genes and edges within two or more networks. As a team, we have devised a similarity metric algorithm which compress multiple dimensional data into two dimensional data by using a method called multi-dimensional scaling. The idea was to create a set of parameters that would analyze multiple genome networks. This has been done by generating a summary table of unique homologous nodes and edges within each networks and then using the data to organize a comparison table that would output similarities between the multiple networks.<p>
  
<p>By using the comparison table, the anticipated outcome of this research is to produce a visual aid called a principle component analysis plot (PCA). This shows the network similarity in a two dimensional graph. This will help researchers easily identify the homologous components between different viral communities. Furthermore, it will allow researchers to identify the genes of the organisms at which these homologous components are exhibited.<p>

# Figures and Outlines


# Contributors
- Pinky Sindhu
- Hannah Lino
- Denee 

# Software Versions
At the time of the development of this tool the software versions used are 
- Snap.py 3.0
- Python 2.7.13
- Gnuplot 5.0
- Graphviz 2.40.1

# Installation Instructions
Please find the appropriate OS versions for the corresponding OS installations.
- Macintosh
    - Python can be installed easily using HomeBrew.
    - HomeBrew can be setup on Macintosh using the command below. Open the Terminal and type in below
    ``ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"``
    - HomeBrew installation will take a while. Click 'Y' whenever the terminal is prompted.
    - Python 2.7 is installed by typing the command below in Terminal 
    ``brew install python``
    - Successful installation of python can be tested by typing ‘python’ on Terminal.
    - If successful it shows up the installed Python Version
    - Also this is an addition step to make sure the Pythonpath variables are set properly.This can be done by typing the command below in Terminal
     ``brew link python``
    - Download the latest version of Snap.py from  https://snap.stanford.edu/snappy/
    - Navigate to the to the folder where the software package is downloaded through the terminal
    ``cd snap-3.0.0-3.0-macosx10.7.5-x64-py2.7``
    - Install the Snap through the terminal with command
    ``sudo python setup python.py install``
    - The terminal will prompt for the administrator password. Type password and click enter.
    - The Snap Installation is complete
    - The tool requires additional Python libraries for the tool to run. It can be installed using by typing the below commands on Terminal one by one
    ``brew install numpy``
    ``brew install scipy``
    ``brew install matplotlib``
    ``brew install scikit-learn``
    - For graphical plotting of networks, the gnuplot can be installed using typing the command below
    ``brew install gnuplot``
    - Similarly for the same functionality the graphviz can be installed using
    ``brew install graphviz``

These steps conclude the OSX installation steps required for this tool.

- Windows
    - Download the Anaconda Installer from the following location https://www.continuum.io/downloads
    - Select the installer corresponding to Python Version 2.7
    - Double-click the .exe file to install Anaconda and follow the instructions on the screen.
    - The Python installation is complete and we can verify the steps by selecting jupyter notebook from the Start Menu
    - The packages numpy, scipy,matplotlib,scikit-learn are required for the Genome Network tool. These can be installed using typing the command below in Terminal
    ``conda install package-name``
    - The ‘package-name’ can be replaced with the exact package name as listed in the link -  https://docs.continuum.io/anaconda/pkg-docs
    - Download the Snap.Py 3.0 windows version from this location https://snap.stanford.edu/snappy/release/ .
    - On Windows, Snap.py requires a 64-bit operating system version.  V  isual C++ Redistributable for Visual Studio 2012 must be installed on the system. You need to download and install the 64-bit version vcredist_x64.exe, not 32-bit version vcredist_x86.exe.
    - After downloading the Snap.py from the link given above, open Command Prompt and navigate in terminal to the folder where the package is downloaded.
    ``brew install numpy``
    ``brew install scipy``
    ``brew install matplotlib``
    ``brew install scikit-learn``
     - Type in the below commands on the terminal
    ``tar zxvf snap-3.0.0-3.0-centos6.5-x64-py2.6.tar.gz``
    ``cd snap-3.0.0-3.0-centos6.5-x64-py2.6``
    ``sudo python setup.py install``
These steps conclude the Windows installation steps required for this tool. 

# User Guide
- Introduction

To run the Genome Network Tool, please follow the Installation Guide to setup the environment. Once the environment is set to run the tool in Python environment, go to the GitHub location provided on the document and download the files required for the tool.

- Steps

After setting up the environment open Terminal or Command Prompt and type Python followed by the name of the Python File. In the Genome Network Analysis Tool, the code is present in the file named ‘snap_network_comare.py’. Please follow the steps below
  - Open Terminal and type  python snap_network_comapre.py
  - Go to the location where the ‘snap_network_compare.py’ file is saved.
  - The PCA plot can be recovered from the same location with name ‘pca_plot.png’
  
# Developer’s Guide
- Introduction

The tool creates networks based on the nodes and edges listed in the text file. The tool can alternatively works if the networks can be encoded using SNAP Graph Type ‘PNGraph’. After the networks are encoded in either one of the methods mentioned above the tool algorithm creates a similarity matrix which compares each networks against all possible edges of the network. The similarity matrix is enoced to a numpy matrix and the PCA is plotted by reducing the dimension size to 2.

- Working

The tool runs on Python environment. The tool also requires additional libraries to plot PCA. The tool can be run through Terminal or Anaconda platform. Download the code from the GitHub Location provided and save the files in the Python Class Path if in case of Windows machine or any location if in case of Macintosh environments. Run the program using Terminal interface or Jupyter Notebook. The PCA plot will be saved on the same location as of the code files if running on the Terminal. Otherwise the PCA plot can be viewed on the Jupyter Web interface. The PCA plot can be customized according to the needs by modifying the code in PCA plot block.
 
- Blocks

The logic of the tool is divided into three major blocks. 1. Reading or creating networks 2. Algorithm for generating networks in a matrix representation. 3. Code to plot PCA and save into a file.

