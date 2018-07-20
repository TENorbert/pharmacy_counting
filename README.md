
# Solution to Insight Pharmacy Counting Problem.
  Pharmacy counting problem is defined here:
  https://github.com/InsightDataScience/pharmacy_counting

# Solution Approach
In order to generate a list of drugs with the following constraints:
 - The drug name,
 - The total number of UNIQUE drug Prescribers,
 - The total drug cost,
 - Listed in descending order:
    1) Based on the total drug cost
    2) The drug name(if there is a tie in Total Drug Cost)

  I used three notions: Data structures and Algorithms and Classes.

 # Implememntation
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
  where
    _a)Total Cost is sum of all costs made by all the prescribers associated to a given drug name.
    _b) Total Unique count of all Prescriber associated with the same drug name as (a)

     - i.e class Drug:

             - Properties: drug name, Prescriber count, Total cost

             - Methods: override less than, greater than and __compare__

    Class __Drug__(object):

            - properties__:(drug_name, prescriber_count, total_cost)

            - methods:(lt,gt,compare)

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


