# Events

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.530-blue.svg)](https://doi.org/10.25663/brainlife.app.530)

Brainlife App to detect ECG related components using `find_bads_ecg` function.

## app-events documentation

1) Input file is:
    * `meg/fif` meg data file
    * `ica/fif` ica object file

2) Input parameters:
    * `threshold` Value above which a feature is classified as outlier.
    * `l_freq` Low pass frequency.
    * `h_freq` High pass frequency.
    * `method` The method used for detection. If 'ctps', cross-trial phase statistics [7] are used to detect ECG-related components. See Notes.
    * `reject_by_annotation` Whether to omit bad segments from the data before fitting. If True (default), annotated segments whose description begins with 'bad' are omitted. If False, no rejection based on annotations is performed.
    * `measure` Which method to use for finding outliers among the components:

3) Ouput files are:
    * `ica/fif` ica object file which included the ecg_indices to be execluded. 
    * a plot of the new ICA components.
   

## Authors
- Saeed ZAHRAN(saeedzahranutc@gmail.com)

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

*- brainlife.io Publishing and Apps:*

Avesani, P., McPherson, B., Hayashi, S. et al. **The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services**. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

*- MNE-Python package:* 

Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Goj R, Jas M, Brooks T, Parkkonen L, and Hämäläinen MS.  **MEG and EEG data analysis with MNE-Python**. Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University

