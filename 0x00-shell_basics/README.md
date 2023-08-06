## Shell, Basics

This is directory contains 15 mandatory task and 5 advance.
The task are creating shell script that performs some common shell operation
Enjoy:

- Mandatory:
  - Task 0: Prints the absolute path name
  - Task 1: Displays your current directory.
  - Task 2: A script that changes the working directory to user's home dir.
  - Task 3: Display current directory contents in a long format.
  - Task 4: Displays current directory including hidden files, using the long format.
  - Task 5: Display current directory contents, long format, with user & grp ids & dot files
  - Task 6: Creates a directory named my_first_directory in /tmp/ dir.
  - Task 7: Moves the file betty from /tmp/ to /tmp/my_first_dir...
  - Task 8: Deletes the file betty from /tmp/my_first_dir...
  - Task 9: Delete the directory my_first_directory in the /tmp dir.
  - Task 10: Changes the working directory to the previous one.
  - Task 11: List all files include hidden files.
  - Task 12: prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
  - Task 13: Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
  - Task 14: copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

- Advanced:
  - Task 15: moves all files beginning with an uppercase letter to the directory /tmp/u.
  - Task 16: deletes all files in the current working directory that end with the character ~.
  - Task 17: creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
  - Task 18: Write a command that lists all the files and directories of the current directory, separated by commas (,).

	- Directory names should end with a slash (/)
	- Files and directories starting with a dot (.) should be listed
	- The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
	- Only digits and letters are used to sort; Digits should come first
	- You can assume that all the files we will test with will have at least one letter or one digit
	- The listing should end with a new line
  - Task 19: Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
