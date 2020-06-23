

import json
import requests


REGIONS_OSM_CODES = \
	{'Qassim':'3679872',
	'Riyadh':'3678409',
	'Tabuk':'3679867',
	'Medina':'3679869',
	'Mecca':'3678639',
	'Northern Borders':'3673927',
	'Al Jouf':'3842543',
	'Hail':'3676707',
	'Al Bahah':'3679888',
	'Jazan':'3679903',
	'Asir':'3678598',
	'Najran':'3667317',
	'Eastern Region':'3667294'}


output = dict([('type', 'FeatureCollection'), ('features', [])]) 
header = {'User-Agent': 'Mozilla/5.0'}

for k in REGIONS_OSM_CODES:
	url = "https://nominatim.openstreetmap.org/reverse?osm_type=R&osm_id=%s&format=json&polygon_geojson=1" % REGIONS_OSM_CODES[k]

	r = requests.get(url)
	data = r.json()

	feature = dict([('type', 'Feature'), ('properties', dict()), ('geometry', dict())])
	feature['properties']['name'] = k
	feature['geometry']['type'] = data['geojson']['type']
	feature['geometry']['coordinates'] = data['geojson']['coordinates']
	
	output['features'].append(feature)

with open('SA_regions.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
