
Your first step in using version 5.6.2 of the Gurobi Optimizer
is to download the appropriate distribution for your platform:

 Gurobi-5.6.2-win32.msi:      32-bit Windows installer
 Gurobi-5.6.2-win64.msi:      64-bit Windows installer
 gurobi5.6.2_linux64.tar.gz:  64-bit Linux distribution
 gurobi5.6.2_mac64.pkg:       64-bit Mac OS distribution
 gurobi5.6.2_power64.tar.gz:  64-bit AIX distribution

If you have installed a previous version of the Gurobi Optimizer,
we recommend that you uninstall it before installing this version.

For Windows and Mac users, you can simply double-click on
the installer once you have downloaded it.  It will guide you
through the installation process.

For Linux and AIX users, you will first need to choose an install
location (we recommend /opt for a shared installation).  You can then
copy the Gurobi distribution to that location and do a 'tar xvfz
gurobi5.6.2_linux64.tar.gz' (e.g.) to extract the Gurobi files.
Please check our supported platform list (in the Release Notes or
on our web site) to make sure that your operating system is supported.

Once the Gurobi files have been installed, your next step is to
consult the Release Notes and the Gurobi Quick Start guide.  The
Release Notes are accessible from the following locations:

Windows: c:\gurobi562\win32\ReleaseNotes.html or
         c:\gurobi562\win64\ReleaseNotes.html
Linux: /opt/gurobi562/linux64/ReleaseNotes.html
Mac: /Library/gurobi562/mac64/ReleaseNotes.html
AIX: /opt/gurobi562/power64/ReleaseNotes.html

The Quick Start Guide provides instructions for obtaining and
installing your Gurobi Optimizer license.  The Release Notes
contain information about this release, as well as a link
to the Quick Start Guide.

If you already have a Gurobi Version 5 license (in file
'gurobi.lic'), and you would like to store it in the
default location, you should copy the file to c:/gurobi562
on Windows, /opt/gurobi562 on Linux or AIX, or
/Library/gurobi562 on Mac.

Note that, due to limited Python support on AIX, our AIX port
does not include the Interactive Shell or the Python interface.
We also don't provide an R interface on AIX.
