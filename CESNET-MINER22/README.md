# Dataset report for CESNET-MINER22

* Example
    * Metric-Showcase-Miner-22-sampled.ipynb - Support Jupyter notebook to display metadata from NDVM tool
    * basic_config.toml - Input configuration for LLM Analyzer tool
    * config.yml - Input configuration for NDVM tool
    * get-dataset.py - Script to get this dataset
    * miner_input.toml - Input dataset report file
* Input
    * cesnet-miner-22-paper.pdf - Published paper about the original dataset. It is used by LLM Analyzer 
    * cited - directory with published paper with citation of the original paper. It is used by LLM Analyzer 
    * miner22-sampled.csv - Sampled input dataset for this example. It is used by NDVM
* Output
    * main_analysis_miner_22_example.toml - Main output of the LLM Analyzer
    * main_analysis_miner_22_example_debug.toml - Debug output from the main paper processing using LLM Analyzer
    * per_paper_reference_miner_22_example.toml - Per paper analysis from the LLM Analyzer of the cited paper
    * reference_analysis_miner_22_example_debug.toml - Debug output from cited papers processing using LLM Analyzer
    * report-dataset-1752469252.csv - Dataset metrics report with metadata from the NDVM tool
    * report-katoda-dataset-1752469252.toml - Dataset metrics report in the format for the Dataset Catalog report
  
