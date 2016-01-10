FIRSTMastery
============

A centralized training resource for the [FIRST](http://www.usfirst.org/) Robotics community.

Dev Server: [Link](http://dev.firstmastery.com/)

Running the Development Environment
-----------------------------------

    $ cd /path/to/project-name
    $ gulp

To test it visit `http://localhost:8080/` in your browser.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

For a complete list of commands:

    $ gulp help


Initializing or Resetting the project
------------------------------------

    $ cd /path/to/project-name
    $ npm install
    $ gulp

If something goes wrong you can always do:

    $ gulp reset
    $ npm install
    $ gulp

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

To install [Gulp][] as a global package:

    $ npm install -g gulp

Deploying on Google App Engine
------------------------------

    $ gulp deploy

Before deploying make sure that the `main/app.yaml` and `gulp/config.coffee`
are up to date.

GOALS and Objectives :
---------------------
- Build the best learning platform for the FIRST community.
- Make the platform as collaborative and community central as possible.
- Make the project modular and understanstable so anyone can contribute.
- *become a contributor and introduce your goals...

All Contributions are welcome. 