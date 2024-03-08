# gyaan
Following are the structure that we will be following for our services.

As per the django structure we will be having views and urls in every app.
These endpoints and views will be total for internal purpose which suggests
to only have the endpoints being called from django admin page not by anyone
outside the system.

In every app we will be having api folder with following files:
1. urls.py
2. views.py
3. utils.py
4. data_utils.py

Given that model is going to be our main backend entity the above order is in
descending order given distant from the main entity as a parameter.
This tells that:
1. data_utils : only module doing direct operation on models of app now we have moved it to data_utils.py of _gybase
   that we will be using to perform model operation.
2. utils.py : called by views.py and utils.py will be calling data_utils 
   for database operation.
3. views.py: Called by urls.py and calls utils.py 
4. urls.py: It contains all endpoints which ever being used externally.

Note: 
1. We are always open to add more helper modules in api package on app level.
2. We should never use data_utils outside the api package/folder.
