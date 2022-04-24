# Student wiki: Besjana

##  Week 4
Work assigned to me for this week :  
>dealing with UI  (more precisely, sketches and prototype)  

Work I did this week :  
I did the sketche which are uploaded in the ***/sketches*** folder (hand-drawn). Then using Figma, I turned some of them into wireframes. I have yet to finish them all. 
Something that was not explicitly assigned was : use case diagram.  

Me and Hysen gathered and worked on it and one version of it is uploaded on the ***/diagrams*** folder .
The use case diagram consists of all the actors that , so far, we think are part of the software.
The actors are:
-	User (which is somehow used as a blueprint for some use cases )
	- Log in
	- Sign up 
	- Reset password
	-  Change profile settings and user info
	-  Delete account 
	-  View notifications
-	Admin (extends the User)
-	Problem Setter (extends the User)
- Solver (extends the User)
- Judger (non-human actor )
 
 Lastly, I became a member of codeJudger in Trello to view the tasks in kan-ban style.

😃

##  Week 3

The work I had for this week , consisted of making up use-cases and scenarios, which will be later on turned into use-case diagram. 

All in all, so far I have identified 3 actors , namely:
- User
- Author of problems
- Tester (provide test cases)  

---
  
<br>

> ***Identify the actor:***  
*problem provider/author*

Possible ways the author can interact with the system are:
-	log in as an author
o	apply to be a problem writer
o	proof of eligibility 

-	upload the problem and valid test cases 
-	provide help during contests [supposedly your problems will first appear during contests and then remain as permanent problems/challenges]
 

> *a description of a use-case*   
***Name of use-case :***   
*Upload the problem and valid test cases.*  

The author is assumed to be eligible for submission at this point and hence already has an account with the right privileges.   
The author is past the log-in phase.  
The author submits information about the problem, such as level of difficulty and keywords related to the nature of the problem. The problem is described roughly, in other words a first draft is provided.  
An admin will review the problem proposal and will determine on the changes that need to be made, or even if the problem will be accepted at all.

In this point the author (name of the actor) has two options :
-	if the problem is accepted  
o	refine it [make a better, final description]  
o	submit a full solution  
o	submit test cases
-	if the problem is not accepted   
o	make changes   
o	try again   

After the problem has been under the inspection of the admin, testers then the Problem takes the status ***Ready*** and is considered part of the contest. 



##  Week 2  

Firstly, it was decided that the project was a coding contest software.
I was part of the group which was assigned the task of doing reasearch in smilar topics and below I have written a brief sumamry :  
First of all , I looked into 10 different apps, namely TopCoder, Coderbyte, Project Euler, HackerRank, CodeChef, Exercism.io, Codewars, LeetCode, SPOJ (Sphere Online Judge ) and CodinGame .

What I noticed was that, these webapps could be divided in two categories:  
1- paid and crowdsourcing approach   
2- individual, fun challenges

Some common features were: number of programming languages (more than 10), some ranking system and different filters, discussion forums etc.

I will be talking about evey page a little more in detail :

- Topcoder 
  - something that was not in most pages was the fact that they used crowdsourcing to provide companies with skilled challenge solvers and programmers with the job opportunity 
- CoderByte
  - 10 programming languages   
	it includes starter learning courses   
	you can view the solutions of other people
	career resources
- ProjectEuler
  - series of challenging mahtematical/computer programming problems 
	108 different programming languages to solve the problems
 
- HackerRank
  - reveals solution , but does not count oints for progress  
	there is a discussion area, where as the name states , people discuss and reveal their code
	people are ranked by their country , company or school   
	they include dark mode for and I quote "better coding experience"  
	over 40 languages supported
- CodeChef
  - monthly challenges 
  - practice problems
  - job announcements
  - upcoming events
- Exercism.io
  - 57 programming anguages 
	you can see the stats of how many people use each of the 57 languages  
    offers feedback on the code delivered   
		-automated feedback [generated immediately]  
		-mentor feedback [written by a team who will look at the solution and make suggestions on how to improve it]  
		-private feedback 
- Codewars
  - lets you improve your coding skills using games 
	solo and multi-player    
    coding games are turn-based; at each turn your program gets new input and must output the action   
	27 programming languages to choose from   
	it gives you hints  in pseudocode form   
	it provides with the entire solution  
	aesthetically speaking, you can customize the theme , edit mode , keybindings , editor configurations [same syntax as vs code for config] , languages ,you can even install plugins, such as external code editor 
- LeetCode
  - support 14 popular coding languages 
	-create own exercises  
	-their Playground tool is a "powerful" dev tool which helps to test, debug and even write project online  
	- chapters for learning
	-contests, interview , problems
- SPOJ 
  - online judge   
	tags   
	the problems were divided into :		
        classical , challenge , partial , tutorial , riddle , basics


---

##  Week 1 
This week we were supposed to come up with ideas for the project.

The ideas I gave as possible project topics were :  
-   public transportation management system 
-   game 


Another thing that I did this week was deciding on a leader for our group :  
And our leader is  (drumrolls 👏 🔥) Hysen !!!  

We also talked about the initial division of roles :  
I volunteered to participate in the database design, since most people were keen on taking on the frontend part.  

A whatsapp group was opened for the little details, such as the usual meeting time or different useful links to be shared, and I participated to make the communication easier.

We have our repo (I mean this wiki is on github), where we post everything related to the progress of our work.
We were also encouraged to look into markdown and mermaid (diagram tool) for smoother documentation process.
All in all, that is what I did this week.