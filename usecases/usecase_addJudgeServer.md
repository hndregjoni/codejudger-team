| UC Name	  | UC_Add_judge_server |
| :---        |    :---   |
| Summary      | Judge servers are aimed to be horizontally scalable, even though one can do the job. An Admin can add additional ones. |
| Dependency   | - Health metrics usecase. |
| Actors   | Admin |
| Preconditions   | - The server to be added must be set up. <br> - No two servers can share the same (host, port) tuple |
| Description of the Main Sequence   | 1. Admin opens list of Judge servers. <br> 2. Admin clicks the "Add" button. <br> 3. Admin is asked for the hostname and the port. <br> 4. Admin is asked for an authentication mechanism (no auth, basic authentication, cryptographic key, or auth token can be implemented.) <br> 5. Admin can add priority configuration, and capacity. <br> 6. Admin can ping the server for availability. <br> 7. Admin adds languages supported by the server. |
| Description of the Alternative Sequence   | The languages supported can be added: <br> - Manually from a list. <br> - Queried from the server. |
| Non functional requirements   | - Transport security and isolation of the judge servers. <br> |
| Postconditions   | A functional judge server is added, and ready to receive queued problems. |
