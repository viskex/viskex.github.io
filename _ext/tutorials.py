tutorials = {
    "01": {
        "title": "Introduction",
        "description": "Introduction on simple 1D, 2D and 3D meshes",
        "steps": {
            "1D": {
                "dolfinx": "tutorials/01_introduction/tutorial_plot_mesh_1d_dolfinx.html",
                "firedrake": "tutorials/01_introduction/tutorial_plot_mesh_1d_firedrake.html"
            },
            "2D": {
                "dolfinx": "tutorials/01_introduction/tutorial_plot_mesh_2d_dolfinx.html",
                "firedrake": "tutorials/01_introduction/tutorial_plot_mesh_2d_firedrake.html"
            },
            "3D": {
                "dolfinx": "tutorials/01_introduction/tutorial_plot_mesh_3d_dolfinx.html",
                "firedrake": "tutorials/01_introduction/tutorial_plot_mesh_3d_firedrake.html"
            },
        },
    },
    "02": {
        "title": "Application to Lake Garda",
        "description": "Interactive visualization of meshes and simulations for Lake Garda",
        "steps": {
            "Application to Lake Garda": {
                "dolfinx": "tutorials/02_garda/tutorial_garda_dolfinx.html",
                "firedrake": "tutorials/02_garda/tutorial_garda_firedrake.html"
            },
        },
    },
}

next = {
    # tutorial 01: plot mesh
    "tutorials/01_introduction/tutorial_plot_mesh_1d_dolfinx.html": {
        "next step: plot subdomains": "tutorial_plot_subdomains_1d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_mesh_1d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_mesh_2d_dolfinx.html": {
        "next step: plot subdomains": "tutorial_plot_subdomains_2d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_mesh_2d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_mesh_3d_dolfinx.html": {
        "next step: plot subdomains": "tutorial_plot_subdomains_3d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_mesh_3d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_mesh_1d_firedrake.html": {
        "next step: plot subdomains": "tutorial_plot_subdomains_1d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_mesh_1d_dolfinx.html"
    },
    "tutorials/01_introduction/tutorial_plot_mesh_2d_firedrake.html": {
        "next step: plot subdomains": "tutorial_plot_subdomains_2d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_mesh_2d_dolfinx.html"
    },
    "tutorials/01_introduction/tutorial_plot_mesh_3d_firedrake.html": {
        "next step: plot subdomains": "tutorial_plot_subdomains_3d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_mesh_3d_dolfinx.html"
    },
    # tutorial 01: plot subdomains
    "tutorials/01_introduction/tutorial_plot_subdomains_1d_dolfinx.html": {
        "next step: plot boundaries": "tutorial_plot_boundaries_1d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_subdomains_1d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_subdomains_2d_dolfinx.html": {
        "next step: plot boundaries": "tutorial_plot_boundaries_2d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_subdomains_2d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_subdomains_3d_dolfinx.html": {
        "next step: plot boundaries": "tutorial_plot_boundaries_3d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_subdomains_3d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_subdomains_1d_firedrake.html": {
        "next step: plot boundaries": "tutorial_plot_boundaries_1d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_subdomains_1d_dolfinx.html"
    },
    "tutorials/01_introduction/tutorial_plot_subdomains_2d_firedrake.html": {
        "next step: plot boundaries": "tutorial_plot_boundaries_2d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_subdomains_2d_dolfinx.html"
    },
    "tutorials/01_introduction/tutorial_plot_subdomains_3d_firedrake.html": {
        "next step: plot boundaries": "tutorial_plot_boundaries_3d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_subdomains_3d_dolfinx.html"
    },
    # tutorial 01: plot boundaries
    "tutorials/01_introduction/tutorial_plot_boundaries_1d_dolfinx.html": {
        "next step: plot a scalar field": "tutorial_plot_scalar_field_1d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_boundaries_1d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_boundaries_2d_dolfinx.html": {
        "next step: plot a scalar field": "tutorial_plot_scalar_field_2d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_boundaries_2d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_boundaries_3d_dolfinx.html": {
        "next step: plot a scalar field": "tutorial_plot_scalar_field_3d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_boundaries_3d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_boundaries_1d_firedrake.html": {
        "next step: plot a scalar field": "tutorial_plot_scalar_field_1d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_boundaries_1d_dolfinx.html"
    },
    "tutorials/01_introduction/tutorial_plot_boundaries_2d_firedrake.html": {
        "next step: plot a scalar field": "tutorial_plot_scalar_field_2d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_boundaries_2d_dolfinx.html"
    },
    "tutorials/01_introduction/tutorial_plot_boundaries_3d_firedrake.html": {
        "next step: plot a scalar field": "tutorial_plot_scalar_field_3d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_boundaries_3d_dolfinx.html"
    },
    # tutorial 01: plot scalar field
    "tutorials/01_introduction/tutorial_plot_scalar_field_1d_dolfinx.html": {
        "repeat this step with firedrake": "tutorial_plot_scalar_field_1d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_scalar_field_2d_dolfinx.html": {
        "next step: plot a vector field": "tutorial_plot_vector_field_2d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_scalar_field_2d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_scalar_field_3d_dolfinx.html": {
        "next step: plot a vector field": "tutorial_plot_vector_field_3d_dolfinx.html",
        "repeat this step with firedrake": "tutorial_plot_scalar_field_3d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_scalar_field_1d_firedrake.html": {
        "repeat this step with dolfinx": "tutorial_plot_scalar_field_1d_dolfinx.html"
    },
    "tutorials/01_introduction/tutorial_plot_scalar_field_2d_firedrake.html": {
        "next step: plot a vector field": "tutorial_plot_vector_field_2d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_scalar_field_2d_dolfinx.html"
    },
    "tutorials/01_introduction/tutorial_plot_scalar_field_3d_firedrake.html": {
        "next step: plot a vector field": "tutorial_plot_vector_field_3d_firedrake.html",
        "repeat this step with dolfinx": "tutorial_plot_scalar_field_3d_dolfinx.html"
    },
    # tutorial 01: plot vector field
    "tutorials/01_introduction/tutorial_plot_vector_field_2d_dolfinx.html": {
        "repeat this step with firedrake": "tutorial_plot_vector_field_2d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_vector_field_3d_dolfinx.html": {
        "repeat this step with firedrake": "tutorial_plot_vector_field_3d_firedrake.html"
    },
    "tutorials/01_introduction/tutorial_plot_vector_field_2d_firedrake.html": {
        "repeat this step with dolfinx": "tutorial_plot_vector_field_2d_dolfinx.html"
    },
    "tutorials/01_introduction/tutorial_plot_vector_field_3d_firedrake.html": {
        "repeat this step with dolfinx": "tutorial_plot_vector_field_3d_dolfinx.html"
    },
    # tutorial 02
    "tutorials/02_garda/tutorial_garda_dolfinx.html": {
        "repeat this tutorial with firedrake": "tutorial_garda_firedrake.html"
    },
    "tutorials/02_garda/tutorial_garda_firedrake.html": {
        "repeat this tutorial with dolfinx": "tutorial_garda_firedrake.html"
    },
}
