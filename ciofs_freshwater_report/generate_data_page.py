"""Generate the model-data comparison notebooks to be turned into pages."""


import subprocess
import intake
import nbformat as nbf
import pandas as pd
import ocean_model_skill_assessor as omsa
from datetimerange import DateTimeRange
import numpy as np
import pathlib
import cf_pandas as cfp
import report_utils.page_utils as pu
import cook_inlet_catalogs as cic
# import more_utils as mu
import report_utils.utils as utils
from datetimerange import DateTimeRange

slugs_compared = [
                "adcp_moored_noaa_coi_2005",
                "adcp_moored_noaa_coi_other",
                "ctd_transects_barabara_to_bluff_2002_2003",
                "ctd_transects_cmi_kbnerr", 
                "ctd_transects_cmi_uaf",
                "ctd_transects_gwa", 
                "ctd_transects_otf_kbnerr",
                "ctd_transects_uaf",  
                "ctd_profiles_2005_noaa",
                "ctd_profiles_kachemack_kuletz_2005_2007",
                "ctd_profiles_kb_small_mesh_2006",
                "drifters_ecofoci",
                "drifters_uaf",
                "hfradar",
                "moorings_aoos_cdip",
                "moorings_circac",
                "moorings_kbnerr",
                "moorings_kbnerr_bear_cove_seldovia",
                "moorings_kbnerr_historical", 
                "moorings_kbnerr_homer",
                "moorings_noaa",
                "moorings_uaf",
]


def page():
  
    nb = nbf.v4.new_notebook()
    # nb['cells'] = [pu.imports_cell(),]

    nb['cells'].append(pu.text_cell(pu.header_text("Dataset Pages", header=1)))

    ## Loop over source names
    for slug in slugs_compared:
        
        cat =  intake.open_catalog(cic.utils.cat_path(slug))

        link1 = f"https://ciofs.axds.co/outputs/pages/data/{slug}.html"
        link2 = f"https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/{slug}.html"
        # nb['cells'].append(pu.text_cell(f"{slug}: [Dataset description]({link1}), [catalog page]({link2})"))

        nb['cells'].append(pu.text_cell(pu.header_text(cat.metadata["project_name"], header=2)))
        
        if "drifter" in slug:
            text = f"""
* {cat.metadata["overall_desc"].lstrip()}
* {cat.metadata['summary'].lstrip()}
* [Catalog page]({link2}), link to page in GitHub repository documentation.

"""
        else:
            text = f"""
* {cat.metadata["overall_desc"].lstrip()}
* {cat.metadata['summary'].lstrip()}
* [Dataset description]({link1}), link to page in CIOFS Hindcast report {{cite:p}}`ciofs_hindcast`.
* [Catalog page]({link2}), link to page in GitHub repository documentation.

"""

        nb['cells'].append(pu.text_cell(text))

    file = "data_catalogs.ipynb"
    nbf.write(nb, file)

    # Run jupytext command
    subprocess.run(["jupytext", "--to", "myst", file])


# Generate comparison pages
if __name__ == "__main__":

    page()
