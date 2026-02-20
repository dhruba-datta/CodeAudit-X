# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    if (obj.income >= 75000 and obj.credit_score >= 720):
        return True
    else:
        return False

# Implement the unittest.
class TestSuite(unittest.TestCase):
    def test_is_suitable(self):
        self.assertTrue(is_suitable(Client(75000, 720)))
        self.assertTrue(is_suitable(Client(75000, 720)))
        self.assertFalse(is_suitable(Client(75000, 720)))
        self.assertFalse(is_suitable(Client(75000, 720)))

if __name__ == '__main__