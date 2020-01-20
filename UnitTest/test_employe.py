import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setup')
        emp1=Employee('ravi','prasad',6000)
    
    def tearDown(self):
        print('tearDown\n')


    def test_email(self):
        emp1=Employee('ravi','prasad',6000)
        
        self.assertEqual(emp1.email, 'ravi.prasad@gmail.com')


        emp1.first='Kalyan'
        self.assertEqual(emp1.email, 'Kalyan.prasad@gmail.com')

    def test_fullname(self):
        emp1=Employee('ravi','prasad',5000)
        self.assertEqual(emp1.fullname, 'ravi prasad')

        emp1.first='Kalyan'
        self.assertEqual(emp1.email, 'Kalyan prasad')

    def test_apply_raise(self):
        emp1=Employee('ravi','prasad',5000)
        
        emp1.apply_raise()

        self.assertEqual(emp1.pay, 52500)


if __name__=="__main__":
    unittest.main()