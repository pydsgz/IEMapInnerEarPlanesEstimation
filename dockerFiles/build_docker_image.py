import os

# Do not forget to login to IEsegmap account first with the command
# docker login

# Specify version that will be appended to the Docker image name
version = '0.1.0'

# Get the current directory 
current_folder = os.getcwd()

# Download supplements
if not os.path.exists(os.path.join(current_folder, 'innerEarSupplements_v_0_1_3.zip?dl=0')):
    os.system(f'wget https://www.dropbox.com/s/wdelnnxndgana0e/innerEarSupplements_v_0_1_3.zip?dl=0 -P {current_folder}')
if not os.path.exists(os.path.join(current_folder,'ants')):
    # Get the zip file 
    zip_file = os.path.join(current_folder, 'innerEarSupplements_v_0_1_3.zip?dl=0')

    # Unzip it and delete the zip file
    os.system(f'unzip {zip_file} -d {current_folder}')
    #os.system(f'rm {zip_file}')

# Docker build 
docker_file = os.path.join(current_folder, 'Dockerfile')
os.system(f'docker build -t iesegmap/ie-plane-normals:{version} {current_folder}/.')
