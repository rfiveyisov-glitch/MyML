import os

# Root directory (sənin MyML qovluğun)
ROOT_DIR = os.getcwd()
README_PATH = os.path.join(ROOT_DIR, "README.md")

# Template for each module
MODULE_DESC = "This folder contains experiments and notebooks related to {}."

# Start root README content
lines = [
    "# Machine Learning Portfolio: Data Analysis & Modeling\n",
    "## Project Overview\n",
    "Structured repository of ML experiments including supervised, unsupervised learning and data analysis pipelines.\n",
    "---\n",
    "## Repository Structure\n",
    "```\n"
]

# Iterate over all folders in root
for folder in sorted(os.listdir(ROOT_DIR)):
    folder_path = os.path.join(ROOT_DIR, folder)
    if os.path.isdir(folder_path):
        # Skip hidden folders or .git
        if folder.startswith("."):
            continue
        # Add folder as module
        lines.append(f"{folder}/    # {MODULE_DESC.format(folder)}\n")
        # List notebook files inside folder
        notebooks = [f for f in os.listdir(folder_path) if f.endswith(".ipynb")]
        for nb in notebooks:
            lines.append(f"    - {nb}\n")

lines.append("```\n")
lines.append("---\n")
lines.append("## Technologies & Libraries\n")
lines.append("- Python 3.x\n- NumPy, Pandas\n- Scikit-learn\n- Matplotlib, Seaborn\n- Jupyter Notebook\n")
lines.append("---\n")
lines.append("## Workflow\n")
lines.append("1. Data Loading\n2. Data Cleaning & Preprocessing\n3. Exploratory Data Analysis (EDA)\n4. Feature Engineering\n5. Model Training\n6. Model Evaluation\n7. Visualization & Interpretation\n")

# Write to README.md
with open(README_PATH, "w", encoding="utf-8") as f:
    f.writelines([line + "\n" if not line.endswith("\n") else line for line in lines])

print(f"Root README.md successfully generated at {README_PATH}")
