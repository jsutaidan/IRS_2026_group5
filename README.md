# IRS_2026_group5
lab

<img width="742" height="599" alt="image" src="https://github.com/user-attachments/assets/8bcf3297-46fb-4598-9724-7b7ce9247616" />

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PineappleGossipBot(Node):
    def __init__(self):
        super().__init__('PineappleGossipBot')

        self.publisher_ = self.create_publisher(String, 'status_updates',10)

        timer_period = 2
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Jeff has arisen for the pinapples amarageon {self.i}!'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    pineapple_gossip_bot = PineappleGossipBot()
    rclpy.spin(pineapple_gossip_bot)
    pineapple_gossip_bot.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


