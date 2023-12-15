class AnonymousSurvey: 
    """collect anonymous answers to a survey question """
    def __init__(self, question):
        """Store a question, and prepare to store resonses"""
        self.question = question
        self.responses = [] 

    def show_question(self): 
        """show the survey question"""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a singel resonse to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all  the responses that have been given"""
        print("Survey Results: ")
        for response in self.responses:
            print(f"- {response}")