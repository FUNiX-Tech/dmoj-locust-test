
from locust import task     
from test_files.main import Main

submission_source_code = "print('test submit 1111')"
language_id = 1 # python 2

class LoadProblemTest(Main):
    
    def on_start(self):
        super(LoadProblemTest, self).on_start()
        self.fetch_problem_page()

    
    def fetch_problem_page(self):
        if self.username != "NONE":
            response = self.client.get(self.problem_path)
            if response.cookies.get('csrftoken'):
                self.csrftoken = response.cookies['csrftoken']
            assert response.status_code == 200
        
    @task
    def submit_problem(self):
        if self.username != 'NONE':
            response = self.client.post(self.problem_path, {
                'source': submission_source_code,    
                'language': language_id,
                'csrfmiddlewaretoken': self.csrftoken
            },cookies=self.session_cookie)
            print("submission response", response)
            assert response.status_code == 200
            print(f"{self.username} made a submission")