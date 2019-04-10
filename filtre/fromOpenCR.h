#ifndef _ROS_filtre_fromOpenCR_h
#define _ROS_filtre_fromOpenCR_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace filtre
{

  class fromOpenCR : public ros::Msg
  {
    public:
      typedef float _actKp_type;
      _actKp_type actKp;
      typedef float _actKi_type;
      _actKi_type actKi;
      typedef float _actKd_type;
      _actKd_type actKd;
      typedef float _actSpd_type;
      _actSpd_type actSpd;

    fromOpenCR():
      actKp(0),
      actKi(0),
      actKd(0),
      actSpd(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_actKp;
      u_actKp.real = this->actKp;
      *(outbuffer + offset + 0) = (u_actKp.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_actKp.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_actKp.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_actKp.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->actKp);
      union {
        float real;
        uint32_t base;
      } u_actKi;
      u_actKi.real = this->actKi;
      *(outbuffer + offset + 0) = (u_actKi.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_actKi.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_actKi.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_actKi.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->actKi);
      union {
        float real;
        uint32_t base;
      } u_actKd;
      u_actKd.real = this->actKd;
      *(outbuffer + offset + 0) = (u_actKd.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_actKd.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_actKd.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_actKd.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->actKd);
      union {
        float real;
        uint32_t base;
      } u_actSpd;
      u_actSpd.real = this->actSpd;
      *(outbuffer + offset + 0) = (u_actSpd.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_actSpd.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_actSpd.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_actSpd.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->actSpd);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_actKp;
      u_actKp.base = 0;
      u_actKp.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_actKp.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_actKp.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_actKp.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->actKp = u_actKp.real;
      offset += sizeof(this->actKp);
      union {
        float real;
        uint32_t base;
      } u_actKi;
      u_actKi.base = 0;
      u_actKi.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_actKi.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_actKi.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_actKi.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->actKi = u_actKi.real;
      offset += sizeof(this->actKi);
      union {
        float real;
        uint32_t base;
      } u_actKd;
      u_actKd.base = 0;
      u_actKd.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_actKd.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_actKd.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_actKd.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->actKd = u_actKd.real;
      offset += sizeof(this->actKd);
      union {
        float real;
        uint32_t base;
      } u_actSpd;
      u_actSpd.base = 0;
      u_actSpd.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_actSpd.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_actSpd.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_actSpd.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->actSpd = u_actSpd.real;
      offset += sizeof(this->actSpd);
     return offset;
    }

    const char * getType(){ return "filtre/fromOpenCR"; };
    const char * getMD5(){ return "1a32b7ca5678341ca4ad1bf6de8edf68"; };

  };

}
#endif