(page:model_assessment)=
# Model Assessment Summary

A summary of the model comparisons with the data variables is given in this section. The "Overview" pages have Taylor diagrams and plots that show the skill score as a summary metric from each model-data comparison shown in the subpages (see {ref}`page:intro_comparisons`).

The previous report {cite:p}`ciofs_hindcast` demonstrated that the CIOFS Hindcast model does not having enough freshwater input into the system to have realistic salinity variability, nor accurate salinity. The CIOFS Hindcast model performs better for other variables. The major seasonal sea water temperature signal is well-captured, though temperature anomaly is not. CIOFS Hindcast captures the tidal sea surface height well, and mostly does well at subtidal sea surface height as well. It also captures horizontal speed reasonably well.

Next we will summarize how the CIOFS Hindcast and CIOFS Freshwater models perform when compared with the data across these variables. See {ref}`page:intro_comparisons` for how to read in the individual model-data comparison figures.


## Salinity

The CIOFS Freshwater model is forced with freshwater accounting for the whole watershed, and the amount of freshwater input into the model is much higher than is input into the CIOFS Hindcast model (see details in {ref}`page:model_description`). Given this, we can expect there to be much fresher water in the salinity field compared to the CIOFS Hindcast. 

The salinity field is captured much better by CIOFS Freshwater than CIOFS Hindcast when looking at CTD transects (see {numref}`Fig. {number}<fig-ctd_transects_by_region>`). For example, whereas a CIOFS Hindcast CTD transect ({numref}`Fig. {number}<fig-ctd_transects_cmi_kbnerr_Cruise_06-Line_2_salt-ciofs-hindcast>`) is nearly uniformly salty, the equivalent CIOFS Freshwater transect ({numref}`Fig. {number}<fig-ctd_transects_cmi_kbnerr_Cruise_06-Line_2_salt-ciofs-fresh>`) has good horizontal variability and some vertical variability.




```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/ctd_transects_cmi_kbnerr/ctd_transects_cmi_kbnerr_ciofs_hindcast/ctd_transects_cmi_kbnerr_Cruise_06-Line_2_salt.png
---
name: fig-ctd_transects_cmi_kbnerr_Cruise_06-Line_2_salt-ciofs-hindcast
---
Example of CIOFS Hindcast CTD transect comparison with salinity data (from the CMI KBNERR project of repeated transects across Cook Inlet).
```


```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/ctd_transects_cmi_kbnerr/ctd_transects_cmi_kbnerr_ciofs_fresh/ctd_transects_cmi_kbnerr_Cruise_06-Line_2_salt.png
---
name: fig-ctd_transects_cmi_kbnerr_Cruise_06-Line_2_salt-ciofs-fresh
---
Example of CIOFS Freshwater CTD transect comparison with salinity data (from the CMI KBNERR project of repeated transects across Cook Inlet).
```


Similarly, a CIOFS Hindcast along-bay CTD transect ({numref}`Fig. {number}<fig-ctd_transects_gwa_transect_AlongBay-2014-08-14_salt-ciofs-hindcast>`) is nearly uniformly salty, while the equivalent CIOFS Freshwater transect ({numref}`Fig. {number}<fig-ctd_transects_gwa_transect_AlongBay-2014-08-14_salt-ciofs-fresh>`) has good horizontal variability and vertical variability, though the water is still too salty.


```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/ctd_transects_gwa/ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2014-08-14_salt.png
---
name: fig-ctd_transects_gwa_transect_AlongBay-2014-08-14_salt-ciofs-hindcast
---
Example of CIOFS Hindcast CTD transect comparison with salinity data (from the GWA project of repeated transects across Cook Inlet).
```


```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/ctd_transects_gwa/ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2014-08-14_salt.png
---
name: fig-ctd_transects_gwa_transect_AlongBay-2014-08-14_salt-ciofs-fresh
---
Example of CIOFS Freshwater CTD transect comparison with salinity data (from the GWA project of repeated transects across Cook Inlet).
```

Looking at CTD profiles, CIOFS Freshwater has both better correlation and improved variance over CIOFS Hindcast (see {numref}`Fig. {number}<fig-ctd_profiles_by_region>`). Salinity profiles in Kachemak Bay are better in CIOFS Freshwater. In the example profiles below, CIOFS Hindcast has a well-mixed profile that is salty whereas CIOFS Freshwater has a more realistic, fresh surface layer.


```{image} ciofs-skill-assessment/ciofs_skill_assessment/report/ctd_profiles_kachemack_kuletz_2005_2007/ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_202_0_salt.png
:width: 40%
```

```{image} ciofs-skill-assessment/ciofs_skill_assessment/report/ctd_profiles_kachemack_kuletz_2005_2007/ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_202_0_salt.png
:width: 40%

```

