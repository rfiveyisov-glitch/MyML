import os
import subprocess

# --- 1️⃣ Root README yeniləmə hissəsi ---
ROOT_DIR = os.getcwd()
README_PATH = os.path.join(ROOT_DIR, "README.md")

MODULE_DESC = "This folder contains experiments and notebooks related to {}."

lines = [
    "# Machine Learning Portfolio: Data Analysis & Modeling\n\n\n",
    "## Project Overview\n",
    "Structured repository of ML experiments including supervised, unsupervised learning and data analysis pipelines.\n",
    "---\n\n\n",
    "## Repository Structure\n",
    "```\n"
]

for folder in sorted(os.listdir(ROOT_DIR)):
    folder_path = os.path.join(ROOT_DIR, folder)
    if os.path.isdir(folder_path) and not folder.startswith("."):
        lines.append(f"{folder}/    # {MODULE_DESC.format(folder)}\n")
        notebooks = [f for f in os.listdir(folder_path) if f.endswith(".ipynb")]
        for nb in notebooks:
            lines.append(f"    - {nb}\n")

lines.append("```\n")
lines.append("---\n\n\n")
lines.append("## Technologies & Libraries\n")
lines.append("- Python 3.x\n- NumPy, Pandas\n- Scikit-learn\n- Matplotlib, Seaborn\n- Jupyter Notebook\n")
lines.append("---\n\n\n")
lines.append("## Workflow\n")
lines.append("1. Data Loading\n2. Data Cleaning & Preprocessing\n3. Exploratory Data Analysis (EDA)\n4. Feature Engineering\n5. Model Training\n6. Model Evaluation\n7. Visualization & Interpretation\n")

with open(README_PATH, "w", encoding="utf-8") as f:
    f.writelines([line + "\n" if not line.endswith("\n") else line for line in lines])

print(f"Root README.md successfully generated at {README_PATH}")

# --- 2️⃣ Git avtomat add, commit, push ---
commit_message = "Update root README and auto push changes"

try:
    # Stage changes
    subprocess.run(["git", "add", "."], check=True)
    # Commit
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    # Push
    subprocess.run(["git", "push"], check=True)
    print("Changes successfully pushed to GitHub.")
except subprocess.CalledProcessError as e:
    print("Git operation failed. Details:")
    print(e)