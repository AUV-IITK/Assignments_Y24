import rclpy
from rclpy.executors import MultiThreadedExecutor
from my_package.publisher_node import PublisherNode
from my_package.subscriber_node import SubscriberNode

def main(args=None):
    rclpy.init(args=args)

    publisher = PublisherNode()
    subscriber = SubscriberNode()

    executor = MultiThreadedExecutor()
    executor.add_node(publisher)
    executor.add_node(subscriber)

    try:
        executor.spin()
    finally:
        publisher.destroy_node()
        subscriber.destroy_node()
        rclpy.shutdown()

