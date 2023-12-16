import unittest 
from survey import AnonymousSurvey 

class testAnonymousSurvey(unittest.TestCase):
    """test for the class AnonymousSurvey"""

    def setUp(self):
        """create a survey and a set of responses for use in all test methods"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_resonse(self):
        """test that a single response is stored properly"""

        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_resonses(self):
        """Test that there are 3 resonses stored properly"""
        my_survey = AnonymousSurvey(question="What language did you first learn to speak?")
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ =='__main__':
    unittest.main()

##Set up method
    
import unittest 
from survey import AnonymousSurvey 

class testAnonymousSurvey2(unittest.TestCase):
    """test for the class AnonymousSurvey"""

    def setUp(self):
        """create a survey and a set of responses for use in all test methods"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_resonses(self):
        """Test that 3 individual responses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main() 