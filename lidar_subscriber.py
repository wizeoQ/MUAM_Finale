import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2


class LidarSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_subscriber') #Инициализация узла
        self.subscription = self.create_subscription(
            PointCloud2,
            'aufd/merged/points', #Имя топика
            self.listener_callback,
            10
            )
        self.counter = 0


    def listener_callback(self,msg):
        #Вывод нулевого элемента массива    
        self.get_logger().info(f'Данные с лидара ({self.counter}): {msg.data[0]}') 
        self.counter +=1


def main(args=None):
    rclpy.init(args=args)
    node = LidarSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
