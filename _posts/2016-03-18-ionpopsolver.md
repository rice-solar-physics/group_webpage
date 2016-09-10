---
layout: post
title: IonPopSolver Code Now Available
---
Recently, the Bradshaw group has made available the IonPopSolver code, a set of routines used to assess the impact of non-equilibrium ionization given timeseries temperature and density data. More specifically, IonPopSolver calculates the current ionization state for a given element and a range of ions and then returns an effective temperature, the temperature you would expect to observe assuming ionization equilibrium. The input data can either be output from a numerical simulation (e.g. [EBTEL](https://github.com/rice-solar-physics/EBTEL_C)) or temperature and density derived from a set of observations.

The code and installation instructions can be found on [GitHub](https://github.com/rice-solar-physics/IonPopSolver). If you encounter any problems installing or using the code, [create an issue on GitHub](https://github.com/rice-solar-physics/IonPopSolver/issues). The physical and numerical details of the code can be found in [Bradshaw (2009)](http://adsabs.harvard.edu/abs/2009A%26A...502..409B). If you use this software in a published work, please cite the formerly mentioned paper and mention the use of this code.   
