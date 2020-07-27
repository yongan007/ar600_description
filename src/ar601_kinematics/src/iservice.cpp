
#include "ros/ros.h"
#include "ik_lr_12.h"
#include "ar601_kinematics/IK.h"

bool ik(ar601_kinematics::IK::Request& req, ar601_kinematics::IK::Response& res)
{	
	VectorXd angles = VectorXd::Zero(6);
    ik_lr_12(req.x, req.y, req.z, req.phi_x, req.phi_y, req.phi_z, req.x_t, req.y_t, req.z_t, req.phi_x_t, req.phi_y_t, req.phi_z_t, angles ,req.left);       
    for (int i = 0; i < 6; i++)
	{
        res.angles.push_back(angles(i)); // * 57.2958); // in radians
    }
    return true;
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "ik_server_node");
    ros::NodeHandle n;
    ros::ServiceServer service = n.advertiseService("ik_server", ik);
    ros::spin();
    return 0;
}
