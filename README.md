# bank_branches
A REST service that can fetch bank details, using the data given in the API’s query parameters.

A REST API (Representational State Transfer Application Programming Interface) is a type of web service that follows the principles of the REST architectural style. REST is a set of guidelines and constraints that dictate how web applications should communicate with each other over HTTP.

Tools
Flask
Postgresql

Data is stored in Postgresql (free storage only 10000 rows) provided by render.Flask is used to fetch the given Request URL

Request URL  - /api/search?q=Mumbai&limit=2&offset=1 

![image](https://user-images.githubusercontent.com/82455658/221837121-6642756e-26c4-4808-9e79-b6979b719bd2.png)


Request URL  - /api/branch?q=LONI&limit=1&offset=1 

![image](https://user-images.githubusercontent.com/82455658/221836918-d2710a92-76c1-421e-b61e-91d224deb74a.png)
