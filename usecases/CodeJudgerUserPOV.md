| UC Name	  | UC_0 : Initial system view |
| :---        |    :----:   |
| Summary      | CodeJudger is a web-application that provides all basic needs to learn & practice coding. The user can watch tutorials, solve different problems of their choices, enter the daily challenge, or ask for help in the forum. |
| Dependency   | This web-app depends on the database that will store all the exercises and on the solver that provides their solutions. |
| Actors   | User – signs up, logs in, chooses programming language and practices it. <br> Admin – Can ban or ban users and deals with problems that may arise. <br> Problem setter – picks exercises to add as daily challenges or regular practice problems. <br> Solver – provides solution to exercises. <br> Judger – runs the code entered by user |
| Preconditions   | There must be a leaderboard that keeps track of every user’s right answers. <br> User must have an account or create one. <br> Admin must check on web-app frequently to avoid technical problems. |
| Description of the Main Sequence   | 1.	Sign up/ log in <br> 2.	Choose language of your liking <br> 3.	Choose crash course  <br> 4.	Watch through all/some of the tutorial <br> 5.	Go to tournament <br> 6.	Choose the difficulty of the problem <br> 7.	Choose the exercise <br> 8.	Write the answer <br> 9.	Get reaction from solver <br> 10.	If answer isn’t right, you can see solution from solve or ask on the forum. <br> 11.	See the leaderboard ranking |
| Description of the Alternative Sequence   | 1.	Sign up/ log in <br> 2.	Choose language of your liking <br> 3.	Go to daily challenge  <br> 4.	Write the answer <br> 5.	Get reaction from solver<br> 6.	If answer isn’t right, you can see solution from solver or ask on the forum. <br> 7.	See the leaderboard ranking |
| Non functional requirements   |  Credentials should be protected . <br> Small amount of time to retrieve problems and display them. |
| Postconditions   | User has answered or at least studied an exercise. |
