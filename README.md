# Python Tricks
The repository contains python tips & tricks which I find interesting. They are presented in the form of experiments, with each script demonstrating the usage, attributes of a particular concept.

## Getting Started
All the experiments are run on `python 3.7`.

1. Clone the repository
2. If you do not have python3.7 installed. Run the below steps for easy installation using [asdf](https://asdf-vm.com/). *asdf* allows us to manage multiple runtime versions such for different languages such as `nvm`, `rbenv`, `pyenv`, etc using a CLI tool
	* Install asdf using this [guide](https://asdf-vm.com/#/core-manage-asdf-vm?id=install)
	* Now install `python3.7`
	```bash
	asdf plugin add python
	asdf install python 3.7.0
	asdf local python 3.7.0	# sets python3.7 as interpreter for the project
	```
	* Check the set python version
	```bash
	asdf current python
	```
3. Install poetry. [Poetry](https://python-poetry.org/docs/) is a python dependency management & packaging tool. Allows us to declare project libraries dependency & manage them
	```bash
	asdf plugin add poetry
	asdf install poetry latest # current 1.0.10; might need sudo
	asdf local poetry 1.0.10
	```
4. Install all dependencies
```bash
poetry install
```

## Running an experiment
To run an experiment, simply run the corresponding script. For example - to demonstrate *memoization* experiment.
```bash
python memoization.py
```

## Sources
1. [Sebastian Mathot's Python Lecture Series](https://www.youtube.com/playlist?list=PLR-r0edywujd8D-R2Kue1C_wYEK_4Ii71)




