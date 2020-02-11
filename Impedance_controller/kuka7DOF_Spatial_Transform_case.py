
import numpy as np
import rbdl
import yaml

def get_joint_num():
    num = 7
    return num

# Create a body for a given mass, center of mass, and inertia at
# the CoM
mass_arr = [[1],[1],[1],[1],[1],[1],[1],[1]]#good
mass_arr = np.array(mass_arr) 

# Get the distance vector between two adjacent bodies
# The location of the joints with respect to the previous links frame. These values are directly taken from the yaml file in Joints>parent pivot.
parent_dist = [[0.0,0.0,0.0],[0.0,0.0,0.103],[0.0,0.013,0.209],[0.0,-0.194,-0.009],[0.0,-0.013,0.202],[-0.002,0.202,-0.008],[0.002,-0.052,0.204],[-0.003,-0.05,0.053]]
parent_dist = np.array(parent_dist)

# create the COM for the bodies
# In the yaml file the center of mass of each link is described in the local coordinate frame. However, the orientation and possibly the position 
# of that frame maybe different than the frame in which your link's joint frame is described in the RBDL. So, you have to find and define the COM w.r.t
#the frame in which you described your model in the RBDL. The best way to do this is to open your model in the Blender software and campare your local frame
# with the RBDL frame and find the corresponding values for the COM.
com_pos = [[0.001,0,0.06],[0.0,-0.017,0.134],[0.0,-0.074,0.009],[0.0, 0.017, 0.134],[-0.001,0.081,0.008],[0.0,-0.017,0.129],[0.0,0.007,0.068],[0.006,0.0,0.015]]#
com_pos = np.array(com_pos)

# create the inertia for the bodies
inertia = [[0.01,0.01,0.01],[0.00815814, 0.007363868, 0.003293455],[0.00812252, 0.00329668, 0.00733904],[0.008159,0.007421,0.00330],[0.0081471,0.003297,0.0073715],[0.0077265,0.006950,0.00329],[0.002983,0.003299,0.003146],[0.000651,0.0006512,0.001120]] #
inertia = np.array(inertia) # 8x3


# Create a joint from joint type The revolute joint can be selected(X,Y,Z)
# can be selected to define the axis of rotation
joint_rot_z = rbdl.Joint.fromJointType ("JointTypeRevoluteZ")
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
trans.E = np.eye(3)#np.array([[0.0, -1.0, 0.0],[1.0,0.0,0.0],[0.0,0.0,1.0]])
trans.r = parent_dist[0]
trans1 = rbdl.SpatialTransform()
trans1.E =np.eye(3)
trans1.r = parent_dist[1]
trans2 = rbdl.SpatialTransform()
trans2.E = np.array([[1.0, 0.0, 0.0],[0.0,0.0,-1.0],[0.0,+1.0,0.0]])
trans2.r = parent_dist[2]
trans3 = rbdl.SpatialTransform()
trans3.E =np.array([[1.0, 0.0, 0.0],[0.0,0.0,+1.0],[0.0,-1.0,0.0]])
trans3.r = parent_dist[3]
trans4 = rbdl.SpatialTransform()
trans4.E =np.array([[1.0, 0.0, 0.0],[0.0,0.0,+1.0],[0.0,-1.0,0.0]])
trans4.r = parent_dist[4]
trans5 = rbdl.SpatialTransform()
trans5.E =np.array([[1.0, 0.0, 0.0],[0.0,0.0,-1.0],[0.0,+1.0,0.0]])
trans5.r = parent_dist[5]
trans6 = rbdl.SpatialTransform()
trans6.E =np.array([[1.0, 0.0, 0.0],[0.0,0.0,-1.0],[0.0,+1.0,0.0]])
trans6.r = parent_dist[6]
trans7 = rbdl.SpatialTransform()
trans7.E =np.array([[1.0, 0.0, 0.0],[0.0,0.0,+1.0],[0.0,-1.0,0.0]])
trans7.r = parent_dist[7]
# A=np.array([],[])
# DH parameters
# trans = rbdl.SpatialTransform()
# trans.E = np.eye(3)#np.array([[0.0, -1.0, 0.0],[1.0,0.0,0.0],[0.0,0.0,1.0]])
# trans.r = parent_dist[0]
# trans1 = rbdl.SpatialTransform()
# trans1.E =np.eye(3)
# trans1.r = parent_dist[1]
# trans2 = rbdl.SpatialTransform()
# trans2.E = np.array([[1.0, 0.0, 0.0],[0.0,0.0,+1.0],[0.0,-1.0,0.0]])
# trans2.r = parent_dist[2]
# trans3 = rbdl.SpatialTransform()
# trans3.E =np.array([[1.0, 0.0, 0.0],[0.0,0.0,-1.0],[0.0,+1.0,0.0]])
# trans3.r = parent_dist[3]
# trans4 = rbdl.SpatialTransform()
# trans4.E =np.array([[1.0, 0.0, 0.0],[0.0,0.0,-1.0],[0.0,+1.0,0.0]])
# trans4.r = parent_dist[4]
# trans5 = rbdl.SpatialTransform()
# trans5.E =np.array([[1.0, 0.0, 0.0],[0.0,0.0,+1.0],[0.0,-1.0,0.0]])
# trans5.r = parent_dist[5]
# trans6 = rbdl.SpatialTransform()
# trans6.E =np.array([[1.0, 0.0, 0.0],[0.0,0.0,+1.0],[0.0,-1.0,0.0]])
# trans6.r = parent_dist[6]
# trans7 = rbdl.SpatialTransform()
# trans7.E =np.array([[1.0, 0.0, 0.0],[0.0,0.0,-1.0],[0.0,+1.0,0.0]])
# trans7.r = parent_dist[7]
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
I3_x = inertia[3][0]
I3_y = inertia[3][1]
I3_z = inertia[3][2]
I4_x = inertia[4][0]
I4_y = inertia[4][1]
I4_z = inertia[4][2]
I5_x = inertia[5][0]
I5_y = inertia[5][1]
I5_z = inertia[5][2]
I6_x = inertia[6][0]
I6_y = inertia[6][1]
I6_z = inertia[6][2]
I7_x = inertia[7][0]
I7_y = inertia[7][1]
I7_z = inertia[7][2]


