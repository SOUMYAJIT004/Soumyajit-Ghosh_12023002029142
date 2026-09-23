import unittest
import pytest
from pages.search_page import SearchPage
from utils.csv_reader import read_test_data

@pytest.mark.usefixtures("setup_teardown")
class TestSearch(unittest.TestCase):
    
    def test_search_products(self):
        search_page = SearchPage(self.driver)
        
        # Read test data from CSV
        test_data = read_test_data('test_data.csv')
        
        for row in test_data:
            query = row['search_query']
            expected = row['expected_result']
            
            with self.subTest(query=query):
                search_page.search_product(query)
                
                if query == 'InvalidProduct':
                    self.assertEqual(search_page.get_no_results_message(), expected)
                else:
                    self.assertTrue(search_page.has_results())
