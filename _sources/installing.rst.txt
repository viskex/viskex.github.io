Installation
============
.. meta::
    :description lang=en:
        Installation requirements are automatically handled during the setup.
        In order to run the tutorials you may need to install one of the supported finite element backends.

Prerequisites
-------------

Installation requirements are automatically handled during the setup.
In order to run the tutorials you may need to install one of the supported finite element backends, namely `dolfinx <https://github.com/FEniCS/dolfinx>`__ and `firedrake <https://github.com/firedrakeproject/firedrake>`__.

Installation
------------

**viskex** is available on PyPI. It uses extras to specify the finite element backend when installing via `pip` and to install additional packages required to run the tutorials.

Installation with the dolfinx backend
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    python3 -m pip install 'viskex[backend-dolfinx,tutorials]'

Installation with the firedrake backend
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    python3 -m pip install 'viskex[backend-firedrake,tutorials]'

Running tutorials
-----------------

To run the tutorials, first clone the **viskex** repository. Then, ensure you check out the tag that corresponds to the version of **viskex** currently installed.

.. code-block:: console

    git clone https://github.com/viskex/viskex.git
    cd viskex
    VISKEX_VERSION=$(python3 -c "import viskex; print(viskex.__version__)")
    git checkout ${VISKEX_VERSION}
