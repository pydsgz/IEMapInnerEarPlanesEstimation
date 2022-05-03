# IEMapInnerEarPlanesEstimation
Fully automatic bilateral inner ear atlas-based localization/segmentation + plane estimation for 3 semi-circular canals (SCCs), using IEMap and ANTs deformable registration.

If you use this repository, please cite the following papers:
  - Go et al., _Persistent horizontal and vertical, MR-induced nystagmus in resting state Human Connectome Project data_, NeuroImage, 2022, DOI: https://doi.org/10.1016/j.neuroimage.2022.119170
  - Ahmadi et al., _IE-Map: a novel in-vivo atlas and template of the human inner ear_, Scientific Reports, 2021, DOI: https://doi.org/10.1038/s41598-021-82716-0

Please note that the method is currently being validated. We cannot guarantee for the accuracy of the segmentation, a manual/visual qualitative control of all outputs are required.

# Docker usage
Specify local input and output folders to mount to the docker container with the option -v. The local input folder should contain the image(s) that will be processed and local output folder should be an empty folder where the output files will be saved. In the Docker container, input and output directories are located in the main dir location (/input and /output).

## Single-channel (i.e. single-contrast/single-modal) registration example
The example command below will process the T2 image (called my_T2.nii.gz) that you have on your local computer (in /home/exampleComputer/Desktop/localInput) and save the results to the output folder you specify (/home/exampleComputer/Desktop/localOutput/). This requires running the docker image with the correct volume mappings (first level of indentation) and then specifying the program parameters for running `iemap_seg.py` (second level of indentation):
 
    docker run \
       -v /home/exampleComputer/Desktop/localInput/:/input \
       -v /home/exampleComputer/Desktop/localOutput/:/output \
       iesegmap/ie-plane-normals:0.1.0 \
          --input_head_volumes /input/my_T2.nii.gz \
          --matching_template_modalities_head T2 \
          --input_ie_volumes /input/my_T2.nii.gz \
          --matching_template_modalities_ie T2 \
          --accuracy_head accurate \
          --accuracy_ie accurate \
          --output_dir /output

For all available processing options, run the code below after replacing "version" with the current version number you are running:

    "docker run iesegmap/ie-plane-normals:version --help"


