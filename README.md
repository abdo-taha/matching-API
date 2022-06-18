# matching-API
a service to match wrong spelled medicine name using spark (part of graduation project)
## map-reduce
mapping medicin list and the query medicin name to the ratio of matching using get_close_matches 
which is a copy of original function from difflib library<br />
reducing the result to best 5 matches
### API is running using Flask 
## GET
| | |
|---|---|
|end point | http://127.0.0.1:5000/test/ |
body type | json 
body | { "name":"Tulrampator" } 
response | { "data": [ [ 1.0, "Tulrampator" ], [ 0.7619047619047619, "Farampator" ], [ 0.6666666666666666, "Mibampator" ], [ 0.631578947368421, "Tramadol" ], [ 0.6086956521739131, "Tramiprosate" ] ] }
