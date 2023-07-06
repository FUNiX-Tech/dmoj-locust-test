# dmoj-locust-test

###### https://locust.io

---

- How to install:

  1. Git clone this repository.
  2. In the main directory, `python3 -m venv venv`.
  3. `. venv/bin/activate`
  4. `make requirements.txt`

---

- There are available load testings:

  1. Contest joining.
  2. Problem page loading.
  3. Problem submitting.

---

- How to use:
  1. Copy the file's content in the `test_files` folder that you want to test to the locustfile.py.
  2. Modify the config in `/test_files/main.py`:
     - users_number
     - problem_path
     - username_prefix
     - password
     - wait_time (in the Main class)
  3. Depending on which test you are going to perform, modify the config in the test file.
  4. Run `locust` in terminal.
  5. Go to `http://localhost:8089`
  6. Fill out the fields:
     - Number of users: is equivalent to the `users_number` in the main.py file.
     - Spawn rate: from 1 to `Number of users`, read the official documentation.
     - Host: https://dmoj.vvvv.space.
  7. Click **Start swarming**
