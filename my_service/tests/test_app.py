import unittest
from app import create_app, db
from app.models import Customer, Order

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_customer(self):
        response = self.client.post('/customers', json={'name': 'John Doe', 'code': 'JD001'})
        self.assertEqual(response.status_code, 201)

    def test_add_order(self):
        response = self.client.post('/orders', json={'item': 'Widget', 'amount': 10.99, 'customer_id': 1})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
