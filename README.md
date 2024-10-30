# Report for CIOFS Ocean Model with Improved Freshwater Forcing


## Create report content

The models have already been run, and the outputs from steps 2-5 are available in their respective repositories on GitHub so that the report pieces are all available, though these steps could all be repeated by running the projects below instead of using the available outputs.

1. Run ROMS models
    * ROMS set up described for CIOFS hindcast model in [previous project report](https://ciofs.axds.co/model_overview_and_setup/description_of_models.html) and for CIOFS freshwater model in the [present project report](https://ciofs-fresh.axds.co/model_description.html).
    * The forcing file set up for CIOFS freshwater is provided in this repository (`ciofs_freshwater_roms_setup`, which are originally from [https://github.com/ESMG/pyroms/tree/python3/examples/Hill_runoff/new_ROMS](https://github.com/ESMG/pyroms/tree/python3/examples/Hill_runoff/new_ROMS))
    * CIOFS Hindcast model output is available at its [portal link](https://portal.aoos.org/?ls=nXIcHlsW#module-metadata/ff82ba46-9d33-487e-aa83-d57c7521d6b0)
    * CIOFS Freshwater model output is available at its [portal link](https://ciofs-fresh.axds.co/model_description.html#)
1. Make plots to compare the mean surface salinity between the two models with  [ciofs-fresh-hind-salinity-plots](https://github.com/axiom-data-science/ciofs-fresh-hind-salinity-plots). Clone project into `ciofs-freshwater-report/ciofs_freshwater_report`.
1. Access datasets to compare with model output through [cook-inlet-catalogs](https://github.com/axiom-data-science/cook-inlet-catalogs). Clone project into `ciofs-freshwater-report/ciofs_freshwater_report`.
1. Run numerical particle simulations to match drifter data using files in [ciofs-drifter-sims](https://github.com/axiom-data-science/ciofs-drifter-sims). Clone project into `ciofs-freshwater-report/ciofs_freshwater_report`.
1. Run model-data comparisons and plots with [ciofs-skill-assessment](https://github.com/axiom-data-science/ciofs-skill-assessment). Clone project into `ciofs-freshwater-report/ciofs_freshwater_report`.


## Set up environment

Set up environment with `environment.yml`:

    mamba env create -f environment.yml


## Compile report

Activate environment with 

    conda activate ciofs-freshwater-report

In `ciofs_freshwater_report`:

    jupyter-book build .

After compiling locally, move the report to its sharing location, which is currently `/mnt/vault/http_files/ciofs_fresh`.
