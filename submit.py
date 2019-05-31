"""
launch HPC LSF jobs
from interactive node:

module add python/anaconda/2018.12/3.6
source activate submit

submit

"""
from subprocess import run, PIPE
import sys


job = """#BSUB -q short-ib
#BSUB -J subtest
#BSUB -oo subtest.out
#BSUB -eo subtest.err
. /etc/profile
module add python/anaconda/2019.3/3.7
source activate submit
simple arg1 arg2 arg3
"""


def main():
    """The entry point. After pip install, submit is available."""
    p = run("bsub", input=job, encoding='ascii', stderr=PIPE, stdout=PIPE)
    # it can be useful to record the job id, return code of submission, etc.
    print("return code:", p.returncode, file=sys.stderr)
    print("stderr:", p.stderr)
    print("stdout:", p.stdout)


if __name__ == "__main__":
    main()
