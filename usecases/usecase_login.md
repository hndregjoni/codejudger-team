| UC Name	  | UC code and name goes here |
| :---        |    :----   |
| Summary      | Log-in phase      |
| Dependency   | Does not have dependencies   |
| Actors   | The actors that initiates the use case is the User. No additional actors involved        |
| Preconditions   | - User must be registered .<br> - User must not be banned        |
| Description of the Main Sequence   | 1. User opens Home (initial contact with UI)  <br>  2.	User goes to Log In <br> 3.	User enters password and username   <br>4. If the credentials are correct, user is directed to problems  <br> 5. Else, user is prompted with the error messages and tries again for a few times  <br> 6. If logging in fails overall , the user must wait a short time before trying again.     |
| Description of the Alternative Sequence   | 1. User opens Home (initial contact with UI)  <br>  2.	User goes to Log In <br> 3. User selects one icon of social media <br> 4. User puts credentials and presses the Login button <br>5.Credentials are verified and if they are correct, user logs in successfully <br> 6. Else the user is asked to try again  |
| Non functional requirements   | Credentials should be protected . <br> Password hashed      |
| Postconditions   | User is logged in |
