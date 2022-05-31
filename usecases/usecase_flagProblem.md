| UC Name	  | UC code and name goes here |
| :---        |    :---   |
| Summary      | User can flag problem (wrong testcases, vague statement, etc.) |
| Dependency   | This usecase is mutually dependant with the solution flagging |
| Actors   | Solver, ProblemSetter, and Admin |
| Preconditions   | - User must be logged in. <br> - Problem setter can't flag own problem. <br> - User can flag only once, until reviewed. |
| Description of the Main Sequence   | 1. User has a problem open. <br> 2. Problem appears to be inappropriate (the content), or irrelevant (i.e. empty solution) <br> 3. User is presented a flagging button, which they use. 4. User is provided a list of reasons, which they can choose from. 5. User can leave a remark. |
| Description of the Alternative Sequence   | - |
| Non functional requirements   | - The major concern with flagging has to do with the ethical grounds of a solution. One can't use it as a medium of an unintended pursue. <br> - Another concern is that of aiming for qualitative content. |
| Postconditions   | - Problem is flagged and can't be flagged twice by user. <br> - User is notified, problem author is notified, and admins are notified. |
