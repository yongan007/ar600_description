
#include <math.h>
#include <Eigen/Core>
#include <Eigen/Dense>
using namespace std;
using namespace Eigen;

const double foot_z = 0.1455; //distance between floor and foot joints intersection
const double ankle_z = 0.030; //distance between foot and ankle joints intersection 
const double leg_up = 0.277; //upper leg link length
const double leg_down = 0.28; //lower leg link length
const double com_x = -0.006; // com coordinates in hip CS
const double com_y = -0.088;
const double com_z = 0.006;


void fk_com(double q1, double q2, double q3, double q4, double q5, double q6, Ref<VectorXd> position,bool left)
{
  //Function calculates position of COM in left/right CS given angles
    q1 = -q1;
    q2 = -q2;
    q3 = -q3;
    q4 = -q4;
    q5 = -q5;
    q6 = -q6;
    Matrix4d T_b;
    T_b <<     1, 0, 0,       0,
               0, 1, 0,       0,
               0, 0, 1, foot_z,
               0, 0, 0,       1;

    Matrix4d T_t;
    if (left)
    {
      T_t <<   1, 0, 0, com_x,
               0, 1, 0, com_y,
               0, 0, 1, com_z,
               0, 0, 0,      1;
    }
    else
    {
      T_t <<   1, 0, 0, com_x,
               0, 1, 0, -com_y,
               0, 0, 1, com_z,
               0, 0, 0,      1;
    }

    Matrix4d T_1;
    T_1 <<     1,       0,        0,       0,
               0, cos(q6), -sin(q6), -ankle_z*sin(q6),
               0, sin(q6),  cos(q6),  ankle_z*cos(q6),
               0,       0,        0,       1;

    Matrix4d T_2;
    T_2 <<     cos(q5),  0, sin(q5), leg_down*sin(q5),
               0      ,  1,       0,            0,
               -sin(q5), 0, cos(q5), leg_down*cos(q5),
               0,        0,       0,            1;

    Matrix4d T_3;
    T_3 <<     cos(q4),  0, sin(q4), leg_up*sin(q4),
               0      ,  1,       0,            0,
               -sin(q4), 0, cos(q4), leg_up*cos(q4),
               0,        0,       0,            1;

    Matrix4d T_4;
    T_4 <<     cos(q3),  0, sin(q3), 0,
               0      ,  1,       0, 0,
               -sin(q3), 0, cos(q3), 0,
               0,        0,       0, 1;

    Matrix4d T_5;
    T_5 <<     1,       0,        0, 0,
               0, cos(q2), -sin(q2), 0,
               0, sin(q2),  cos(q2), 0,
               0,       0,        0, 1;

    Matrix4d T_6;
    T_6 <<     cos(q1), -sin(q1), 0, 0,
               sin(q1),  cos(q1), 0, 0,
                     0,        0, 1, 0,
                     0,        0, 0, 1;

    Matrix4d T = T_b * T_1 * T_2 * T_3 * T_4 * T_5 * T_6 * T_t;
    position << T(0,3), T(1,3), T(2,3);
}