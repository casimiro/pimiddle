from locust import HttpLocust, TaskSet, task
import json


class WebsiteTasks(TaskSet):
    @task(100)
    def temp(self):
        data = {'device_id': '111420111', 'temp': 33.3354}
        self.client.post('/', data=json.dumps(data))


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 9000
