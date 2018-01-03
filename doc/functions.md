# SASTBX Document - version 1.0.0
## Functions

### Intensity calculation
The calculation of SAS intensities is essential when comparing macromolecular models with experimental data. In the SASTBX, a spherical harmonics expansion method (Svergun et al., 1995) was implemented. Displaced solvent parameters are approximated using van der Waals radii obtained from the monomer library(Vagin et al., 2004).Surface-bound solvent is modeled by a single uniform-density layer extending from the outer molecular surface (Svergun et al., 1995). Intensity profiles can be computed using a three-dimensional Zernike expansion method (ZNK) as well. This method provides an alternative treatment of displaced and surface-bound solvent and is more appropriate for macromolecular models with complex surfaces(Fig. 1).(Liu et al., 2012)

### P(r) estimation
  The pair distance distribution function, P(r), can reveal structural characteristics of the studied molecules and is one of the most used procedures in SAXS analysis (Koch et al., 2003). In the SASTBX, a highly flexible functional form is used to parametrize P(r):

<div align = center>
 <img src="/Users/Song/Downloads/cctbx/gui/sasqt/pictures/prFunction.png" width = "200" height = "50"  align = 'center' />
 </div>

$g(r)$ is a prior distribution function. By default, $g(r)$ is set to the PDDF of a sphere.The exponential modifier function is a linear combination of Chebyshev polynomials $[T_m(r)]$,whose maximum order is M.The parameters of the approximation function $(a_m)$ are optimized to minimize the discrepancy between the resulting intensity profiles and the experimental data. The Chebyshev polynomials are orthogonal in the domain [ 1, 1] with an appropriate weighting function, so the optimizations can benefit from faster convergence.
<div align = center>
 <img src="/Users/Song/Downloads/cctbx/gui/sasqt/pictures/intensity_1.png"   align = 'center' />
 </div>
 **Figure 1** 
 *The solvent layers of a protein with a hole (PDB code 2e2g; Nakamura et al., 2008). The outer solvent layer (green) can be modeled with the spherical harmonics expansion method, but the inner layer (brown) is typically neglected. Both layers are automatically included when using the Zernike expansion method.*
 
 The comparisons of calculated intensity profiles using these two methods are summarized in Fig. 2. It is clear that the two methods yield very similar scattering profiles for the proteins in vacuo. The displaced solvent contributions have only minor differences. The surface-bound solvent gives very different scattering profiles for the proteins in Figs. 2(b) and 2(c), according to these two methods. The Debye formula is also implemented for the in vacuo SAXS profile calculation.
<div align = center>
 <img src="/Users/Song/Downloads/cctbx/gui/sasqt/pictures/intensity_2.png"   align = 'center' />
 </div>
 **Figure 2** 
 *(a) A comparison between intensity profiles computed using SHE and ZNK. The SHE (solid lines) and ZNK (circles) methods give very similar results for the overall scattering profiles (colored in black). The scattering profiles for the protein (in vacuo) (red) and displaced solvent (green) from the two methods are also in good agreement. For molecules with irregular surfaces (b) or large cavities/holes (c), the surface-bound solvent molecules have very different scattering profiles (blue). Reproduced from the work by Liu et al. (2012) with permission of the International Union of Crystallography.*
 
###Shape Search Engine
When no available atomic model matches a SAS profile, a low- resolution model envelope can be obtained by Shape Search Engine.This ab ovo method constructs low-resolution three-dimensional models based on the provided SAS profile and a shape database derived from structural databases such as the Protein Data Bank. This procedure automatically determines the shape and size of the molecule within one minute on a typical computer, given a SAS profile as the only input. The results are composed of several, 10 by default, candidate shapes that are aligned and subsequently clustered using a hierarchical clustering algorithm. The clustering procedure serves as an internal model consistency check, indicating the quality of the solution and the experimental data.
Here is an example in Fig.3: the results from Shape Search Engine with a lysozyme experimental SAXS profile. 
<div align = center>
 <img src="/Users/Song/Downloads/cctbx/gui/sasqt/pictures/shapeup.png"   align = 'center' />
 </div>
 
### Model superposition
Models at different resolutions or without a known point-to-point correspondence are usually difficult to compare. Here,we utilizes a fast rotational matching method facilitated by three-dimensional Zernike poly- nomial representation and fast Fourier transformation.




 
 
 


### Reference
* Liu, H., Hexemer, A., & Zwart, P. H. (2012). The Small Angle Scattering ToolBox (SASTBX): an open-source software for biomolecular small-angle scattering. Journal of Applied Crystallography, 45(3), 587-593.
* Koch, M. H., Vachette, P. & Svergun, D. I. (2003). Q. Rev. Biophys. 36, 147–227.
* Svergun, D., Barberato, C. & Koch, M. H. J. (1995). J. Appl. Cryst. 28, 768–773.
* Vagin, A. A., Steiner, R. A., Lebedev, A. A., Potterton, L., McNicholas, S.,Long, F. & Murshudov, G. N. (2004). Acta Cryst. D60, 2184–2195.