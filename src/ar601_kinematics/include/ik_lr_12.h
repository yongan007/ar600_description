
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

void wrist(Ref<MatrixXd> A, double& q1, double& q2, double& q3)
{
    if (abs(abs(A(1, 2)) - 1) < 0.0001) {
        // Achtung!
        q1 = 0;
        q2 = 0;
        q3 = 0;
        return;
    }
    q1 = atan2(A(1, 0), A(1, 1));
    q3 = atan2(A(0, 2), A(2, 2));
    if (abs(A(2, 2)) >= 0.0001){
        q2 = atan2(-A(1, 2) * cos(q3), A(2, 2));
    }else{
        q2 = atan2(-A(1, 2) * sin(q3), A(0, 2));
    }
}
void f_t1(double q, Ref<MatrixXd> T1)
{
    Matrix4d T10;
    T10 << 1,      0,      0, 0,
          0, cos(q), -sin(q), 0,
          0, sin(q),  cos(q), 0,
          0,      0,       0, 1;

    Matrix4d T11;
    T11 << 1, 0, 0,        0,
           0, 1, 0,        0,
           0, 0, 1, ankle_z,
           0, 0, 0,        1;
    T1 = T10 * T11;

}
void f_t2(double q, Ref<MatrixXd> T2)
{
    Matrix4d T20;
    T20 << cos(q), 0, sin(q), 0,
                0, 1,      0, 0,
          -sin(q), 0, cos(q), 0,
                0, 0,      0, 1;

    Matrix4d T21;
    T21 << 1, 0, 0,        0,
           0, 1, 0,        0,
           0, 0, 1, leg_down,
           0, 0, 0,        1;
    T2 = T20 * T21;
}

void f_t3(double q, Ref<MatrixXd> T3)
{
    Matrix4d T30;
    T30 << cos(q), 0, sin(q), 0,
                0, 1,      0, 0,
          -sin(q), 0, cos(q), 0,
                0, 0,      0, 1;

    Matrix4d T31;
    T31 << 1, 0, 0,        0,
           0, 1, 0,        0,
           0, 0, 1,   leg_up,
           0, 0, 0,        1;
    T3 = T30 * T31;
}

void ik_left(double x, double y, double z, Ref<MatrixXd> R, double x_t, double y_t, double z_t, Ref<MatrixXd> Rt, Ref<VectorXd> angles)
{
    Matrix4d T;
    T << 1, 0, 0, x,
         0, 1, 0, y,
         0, 0, 1, z,
         0, 0, 0, 1;
    Matrix4d Tt;
    Tt << 1, 0, 0, x_t,
          0, 1, 0, y_t,
          0, 0, 1, z_t,
          0, 0, 0,   1;
    Matrix4d I;
    I = R.inverse() * T.inverse() * Tt * Rt;
    x = I(0, 3);
    y = I(1, 3);
    z = I(2, 3);
    R = R.inverse() * Rt;
    double xx, yy, zz;
    Matrix4d T_b_inv;
    T_b_inv << 1, 0, 0,       0,
               0, 1, 0,       0,
               0, 0, 1, -foot_z,
               0, 0, 0,       1;

    Matrix4d T_t_inv;
    T_t_inv << 1, 0, 0, -com_x,
               0, 1, 0, -com_y,
               0, 0, 1, -com_z,
               0, 0, 0,      1;
    Matrix4d M;
    M << 1, 0, 0, x,
         0, 1, 0, y,
         0, 0, 1, z,
         0, 0, 0, 1;
    T = M * R;
    Matrix4d xyz = T_b_inv * T * T_t_inv;
    xx = xyz(2, 3);
    yy = -xyz(1, 3);
    zz = xyz(0, 3);
    double q1 = 0, q2 = 0, q3 = 0, q4 = 0, q5 = 0, q6 = 0;

    q6 = atan(yy / xx);
    q4 = -acos((pow(xx - ankle_z*cos(q6), 2) + pow(yy-ankle_z*sin(q6), 2) + pow(zz, 2)-pow(leg_down,2)-pow(leg_up,2)) / (2 * leg_up*leg_down));
    q5 = -atan(leg_up*sin(q4) / (leg_down +leg_up*cos(q4))) + atan(zz / sqrt(pow(xx- ankle_z*cos(q6), 2) + pow(yy-ankle_z*sin(q6), 2)));


    Matrix4d T1;
    f_t1(q6, T1);
    Matrix4d T2;
    f_t2(q5, T2);
    Matrix4d T3;
    f_t3(q4, T3);
    Matrix4d T46 = (T1 * T2 * T3).inverse() * (T_b_inv * T * T_t_inv);
    wrist(T46, q1, q2, q3);
    angles << q1, q2, q3, q4, q5, q6;
    angles = -angles;
}
void ik_lr_12(double x, double y, double z, double phi_x, double phi_y, double phi_z, double x_t, double y_t, double z_t, double phi_x_t, double phi_y_t, double phi_z_t, Ref<VectorXd> Res,bool left)
{
    Matrix4d Rx;
    Rx <<   1,           0,           0,    0,
            0,  cos(phi_x), -sin(phi_x),    0,
            0,  sin(phi_x),  cos(phi_x),    0,
            0,           0,           0,    1;
    
    Matrix4d Ry;
    Ry << cos(phi_y), 0, sin(phi_y), 0,
                   0, 1,          0, 0,
         -sin(phi_y), 0, cos(phi_y), 0,
                   0, 0,          0, 1;

    Matrix4d Rz;
    Rz << cos(phi_z), -sin(phi_z), 0, 0,
          sin(phi_z),  cos(phi_z), 0, 0,
                   0,           0, 1, 0,
                   0,           0, 0, 1;

    Matrix4d R = Rz * Ry * Rx; //Orientation of foot is given as XYZ in fixed CS
    Rx << 1,            0,             0, 0,
          0, cos(phi_x_t), -sin(phi_x_t), 0,
          0, sin(phi_x_t),  cos(phi_x_t), 0,
          0,            0,             0, 1;

    Ry << cos(phi_y_t), 0, sin(phi_y_t), 0,
                     0, 1,            0, 0,
         -sin(phi_y_t), 0, cos(phi_y_t), 0,
                     0, 0,            0, 1;

    Rz << cos(phi_z_t), -sin(phi_z_t), 0, 0,
          sin(phi_z_t),  cos(phi_z_t), 0, 0,
                     0,             0, 1, 0,
                     0,             0, 0, 1;

    Matrix4d R_t = Rz * Ry * Rx; //Orientation of torso is given as XYZ in fixed CS
    if (!left)
    {
        MatrixXd temp(3,1), dr,Rt(3,3);
        
        Rt <<R_t(0,0),R_t(0,1),R_t(0,2),
             R_t(1,0),R_t(1,1),R_t(1,2),
             R_t(2,0),R_t(2,1),R_t(2,2);
        
	    temp <<        0,
			    -2*com_y,
			           0;
	    dr=Rt*temp;
	    x=x+dr(0);
	    y=y+dr(1);
	    z=z+dr(2);
    }

    ik_left(x, y, z, R, x_t, y_t, z_t, R_t, Res);
}
