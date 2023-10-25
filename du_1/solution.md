# Principles of data organisation HW 1



## Task 1
**id(primary_key)**: 4 B
Since 3 B is not sufficient due to the number of records in our dataset.
**manufacturer_identifier**: 1 B
Well since there are only 4 possible values, in theory we need only two bits. But it makes probably most sense not to overlap different fields so we use whole byte.
**serial_number**: 2 B
This number highly depends on the application requirements, but since we can assume that new planes(from single manufacture) are not produced in high rate, we can expect that 2 B will be sufficient enough.
(obviously there could be some demands from the marketing point of view but we'll ignore it)

**aircraft_type**:

**weight**:

**length**:

**wings_span**:

**passangers_capacity**:

**cargo_space_volume**:




## Task 3




## Task 4



## Task 5
