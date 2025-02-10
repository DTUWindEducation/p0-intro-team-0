## Git questions to answer

In `GitAnswers.md`, write 1 to 2 sentences to answer each of the following
questions.  (Note that for question 6 you will need to also push an image.)

1.	What is the difference between git and GitLab?  
Git is a software program that can be installed in a computer that works as a version control system for tracking code changes, while GitLab is an online hosting service that can host a copy of a Git repository that one can access with secure internet connection.

2.	What is the difference between GitLab, GitHub, and BitBucket? 
GitLab, GitHub and Bitbucket are all Git repository hosting services. While they all support Git, each one has unique features and target different audiences, e.g. GitLab is DevOps-friendly, GitHub is community-driven and Bitbucket caters to private repositories and businesses.

3.	Why would I ever want to use git, but not GitLab?  
One would want to just use Git (and not GitLab) if one only needed local version control (in its own computer)

4.	What are the steps to update the GitLab server with some changes I made on my computer?  
Check for changes with "git status" -> Stage the modified files with "git add" -> Commit the changes with "git commit -m (…) including a message -> Pull latest changes from GitLab to avoid conflicts with "git pull …" -> Push local changes to GitLab with "git push"

5.	What is a branch and why would I use one?  


6.	How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?  


7.	Give an example of a set of git commands that would result in a merge conflict.  


8.	Is Git suitable for latex documents?  


9.	Should I from now on version my word and powerpoint slides using git? Why/why not?  
You can, but the version control would only be in a "was it changed" way, and cannot show line-by-line differences. 

10.	What could happen when I push my latest commit to the remote repository without pulling first?  
The push fails, and git asks you to pull before pushing, as the remote repo has changes other than the one you are pushing.

11.	What happens when I pull without commiting my local changes first?  
If the pull doesn't affect files you have changes in, nothing. If it does, git will ask you to resolve the conflicts first.

12.	What is the difference between branching and forking?
Branching creates a branch in the same repo, but forking creates a new repo, and copies all the current files. 

