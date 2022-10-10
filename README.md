# softwareEngineeringProject
 Software Engineering project for Fall 2022.
# Team 5 - Laser Tag

# Team members
1. Preston Birdsong
2. Grant Botti
3. Miguel Hernandez-Gonzalez
4. Len Huang
5. Keith Mussino
6. Dylan Vaughn

# First, you need to make sure you have Git installed. 
To check if it is installed on Mac. Simply do: 
```
$ git --version
```
If it is not installed, you will be prompted to install. 


To install on Linux: 
```
$ sudo dnf install git-all
```

To install on Windows: 
Download from the following website: 
https://git-scm.com/download/win 

# Once Git is installed, you are ready to download Heroku. 
On Mac, simply do: 
```
$ brew tap heroku/brew && brew install heroku

```

On Windows, click the following link for 64-bit: 
https://cli-assets.heroku.com/heroku-x64.exe 

For 32-bit click here:
https://cli-assets.heroku.com/heroku-x86.exe

Verify your installation with: 
```
$ heroku --version
```
# To run our Laser-Tag project
```python 
To ensure our project runs correct, you must not have any previous data from heroku
To start, you must use our heroku credentials:
$ Heroku login
Enter this command for psql:
$ heroku pg:psql -a team101
Press spacebar to move onto the player entry screen. 
This project can now run.
```

# To install Flask 
```python
pip install Flask
Note: If 'pip' does not work, try 'pip3'
```

# Installing PSQL for MAC
```python
For Mac:
$brew install postgresql

For Windows:
PostgreSQL client [https://www.enterprisedb.com/downloads/postgres-postgresql-downloads]
Download and run the setup wizard for you system architecture
During component installation only select pgAdmin
You can verify access via the Command Prompt using the following command:
psql -V
If that doesn’t work then you will need to update your system’s PATH variable and then restart your Command Prompt
Add an entry similar to [C:\Program Files\PostgreSQL12\bin\]
```

# Kill Command
(CTRL+C to kill)
