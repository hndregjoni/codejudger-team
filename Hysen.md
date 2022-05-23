# Student wiki: [Hysen](https://github.com/hndregjoni)

# Week 7
This week I worked primarily on organizing some of the work with the diagrams, handling the distribution of tasks, and also started working ever so slightly on the Judge Server.
The diagrams mostly consisted of Activity diagrams, pertaining to the Usecase tables. Some worked on by me were:
- Creation of a problem
- Forking of a problem
- Password reset

One major part of my efforts this week also went on bootstrapping the judging server. This was very minimal and consisted in me working on a CLI tool that will be invoked to run the testcases
over an executable file (which will be a compiled solution, or some script that runs the interpreter over a solution in an interpreted language.).

# Week 6
This week primarily went by with me explaining the implementation decision and details. I also ended up switching Flask for FastAPI, and as such ending up also choosing a front end framework. The two more forefront options were NextJs and NuxtJs. NextJs was attempted, but it didn't really fit with the requirements, so Nuxt was chosen. I also ended up configuring a basic Docker set up (based on an official FastAPI boilerplate). I also worked on some stuff I should have finished since long ago:
1. The ERD diagram.
2. A more spanning list of usecase scenarios.
3. The requirement document.

# Week 5
This week I worked primarily on typesetting the Requirement Specification Document in a VCS-friendly format, and for
that I chose $\LaTeX$ (another option I was considering was Markdown,but tables of content in that would require lots of work). The most initial version of this document (very empty) can be found in this commit: [d1af2481306199b539f466d9e96282a1dd79b1cf](https://github.com/hndregjoni/codejudger-team/tree/d1af2481306199b539f466d9e96282a1dd79b1cf/requirement_document)

As a second thing I did, I actually created a simple Flask boilerplate for the webapp, which currently lacks even authentication, but it has some of the basics laid down. This is only pertinent for the web interface (which is only one part of the system), but the tech stack for now will be:

- *Language*: Python
- *Framework*: Flask
- *ORM*: SqlAlchemy
- *DB*: Postgre

For a more streamlined development experience Docker will be used, and over the course of Sunday I made it so the Dockerfile and the docker-compose.yml are sufficiently usable.

As for managerial duties, I distributed some work pertaining to the Activity and the State diagram.

# Week 4
As a carried effort from last week, we furnished our Trello boards. I also worked on the Gantt chart,
setting up a rough sketch of what we will spend our time on. I worked on some sketches of the ERD which have
yet to be finalized, but are still commited to the repo. Furthermore, I instructed my team mates on the way one would go about to using git (setitng up the keys, cloning, branching and all that.). We improved the project
structure slightly, and also set up Git LFS for large files, which we used to upload the wireframes of the user interface.

# Week 3
This week I decided upon a task that would be fit for this week, which happened to be the coming up with usecase scenarios. Apart from that, an overview of the possible diagrams
required was done. With some help, I worked on the Usecase diagram, creating a general sketch of the actors and their respective usecases.

The actors, up to now (and based on Besjana's work), are:
1. User
2. Admin (an extension of User)
3. Problem Setter (an extension of User)
4. Tester (not an actual individual, moreso the part of the system that will do the judging)

Some tasks for next week were also discussed.

# Week 2
This other week I prepared the repositories to be used. The idea is to separate the main repository which will host the implementation in the coming weeks, from the repository which will contain the material required by the course.
The repos are:
1. [codejudger](https://github.com/hndregjoni/codejudger)
2. [codejudger-team](https://github.com/hndregjoni/codejudger-team/)

Links to resources to learn the new tools were shared by me in the group chat (for git, Markdown and Mermaid). As for the tasks, they were a bit more diversified this week. We were separated in two groups, with the following tasks:
1. Listing existing solutions to the problem we chose: Besjana, Nika, Luis.
2. Listing features that we would think belong to such an application: Hysen, Dario, Inis

My conclusion to the task was as follows (a rough initial sketch):

> The application will be a platform that allows for code competitions, and coding problem evaluation. The basic idea is to have a collection of problems, which will be curated by specific users of the system. These problems might have other additional attributes to them, which might allow for more flexible organization of problems (i.e. courses, timed events, etc.).<br>
> Users should be allowed to solve the problems in a language they choose, and the range of choices should be decently large. It would be good if a point system was also in place.

---

# Week 1
In this first week I was acquainted with the team. We decided upon a leader, and that ended up being me. As a first thing, we created a means of communication (WhatsApp group), and the members were invited (after some hoops had to be jumped through).

After that, an online meeting was commenced on Tuesday. We briefly went through what the project meant, and what we would potentially be dealing with eventually. One thing we agreed upon was that one good takeway from this project would be the bulk of methodologies and diagramming techniques we would be learning. For that reason, we decided that we would all participate in filling this documentation, even though only some of us would actively participate in the implementation.

The main task for the week, for everyone, was to suggest topics for the project. The ones I suggested were:
1. A code judging system.
2. A billing system.

The first idea was decided.

We also set some ground rules as to the participation in the future weeks. No technologies were decided this week, but we went over the capabilities of the team. They were generally within the confines of what we did at university.