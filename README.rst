Confiture
=========

    Funny fact: confiture looks like configure.

Confiture, what's that?
-----------------------

[STRIKEOUT:Jam typically contains both the juice and flesh of a fruit or
vegetable, although some cookbooks define it as a cooked and jelled
puree. The term "jam" refers to a product made of whole fruit cut into
pieces or crushed, then heated with water and sugar to activate its
pectin before being put into containers.]

Confiture is a small piece of code to test a ``yaml`` configuration
file. By test we mean check that some required fields are indeed set.

Installation
------------

::

    spread confiture

Oh really? - No.

::

    pip install confiture

Oh really? - Nope, pip name ``confiture`` was already used.

.. code:: bash

    pip install spread-confiture

Oh really? - Hell yeah.

Requirements
~~~~~~~~~~~~

This project requires ``pyyaml`` to parse ``yaml`` files.

Usage
-----

Template file
~~~~~~~~~~~~~

A template file is a file that describes the fields that we want to
check when parsing a configuration file. It is also written in ``yaml``,
with the following scheme:

.. code:: yaml

    foo:
        bar: ""
        foobar:
            foo: ""
            bar: ""

    bar: ""

A configuration file is consistant relatively to the template file if
every required field specified by the template are set. Note that the
configuration can also set other fields that are not specified by the
template.

Create a ``Confiture`` object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a ``Confiture`` object relatively to a given template file:

.. code:: python

    from confiture import Confiture
    # conf pour confiture ou configration ?
    conf = Confiture("examples/templates/confiture.yaml")

Parse a configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the ``Confiture`` object is created, we can test ``yaml``
configuration files:

.. code:: python

    # Simple test
    conf.check("examples/config/blueberry_ok.yaml")
    # Test et récupération du contenu du fichier sous forme de dictionnaire
    config = conf.check_and_get("examples/config/blueberry_ok.yaml")

If the configuration file is not consistant with the template, a
``ConfigFileError`` exception is raised.

Example
-------

Code
~~~~

.. code:: python

    from confiture import Confiture, ConfigFileError

    print "[*] loading template"
    confiture = Confiture("examples/templates/confiture.yaml")
    print "[*] checking required files for blueberry"
    try:
        confiture.check("examples/config/blueberry_ok.yaml")
        print "[*] blueberry file is correct"
    except ConfigFileError as e:
        print e.message
    print "[*] checking required files for banana"
    try:
        confiture.check("examples/config/banana_ko.yaml")
        print "[*] banana file is correct"
    except ConfigFileError as e:
        print e.message

Output
~~~~~~

::

    (confiture) > python ./example.py 
    [*] loading template
    [*] checking required files for blueberry
    [*] blueberry file is correct
    [*] checking required files for banana
    *** fruit field not found -- aborting

FAQ
---

**How did you get the idea to do (some) Confiture?**

*It was a forbidden morning of September, breakfast time. At the exact
moment when I started speading Nutella on my toast...*

**Why a documentation?**

*Because a project without documentation is like a Confiture without
bananas.*

**Why a documentation THAT long?**

*Because documentation is like banana in Confiture, the more there is
the better it tastes.*

**Why a documentation THAT long for a project this simple?**

*Because now I can say that once in my life I wrote a documentation
longer than the code itself.*
