Installation
============
.. meta::
    :description lang=en:
        viskex is available on PyPI. Use pip extras to install all required dependencies.
        In order to run the tutorials you may need to install one of the supported finite element backends.

Prerequisites
-------------

In order to run the tutorials you may need to install one of the supported finite element backends, namely `dolfinx <https://github.com/FEniCS/dolfinx>`__ and `firedrake <https://github.com/firedrakeproject/firedrake>`__.

Installation
------------

**viskex** is available on PyPI. Use `pip` extras to select the finite element backend and install additional dependencies needed for the tutorials.

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
