import os
import sys


base_dir = os.path.dirname(os.path.dirname(__file__)) 
project_root = os.path.abspath(os.path.join(base_dir, os.pardir))
sys.path.append(project_root)