Salinity time series are not well-represented by either model (see {numref}`Fig. {number}<fig-moorings_by_region_salt>`). While we find some improved skill score for CIOFS Freshwater, primarily we find substantially more variability as compared with CIOFS Hindcast. For example, this is noticeable at a deep mooring where the subtidal salinity time series from CIOFS Hindcast across a year is relatively constant ({numref}`Fig.  {number}<fig-moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2006-01-01_2007-01-01_subtidal-ciofs-hindcast>`) but the additional freshwater leads to increased variability in the CIOFS Freshwater model ({numref}`Fig.  {number}<fig-moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2006-01-01_2007-01-01_subtidal-ciofs-fresh>`), though not much improved skill score (0.3 vs 0.1). 


```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_kbnerr_bear_cove_seldovia/moorings_kbnerr_bear_cove_seldovia_ciofs_hindcast/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: fig-moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2006-01-01_2007-01-01_subtidal-ciofs-hindcast
---
Example of CIOFS Hindcast deep water subtidal time series comparison with salinity data (Station `nerrs-kacsdwq`).
```

```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_kbnerr_bear_cove_seldovia/moorings_kbnerr_bear_cove_seldovia_ciofs_fresh/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: fig-moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2006-01-01_2007-01-01_subtidal-ciofs-fresh
---
Example of CIOFS Freshwater deep water subtidal time series comparison with salinity data (Station `nerrs-kacsdwq`).
```



## Currents

The currents are mostly captured similarly for the two models for HF Radar and ADCP data, though generally the subtidal time series from CIOFS Fresh have improved variance.

However, comparisons between *in situ* drifters and numerical particle simulations show differences between the models depending on the area and depth of the domain in which the drifter was traveling. The EcoFOCI drifters mostly traveled outside of Cook Inlet in the Gulf of Alaska where differences in freshwater due to the improved freshwater forcing in CIOFS Freshwater are minimal. Accordingly, the particle simulations and skill scores there are similar between the two models. These and deeper UAF drifter results can particularly be seen in the overview plots at 15m and 40m depth (see salinity profile above for variability with depth for example).

The UAF drifters are in Cook Inlet where freshwater is potentially an important feature, and they were run at multiple depths. The rest of the UAF drifters besides those run at 15m depth were run at 7.5, 5, and 1m depth, and with shallower depth there is increasing difference between the CIOFS Hindcast and CIOFS Freshwater particle simulations as the freshwater takes on a more important role. For example, the CIOFS Hindcast 1m particles ({numref}`Fig.  {number}<fig-CIDrifter0008Y2013_MicrostarSurfaceAt1M_deployment4-ciofs-hindcast>`) are limited in transport compared to the CIOFS Freshwater particles ({numref}`Fig.  {number}<fig-CIDrifter0008Y2013_MicrostarSurfaceAt1M_deployment4-ciofs-fresh>`), which travel much farther through the Inlet with the freshwater present in the system. The CIOFS Freshwater particles are much more accurate than the CIOFS Hindcast particles.

```{figure} ciofs-drifter-sims/ciofs_drifter_sims/CIOFS/CIDrifter0008Y2013_MicrostarSurfaceAt1M_deployment4.png
---
name: fig-CIDrifter0008Y2013_MicrostarSurfaceAt1M_deployment4-ciofs-hindcast
width: 70%
---
Example of CIOFS Hindcast 1m drifter and particle simulations (drifter `CIDrifter0008Y2013_MicrostarSurfaceAt1M_deployment4`).
```


```{figure} ciofs-drifter-sims/ciofs_drifter_sims/CIOFSFRESH/CIDrifter0008Y2013_MicrostarSurfaceAt1M_deployment4.png
---
name: fig-CIDrifter0008Y2013_MicrostarSurfaceAt1M_deployment4-ciofs-fresh
width: 70%
---
Example of CIOFS Freshwater 1m drifter and particle simulations (drifter `CIDrifter0008Y2013_MicrostarSurfaceAt1M_deployment4`).
```



## Temperature

The seasonal temperature range is relatively easy to capture by a numerical model, and both the CIOFS Hindcast and Freshwater models often capture the full tidal or subtidal temperature time series shown in the moorings data. However, they do have differences. While the CIOFS Hindcast model has the full seasonal temperature range at the head of the Inlet (NOAA 9455920, {numref}`Fig.  {number}<fig-moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal-ciofs-hindcast>`) and the south end of Kodiak Island (NOAA 9457804), it is a bit too cool relative to the data in the summer west of Kodiak Island (WMO 46077) and in the spring and summer east of Kodiak Island (NOAA 9457292). In Kachemak Bay, the CIOFS Hindcast model is more likely to be somewhat cold relative to the data throughout the year at the surface ({numref}`Fig.  {number}<fig-moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2006-01-01_2007-01-01_subtidal-ciofs-hindcast>`) and at depth ({numref}`Fig.  {number}<fig-moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal-ciofs-hindcast>`), except in the summer.

