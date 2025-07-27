# Dataset report for CESNET-MINER22-PPI

* Example
    * Metric-Showcase-Miner-22-PPI-sampled.ipynb - Support Jupyter notebook to display metadata from NDVM tool
    * Reporter-CESNET-Miner-22-PPI-sampled.ipynb Support Jupyter notebook to display metadata from Drift Analyzer tool
    * config.yml - Input configuration for NDVM tool
    * experiment_runner.py - Input configuration for Drift Analyzer tool
    * get-dataset.py - Script to get this dataset
* Input
    * miner22-ppi-sampled.csv - Sampled input dataset for this example. It is used by NDVM and Drift Analyzer.
* Output
    * report-dataset-1752615844-metric1 - Metadata for dataset quality metric 1 from NDVM tool
    * report-dataset-1752615844-metric2 - Metadata for dataset quality metric 2 from NDVM tool
    * report-dataset-1752615844-metric3 - Metadata for dataset quality metric 3 from NDVM tool
    * report-dataset-1752615844.csv - Dataset metrics report with metadata from the NDVM tool
    * report-katoda-dataset-1752615844.toml - Dataset metrics report in the format for the Dataset Catalog report
    * logs_baseline.pkl - Drift detection metadata from Drift Analyzer with retraining policy disabled
    * logs_baseline_retraining.pkl Drift detection metadata from Drift Analyzer with retraining policy enabled.