# Creation of inertia Matrix
inertia_matrix=[[I_x, 0, 0], [0, I_y, 0], [0, 0, I_z]],[[I1_x, 0, 0], [0, I1_y, 0], [0, 0, I1_z]],[[I2_x, 0, 0], [0, I2_y, 0], [0, 0, I2_z]],[[I3_x, 0, 0], [0, I3_y, 0], [0, 0, I3_z]],[[I4_x, 0, 0], [0, I4_y, 0], [0, 0, I4_z]],[[I5_x, 0, 0], [0, I5_y, 0], [0, 0, I5_z]],[[I6_x, 0, 0], [0, I6_y, 0], [0, 0, I6_z]],[[I7_x, 0, 0], [0, I7_y, 0], [0, 0, I7_z]]
# print 'inertia', inertia_matrix
# print 'inertia', inertia_matrix[0][0]

inertia_matrix = np.array(inertia_matrix)

# Creating each body of the robot
body = rbdl.Body.fromMassComInertia(mass_arr[0], com_pos[0], inertia_matrix[0])
body1 = rbdl.Body.fromMassComInertia(mass_arr[1], com_pos[1], inertia_matrix[1])
body2 = rbdl.Body.fromMassComInertia(mass_arr[2], com_pos[2], inertia_matrix[2])
body3 = rbdl.Body.fromMassComInertia(mass_arr[3], com_pos[3], inertia_matrix[3])
body4 = rbdl.Body.fromMassComInertia(mass_arr[4], com_pos[4], inertia_matrix[4])
body5 = rbdl.Body.fromMassComInertia(mass_arr[5], com_pos[5], inertia_matrix[5])
body6 = rbdl.Body.fromMassComInertia(mass_arr[6], com_pos[6], inertia_matrix[6])
body7 = rbdl.Body.fromMassComInertia(mass_arr[7], com_pos[7], inertia_matrix[7])
# Specifying joint Type
# joint_type = rbdl.Joint.fromJointType(joint_rot_z)

