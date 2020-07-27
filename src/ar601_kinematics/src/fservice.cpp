#include "ros/ros.h"
#include "fk_com.h"
#include "ar601_kinematics/FK.h"

bool fk(ar601_kinematics::FK::Request& req, ar601_kinematics::FK::Response& res)
{
    VectorXd positions = VectorXd::Zero(3);
    fk_com(req.q1, req.q2, req.q3, req.q4, req.q5, req.q6, positions, req.left);
    for (int i = 0; i < 3; i++)
    {
        res.positions.push_back(positions(i));
    }
    return true;
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "fk_server_node");
    ros::NodeHandle n;
    ros::ServiceServer service = n.advertiseService("fk_server", fk);
    ros::spin();
    return 0;
}
