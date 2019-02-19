"""
launch HPC jobs
from interactive node:
module add python/anaconda/2018.12/3.6
source activate submit

submit

"""
from subprocess import run

cmd = [
    'bsub',
    '-q', 'short-ib',
    '-J', 'subtest',
    '-oo', 'P-subtest.out',
    '-eo', 'P-subtest.err',
    ". /etc/profile",
    "module add python/anaconda/2018.12/3.6",
    "source activate submit",
    'simple', 'arg1', 'arg2', 'arg3'
]


def main():
    process = run(cmd, capture_output=True)
    print(process)
