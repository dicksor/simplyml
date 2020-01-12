import subprocess

# generate trees
subprocess.call("python parser_sml.py Examples/example1.txt")
subprocess.call("python parser_sml.py Examples/example2.txt")
subprocess.call("python parser_sml.py Examples/example3.txt")

# generate threader
subprocess.call("python threader.py Examples/example1.txt")
subprocess.call("python threader.py Examples/example2.txt")
subprocess.call("python threader.py Examples/example3.txt")

# generate output
subprocess.call("python compiler.py Examples/example1.txt")
subprocess.call("python compiler.py Examples/example2.txt")
subprocess.call("python compiler.py Examples/example3.txt")