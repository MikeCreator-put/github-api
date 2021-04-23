from typing import Optional, Dict
from github import Github
from flask import Flask, jsonify

app = Flask(__name__)
g = Github()


class UserDataRetriever(object):
    @property
    def repositories(self):
        return self._repositories

    @property
    def stars_sum(self):
        return sum(self.repositories.values())

    @repositories.setter
    def repositories(self, value):
        self._repositories = value

    @stars_sum.setter
    def stars_sum(self, value):
        self._stars_sum = value

    def __init__(self, username: str):
        self.user: Optional[Github] = g.get_user(username) or None
        self.stars_sum: int = 0
        self.repositories: Dict[str, int] = {}
        self.__fetch_repositories()

    def __fetch_repositories(self):
        if self.user:
            for repo in self.user.get_repos():
                self.repositories[repo] = repo.stargazers_count

    def to_json(self):
        return {
            "username": self.user,
            "stars_sum": self.stars_sum,
            "repositories": self.repositories
        }


@app.route('/user-summary/<string:username>', methods=['GET'])
def get(username):
    user_data = UserDataRetriever(username)
    if user_data.user is None: return {"error": f"User {username} doesn't exist"}, 404
    return user_data.to_json(), 200


@app.route('/', methods=['GET'])
def index():
    return {
        "message": "To get the information about any GitHub user simply add his username after '/user-summary/' ; for "
                   "example: tmp.com/user-summary/MikeCreaptor-put"}


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == '__main__':
    app.run()