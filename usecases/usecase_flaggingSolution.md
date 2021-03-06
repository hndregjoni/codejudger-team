| UC Name	  | UC_Flagging_solution|
| :---        |    :---   |
| Summary      | Some solutions may be inappropriate or obviously irrelevant. This usecase covers the flagging/reporting of these solutions. |
| Dependency   | Mutual dependency with Flagging Problem. |
| Actors   | Primary actors are the Problem Setter and the Admin. A secondary actor can be the Solver. |
| Preconditions   | - User must be logged in. <br> - User can't flag own solution. <br> - User can flag only once, until reviewed. |
| Description of the Main Sequence   | 1. User has a solution open. <br> 2. Solution appears to be inappropriate (the content), or irrelevant (i.e. empty solution) <br> 3. User is presented a flagging button, which they use. 4. User is provided a list of reasons, which they can choose from. 5. User can leave a remark. |
| Description of the Alternative Sequence   | - |
| Non functional requirements   | - The major concern with flagging has to do with the ethical grounds of a solution. One can't use it as a medium of an unintended pursue. <br> - Another concern is that of aiming for qualitative content. |
| Postconditions   | - Solution is flagged and can't be flagged twice by user. <br> - User is notified, problem author is notified, and admins are notified. |
