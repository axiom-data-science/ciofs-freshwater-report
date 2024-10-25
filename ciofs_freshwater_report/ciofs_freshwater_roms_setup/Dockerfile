FROM ubuntu:latest

RUN apt-get update && apt-get install -y wget bzip2 git parallel libnetcdf-dev libnetcdff-dev gfortran

# Install Miniconda
RUN wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
    bash Miniforge3-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniforge3-Linux-x86_64.sh
ENV PATH /opt/conda/bin:$PATH

# Create and activate conda environment
COPY environment.yaml /tmp/environment.yaml
RUN mamba env update -n base -f /tmp/environment.yaml && \
    conda clean -afy

RUN git clone https://github.com/cliu3/pyroms.git
RUN pip install -e pyroms/pyroms
RUN pip install -e pyroms/pyroms_toolbox
RUN pip install -e pyroms/bathy_smoother

# Set working directory
WORKDIR /app
# Default command
CMD [ "bash" ]
