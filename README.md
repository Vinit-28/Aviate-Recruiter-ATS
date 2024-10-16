This is the coding assignment given by aviate.jobs, below are the requirements of the assignment:

- You need to create a table called "Candidate" with columns: [Name, Age, Gender, Email, Phone number]
- You have to create api endpoints to: create, update and delete a candidate. Also create an api endpoint to Search candidate (Explained in detail below).
- Searching should work on candidates name and should return result sorted based on relevancy. Relevancy is defined as the number of words in the search query that can be found in candidates name.
- Example of searching api: if the search query is “Ajay Kumar yadav” the order of results will be [“Ajay Kumar Yadav”, “Ajay Kumar”, “Ajay Yadav”, “Kumar Yadav”, “Ramesh Yadav”, “Ajay Singh”]
- As we can see in the example above, even if the names are partial matches they are still part for the search result.
- *IMPORTANT*: In order to improve the efficiency of the searching api, you must only use orm queries to filter and sort the candidates. You can't use python script for either filtering or sorting.
