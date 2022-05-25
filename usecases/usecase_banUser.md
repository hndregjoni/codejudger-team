| UC Name	  | UC code and name goes here |
| :---        |    :----  |
| Summary      | Admin bans user    |
| Dependency   | -  |
| Actors   | Admin     |
| Preconditions   | -There must be users registered    |
| Description of the Main Sequence   | 1.	Open 'Home'  <br>  2. Go to 'Manage Users' <br> 3. Search user by username <br> 4.	  Press 'Ban User' <br> 5. Write a comment in the textbox explaining the reason of banning  <br> 6. Send email notifying user of them being banned <br> 7. Refresh page and see if the account's status has changed   |
| Description of the Alternative Sequence   | 1. Step 1-3 are from the main sequence are performed <br> 2. Press "Alert user" for possible ban <br> 3. Write a comment explaining why <br> 4. If User takes into account the comment, remove 'Yellow' status from account <br> 5. Else, ban User permanently  |
| Non functional requirements   | The system shall implement user privacy as set out in the preferences |
| Postconditions   | User is banned from the system  |
