#! /usr/bin/python3

import csv, sys

water_coords = []
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if (float(row[2]) < 0):
            water_coords.append(row)

interval = int(len(water_coords) / int(sys.argv[2]))
with open('compressed_data.csv', mode='w') as f:
    writer = csv.writer(f, delimiter=',')
    for row in water_coords[0::interval]:
        writer.writerow(row)
