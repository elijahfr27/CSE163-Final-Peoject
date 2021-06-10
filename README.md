## CSE 163 Final Project: Working with Education Data
The project file contains all the functions for creating the project
visualizations and running the machine learning. The data files need
to be downloaded and added to the project folder before any of the
programs will run.

## Libraries
The libraries that need to be installed to use the files are pandas, seaborn,
and matplotlib. If running this project through VS Code, after installing Python
and selecting Python as the interpreted, these libraries are be installed by using
the following in the terminal:
```bash
python -m pip install matplotlib
```
```bash
python -m pip install pandas
```
```bash
python -m pip install seaborn
```
The following link has more information about set-up and installing libraries:
- https://code.visualstudio.com/docs/python/coding-pack-python

## Data
The data this project uses can be downloaded from the following links:
- https://data.wa.gov/Education/Report-Card-Graduation-2014-15-to-Most-Recent-Year/9dvy-pnhx
- https://data.wa.gov/Education/Report-Card-Enrollment-from-2014-15-to-Current-Yea/rxjk-6ieq 
- https://data.wa.gov/Education/Report-Card-Assessment-Data-from-2014-15-to-Curren/292v-tb9r
- https://data.wa.gov/Education/Report-Card-Discipline-for-2014-15-to-Current-Year/fwbr-3ker
- https://data.wa.gov/Education/Report-Card-SQSS-from-2014-15-to-Current-Year/inqc-k3vt

All the data files should be downloaded as csv files and moved to the same folder containing
all the files for the project.

## Running the project
Once all the data has been downloaded and added to the project file, the project files can now
be run. All the python files can be run from the terminal by using:
```bash
python program_name.py
```

The name of the file should be filled in for program_name. The filtering_data.py should be run
first to generate the condensed data. Then the state_data_visualizations.py and district_data_visulization.py
can be run since they rely on the condensed data. These will generate visualizations of the data.
Then the machine learning file can be run for the machine learning model generated from the modified district data. 