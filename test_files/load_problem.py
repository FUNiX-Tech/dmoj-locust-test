from locust import task     
from test_files.main import Main

class LoadProblemTest(Main):
    
    @task
    def fetch_problem_page(self):
        response = self.client.get(self.problem_path)
        if response.cookies.get('csrftoken'):
            self.csrftoken = response.cookies['csrftoken']
        assert response.status_code == 200