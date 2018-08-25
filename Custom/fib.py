import string
from datetime import datetime
from datetime import timedelta
import ananas

TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

class FibonacciBot(ananas.PineappleBot):
    def init(self):
        self.config.prev_increment = 1
        self.config.next_increment = 1
        self.config.next_toot = datetime.now()

    @ananas.schedule(minute="*")
    def post_fibonacci(self):
        if (datetime.now() > datetime.strptime(self.config.next_toot, TIME_FORMAT)):
            self.log("debug", "Updating!")
            prev_increment = int(self.config.prev_increment)
            next_increment = int(self.config.next_increment)
            self.mastodon.status_post(prev_increment)
            self.config.prev_increment = next_increment
            self.config.next_increment = next_increment + prev_increment
            self.config.next_toot = datetime.strftime(datetime.now() + timedelta(seconds=prev_increment), TIME_FORMAT)


