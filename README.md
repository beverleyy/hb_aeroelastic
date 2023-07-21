# hb_aeroelastic

Repository for aeroelastic flutter analysis with harmonic balance method.

## Contents

* **SU2_casefiles**: Test cases using custom SU2 code (beverleyy/SU2). NASA benchmark supercritical wing cases 1 and 3 (somewhat inaccurate) and Isogai wing forced oscillations.

* **OptTP.py**: Script for selection of optimal time period as per Nimmagadda et al. 2016. To run: `python3 OptTP.py` and it will prompt for the desired frequencies.

* **Ritz.ipynb**: Notebook for estimating wing mode shapes using Rayleigh-Ritz method.

* **read_surface.ipynb**: Notebook to calculate time-history of pressure forces for each cell and associated cell normal vectors.

* **ifar_flutter.ipynb**: Notebook for flutter estimate using (a) Unsteady Wagner aerodynamics, (b) P-K Theodorsen aerodynamics. 

* **HBinterpol.py**: Python functions to calculate the Einv matrix and interpolate time domain data from harmonic balance calculation.

## Work in progress

* Fix the BSCW case files to better match experimental data

* Add the 3D Theodorsen code to the flutter estimate notebook

* Add flexible motion to SU2 Python wrapper

## Note

Due to large file size, some `.dat` or `.vtu` files are not included in this repository. Therefore, some of steady-state cases may be required to be re-run locally if this repository is cloned.
