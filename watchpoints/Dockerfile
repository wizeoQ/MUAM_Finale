# Базовый образ с ROS2 Humble
FROM ros:humble-ros-base
# Обновление системы
RUN apt update && apt upgrade -y
# Установка инструментов разработки
RUN apt install -y python3-colcon-common-extensions git
RUN apt-get update && apt-get install -y \
ros-humble-cv-bridge \
# сам пакет cv_bridge для ROS2 Humble
python3-opencv \
# OpenCV для Python3
python3-numpy \
# numpy - зависимость cv_bridge
libboost-python-dev \
# boost-python - зависимость cv_bridge
&& rm -rf /var/lib/apt/lists/*
# Настройка рабочего пространства
WORKDIR /datasets
