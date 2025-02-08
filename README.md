## Installation instructions

+ Clone the Spacewalks repository to your local machine using Git.
If you don't have Git installed, you can download it from the official Git website.

\`\`\`
git clone https://github.com/your-repository-url/spacewalks.git
cd spacewalks
\`\`\`

+ Install the necessary dependencies:
\`\`\`
python3 -m pip install pandas==2.2.2 matplotlib==3.8.4 numpy==2.0.0 pytest==7.4.2
\`\`\`

+ To ensure everything is working correctly, run the tests using pytest.

\`\`\`
python3 -m pytest
\`\`\`

## Usage Example

To run an analysis using the eva_data_analysis.py script from the command line terminal,
launch the script using Python as follows:

\`\`\`
# Usage Examples
python3 eva_data_analysis.py eva-data.json eva-data.csv
\`\`\`

The first argument is path to the JSON data file.
The second argument is the path the CSV output file.
