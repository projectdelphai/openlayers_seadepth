# openlayers_seadepth
Test process for converting XYZ sea depth data into contour levels and mapping online using open layers

### Process:
1. Given a CSV with the following colums: long,lat,elevation: Since XYZ data can be overly large, I compressed the data with:
``` python3 compress_elevation_data.py test_ontario.csv 6000```

    test_ontario.csv being the csv with 61k data points it and 6000 being what I wanted to trim it down to. The script removes all positive elevation points and then takes every nth interval data point (n = 61k data points - positive elevations / 6000)
  
    Theoretically QGIS should be able to generate contours on all the points but I noticed it does a lot better with only the negative points and a subset of the full data collection.
  
1. You'll need to add "long,lat,elevation" to the very first line of the csv that's generated. The script doesn't do it yet.
1. In QGIS, Start a new project (run it as administrator so that you can export as geojson, I kept getting permission denied errors), open Layer->Data Source Manager then Delimited Text and open the CSV you trimmed down. When importing makes sure to set the Z field to the third column in Geometry Definition and the projection to the defailt WG84
1. I like to add the OpenStreeMap XYZ tiles from the sidebar so I can ensure it imported correctly
1. Making sure the generic contour plugin is installed, create the contours (Vector->Contour->Generate Contours). Make sure to use filled contours, I did equal quantile and 10 levels. Set the maximum to something to get rid of any contours that go over land. For example, I set my maximum to -12 so that it got rid of any contours spanning over land. You could also possible set your levels higher to 20 and then manually get rid of any contours that mess up the water boundary. Feel free to apply a blue color scheme and inverse it to get a realistic view already.
1. Right click on the created layer, export->save feature as->geojson. Make sure to specify a file name somewhere where you can get it again.
1. Go to https://gist.github.com/ and copy paste the file contents in there. Create a public gist. It needs to be public so that your website can find it.
1. After that just go to the gist, press the raw button to get the raw data. Copy that url and then put it in the index.html where it says "GIST_URL_FOR_GEOJSON_FILE". 
1. Apply for a Bings Map dev api key and put it where it says "PUT_BING_MAPS_DEV_KEY". 
1. You can test the file now and then copy this html and javascript code wherever you need a map.

### Extra things:
1. The "Fill" code on line 75-76 is a hacked together piece of code that takes the index of each polygon and maps it along the hsla color range of hsla(XXX, 100%, 47%, 1). It does this by taking 200 - the index\*20 to get a color indicative of a elevation color range. Feel free to mess with this equation to get any color scheme you want.
2. This openlayers map does not lock you into the ontario map view. Ideally it wouldn't let you leave just so people don't lose where they are.
3. I'd like to add tooltips when hovering over each region to say the elevation range at that time. You can pull this from feature.get('elevation_min') and feature.get('elevation_max'). In QGIS, you should also be able to set a custom label based on the min and max for the tooltip if you wanted.
