# DatasetCatalog-Example
Getting started example with the Dataset Catalog report demonstrated on sampled dataset CESNET-MINER22. This repositori is divaded in two examples:
* CESNET-MINER22: represents the original dataset that provides raw captured data with annotation.
* CESNET-MINER22-PPI: represents derived dataset that cotains PPI data insted of raw captured data.

Both folders have the following structure:
* input: contains all input files for the dataset report
* output: contains all output files for the dataset report from dataset analysis
* example: contains configuration and support files for creation of the dataset report using [DatasetCatalog-Tools](https://github.com/FETA-Project/DatasetCatalog-Tools)

Both datasets are processed towards the dataset report. You can check generated results or re-run the evaluation. During re-run follow the instruction below. Based on you environment change filesystem path to match required files in configuration. More comment about each file you will see in the specific folders.

## Getting Started Instructions
1. Download this repository. It provides all sample files for the Getting Started showcase
2. Download the [DatasetCatalog-Tools](https://github.com/FETA-Project/DatasetCatalog-Tools) repository. It contains all the dataset quality evaluation tools to get inputs for the dataset report.
3. Follow the Getting Started instructions below.

### CESNET-MINER22
This folder represents the original dataset that provides raw captured data with annotation. To process this dataset we can use NDVM and LLM Analyzer from [DatasetCatalog-Tools](https://github.com/FETA-Project/DatasetCatalog-Tools). 
1. To start with LLM Analyzer we need to update the configuration files. Use `example/basic_config.toml` and `example/miner22-example.toml`
2. Copy config files to LLM Analyzer directory together with input files `input/cited` and `input/cesnet-miner-22-paper.pdf` 
3. Run LLM Analyzer `python3 main.py`
4. As results we get summarization for input files that can be directly used for dataset report
5. To start with NDVM we need to update the configuration files. Use `example/config.yml` and `input/miner22-sampled.csv`
6. Run NDVM `python3 dataset_report.py -d CESNET-MINER22/input/miner22-sampled.csv -o CESNET-MINER22/output -l "string LABEL" -c config.yml` and map properly input files
7. As result we get dataset metrics and metadata about the input dataset.
8. This output can be directly used for the dataset report. For visualization of collected metadata from NDVM we can use `example\Metric-Showcase-Miner-22-sampled.ipynb`
   
### CESNET-MINER22-PPI
This folder represents the derived dataset that cotains PPI data insted of raw captured data. To process this dataset we can use NDVM and Drift Analyzer from [DatasetCatalog-Tools](https://github.com/FETA-Project/DatasetCatalog-Tools). 
1. To start with NDVM we need to update the configuration files. Use `example/config.yml` and `input/miner22-ppi-sampled.csv`
2. Run NDVM `python3 dataset_report.py -o CESNET-MINER22-PPI/output/ -d CESNET-MINER22-PPI/input/miner22-sampled-ppi.csv -l label -c config.yml` and map properly input files
3. As result we get dataset metrics and metadata about the input dataset.
4. This output can be directly used for the dataset report. For visualization of collected metadata from NDVM we can use `example\Metric-Showcase-Miner-22-PPI-sampled.ipynb`
5. To start with Drift Analyzer we need to update the configuration files. Use `example/experiment_runner.py`
6. Math import of the `detector` module from [drift-analyzer]([https://github.com/FETA-Project/DatasetCatalog-Tools](https://github.com/FETA-Project/DatasetCatalog-Tools/tree/main/drift-analyzer) with `example/experiment_runner.py`
7. Run Drift Analyzer with `python3 experiment_runner.py`
8. Edit `retrain` parameter in `experiment_runner.py` from False to True. Update the output filename from `logs_baseline.pkl` to `logs_baseline_retraining.pkl`. With this update we get dataset drift validation with retraining strategy.
9. As result we directly get dataset drift statistics for the dataset report and more detailed metadata about the whole workflow.
10. For visualization of collected metadata from Drift Analyzer we can use `example\Reporter-CESNET-Miner-22-PPI-sampled.ipynb`

# Acknowledgments
This project was supported by the Ministry of the Interior of the Czech Republic, grant No. VJ02010024: Flow-Based Encrypted Traffic Analysis.
