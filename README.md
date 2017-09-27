![crowdflow-logo](crowdflowLogo.png)

# MF_landing_data_analysis
This repository contains primers and examples to analyze the pedestrian tracking dataset collected at Eindhoven University of Technology (cf. Phys.Rev.E paper  https://doi.org/10.1103/PhysRevE.95.032316 ). 

The dataset has `DOI`: `10.4121/uuid:25289586-4fda-4931-8904-d63efe4aa0b8`  and will soon be downloadable from the `4TU.ResearchData` server.



The dataset contains pedestrian trajectories recorded on a nearly 24/7 schedule in a landing in the Metaforum building at Eindhoven University of Technology. The data acquisition spanned over a year and, overall, nearly 250.000 trajectories have been collected. The purpose of the dataset is to enable ensemble analyses of diluted pedestrian motion. Depth imaging data has been first obtained via an overhead Microsoft Kinect sensor. Hence, ad hoc localization algorithms and PTV-like tracking have been employed to estimate the trajectory of individual heads (cf. publication). 


This [jupyter notebook](Plot-trajectories.ipynb) shows how to use python pandas and the scripts in the file `MF_domain_related.py` to visualize the trajectories. 

## Examples:

Trajectories visualization 
![](trajectories_ex.png)

Position depth map
![](depth_maps_ex.png)

Walking speed pdf conditioned to the walking direction
![](walking_speed_pdf.png)
