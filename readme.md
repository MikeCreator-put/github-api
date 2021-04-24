# GitHub REST API 


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Instructions](#instructions)
* [Further developement ideas](#ideas)

## General info
One of the recruitment tasks for a Software Engineer Intern at Allegro.

The main principle of the task was to create software allowing to:

- list out the repositories and their stars
- return sum of stars from all the repositories

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
2. In terminal type in: `pip install -r requirements.txt`
3. Run app.py: `python app.py`
3. Now, as long as the app is running, you should be able to access it under the url: http://127.0.0.1:5000/ in a browser of your choice.
### Using the app with curl
1. Open command line / terminal.
2. Type in: `curl -X GET https://github-api-mskrzypczak.herokuapp.com`
3. Follow further instructions
#### Example of usage
`curl -X GET https://github-api-mskrzypczak.herokuapp.com/user-summar/allegro`

## Further development ideas
My main idea for future development of the application would be to provide it with cache memory