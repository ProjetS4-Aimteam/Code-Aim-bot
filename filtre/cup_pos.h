#ifndef _ROS_filtre_cup_pos_h
#define _ROS_filtre_cup_pos_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace filtre
{

  class cup_pos : public ros::Msg
  {
    public:
      typedef float _cup_distance_type;
      _cup_distance_type cup_distance;
      typedef float _cup_angle_type;
      _cup_angle_type cup_angle;

    cup_pos():
      cup_distance(0),
      cup_angle(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_cup_distance;
      u_cup_distance.real = this->cup_distance;
      *(outbuffer + offset + 0) = (u_cup_distance.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_cup_distance.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_cup_distance.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_cup_distance.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->cup_distance);
      union {
        float real;
        uint32_t base;
      } u_cup_angle;
      u_cup_angle.real = this->cup_angle;
      *(outbuffer + offset + 0) = (u_cup_angle.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_cup_angle.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_cup_angle.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_cup_angle.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->cup_angle);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_cup_distance;
      u_cup_distance.base = 0;
      u_cup_distance.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_cup_distance.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_cup_distance.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_cup_distance.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->cup_distance = u_cup_distance.real;
      offset += sizeof(this->cup_distance);
      union {
        float real;
        uint32_t base;
      } u_cup_angle;
      u_cup_angle.base = 0;
      u_cup_angle.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_cup_angle.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_cup_angle.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_cup_angle.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->cup_angle = u_cup_angle.real;
      offset += sizeof(this->cup_angle);
     return offset;
    }

    const char * getType(){ return "filtre/cup_pos"; };
    const char * getMD5(){ return "cbb4a3fdcb2c32eff1b6d3cb259ee682"; };

  };

}
#endif