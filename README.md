# IPa2 : Install Programs in armadillo2
## Synopsis

This script will help programmers to prepare all program files needed to create a program caps with NetBeans IDE for Armadillo.

## Installation

* Work with:
  - Python 2.7.12
  - PyYAML extension : http://pyyaml.org/wiki/PyYAML
  - need to be installed on the same directory as armadillo like:\
    $ ls . \
        armadillo2-master\
        IPa2-master

## Yaml file

* see:
  - ./explanation_of_yaml_file_content.yml
  - ./explanation_of_yaml_file_content_test.yml
  - ./inputs/* for examples

## Helper
* -h, --help get the help
* -t, --test launch as test (output directory will be outputs)
* -y  <input yanl file>] is the yaml file directory

## Directories

* ./packages/ = modules for program, editors, properties and utilities
* ./outputs/ = output files in test mode
* ./inputs/  = input files
* ../armadillo2-master/src/biologic/ to get biologic formats of input and output
Not in test:
* ../armadillo2-master/data/properties/ to install properties capsules files
* ../armadillo2-master/src/editors/ to install editors capsules files
* ../armadillo2-master/src/programs/ to install program capsules file

## License

MIT
