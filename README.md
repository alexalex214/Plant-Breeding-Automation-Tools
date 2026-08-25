# Plant Breeding & Genomic Data Automation Tools

A collection of computational workflows, bioinformatic tools, and statistical analysis scripts in **Python** and **R** designed to streamline plant phenotyping, sequence analysis, various statistical analyses and research documentation.

---

## Repository Structure & Script Overview

### Bioinformatics & Sequence Analysis
* **`expasy-blastp-Q22V.py` (Python):** Automates translation of raw DNA sequences using the ExPASy translation API, queries NCBI BLAST (`blastp`) and shows non-synonymous amino acid substitutions for downstream functional prediction tools (e.g., SIFT).

### Plant Phenotyping & Statistical Analysis
* **`root_phenotyping_analysis.R` (R):** Statistical pipeline for plant phenotyping data.
  * **Data Aggregation & Wrangling:** Processes time-series traits across lines and treatments (`dplyr`, `tidyverse`).
  * **Exploratory Visualizations:** High-resolution scatterplot matrices (`GGally`), trait trajectory line plots with error bars, QQ-plots and boxplots (`ggplot2`).
  * **Hypothesis Testing & Modeling:** Shapiro-Wilk normality tests, ANOVA, linear regression (`lm`), Wilcoxon effect sizes (`rstatix`) and estimated marginal means with post-hoc pairwise comparisons (`emmeans`).
  * **Multivariate Trait Profiling:** Principal Component Analysis and biplot visualizations.

### Population & Clustering Workflows
* **`bar_graph_normal_distribution.py` (Python):** Calculates population parameters ($\mu, \sigma$) and overlays Gaussian normal distribution density curves onto dual-population histograms using `pandas`, `numpy`, and `matplotlib`.
* **`cluster_tree.py` (Python):** Computes pairwise Euclidean distance matrices (`scipy.spatial.distance`), exports formatted Excel matrices and constructs hierarchical clustering dendrograms (`scipy.cluster.hierarchy`).
* **`pca_dendrogram.py` (Python):** Performs Dimensionality Reduction via PCA (`scikit-learn`), visualizes PC1/PC2 genotype projections and generates Ward's minimum variance hierarchical dendrograms.

### Academic Workflow Utilities
* **`references_formatting_by_doi.py` (Python):** Queries the CrossRef REST API to extract publication metadata by DOI and automatically formats bibliographic citations to match the style guidelines of *Theoretical and Applied Genetics (TAG)*.

---

## Tech Stack & Dependencies

* **Python 3.x:** `pandas`, `numpy`, `matplotlib`, `scipy`, `scikit-learn`, `biopython`, `requests`
* **R (v4.x):** `tidyverse`, `dplyr`, `ggplot2`, `GGally`, `rstatix`, `emmeans`

---

## Author
**Alexander Milovanov, PhD**  
*Plant Genetics & Molecular Breeding Scientist*  
[LinkedIn Profile](https://www.linkedin.com/in/alexander-milovanov-5810a4a8) | [GitHub](https://github.com/alexalex214)
