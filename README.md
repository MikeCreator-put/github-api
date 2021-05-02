# GitHub REST API overlay


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Instructions](#instructions)
* [Further development ideas](#further-development-ideas)
* [Additional information](#additional-information)


## General info
One of the recruitment tasks for a Software Engineer Intern position at Allegro (2021).

The main principle of the task was to create software allowing to:

- list out the repositories and their stars
- return the sum of stars from all the repositories

of any GitHub user.

## Technologies
- Python 3.8.8
- Flask 1.1.2

## Instructions
#### Using the app in web
As the application is currently deployed on Heroku.com you can simply visit [this link](https://github-api-mskrzypczak.herokuapp.com/) and follow further instructions.
##### Example of usage
> https://github-api-mskrzypczak.herokuapp.com/user-summary/allegro

### Using the app locally 
1. Clone this repository
2. In the terminal type in: `pip install -r requirements.txt`
3. Run app.py: `python app.py`
3. Now, as long as the app is running, you should be able to access it under the URL: http://127.0.0.1:5000/ in a browser of your choice.
### Using the app with curl
1. Open command line/terminal.
2. Type in: `curl -X GET https://github-api-mskrzypczak.herokuapp.com`
3. Follow further instructions
#### Example of usage
`curl -X GET https://github-api-mskrzypczak.herokuapp.com/user-summary/allegro`

## Further development ideas
Here are my ideas for future development:

- Providing the application with cache memory, so that repeated requests wouldn't need to be fetched from the GitHub API.
- Collecting more data: class `UserDataRetriever` can easily be modified to extract more data from the `Github` object `user` (for example traffic information of each repository)

## Additional information
This was my first ever encounter with API, Flask, or even JSON file format, so I am aware that there might be some mistakes in my code or even in the approach to the problem itself. Please, feel free to leave your feedback via issues.
