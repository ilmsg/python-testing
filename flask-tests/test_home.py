import unittest
from app import app

class TestHome(unittest.TestCase):
	def test(self):
		with app.test_client() as c:
			resp = c.get('/')

			self.assertEqual(resp.status_code, 200)

if __name__ == "__main__":
	unittest.main()

# python3 test_home.py
# python3 test_home.py -v