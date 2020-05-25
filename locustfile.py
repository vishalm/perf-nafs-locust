from locust import HttpLocust, TaskSet, task, between

headers = {
"Host": "nafs-http-lb-1264996261.eu-west-1.elb.amazonaws.com",
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
"Cookie": "_ga=GA1.1.13800830.1589609339; _gid=GA1.1.1917795533.1589609339; _gat_gtag_UA_110109346_1=1; XSRF-TOKEN=eyJpdiI6InUwZ0VPcUgxNXhqWmV5dnNUV0FjSEE9PSIsInZhbHVlIjoiN0d3OSs1bFEzY0tINVFQcWJvNThFaWxzdm5BV2d2OUlwM0xkcjNBTjNRMU4zQ0NvTld1Y0FXaUZUYzBLUmRlXC8iLCJtYWMiOiI4MWZmYTgyMTQ3NDliMzE3NzYxN2M1NDkyMTM2YTFiY2UwMTZmMTRhMzI3MzEwMDJiYTU2ZDQ0Yzc2YjA1OWExIn0%3D; laravel_session=eyJpdiI6IldaXC9FVTl2OEtIYWIrTGVGclQ5cXhRPT0iLCJ2YWx1ZSI6IlhvZ3pUNzBXS3pFY2FxR2xOSEJVMHZvRDdhdnZMYTdWd1BiK21aekpKN1ZxNTM1NFV2WkxGTjdEMmw1NSt4b0UiLCJtYWMiOiI4MjU2NWFmZTAxZjU4Mjg3NDRjMWU4YzQxZGQ5YTk1M2I2YjY5N2MzOTBlM2QxYjExZDVjZmE0ZWQ3MGYyNTI2In0%3D"
}

def open_competitions(l):
    l.client.get("/competitions")

def open_competition_name(l):
    l.client.get("/competitions/TEST")

def open_welcome(l):
    l.client.get("/welcome")

def login(l):
    # response = l.client.post("/login", data={"_token":"RHnkp9SuCzp3XdxW0AAlOfwDMwIPimfmSFqroLCE",
    # "username":"hit","password": "hiten12345"}, headers=headers)
    l.client.get("/login")



class UserBehavior(TaskSet):

    def on_start(self):
        self.client.verify = False

    @task(1)
    def get_competitions_list(self):
        open_competitions(self)

    @task(2)
    def get_competition_name(self):
        open_competition_name(self)
    
    @task(3)
    def get_login(self):
        login(self)

    # @task(2)
    # def on_run2(self):
    #     open_welcome(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1.0, 2.0)