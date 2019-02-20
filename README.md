# Submit batch jobs to the HPC using python

This repo covers a few useful aspects of conda, pip, and subprocess - ultimately
aimed at running LSF jobs on a cluster, but covers other useful scenarios.

## Setup

Using `setuptools` we can pip install to include modules in the python path.
From the directory containing the file `setup.py`

    pip install -e .

Here, using the -e flag allows the python modules to remain editable. Of course,
if not in the working directory, the path to `setup.py` can be specified.

For the example here, we include entry points to module functions, giving console
commands: `simple` and `submit`

## Conda Environment

Creating virtual environments is a useful way to manage dependencies. For Anaconda
python installs, the `conda` command allows the creation and updating of virtual envs.
Especially useful is the ability to create or update envs from a file:

    conda env create -f env.yml

Where env.yml defines the environment.
For the example here the env installs pip, which is subsequently used to install
our custom module, directly from a git repo.

### HPC

On the cluster, the login node does not have conda command available. It is
necessary to add the anaconda module eg:

    module add python/anaconda/2018.12/3.6

This is probably best done from an interactive queue, but will still install
the env in the `~/.conda` directory.

## Subprocess

With current versions of Python, the recommended call is `run` which is a convenience
function wrapping Popen. In this example, we pipe string input, with ascii encoding,
to the `bsub` command (this command is for LSF batch submission). We pipe out
stderr, stdout and also capture the return code of the command.
