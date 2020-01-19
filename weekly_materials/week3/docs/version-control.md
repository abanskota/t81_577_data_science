
# An introduction to version control with Git

Once in a while, everyone names a document they are working on with version 1, version 2 , version 3 etc. This is a simple example of version control. This gives us an ability to go to different versions of the file and detect changes or revert to a specific one. But with this kind of tracking changes in a document, it quickly becomes unmangeable once the number of versions gets too high.

Version control is a systematic way of keeping track of changes on documents. It is an important part of code development. It gives us a peace of mind, provides an ability to go back and forth to different versions, prevent loosing or writing over files, helps in finding bugs, and allow collaborating with everyone in the projects.

**_Benifits_**:

- Helps with backup and restore
- Fosters better collaboration
- Allows undoing shorterm and longterm changes
- Provides history traceability
- Allows branching and merging


### What is Git?

- The most widely used modern version control system 
- A mature, actively maintained open source project 
- A distributed version control system <ul>
-  Every one has their own copy of the repository  
</ul>

### Install Git

Follow the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install git on your computer.

### Git repository

`Git repository` is  a data structure that tracks the changes in files in a working directory for a project. It is stored in the same directory as the project and inside a subdirectory called .git.

- `Local`

The local repository is the one that is created on the local machine. To save and track the current state of the files in the project directory, it needs to be committed to the local repository. Every commit of a file corresponds to one version. The local repository is itself sufficient for a complete version control of a project if a single person is working on code development of the project.

- `Remote`

Remote repository is hosted on the internet or network somewhere. It serves two purposes: backup of a local and a platform of collaboration among multiple developers. Hosting services like `GitHub` and `Bitbucket` provide platform for creating and stroring remote repostories. We will use `GitHUb` in this class.


### Getting started with Git

**Creating a repository**

It is typically done using one of the two ways:

1. Take a local directory that is currently not under version control, and turn it into a Git repository. To do this, Go to your project directory in the terminal and type:

```bash
git init
```

2. Clone an existing Git repository from elsewhere. Downloading a working copy of an existing repository to your local computer. To clone a repository, type:

```bash
git clone https://github.com/abanskota/t81_577_data_science.git
```

**Tracking Changes to the Repository**

After creation of the repository, as you edit files in your project directory, Git sees them as modified. You can `add` any state of the changes selectively first to a staging area and then `commit` the staged changes. 

As an example, create a new repo named git-repo, and  Initialize the repo using `git init` command. Add  a new file (test.py) to the project directory. 

To see the status of the changes in the project directory, run `git status` command.

```bash
On branch master
No commits yet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
test.py
nothing added to commit but untracked files present (use "git add" to track)
```

Git sees the untracked files just created. Untracked  means that Git sees a file we didn’t have in the previous snapshot (commit). Git doesn't commit the snapshots until it is explicitely asked so. The first line says that you are in branch `master`. When the repo is initialized, there will be only one branch and is called `master`. It can be seen as a repository's default branch. As you progresses with your code developement, you might want to create a separate branch and work within the branch. Once the codes are fully tested, the branch can be merged with master. Here, we will work on master brach itself.

**Staging and commitin Modified Files**

To stage the test.py, run `git add` command. Lets run  `git status` again after staging the file.

```bash
No commits yet
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
new file:   test.py
```

Now git doesn't see any untracked files as the file has already been staged.

To commit the file, run `git commit -m <a short message for your commit>. 

```bash
1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.py
 ```
 
The first commit of the file has been created! Every time you perform a commit, you’re recording a snapshot of your project that you can revert to or compare to later.


### Adding an existing project to GitHub using the command line

Now that you have created a local repository on your empty project directory. You added a text file to the project, and commited the changes to your local repository. As you make modification to the python file and add more files to the project, you will keep commiting those changes. At the same time, you might want to keep a back up of the project and also share your project with others. Follow instructions [here](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line) to add your existing project to GitHub using the command line.








