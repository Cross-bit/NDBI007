# Principles of data organisation HW 1



## Task 1
**id(primary_key)**: 4 B
Since 3 B is not sufficient due to the number of records in our dataset.
**manufacturer_identifier**: 2 B
Well since there are only 4 possible values, in theory we need only two bits. But it makes probably most sense not to overlap different fields so we use whole byte + round it to 2 B.
**serial_number**: 2 B
This number highly depends on the application requirements, but since we can assume that new planes(from single manufacture) are not produced in high rate, we can expect that 2 B will be sufficient enough.
(obviously there could be some demands from the marketing point of view but we'll ignore it)

**aircraft_type_identifier**: 8 B
String code identifier, specifiening type of the aircraft. 
(We will have special code for Passager Aircraft, Cargo Aircraft, Jet, Helicopter, ... etc.)

**weight**: 4 B
Specifies weight of the airplane in tons (with e.g. float IEEE 754 floating point presition). 

**length**: 4 B
Specifies length of the airplane in meters. (again float)

**max_speed**: 4 B
Specifies maximal speed of the airplane in km/h. (again float)

**passangers_capacity**: 2 B
How many passager seats plane can handle. (e.g. ushort)

**cargo_space_volume**: 2 B
Total cargo space size in m^3.

=> Total record size: **32 B**


## Task 2




## Task 3




## Task 4



## Task 5
