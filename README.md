FIRSTMastery
============

A centralized training resource for the [FIRST](http://www.usfirst.org/) Robotics community.

Dev Server: [Link](http://dev.firstmastery.com/)

Running the Development Environment
-----------------------------------

```bash
$ cd /path/to/project-name
$ gulp
```

To test it visit `http://localhost:8080/` in your browser.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

For a complete list of commands:

```bash
$ gulp help
```

Initializing or Resetting the project
------------------------------------

```bash
$ cd /path/to/project-name
$ npm install
$ gulp
```

If something goes wrong you can always do:

```bash
$ gulp reset
$ npm install
$ gulp
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

To install [Gulp][] as a global package:

```bash
$ npm install -g gulp
```

Deploying on Google App Engine
------------------------------

```bash
$ gulp deploy
```

Before deploying make sure that the `main/app.yaml` and `gulp/config.coffee`
are up to date.

Development
-----------
For Design references look at [Bootstrap Material](https://github.com/FezVrasta/bootstrap-material-design#getting-started) & [Bootstrap Elements](http://fezvrasta.github.io/bootstrap-material-design/bootstrap-elements.html)

This is built on top of [gae-init](https://github.com/gae-init/gae-init). Review the project to get idea of what's going on in the overall project. Understanding how gae-init works should give you enough direction on how to make changes.
Tips and Tricks to increase productivity: the gae-init project comes with a bunch of utils to make development easy refer to the d[ocs](http://docs.gae-init.appspot.com/what/) for more help.

Have questions? Submit an [issue](https://github.com/wilfriedE/FIRSTMastery/issues/new).

GOALS and Objectives :
---------------------
- Build the best learning platform for the FIRST community.
- Make the platform as collaborative and community central as possible.
- Make the project modular and understanstable so anyone can contribute.
- *become a contributor and introduce your goals...

All Contributions are welcome. 
