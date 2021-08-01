This Repo has Test cases for the Bitly Rest API:
1. GET  /v4/groups/{group_guid}
2. GET /v4/groups/{group_guid}/bitlinks/{sort}
3. POSt  /v4/bitlinks

List of Test cases:
1. GET  /v4/groups/{group_guid}:
   1. Verify retrieving group details successfully by passing group id
   2. Verifying Forbidden response with status code 403 when passing invalid access code and group id
   
2.GET /v4/groups/{group_guid}/bitlinks/{sort}:
   1. Verifying response with status code 200 when passing valid group id and non-mandatory fields
   2. Verifying response for Bad request with status code 400 by passing invalid values for unit, untits ,Unit_reference ,Invalid sort option
   3. Verifying Forbidden response with status code 403 when passing invalid access code and group id
   4. Verifying Not found response with status code 404 by passing non existing request endpoint
   5. Verifying Internal error response with status code 500 by passing invalid size params
   
3.POSt  /v4/bitlinks:
   1. Verifying response with status code 200 when bitlink got posted successfully
   2. Verifying response for Bad request with status code 400 by passing invalid values for Domain, long_url
   3. Verifying Forbidden response with status code 403 when passing invalid access code and group id
   4. Verifying response for Upgrade Required with status code 402 by passing invalid values for deeplink
   5. Verifying Not found response with status code 404 by passing non existing request endpoint
   6. Verifying Unprocessable Entity response with status code 422 when passing unprocessable entities for tags and deeplinks

Steps to Run the Test Cases:
1. Clone the repository :https://github.com/NamrathaKRao/BITLY_API_Automation.git
2. Install the required modules by running : pip3 install -r requirements
3. Move to BitlyAPI_Automation directory and run : pytest -s -v tests/ --html=report.html
4. Test case report can be viewed by opening report.html file that gets generated once the test is run in any of the browsers
5. Logs can be checked in the automation.log file that gets generated once the test is run 


  
  