```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_noaa/moorings_noaa_ciofs_hindcast/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal-ciofs-hindcast
---
Example of CIOFS Hindcast surface water subtidal time series comparison at the head of the Inlet with temperature data (Station `noaa_nos_co_ops_9455920`).
```

```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_kbnerr_bear_cove_seldovia/moorings_kbnerr_bear_cove_seldovia_ciofs_hindcast/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2006-01-01_2007-01-01_subtidal-ciofs-hindcast
---
Example of CIOFS Hindcast surface water subtidal time series comparison in Kachemak Bay with temperature data (Station `nerrs_kacsswq`).
```

```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_kbnerr_homer/moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal-ciofs-hindcast
---
Example of CIOFS Hindcast deep water subtidal time series comparison in Kachemak Bay with temperature data (Station `nerrs_kachdwq`).
```


CIOFS Freshwater shows consistently low temperatures in the subtidal temperature signal across the year in the same locations shown for CIOFS Hindcast: NOAA 9455920 ({numref}`Fig.  {number}<fig-moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal-ciofs-fresh>`), Kachemak Bay surface ({numref}`Fig.  {number}<fig-moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2006-01-01_2007-01-01_subtidal-ciofs-fresh>`), and Kachemak Bay deep ({numref}`Fig.  {number}<fig-moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal-ciofs-fresh>`).



```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_noaa/moorings_noaa_ciofs_fresh/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal-ciofs-fresh
---
Example of CIOFS Freshwater surface water subtidal time series comparison at the head of the Inlet with temperature data (Station `noaa_nos_co_ops_9455920`).
```

```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_kbnerr_bear_cove_seldovia/moorings_kbnerr_bear_cove_seldovia_ciofs_fresh/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2006-01-01_2007-01-01_subtidal-ciofs-fresh
---
Example of CIOFS Freshwater surface water subtidal time series comparison in Kachemak Bay with temperature data (Station `nerrs_kacsswq`).
```

```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_kbnerr_homer/moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal-ciofs-fresh
---
Example of CIOFS Freshwater deep water subtidal time series comparison in Kachemak Bay with temperature data (Station `nerrs_kachdwq`).
```


CIOFS Freshwater saw some small improvement in the difficult measure of temperature anomaly. For example, showing the same year as the other examples, whereas CIOFS Hindcast demonstrates only moderate skill in this measure with a skill score of 0.6, CIOFS Freshwater has 0.9 and visually follows the trend of the data through the year.


```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_kbnerr_homer/moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean-ciofs-hindcast
---
Example of CIOFS Freshwater deep water subtidal temperature anomaly time series comparison in Kachemak Bay with temperature data (Station `nerrs_kachdwq`).
```

```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_kbnerr_homer/moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean-ciofs-fresh
---
Example of CIOFS Freshwater deep water subtidal temperature anomaly time series comparison in Kachemak Bay with temperature data (Station `nerrs_kachdwq`).
```


CTD transects for temperature are similar between CIOFS Hindcast and CIOFS Freshwater, but CIOFS Freshwater does perform better, as seen in Figs. {numref}`{number}<fig-ctd_transects_by_region>` and {numref}`{number}<fig-ctd_transects_by_season>`.


## Sea Surface Height

Both models capture the tidal sea surface height well. CIOFS Freshwater represents the subtidal sea surface height more accurately than CIOFS Hindcast ({numref}`Fig. {number}<fig-moorings_by_region_ssh>`), and the highest skill scores are at station 9455920 near Anchorage. However, note an important difference in how the CIOFS Freshwater model is able to capture peaks in a way that the CIOFS Hindcast model is not. CIOFS Hindcast for an example year at this station ({numref}`Fig.  {number}<fig-moorings_noaa_noaa_nos_co_ops_9455920_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal-ciofs-hindcast>`) shows subtidal variability, but it misses most unique peaks and troughs. CIOFS Freshwater  ({numref}`Fig.  {number}<fig-moorings_noaa_noaa_nos_co_ops_9455920_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal-ciofs-fresh>`) captures many of these, implying that these peaks and troughs are due to freshwater input.


```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_noaa/moorings_noaa_ciofs_hindcast/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: fig-moorings_noaa_noaa_nos_co_ops_9455920_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal-ciofs-hindcast
---
Example of CIOFS Hindcast subtidal time series comparison with sea surface height data (Station `noaa_nos_co_ops_9455920`).
```


```{figure} ciofs-skill-assessment/ciofs_skill_assessment/report/moorings_noaa/moorings_noaa_ciofs_fresh/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: fig-moorings_noaa_noaa_nos_co_ops_9455920_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal-ciofs-fresh
---
Example of CIOFS Freshwater subtidal time series comparison with sea surface height data (Station `noaa_nos_co_ops_9455920`).
```





