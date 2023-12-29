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

Installation and usage
----------------------

Simply clone the **viskex** public repository:

.. code-block:: console

    git clone https://github.com/viskex/viskex.git

and install the package by typing

.. code-block:: console

    cd viskex
    python3 -m pip install '.[tutorials]'

External libraries used for plotting
------------------------------------
1D plots are provided by :code:`plotly`, while 2D/3D plots are rendered with :code:`pyvista` using :code:`trame`. The default :code:`pyvista` backend is :code:`client` when running in JupyterLab, and :code:`html` when running on Google Colab or Kaggle. Users can customize the active :code:`pyvista` backend by exporting the environment variable :code:`VISKEX_PYVISTA_BACKEND`: such operation is typically not required, with the only notable exceptions being testing different :code:`pyvista` backends on CI, or exporting notebooks to html via :code:`nbconvert`.

Compatibility with upstream releases
------------------------------------

The :code:`main` branch of **viskex** targets the :code:`main` branch of :code:`dolfinx` and :code:`firedrake`, which may contain API changes compared to the latest release of the finite element backend. A new **viskex** version is not necessarily tagged alongside :code:`dolfinx` or :code:`firedrake` releases. Users willing to work with a fixed release of the finite element backend are encouraged to look for a **viskex** `commit <https://github.com/viskex/viskex/commits/main>`__ close to the upstream release date, and do a

.. code-block:: console

    git checkout {commit SHA}

before installing **viskex**.
