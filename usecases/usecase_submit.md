| UC Name	  | UC_Submit_solution|
| :---        |    :----   |
| Summary      | User attempts a solution   |
| Dependency   | This UseCase depends on another UseCase, namely the Run Code UseCase of CodeJudger(name of actor)   |
| Actors   | Solver    |
| Preconditions   | - limited number of total submissions in the queue <br> - limited number of per-problem submission in the queue        |
| Description of the Main Sequence   | 1. Solver picks the problem of choice and reads the problem statement and constraints  <br>  2.	Solver chooses his/her preferred language <br> 3. Solver is promted with the template of solution in the comments <br> 4. Solver writes the assumed solution and Submits it. <br> 5. Behind the scenes , the solution will go through many test cases. <br> 6. The application will direct the user to the percentile in which his/her solution fall in. <br> 6. Else, the solver will try another submission      |
| Description of the Alternative Sequence   | 1. The Solver is past the steps 1-3 in the main sequence <br> 2. Solver presses the 'Run' button as a preliminary step in verifying the correctness. <br> 3. The solution either passes the test or not <br> 4. If the solution does not pass the test, the Solver changes the solution without submitting it.  <br> 5. Else , the Solver submits the solution and waits for the results|
| Non functional requirements   |  -      |
| Postconditions   | In the end, the Solver will either have solved the problem or not.  |
