# COMMON DMOJ NORMAL USER
from locust import HttpUser, between

# config
users_number = 100
problem_path = "/beta/problem/clonehungry1"
username_prefix = "v1userfortest"
password = "funix.edu.vn"

i = 1
class Main(HttpUser): 
    wait_time = between(1, 3) # modify this one if you want to
    username = "NONE"
    session_cookie = {}
    csrftoken = "NONE"
    problem_path = "NONE"
    password = "NONE"
    abstract = True
    
    def __init__(self, *args, **kwargs): 
        super(Main, self).__init__(*args, **kwargs)
        
        self.problem_path = problem_path
        self.password = password
        global i
        if i <= users_number:
            self.username = username_prefix + str(i)
            i += 1
        
    def on_start(self):
        if self.username != "NONE":
            self.login()
            
        return super(Main, self).on_start()
    
    def on_stop(self):
        self.logout()
        return super(Main, self).on_stop()
        
    def login(self):
        # fetch login page
        self.client.headers['Referer'] = self.client.base_url
        response = self.client.get("/accounts/login")
        self.csrftoken = response.cookies['csrftoken']
        
        # login
        response = self.client.post("/accounts/login/", {"username": self.username, "password": self.password, "csrfmiddlewaretoken": self.csrftoken}, allow_redirects=False)
        assert response.status_code == 302
        print(f"{self.username} logged in.")
        session_cokkie = response.cookies.get("sessionid")
        self.session_cookie = {"sessionid": session_cokkie}
        
    def logout(self):
        self.client.post("/accounts/logout/", {"csrfmiddlewaretoken": self.csrftoken })
        
