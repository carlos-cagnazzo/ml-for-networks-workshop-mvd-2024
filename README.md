# Feature Extraction for BGP Anomaly Detection

This project provides a set of Python scripts to extract features from BGP (Border Gateway Protocol) update data, enabling anomaly detection and further analysis. The scripts process BGP data in configurable time windows and generate feature files for metrics such as update counts, announcements, and withdrawals.

All scripts have a common command line and some common features like:

- Configurable **time windows** and **starting timestamps** ensure consistency across feature files.
- Progress bars and feedback during processing for large datasets.
- Designed for scalability with PETL and Rich libraries.

This project utilizes BGP data sourced from the RIPE NCC's Routing Information Service (RIS). RIPE RIS provides publicly available, high-quality BGP routing data collected from a global network of Remote Route Collectors (RRCs). These datasets serve as a critical resource for researchers and engineers in understanding Internet routing dynamics and detecting anomalies.

I acknowledge and thank the RIPE NCC for maintaining and sharing the RIS data, which has been instrumental in the development of this project. For more information about RIPE RIS and access to their datasets, visit [https://ris.ripe.net](https://ris.ripe.net). 


You can include this in the README under a **Data Source** or **Acknowledgments** section. Let me know if you’d like help with placement or additional edits! 🚀


## Features Currently Extracted from RIS Data

- **Feature 0**: Total number of BGP update messages per time window.
- **Feature 1**: Number of BGP `ANNOUNCEMENT` messages per time window.
- **Feature 2**: Number of BGP `WITHDRAWAL` messages per time window.

## Requirements

- Python 3.7 or higher
- Dependencies:
  - [PETL](https://petl.readthedocs.io/en/stable/) (Data transformation library)
  - [Typer](https://typer.tiangolo.com/) (CLI library)
  - [Rich](https://rich.readthedocs.io/en/stable/) (Progress bar and console feedback)

Install the required libraries with:
```bash
pip install petl typer rich
```

## File Structure

```
.
├── feature_0.py             # Extracts total BGP updates per window
├── feature_1.py             # Extracts BGP announcements per window
├── feature_2.py             # Extracts BGP withdrawals per window
├── common.py                # Shared utilities for input/output and progress
├── README.md                # Project documentation
```

## Usage

### 1. Extracting Features

Each script accepts the following parameters:
- `--input` (required): Path to the input BGP data file (CSV format).
- `--output` (required): Path to the output feature file (CSV format).
- `--window` (optional): Size of the time window in seconds (default: 300).
- `--start-time` (optional): Start time for time windows (e.g., "2024-12-12 00:00:00"). Defaults to the earliest timestamp in the data.

#### Example: Extract Feature 0
```bash
python feature_0.py --input bgp_data.csv --output feature_0.csv --window 300 --start-time "2024-12-12 00:00:00"
```

#### Example: Extract Feature 1
```bash
python feature_1.py --input bgp_data.csv --output feature_1.csv --window 300 --start-time "2024-12-12 00:00:00"
```

#### Example: Extract Feature 2
```bash
python feature_2.py --input bgp_data.csv --output feature_2.csv --window 300 --start-time "2024-12-12 00:00:00"
```

### 2. Output Format
Each feature file contains:
- **`feature_name`**: Name of the feature (`update_count`, `announcement_count`, or `withdrawal_count`).
- **`timestamp`**: Start time of the time window.
- **`value`**: The metric's value for the time window.

Example Output:
```csv
feature_name,timestamp,value
update_count,2024-12-12 00:00:00,45
update_count,2024-12-12 00:05:00,67
...
```

## Development

### Cloning the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/bgp-feature-extraction.git
cd bgp-feature-extraction
```

### Testing
To test with a subset of data, use the `--head` option to limit the number of input rows:
```bash
python feature_0.py --input bgp_data.csv --output feature_0.csv --window 300 --head 1000
```

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- This project uses [PETL](https://petl.readthedocs.io/), [Typer](https://typer.tiangolo.com/), and [Rich](https://rich.readthedocs.io/).
- Inspired by the need for scalable BGP data analysis and anomaly detection.
