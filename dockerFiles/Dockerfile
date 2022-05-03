# This makes a container for the gear. Replace the first path next to the second COPY function 
# below with a path to your local compiled matlab function

FROM neurodebian:xenial
MAINTAINER Ozzy(ozenctaskin@hotmail.com)

# Initialize some folders
RUN mkdir /input
RUN mkdir /output
COPY ants /segmentation_code/ants
COPY data /segmentation_code/data
COPY iemap_seg.py /segmentation_code/iemap_seg.py
COPY antsRegistration.py /segmentation_code/antsRegistration.py

# Install required packages    
RUN apt-get update \
    && apt-get install -y \
    git \
    wget \
    zip \
    python \
    unzip \
    ants \ 
    libgl1-mesa-glx \
    fsleyes \ 
    xvfb \
    python-vtk

# Install Anaconda
RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
RUN bash Anaconda3-2020.02-Linux-x86_64.sh -b -p /anaconda3
ENV PATH=$PATH:/anaconda3/bin
RUN conda update --all -y
RUN pip install nipype imageio SimpleITK nibabel matplotlib pandas flywheel-sdk
RUN pip install vtk==8.1.2

# Install fsleyes
RUN conda install -c conda-forge fsleyes

ENTRYPOINT ["/anaconda3/bin/python3", "/segmentation_code/iemap_seg.py"]
