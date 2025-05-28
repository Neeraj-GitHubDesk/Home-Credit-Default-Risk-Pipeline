import os

# No project_name prefix here
dirs = [
    "data/raw",
    "data/processed",
    "data/external",
    "artifacts",
    "logs",
    "notebooks",
    "src/config",
    "src/data",
    "src/processing",
    "src/training",
    "src/evaluation",
    "src/deployment",
    "src/monitoring",
    "src/governance",
    "src/utils",
    "tests",
    ".github/workflows",
]

files = [
    "README.md",
    ".gitignore",
    "requirements.txt",
    "environment.yml",
    "setup.py",
    "dvc.yaml",
    "params.yaml",
    "Dockerfile",
    "src/__init__.py",
    "src/config/config.py",
    "src/data/data_ingestion.py",
    "src/data/data_validation.py",
    "src/data/feature_store.py",
    "src/processing/data_preprocessing.py",
    "src/processing/feature_engineering.py",
    "src/training/train.py",
    "src/training/hyperparameter_tuning.py",
    "src/training/model_selector.py",
    "src/evaluation/evaluate.py",
    "src/deployment/app.py",
    "src/deployment/predict.py",
    "src/monitoring/monitor.py",
    "src/governance/lineage_tracker.py",
    "src/utils/logger.py",
    "src/utils/exception.py",
    "src/utils/common.py",
    "tests/test_ingestion.py",
    "tests/test_train.py",
    ".github/workflows/ci.yml"
]

# Create directories
for dir_path in dirs:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Created directory: {dir_path}")
    else:
        print(f"Directory already exists: {dir_path}")

# Create files
for file_path in files:
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            pass
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists: {file_path}")