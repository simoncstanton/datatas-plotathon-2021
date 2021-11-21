# datatas-plotathon-2021
entry for Datatas Plot-a-thon 2021 (https://github.com/datatas/The-Great-DataTas-plot-a-thon)


Nothing fancy here. Simple graph for knowing when *not* to go to Mt Everest.



![deaths_by_season_and_peak_heatmap](https://user-images.githubusercontent.com/84423041/142749924-8fc01e1e-5d75-4597-9e1f-0822298de06a.png)

Create by running
> python .\himalaya_deaths_heatmap.py

[It's a plotly graph so run it and will open in browser, allows to see all tooltips.]


------
------


Also these two graphs. Going somewhere but unresolved.
Interestingly, and sadly, the percentage of deaths of those 'hired' (Sherpas, mostly Nepalese) across all peaks is 28.7, but on Everest it rises to 39.21.

(_Deaths:_ All Peaks - 318 hired, 1106 total. Everest - 120 hired, 306 total.)

This doesn't seem to be the case for injuries though. Removing all records for injury type 'AMS' (heavily biased to 'expeditioners') didn't really change it either (not shown here). So question remains - are Sherpas more skilled, more careful, would removing exposure/frostbite as well as AMS change the picture?

![deaths_cumulative](https://user-images.githubusercontent.com/84423041/142749964-d79ff1a4-3d4b-45b5-a85a-4db9f977b4cf.png)
![injuries_cumulative](https://user-images.githubusercontent.com/84423041/142749965-14fddbaf-985e-4ea8-993f-f3de9a96d93b.png)


Create these by running
> python .\himalaya_deaths.py

and 
> python .\himalaya_injuries.py

then run the .rmd file in R Studio. Note the python files depend on python 3.6+ (for OrderedDict).
