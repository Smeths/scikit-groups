.. scikit-groups documentation master file, created by
   sphinx-quickstart on Fri Jan  5 19:11:01 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to scikit-groups' documentation!
========================================

scikit-groups is a framework for creating mathematical groups and experimenting with them in python. Read the paper_ we produced earlier in the year to get an idea of the kind of problems we will be solving as we develop this package. All of the code used in the paper is available at my github account_.

The project is in its infancy at the moment, but we do have the following short to medium term goals:

1. Producing a developer guide

There are infinitely many ways to define a group. Therefore simplifying the process of augmenting the framework we have produced is vital. Ideally, anyone who is 'group literate' and has basic programming skills should be able to define the relevant aspects of a specific group and add it to our framework with a minimum effort.

2. Developing use cases and show casing interesting group applications

Jupyter notebooks seem like the ideal tool for demonstrating the applications of our package. They allow for the combination of python code, latex, and advanced and interactive plotting tools in one document. Ideally we would like to create a number of use cases in this way.

3. Continuous integration test cases

As we develop different types of groups it is important to regularly regression test and expand the scope of the regression testing we perform. The combination of travis-ci and github seems ideal for this task. 

To get involved, drop us a note on the following irc channel

.. toctree::
   :maxdepth: 2
   
   install
   support



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _paper: https://arxiv.org/abs/1711.05814
.. _account: https://github.com/Smeths/scikit-groups
