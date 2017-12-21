Arrr.py - Pirate Speak for Python
=================================

A simple script / module to turn plain English into Pirate speak. Arrr.

Someone mentioned something called "Pirate Python", I idly wondered if anyone
had made an English to Pirate-ish module/command written in Python (they
hadn't), I realised I had a burning desire to make one, and things got out of
hand. :-)

We have an entirely serious `code of conduct <https://github.com/ntoll/arrr/blob/master/CODE_OF_CONDUCT.rst>`_
and a not-so-serious `code of mis-conduct <https://github.com/ntoll/arrr/blob/master/CODE_OF_MISCONDUCT.rst>`_
for those of a more Piratical disposition.

Installation
------------

To install simply type::

    $ pip install arrr

...and the package will download from PyPI. If you wish to upgrade to the
latest version, use the following command::

    $ pip install --no-cache --upgrade arrr

Command Usage
-------------

Once installed, you'll find you have a ``pirate`` command to use in your shell.

To read the (non-Pirate friendly) help, simply type::

    $ pirate --help

or::

    $ pirate -h

To translate plain English into something Pirate-ish simply call the command
followed by some English sentence::

    $ pirate hello there. how are you today?
    Ahoy there. Weigh anchor and hoist the mizzen! How are ye today?

The ``pirate`` command will reply with a Pirate-ish equivalent (as shown
above).

.. note::

    **This software misbehaves like a Pirate.**

    Sometimes, the ``pirate`` command will not only translate English to
    Pirate-ish, but will also interject with Pirate sayings (such as,
    "Weigh anchor and hoist the mizzen!" as shown above).

    This is entirely normal and perfectly Piratical behaviour. What else
    were you expecting..?

Using the API
-------------

The ``arrr`` module's API is fully documented below. All you really need is to
import the ``translate`` function and use that to return Pirate-ish sentences
from a given input in English::

    from arrr import translate


    english = "Hello there. How are you?"
    pirate = translate(english)
    print(pirate)

The script above will print output similar to that for the command-line usage
example shown above.

Development
-----------

The source code is  `hosted in GitHub <https://github.com/ntoll/arrr>`_. Please
feel free to fork the repository and contribute.
Assuming you have Git installed you can download the code from the canonical
repository with the following command::

    $ git clone https://github.com/ntoll/arrr.git

Ensure you have the correct dependencies for development installed by creating
a virtualenv and running::

    $ pip install -r requirements.txt

Pull requests are most welcome! Honestly, the ``arrr`` module was cobbled
together in about 5 minutes and I went overboard (geddit?) with creating a
simple yet well packaged and documented project so ``arrr`` can act as a good
example for beginner developers.

If you find any bugs, `submit a new issue <https://github.com/ntoll/arrr/issues/new>`_.
