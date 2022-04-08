from pylint import run_pylint
from path import Path
from sys import argv

target_dir_path = Path() / "backend" 

run_pylint(argv=[target_dir_path])
