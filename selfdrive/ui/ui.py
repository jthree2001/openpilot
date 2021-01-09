import subprocess
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))


subprocess.run(["cd", dir_path])
subprocess.run(["./_ui", "LD_LIBRARY_PATH='/system/lib64:$LD_LIBRARY_PATH'"])