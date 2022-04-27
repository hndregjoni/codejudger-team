| UC Name	  | Daily challanges |
| :---        |    :----:   |
| Summary      | Every day the user logs into our software there will be a challange available for him to solve, which changes daily.       |
| Dependency   | Doesn’t depend on previous User case other than the user would nneed to have an account.   |
| Actors   | User <br> Admin    |
| Preconditions   | -User has logged on <br> -Has an account on our software        |
| Description of the Main Sequence   | ●	Step 1:	User logs onto our service.  <br>  ●	Step 2:	User clicks Daily Challenge prompt <br> ●	Step 3:	User will be shown the daily challenge coding question  <br>● Step 4:	User submits an answer (the coding language will be specified) <br>● Step 5:	Timer will be shown determining the time for the next daily challenge     |
| Description of the Alternative Sequence   | 1. User answers the question with a different coding language: <br>●	Program rejects his answer and demand it be written in the specified coding language only  <br>2a. User gets answer right: <br>●	User receives points<br>●	Use case procceds as normal with step 5<br>2b. User gets answer wrong: <br>●	User recievees no point but emotional support to try again, possibly in a form of a cute cat photo. <br>●	Use case procceds as normal with step 5      |
| Non functional requirements   | User should get the answer quickly, no matter the outcome the user only recieves one chance to answer the daily challange and must wait for the next one to try again.      |
| Postconditions   | Doesn't allow further submissions (any user can only submit once) |
