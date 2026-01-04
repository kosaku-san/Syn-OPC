# Syn-OPC

This repository contains the scripts and data used to generate figures for the following paper:

**Title:** Transcriptional Heterogeneity Reveals a Synaptic Gene Program in Developing and Adult Human Oligodendrocyte Precursor Cells  
**Authors:** Grinberg et al.  
**Status:** Under review (Preprint available on bioRxiv)

The preprint version is available [here](https://www.biorxiv.org/cgi/content/short/2026.01.01.697017v1)

------------------------------------------------------------------------
## Files

-   **`Monte Carlo Simulation.py`**
    -   The Python script used to perform the Monte Carlo simulation analysis.
-   **`C2genes.csv`**
    -   A CSV file containing the list of genes associated with the C2 cluster (the target gene set). 
-   **`List of Genes Expressed in Brain.csv`**
    -   A CSV file containing the background list of genes expressed in the brain, used as the reference population for the simulation.

------------------------------------------------------------------------
## Requirements

-   **Python:** To run the scripts, you will need **Python 3.x** installed along with the following built-in libraries:

    random,\
    csv
-   Non-standard hardware is not required.
    
------------------------------------------------------------------------
## Usage

You can run the simulation script from the terminal using the following command:

```bash
python "Monte Carlo Simulation.py"

