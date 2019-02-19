"""
launch HPC jobs
from interactive node:

module add python/anaconda/2018.12/3.6
source activate submit

submit

"""
from subprocess import run

job = """#BSUB -q short-ib
#BSUB -J subtest
#BSUB -oo P-subtest.out
#BSUB -eo P-subtest.err
. /etc/profile
module add python/anaconda/2018.12/3.6
source activate submit
simple arg1 arg2 arg3
"""


def main():
    """The entry point."""
    process = run("bsub", input=job, encoding='ascii', capture_output=True)
    print(process.stdout)
    print(process.stderr)
    print(process.returncode)
