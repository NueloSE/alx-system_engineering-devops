# 0x0A. Configuration management

## General
- This project is simply a set of tasks to familiarize learner with the basic level syntax which is virtually identical in newer versions of Puppet.

## Installations.

### Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.
- check if puppet is installed by running `puppet --version`
- To install Puppet 5.5 for ubuntu:
	1. `sudo apt-get install puppet`
	2. run `puppet --version` to check if successfully installed
	3. get the installed version of ruby by running:
		`apt-cache policy ruby`
	4. Then install by `sudo apt-get install -y ruby=<version of ruby ex: 1:3.0~exp1>
	5. install the following:
		`sudo apt-get install -y ruby-augeas`
		`sudo apt-get install -y ruby-shadow`
		`sudo apt-get install -y puppet`
		`sudo apt autoremove` to remove unneeded file that came along with the installation

### Installing Gem
- run: `gem install puppet-lint`
- run: `puppet-lint` to check successfully installed.
