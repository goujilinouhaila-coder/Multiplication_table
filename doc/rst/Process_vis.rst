Process visualization
=====================

This folder contains all the functions and class that designate the graphic part of the project, 
which uses several graphic tools, such as Tkinter, Canvas and other Widgets.
We have two types of representations, one which is fixed and the other which is interactive.
There also are other aspects of the interface as an example : The GIF generator and other 
aspects of the representation such as the **TABLE** button.

Base visualization
------------------

.. autofunction:: process_vis.base_vis.circle

.. autofunction:: process_vis.base_vis.coord

.. autofunction:: process_vis.base_vis.angle_tab

.. autofunction:: process_vis.base_vis.dot 

.. autofunction:: process_vis.base_vis.name_vertices

Edges visualization
-------------------

.. autofunction:: process_vis.edges_vis.all_edges

.. autofunction:: process_vis.edges_vis.one_edge

Interface
---------

.. autoclass:: process_vis.interface.Interface_gestion

.. autofunction:: process_vis.interface.Interface_gestion.__init__

.. autofunction:: process_vis.interface.Interface_gestion.design_aspect

.. autofunction:: process_vis.interface.Interface_gestion.window_init

.. autofunction:: process_vis.interface.Interface_gestion.graph_init

.. autofunction:: process_vis.interface.Interface_gestion.graph_vis

.. autofunction:: process_vis.interface.Interface_gestion.table

.. autofunction:: process_vis.interface.Interface_gestion.vertices

.. autofunction:: process_vis.interface.Interface_gestion.show_update

.. autofunction:: process_vis.interface.Interface_gestion.slider

.. autofunction:: process_vis.interface.Interface_gestion.move_value

.. autofunction:: process_vis.interface.Interface_gestion.save_frame

.. autofunction:: process_vis.interface.Interface_gestion.save_video

.. autofunction:: process_vis.interface.Interface_gestion.destroy_root

.. autofunction:: process_vis.interface.Interface_gestion.create_table_window

.. autofunction:: process_vis.interface.Interface_gestion.create_description

.. autofunction:: process_vis.interface.Interface_gestion.motion_button