
# Solution to Pharmacy Counting Problem.
  The Pharmacy counting problem is defined here:
  https://github.com/InsightDataScience/pharmacy_counting

# Solution Approach
In order to generate a list of drugs with the following constraints:
 - The drug name,
 - The total number of UNIQUE drug Prescribers,
 - The total drug cost,
 - Listed in descending order of:
    1) The total drug cost,
    2) The drug name(if there is a tie in total drug cost).

  I used three concepts: Data Structures and Algorithms and Classes.

 # Implementation
 I approached the implementing the solution in the following ways:
  - Use list data structures to store individual drug properties like: drug name, cost,
     prescriber full name.
  - Use dictionaries with drug name as keys and prescriber full name and cost as values
    to map drug name to cost and prescriber.
  - Since Prescriber is unique, I use set data structure to represent prescribers for a given drug
  - While a given drug has many different or same cost so I use list data structure to present
  the different or similar prices for each drug.

  - Use dictionaries of sets for drug name-to-prescriber full name mapping
     dictionary of lists for drug name-to-prescriber full name mapping.

  - Now using a class object called Drug to represent: drug name, Unique Prescriber count, Total cost
  where:
    - a)Total Cost is sum of all costs made by all the prescribers associated to a given drug name.
    - b)Total Unique count of all Prescriber associated with the same drug name as (a)

    - i.e Class __Drug__(object):

                - __properties__:(drug_name, prescriber_count, total_cost)

                - __methods__:(__lt__,__gt__,__compare__)

  - Each drug which is an instance of class Drug is stored in a list
  - Using the __Compare__ method we can sort(in terms of Total Cost and Drug Name) the drugs in the list thus:
    thus addressing the constraints of descending order.

  - Finally the properties(drug name, Unique Prescriber count, Total Cost) of the sorted list of Drugs
  are written into the output file.


  # Future Improvements
  - One could use better sorting algorithms like quick sort to improve performance
  - Instead of passing list and dictionaries( particularly for such large datasets),
   using __hash maps__ or __Redis__(key-value data structure server) could be used as
    these have high performance and are more scalable.


