import numpy as np
import rbdl
import yaml

## Loading the file
def yaml_loader(filepath):
    """ Loads a file path """
    with open(filepath, 'r') as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

## Dumping it
def yaml_dumper(filepath):
    """ Dumps data to a yaml file"""
    with open (filepath, 'w') as file_descriptor:
        yaml.dump(data, file_descriptor)

file_path = "/home/farid/MTM_FARID/RBE501/KUKA7DoF/blender-kuka7dof_modified.yaml"
data = yaml_loader(file_path)

Bodies = data.get('bodies')
Num_Bodies = len(Bodies)

Joints = data.get('joints')
num_of_joints = len(Joints)

mass_arr=[]

for body in Bodies:
    mass_arr.append(data[body]['mass'])  
mass_arr = np.array(mass_arr).reshape(len(mass_arr),-1) # dimension: 8x1
mass_arr[0][0] = 1.0

inertia = []
for bdy in Bodies:
    inertia_link_i = []
    inertia_link_i.append(data[bdy]['inertia']['ix'])
    inertia_link_i.append(data[bdy]['inertia']['iy'])
    inertia_link_i.append(data[bdy]['inertia']['iz'])
    inertia.append(inertia_link_i)
inertia = np.array(inertia) # 8x3


# Function to get the position of centre of mass values aka inertial offe
com_pos = []
for body in Bodies:
    com_link_i=[]
    com_link_i.append(data[body]['inertial offset']['position']['x'])
    com_link_i.append(data[body]['inertial offset']['position']['y'])
    com_link_i.append(data[body]['inertial offset']['position']['z'])
    com_pos.append(com_link_i)
com_pos = np.array(com_pos)

# Function to get type of joint
J_type = [['JointTypeFixed']]
for Joint in Joints:
    J_type_yaml = data[Joint]['type']

    if J_type_yaml == 'fixed':
        J_type.append(['JointTypeFixed'])

    elif J_type_yaml == 'revolute':   
        J_type.append(['JointTypeRevoluteZ'])

J_type = np.array(J_type)

# Get the distance vector between two adjacent bodies
parent_dist = [[0,0,0]]
for Joint in Joints:
    parent_dist_i=[]
    parent_dist_i.append(data[Joint]['parent pivot']['x'])
    parent_dist_i.append(data[Joint]['parent pivot']['y'])
    parent_dist_i.append(data[Joint]['parent pivot']['z'])
    parent_dist.append(parent_dist_i)

parent_dist = np.array(parent_dist)

print 'mass', np.shape(mass_arr)
print 'inertia', np.shape(inertia)
print 'com_pos', np.shape(com_pos)
print 'J_type', J_type
print 'parent_dist', np.shape(parent_dist)

model = rbdl.Model()

for i in range(Num_Bodies):

    # Creating of the transformation matrix between two adjacent bodies
    trans = rbdl.SpatialTransform()
    trans.E = np.eye(3)

    trans.r = parent_dist[i]

    # Using principal inertia values from yaml file
    I_x = inertia[i][0]
    I_y = inertia[i][1]
    I_z = inertia[i][2]

    # Creation of inertia Matrix
    inertia_matrix = np.array([[I_x, 0, 0], [0, I_y, 0], [0, 0, I_z]])

    # Creating each body of the robot
    body = rbdl.Body.fromMassComInertia(mass_arr[i], com_pos[i], inertia_matrix)

    # Specifying joint Type
    joint_type = rbdl.Joint.fromJointType(J_type[i][0])
    
    # Adding body to the model to create the complete robot
    append_body = model.AppendBody(trans, joint_type, body)

def get_G(q_):
    q_ = np.asarray(q_)
    # print q_
    q = np.zeros(1)
    q[0] = q_[1]
    # print q
    qdot  = np.zeros(1)
    qddot = np.zeros(1)
    tau   = np.zeros(1)   

    # RBDL inverse dynamics function
    # print 'current pos:', q*180/3.1457
    rbdl.InverseDynamics(model, q, qdot, qddot, tau)
    print tau
    return tau

# q = [0.1]*7 
# q[2]=0.5   
# # q = np.asarray(q)
# Tau = get_G(q)
# print(Tau)