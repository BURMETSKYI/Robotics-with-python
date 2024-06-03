from robot import Robot
from time import sleep

class ObstacleAvoidingBehavior:
    """Simple obstacle avoiding"""
    def __init__(self, the_robot):
        self.robot = the_robot
        self.speed = 40

    # def get_motor_speed(self, distance):
    #     """This method chooses a speed for a motor based on the distance from a sensor"""
    #     if distance < 0.2:
    #         return -self.speed
    #     else:
    #         return self.speed
        
    def get_speeds(self, nearest_distance):
        if nearest_distance >= 1.0:
            nearest_speed = self.speed
            furthest_speed = self.speed
            delay = 100
        elif nearest_distance > 0.5:
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.8
            delay = 100
        elif nearest_distance > 0.2:
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.6
            delay = 100
        elif nearest_distance > 0.1:
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.4
            delay = 100
        else: # Collision
            nearest_speed = -self.speed
            furthest_speed = -self.speed
            delay = 250
        return nearest_speed, furthest_speed, delay

    def run(self):
        # self.robot.set_pan(0)
        # self.robot.set_tilt(0)

        while True:
            # Get the sensor readings in meters
            left_distance = self.robot.left_distance_sensor.distance
            right_distance = self.robot.right_distance_sensor.distance
            # Display this
            self.display_state(left_distance, right_distance)
            print("Left: {l:.2f}, Right: {r:.2f}".format(l=left_distance, r=right_distance))

            # Get speeds for motors from distances
            
            # (1)left_speed = self.get_motor_speed(left_distance)
            # self.robot.set_left(left_speed)
            # right_speed = self.get_motor_speed(right_distance)
            # self.robot.set_right(right_speed)
            # Wait a little
            # sleep(0.05)

            nearest_speed, further_speed, delay = self.get_speeds(min(left_distance, right_distance))
            print(f"Distances: l {left_distance:.2f}, r {right_distance:.2f}. Speeds: n: {nearest_speed}, f: {further_speed}. Delay: {delay}")

            # Send this ti the motors
            if left_distance < right_distance:
                self.robot.set_left(nearest_speed)
                self.robot.set_right(further_speed)
            else:
                self.robot.set_right(nearest_speed)
                self.robot.set_left(further_speed)
            # Wait delay time
            sleep(delay * 0.001)

            
bot = Robot()
behavior = ObstacleAvoidingBehavior(bot)
behavior.run()