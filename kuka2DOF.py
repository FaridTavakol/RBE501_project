import numpy as np
import rbdl
import yaml


# Create a body for a given mass, center of mass, and inertia at
# the CoM
mass_arr = [[1],[1],[1]]#good
mass_arr = np.array(mass_arr) 

# Get the distance vector between two adjacent bodies
parent_dist = [[0,0,0],[0,0,0.103],[-0.013,0.0,0.312]]#[[0,0,0],[1,0,0]]
parent_dist = np.array(parent_dist)

# create the COM for the bodies
com_pos = [[0.001,0,0.06],[0.0,-0.017,0.134],[0.009,0,0.074]]# com_pos = [[0.001,0,0.06],[0.0,-0.017,0.134],[0.0,-0.074,0.009]]# good
com_pos = np.array(com_pos)

# create the inertia for the bodies
inertia = [[0.01,0.01,0.01],[0.00815814, 0.007363868, 0.003293455],[0.00812252, 0.00329668, 0.00733904]]
inertia = np.array(inertia) # 8x3


# Create a joint from joint type The revolute joint can be selected(X,Y,Z)
# can be selected to define the axis of rotation
joint_rot_x = rbdl.Joint.fromJointType ("JointTypeRevoluteX")
joint_fixed= rbdl.Joint.fromJointType ("JointTypeFixed") #for the base and the first link
# Function to get type of joint
# J_type = [['JointTypeFixed']]
# J_type = [['JointTypeRevoluteZ']] 
# J_type = np.array(J_type)



print 'mass', np.shape(mass_arr)
print 'inertia', np.shape(inertia)
print 'com_pos', np.shape(com_pos)
# print 'J_type', J_type
print 'parent_dist', np.shape(parent_dist)

model = rbdl.Model()
model.gravity=[0,0,-9.81] # defining the direction of the gravity in the z direction (the default direction is set in the negative Y direction) 
# for i in range(Num_Bodies):

    # Creating of the transformation matrix between two adjacent bodies
trans = rbdl.SpatialTransform()
trans.E = np.eye(3)
trans.r = parent_dist[0]
trans1 = rbdl.SpatialTransform()
trans1.E = np.eye(3)
trans1.r = parent_dist[1]
trans2 = rbdl.SpatialTransform()
trans2.E = np.eye(3)
trans2.r = parent_dist[2]
# Using principal inertia values from yaml file
I_x = inertia[0][0]
I_y = inertia[0][1]
I_z = inertia[0][2]
I1_x = inertia[1][0]
I1_y = inertia[1][1]
I1_z = inertia[1][2]
I2_x = inertia[2][0]
I2_y = inertia[2][1]
I2_z = inertia[2][2]

# Creation of inertia Matrix
inertia_matrix=[[I_x, 0, 0], [0, I_y, 0], [0, 0, I_z]],[[I1_x, 0, 0], [0, I1_y, 0], [0, 0, I1_z]],[[I2_x, 0, 0], [0, I2_y, 0], [0, 0, I2_z]]
print 'inertia', inertia_matrix
print 'inertia', inertia_matrix[0][0]

inertia_matrix = np.array(inertia_matrix)

# Creating each body of the robot
body = rbdl.Body.fromMassComInertia(mass_arr[0], com_pos[0], inertia_matrix[0])
body1 = rbdl.Body.fromMassComInertia(mass_arr[1], com_pos[1], inertia_matrix[1])
body2 = rbdl.Body.fromMassComInertia(mass_arr[2], com_pos[2], inertia_matrix[2])

# Specifying joint Type
# joint_type = rbdl.Joint.fromJointType(joint_rot_z)

# Adding body to the model to create the complete robot
body_1 = model.AppendBody(trans, joint_fixed, body)
body_2 = model.AppendBody(trans1, joint_fixed, body1)
body_3 = model.AppendBody(trans2, joint_rot_x, body2)

print 'joint_type', joint_rot_x
print 'model', model
# print 'body', body_1
# print 'Inertia', body.mInertia
# print 'trans', trans

q = np.zeros (model.q_size)
qdot = np.zeros (model.qdot_size)
qddot = np.zeros (model.qdot_size)
tau = np.zeros (model.qdot_size)
print(np.shape(q))
print(np.size(q))
q[0] =-105*3.14/180# 3.14
#
# Giving an arbitrary location described in the local frame and printing it's
# location wrt the world frame
COM_L1 = np.array([0.0, 0.0, 0.0])
COM_L1_base = rbdl.CalcBodyToBaseCoordinates (model, q, body_1, COM_L1)
print 'COM_L1_base: ', COM_L1_base
# Giving an arbitrary location described in the local frame and printing it's
# location wrt the world frame
COM_L3 = np.array([0.0, 0.0, 1])
COM_L3_base = rbdl.CalcBodyToBaseCoordinates (model, q, body_3, COM_L3)

print 'COM_L3_base: ', COM_L3_base

rbdl.InverseDynamics(model, q, qdot, qddot, tau)

print 'G: ', tau


def get_G(q_):
    q_ = np.asarray(q_)
    # print "Commanded q is :", q_[1]*180/3.1457
    q = np.zeros(1)
    q[0] = q_[1]
    # print q
    qdot  = np.zeros(1)
    qddot = np.zeros(1)
    tau   = np.zeros(1)   
    # print "q is:    ",q*180/3.1457
    # RBDL inverse dynamics function
    # print 'current pos:', q*180/3.1457
    rbdl.InverseDynamics(model, q, qdot, qddot, tau)
    # print tau
    return tau

# q = [0.1]*7 
# q[2]=0.5   
# # q = np.asarray(q)
# Tau = get_G(q)
# print(Tau)