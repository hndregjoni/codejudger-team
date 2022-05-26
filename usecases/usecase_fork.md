| UC Name	  | UC code and name goes here |
| :---        |    :---   |
| Summary      | A problem setter can easily copy an existing problem by using the fork mechanism |
| Dependency   | This usecase depends on the problem creation usecase. |
| Actors   | The primary actor is the Problem Setter. |
| Preconditions   | - User forking should have problem creation capabilities. <br> - Problem should exist. <br> - Problem should be forkable. <br> - User should be able to see problem. |
| Description of the Main Sequence   | 1. User chooses problem they want to fork. <br> 2. User clicks fork. <br> 3. User decides between hard forking and soft forking. <br> 4. The problem slug is copied over, and a counter is appended. <br> 5. User is presented with the same UI as the problem creation usecase. <br> 6. User edits (or not) the copied constraints. |
| Description of the Alternative Sequence   | Depending on the hard or soft choice, we have: <br> - Hard forking: Repo behind problem is git cloned. <br> - Soft forking: The repo directory is only softlinked. <br> Another alternative flow is in the case when the user specifies a git URL for the forking. |
| Non functional requirements   | - These operations are very file system aware, so care must be had. <br> - Forking a problem from a URL might copy over some large unwanted files, so this should be prevented. <br> - Forking should be performed as a backgroudn task as to not intervene with the user experience. |
| Postconditions   | A new problem is created and it is a fork of the original one. |
