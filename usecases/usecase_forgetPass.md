| UC Name	  | UC_Forget_password |
| :---        |    :----:   |
| Summary      | User forgets password     |
| Dependency   | This usecase depends on the signup usecase   |
| Actors   | User       |
| Preconditions   | User must have a registered account       |
| Description of the Main Sequence   | 1.	User opens Login page  <br> 2. User is aware of not knowing the password, hence it clicks "Forgot" <br> 3.User can choose to write his/her email or username to identify the account    <br> 4. If the username/email exist, an email is sent <br> 5. Else, an error message is displayed <br> 6. Inside the email , press on the confirmation link if you want to reset your password. <br> 7. Type the new password<br> 8.Confirm the typed password <br> 9. Press the button 'Submit' <br> 10. Te system will ridirect the user t login |
| Description of the Alternative Sequence   | 1.	User opens Login page  <br> 2. User is not aware of not knowing the password, hence it cntinues with the normal flow of logging in  <br> 3.	User finds out he/she cannot log in due to the credentials being wrong <br> 4. User performs step 3-10 the same |
| Non functional requirements   | -      |
| Postconditions   | In the end of this usecase , the user will have restored the password|
