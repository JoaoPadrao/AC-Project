# How to Run the Project

> This project involves running a series of Jupyter notebooks that perform data processing, from cleaning to the final prediction. To facilitate sequential execution, a **main.py** script has been included that automates the execution of all the notebooks in the correct order (pipeline).

## Manual Notebook Running Order
- If you prefer to run them manually, follow the order below:
1. **cleaning.ipynb:** Performs initial data cleaning.
2. **outliers.ipynb:** Identifies and treats outliers in the dataset.
3. **feature_engineering.ipynb:** Creates new features.
4. **add_season11.ipynb:** Adds season 11 data to the dataset.
5. **feature_selection.ipynb:** Selects the best features for the model.
6. **predictions.ipynb:** Carries out the predictions and generates the final results.

## Automated Pipeline

- The **main.py** script runs all the notebooks in the correct order. It uses the nbformat and nbconvert libraries to process the notebooks.

- If you haven't installed these libraries yet, run the following command in the terminal:
```bash
pip install nbconvert nbformat
```
- After installing the libraries, run the **main.py** script by executing the following command in the terminal:

```bash
python main.py
```