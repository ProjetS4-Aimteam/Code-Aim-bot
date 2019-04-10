#ifndef _ROS_filtre_toOpenCR_h
#define _ROS_filtre_toOpenCR_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace filtre
{

  class toOpenCR : public ros::Msg
  {
    public:
      typedef float _kpSpeed_type;
      _kpSpeed_type kpSpeed;
      typedef float _kiSpeed_type;
      _kiSpeed_type kiSpeed;
      typedef float _kdSpeed_type;
      _kdSpeed_type kdSpeed;
      typedef float _kpTilt_type;
      _kpTilt_type kpTilt;
      typedef float _kiTilt_type;
      _kiTilt_type kiTilt;
      typedef float _kdTilt_type;
      _kdTilt_type kdTilt;
      typedef float _kpPan_type;
      _kpPan_type kpPan;
      typedef float _kiPan_type;
      _kiPan_type kiPan;
      typedef float _kdPan_type;
      _kdPan_type kdPan;
      typedef int32_t _mode_type;
      _mode_type mode;
      typedef bool _launch_type;
      _launch_type launch;
      typedef float _motor_speed_type;
      _motor_speed_type motor_speed;
      typedef float _tilt_angle_type;
      _tilt_angle_type tilt_angle;
      typedef float _pan_angle_type;
      _pan_angle_type pan_angle;
      typedef float _ini_spd_type;
      _ini_spd_type ini_spd;

    toOpenCR():
      kpSpeed(0),
      kiSpeed(0),
      kdSpeed(0),
      kpTilt(0),
      kiTilt(0),
      kdTilt(0),
      kpPan(0),
      kiPan(0),
      kdPan(0),
      mode(0),
      launch(0),
      motor_speed(0),
      tilt_angle(0),
      pan_angle(0),
      ini_spd(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_kpSpeed;
      u_kpSpeed.real = this->kpSpeed;
      *(outbuffer + offset + 0) = (u_kpSpeed.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_kpSpeed.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_kpSpeed.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_kpSpeed.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->kpSpeed);
      union {
        float real;
        uint32_t base;
      } u_kiSpeed;
      u_kiSpeed.real = this->kiSpeed;
      *(outbuffer + offset + 0) = (u_kiSpeed.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_kiSpeed.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_kiSpeed.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_kiSpeed.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->kiSpeed);
      union {
        float real;
        uint32_t base;
      } u_kdSpeed;
      u_kdSpeed.real = this->kdSpeed;
      *(outbuffer + offset + 0) = (u_kdSpeed.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_kdSpeed.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_kdSpeed.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_kdSpeed.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->kdSpeed);
      union {
        float real;
        uint32_t base;
      } u_kpTilt;
      u_kpTilt.real = this->kpTilt;
      *(outbuffer + offset + 0) = (u_kpTilt.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_kpTilt.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_kpTilt.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_kpTilt.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->kpTilt);
      union {
        float real;
        uint32_t base;
      } u_kiTilt;
      u_kiTilt.real = this->kiTilt;
      *(outbuffer + offset + 0) = (u_kiTilt.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_kiTilt.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_kiTilt.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_kiTilt.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->kiTilt);
      union {
        float real;
        uint32_t base;
      } u_kdTilt;
      u_kdTilt.real = this->kdTilt;
      *(outbuffer + offset + 0) = (u_kdTilt.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_kdTilt.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_kdTilt.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_kdTilt.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->kdTilt);
      union {
        float real;
        uint32_t base;
      } u_kpPan;
      u_kpPan.real = this->kpPan;
      *(outbuffer + offset + 0) = (u_kpPan.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_kpPan.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_kpPan.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_kpPan.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->kpPan);
      union {
        float real;
        uint32_t base;
      } u_kiPan;
      u_kiPan.real = this->kiPan;
      *(outbuffer + offset + 0) = (u_kiPan.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_kiPan.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_kiPan.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_kiPan.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->kiPan);
      union {
        float real;
        uint32_t base;
      } u_kdPan;
      u_kdPan.real = this->kdPan;
      *(outbuffer + offset + 0) = (u_kdPan.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_kdPan.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_kdPan.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_kdPan.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->kdPan);
      union {
        int32_t real;
        uint32_t base;
      } u_mode;
      u_mode.real = this->mode;
      *(outbuffer + offset + 0) = (u_mode.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_mode.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_mode.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_mode.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->mode);
      union {
        bool real;
        uint8_t base;
      } u_launch;
      u_launch.real = this->launch;
      *(outbuffer + offset + 0) = (u_launch.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->launch);
      union {
        float real;
        uint32_t base;
      } u_motor_speed;
      u_motor_speed.real = this->motor_speed;
      *(outbuffer + offset + 0) = (u_motor_speed.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_motor_speed.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_motor_speed.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_motor_speed.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->motor_speed);
      union {
        float real;
        uint32_t base;
      } u_tilt_angle;
      u_tilt_angle.real = this->tilt_angle;
      *(outbuffer + offset + 0) = (u_tilt_angle.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_tilt_angle.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_tilt_angle.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_tilt_angle.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->tilt_angle);
      union {
        float real;
        uint32_t base;
      } u_pan_angle;
      u_pan_angle.real = this->pan_angle;
      *(outbuffer + offset + 0) = (u_pan_angle.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_pan_angle.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_pan_angle.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_pan_angle.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->pan_angle);
      union {
        float real;
        uint32_t base;
      } u_ini_spd;
      u_ini_spd.real = this->ini_spd;
      *(outbuffer + offset + 0) = (u_ini_spd.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_ini_spd.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_ini_spd.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_ini_spd.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->ini_spd);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_kpSpeed;
      u_kpSpeed.base = 0;
      u_kpSpeed.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_kpSpeed.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_kpSpeed.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_kpSpeed.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->kpSpeed = u_kpSpeed.real;
      offset += sizeof(this->kpSpeed);
      union {
        float real;
        uint32_t base;
      } u_kiSpeed;
      u_kiSpeed.base = 0;
      u_kiSpeed.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_kiSpeed.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_kiSpeed.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_kiSpeed.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->kiSpeed = u_kiSpeed.real;
      offset += sizeof(this->kiSpeed);
      union {
        float real;
        uint32_t base;
      } u_kdSpeed;
      u_kdSpeed.base = 0;
      u_kdSpeed.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_kdSpeed.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_kdSpeed.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_kdSpeed.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->kdSpeed = u_kdSpeed.real;
      offset += sizeof(this->kdSpeed);
      union {
        float real;
        uint32_t base;
      } u_kpTilt;
      u_kpTilt.base = 0;
      u_kpTilt.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_kpTilt.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_kpTilt.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_kpTilt.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->kpTilt = u_kpTilt.real;
      offset += sizeof(this->kpTilt);
      union {
        float real;
        uint32_t base;
      } u_kiTilt;
      u_kiTilt.base = 0;
      u_kiTilt.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_kiTilt.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_kiTilt.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_kiTilt.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->kiTilt = u_kiTilt.real;
      offset += sizeof(this->kiTilt);
      union {
        float real;
        uint32_t base;
      } u_kdTilt;
      u_kdTilt.base = 0;
      u_kdTilt.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_kdTilt.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_kdTilt.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_kdTilt.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->kdTilt = u_kdTilt.real;
      offset += sizeof(this->kdTilt);
      union {
        float real;
        uint32_t base;
      } u_kpPan;
      u_kpPan.base = 0;
      u_kpPan.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_kpPan.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_kpPan.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_kpPan.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->kpPan = u_kpPan.real;
      offset += sizeof(this->kpPan);
      union {
        float real;
        uint32_t base;
      } u_kiPan;
      u_kiPan.base = 0;
      u_kiPan.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_kiPan.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_kiPan.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_kiPan.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->kiPan = u_kiPan.real;
      offset += sizeof(this->kiPan);
      union {
        float real;
        uint32_t base;
      } u_kdPan;
      u_kdPan.base = 0;
      u_kdPan.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_kdPan.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_kdPan.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_kdPan.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->kdPan = u_kdPan.real;
      offset += sizeof(this->kdPan);
      union {
        int32_t real;
        uint32_t base;
      } u_mode;
      u_mode.base = 0;
      u_mode.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_mode.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_mode.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_mode.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->mode = u_mode.real;
      offset += sizeof(this->mode);
      union {
        bool real;
        uint8_t base;
      } u_launch;
      u_launch.base = 0;
      u_launch.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->launch = u_launch.real;
      offset += sizeof(this->launch);
      union {
        float real;
        uint32_t base;
      } u_motor_speed;
      u_motor_speed.base = 0;
      u_motor_speed.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_motor_speed.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_motor_speed.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_motor_speed.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->motor_speed = u_motor_speed.real;
      offset += sizeof(this->motor_speed);
      union {
        float real;
        uint32_t base;
      } u_tilt_angle;
      u_tilt_angle.base = 0;
      u_tilt_angle.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_tilt_angle.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_tilt_angle.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_tilt_angle.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->tilt_angle = u_tilt_angle.real;
      offset += sizeof(this->tilt_angle);
      union {
        float real;
        uint32_t base;
      } u_pan_angle;
      u_pan_angle.base = 0;
      u_pan_angle.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_pan_angle.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_pan_angle.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_pan_angle.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->pan_angle = u_pan_angle.real;
      offset += sizeof(this->pan_angle);
      union {
        float real;
        uint32_t base;
      } u_ini_spd;
      u_ini_spd.base = 0;
      u_ini_spd.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_ini_spd.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_ini_spd.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_ini_spd.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->ini_spd = u_ini_spd.real;
      offset += sizeof(this->ini_spd);
     return offset;
    }

    const char * getType(){ return "filtre/toOpenCR"; };
    const char * getMD5(){ return "66664e368e3c18be9617f1286542541c"; };

  };

}
#endif