from collections import deque


class Robot:                            # class to store each robot's attributes
    def __init__(self, name, time):
        self.name = name                # name
        self.time = time                # time to process products
        self.is_free = True             # is the robot free or still processing
        self.job_started = 0            # what time did it start

    def __repr__(self):                 # for test print purposes
        return f"{self.name} - Time: {self.time}, Is free: {self.is_free}"


def convert_to_seconds(time):           # basic converter from "08:00:15" -> 28815
    numbers = time.split(":")
    hours = int(numbers[0])
    mins = int(numbers[1])
    secs = int(numbers[2])

    return secs + mins * 60 + hours * 60 * 60


def convert_to_time(secs):              # basic converter from 28815 -> "08:00:15"
    hours = secs // 3600
    mins = (secs - 3600 * hours) // 60
    seconds = secs % 60
    if hours == 24:
        hours = 0
    return f"{hours:02d}:{mins:02d}:{seconds:02d}"


robots = []                             # list of robots
products = deque()                      # queue for products

robots_input = input().split(";")       # read and add all robots in the queue
for rob in robots_input:
    rob_data = rob.split("-")
    robots.append(Robot(rob_data[0], int(rob_data[1])))

start_time = input()                    # read start time and convert it to int seconds
total_time = convert_to_seconds(start_time)

command = input()                       # read next commands and add products to queue
while command != "End":
    products.append(command)
    command = input()

while len(products) > 0:                # start to process products until the queue is empty
    product = products.popleft()
    total_time += 1                     # add a second for each product

    for i in range(len(robots)):        # start a loop with the count of the robots
        robot = robots[i]               # get the next robot and check if
        if total_time - robot.job_started >= robot.time:
            robot.is_free = True        # it needs to be changed to Free
        if robot.is_free:               # if the robot is free, it does it's job and turns to not free
            robot.job_started = total_time
            print(f"{robot.name} - {product} [{convert_to_time(total_time)}]")
            robot.is_free = False
            break
        else:
            if i == len(robots) - 1:        # if at the end of the loop no robot is free,
                products.append(product)    # we return the product to the queue and go back to the while above
                break

