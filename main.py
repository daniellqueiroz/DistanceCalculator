
import mpu
from nominatim import *

nom = Nominatim()

start = nom.query('Recife,PE,50040-090')
end = nom.query('Jaboatao,PE,54420-006')

x = (float(start[0]['lat']), float(start[0]['lon']))
y = (float(end[0]['lat']), float(end[0]['lon']))

d = round(mpu.haversine_distance(x, y), 1)

print(str(d) + ' KM')

