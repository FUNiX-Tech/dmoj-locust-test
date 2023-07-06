from locust import task     
from test_files.main import Main

contest_code = "contest3"

class JoinContest(Main):
    
    def on_stop(self):
        self.leave_contest()
        super(JoinContest, self).on_stop()
        
    def leave_contest(self):
        if self.username != "NONE":
            response = self.client.post(f'/contest/{contest_code}/leave', {"access_code": "Leave contest", "csrfmiddlewaretoken": self.csrftoken })
            assert response.status_code == 200
            print(response, " left")
    
    @task
    def join_contest(self):
        if self.username != 'NONE':
            response = self.client.post(f'/contest/{contest_code}/join', {"access_code": "Join contest", "csrfmiddlewaretoken": self.csrftoken })
            print(response)
            assert response.status_code == 200
            print(response, " joined")