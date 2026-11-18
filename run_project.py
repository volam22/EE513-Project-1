"""Execute the Project 1 notebook in order. Run from the repository directory."""

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT / "EE513_Project1_Notebook.ipynb"


def main():
    parser = argparse.ArgumentParser(description="Run EE513 Project 1")
    parser.add_argument("--data-root", type=Path, default=None,
                        help="Folder containing the Project 1 RAW image directories")
    args = parser.parse_args()
    env = os.environ.copy()
    if args.data_root is not None:
        if not args.data_root.is_dir():
            parser.error(f"RAW folder does not exist: {args.data_root}")
        env["EE513_DATA_ROOT"] = str(args.data_root.resolve())
    elif not env.get("EE513_DATA_ROOT"):
        parser.error("Provide --data-root PATH or set EE513_DATA_ROOT")
    command = [sys.executable, "-m", "jupyter", "nbconvert",
               "--to", "notebook", "--execute", "--inplace",
               "--ExecutePreprocessor.timeout=900", str(NOTEBOOK)]
    print("Running Project 1 notebook:", NOTEBOOK.name, flush=True)
    subprocess.run(command, cwd=ROOT, env=env, check=True)
    print("Complete. Notebook outputs saved.")


if __name__ == "__main__":
    main()
