# README.md

## Synopsis

  - This is Udacity Full Stack Nanodegree project \#2 , an implementation a Swiss-system tournament.
  - This project involving a ready VM and a PostgreSQL database running on it.

## Environment
  - Python 3.0 or higher.
  - VirtualBox v 4.3.0. recommend.
  - Vagrant 1.7.4 or higher.

## Installation
  0. Configure VM
      - Install VirtualBox
      - Install Vagrant
      - fork [VM-repo](http://github.com/udacity/fullstack-nanodegree-vm)
          - then clone to your local hd
  1. Launch VM (in Bash)
      - ```$ cd full­stack­nanodegree­vm/tournament ```
      - ```$ vagrant up #boot vm```
      - ```$ vagrant ssh #login vm```
  2. Launch psql interactive interface and run script
      - ```vagrant-ubuntu-trusty-32:~$ cd ~/../../vagrant/tournament```
      - ```vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql #launch interface```
      - ```vagrant>>> \i tournament.sql  #init DB and table```
      - ```tournament>>> \q  #quit interface```

## Tests
  - ```vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py```

## Q & A,  Notes
  - Should one start connecting db first for every operation in the python code?
      - Yes, also one should Create db in the very beginning, before running python code
  - More detailed installation instruction?
      - https://storage.googleapis.com/supplemental_media/udacityu/3532028970/P2TournamentResults-GettingStarted.pdf
