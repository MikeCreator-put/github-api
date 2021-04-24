from app import app
import unittest


class FlaskTest(unittest.TestCase):

    def get_response(self, url: str):
        tester = app.test_client(self)
        response = tester.get(url)
        return response

    def test_index(self):
        response = self.get_response("/")
        self.assertEqual(response.status_code, 200)

    def test_index_is_json(self):
        response = self.get_response("/")
        self.assertEqual(response.content_type, "application/json")

    def test_get_user_data(self):
        response = self.get_response("/user-summary/allegro")
        self.assertEqual(response.status_code, 200)

    def test_user_data_is_json(self):
        response = self.get_response("/user-summary/allegro")
        self.assertEqual(response.content_type, "application/json")

    def test_user_data_content(self):
        response = self.get_response("/user-summary/allegro")
        self.assertTrue(b"username" in response.data)
        self.assertTrue(b"stars_sum" in response.data)
        self.assertTrue(b"repositories" in response.data)

    def test_user_does_not_exist(self):
        response = self.get_response("/user-summary/thisisjustarandomusername123987")
        self.assertEqual(response.status_code, 404)

    def test_user_dees_not_exist_is_json(self):
        response = self.get_response("/user-summary/thisisjustarandomusername123987")
        self.assertEqual(response.content_type, "application/json")


if __name__ == "__main__":
    unittest.main()
