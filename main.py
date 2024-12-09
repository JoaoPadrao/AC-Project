import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(notebook_path, kernel_name='python3'):
    print(f"Running notebook: {notebook_path}")
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name=kernel_name)
    try:
        ep.preprocess(notebook, {'metadata': {'path': '.'}})
        print(f"Notebook {notebook_path} executed successfully.")
    except Exception as e:
        print(f"Error while running {notebook_path}: {e}")

def main():
    notebooks = [
        "cleaning.ipynb",
        "outliers.ipynb",
        "feature_engineering.ipynb",
        "add_season11.ipynb",
        "feature_selection.ipynb",
        "predictions.ipynb"
    ]

    for notebook in notebooks:
        run_notebook(notebook)

if __name__ == "__main__":
    main()