# Adding body to the model to create the complete robot
body_1 = model.AppendBody(trans, joint_fixed, body)
body_2 = model.AppendBody(trans1, joint_rot_z, body1)
body_3 = model.AppendBody(trans2, joint_rot_z, body2)
body_4 = model.AppendBody(trans3, joint_rot_z, body3)
body_5 = model.AppendBody(trans4, joint_rot_z, body4)
body_6 = model.AppendBody(trans5, joint_rot_z, body5)
body_7 = model.AppendBody(trans6, joint_rot_z, body6)
body_8 = model.AppendBody(trans7, joint_rot_z, body7)

# print 'joint_type', joint_rot_y
# print 'model', model
# print 'body', body_1
# print 'Inertia', body.mInertia
# print 'trans', trans

q = np.zeros (model.q_size)
qdot = np.zeros (model.qdot_size)
qddot = np.zeros (model.qdot_size)
tau = np.zeros (model.qdot_size)
print("shape of q:",np.shape(q))
print("Size of q:",np.size(q))
#
# Giving an arbitrary location described in the local frame and printing it's
# location wrt the world frame
# COM_L1 = np.array([0.0, 0.0, 0.0])
# COM_L1_base = rbdl.CalcBodyToBaseCoordinates (model, q, body_1, COM_L1)
# print 'COM_L1_base: ', COM_L1_base
# Giving an arbitrary location described in the local frame and printing it's
# location wrt the world frame


def get_end_effector_pos(q):
    point_local = np.array([0.0, 0.0, 0.0])
    end_pos = rbdl.CalcBodyToBaseCoordinates(model, q, body_7, point_local)
    return end_pos

def get_end_effector_jacobian(q):
    J = np.zeros([3,model.qdot_size])
    point_local = np.array([0.0, 0.0, 0.0])
    rbdl.CalcPointJacobian (model, q, body_7, point_local, J)
    # rbdl.CalcBodySpatialJacobian(model, q, body_7, J, True)
    return J

# print 'Point Location wrt base: ', COM_L3_base
# rbdl.InverseDynamics(model, q, qdot, qddot, tau)
# print 'G: ', tau

def get_G(q_):
    q_ = np.asarray(q_)
    # print "Commanded q is :", q_[1]*180/3.1457
    q = np.zeros(7)
    q[0]=q_[0]
    q[1]=q_[1]
    q[2]=q_[2]
    q[3]=q_[3]
    q[4]=q_[4]
    q[5]=q_[5]
    q[6]=q_[6]
    # print q
    qdot  = np.zeros(7)
    qddot = np.zeros(7)
    tau   = np.zeros(7)   
    # print "q is:    ",q*180/3.1457
    # RBDL inverse dynamics function
    # print 'current pos:', q*180/3.1457
    rbdl.InverseDynamics(model, q, qdot, qddot, tau)
    # print tau
    return tau

def get_M(q_):
    q_ = np.asarray(q_)
    q = np.zeros(7)
    
    M = np.zeros([7,7])

    q[0]=q_[0]
    q[1]=q_[1]
    q[2]=q_[2]
    q[3]=q_[3]
    q[4]=q_[4]
    q[5]=q_[5]
    q[6]=q_[6]

    rbdl.CompositeRigidBodyAlgorithm(model, q, M, True)
    return M

def get_C_qdot(q_, qdot_):
    q_ = np.asarray(q_)
    # print "Commanded q is :", q_[1]*180/3.1457
    q = np.zeros(7)
    q[0]=q_[0]
    q[1]=q_[1]
    q[2]=q_[2]
    q[3]=q_[3]
    q[4]=q_[4]
    q[5]=q_[5]
    q[6]=q_[6]
    # print q
    qdot  = qdot_
    qddot = np.zeros(7)
    tau   = np.zeros(7)   
    # print "q is:    ",q*180/3.1457
    # RBDL inverse dynamics function
    # print 'current pos:', q*180/3.1457
    rbdl.InverseDynamics(model, q, qdot, qddot, tau)
    G = get_G(q_)
    tau = np.copy(tau - G)
    return tau    


def inverse_dynamics(q_,qdot_, qddot_):
    q_ = np.asarray(q_)
    # print "Commanded q is :", q_[1]*180/3.1457
    q = np.zeros(7)
    q[0]=q_[0]
    q[1]=q_[1]
    q[2]=q_[2]
    q[3]=q_[3]
    q[4]=q_[4]
    q[5]=q_[5]
    q[6]=q_[6]
    # print q
    qdot  = qdot_
    qddot = qddot_
    tau   = np.zeros(7)   
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