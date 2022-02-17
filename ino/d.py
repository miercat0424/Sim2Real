from isaacgym import gymutil, gymapi
import torch as t


a = t.tensor([-0.707107, 0.0, 0.0, 0.707107])

Quat = [item for item in a ]
Quat = gymapi.Quat(Quat[0],Quat[1],Quat[2],Quat[3])
roll, pitch, yaw = Quat.to_euler_zyx()
print(roll, pitch, yaw)
# print(gymapi.Quat(roll, pitch, yaw, w))