// Generated by gencpp from file dvrk2robosuite/measured_cv.msg
// DO NOT EDIT!


#ifndef DVRK2ROBOSUITE_MESSAGE_MEASURED_CV_H
#define DVRK2ROBOSUITE_MESSAGE_MEASURED_CV_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/Twist.h>

namespace dvrk2robosuite
{
template <class ContainerAllocator>
struct measured_cv_
{
  typedef measured_cv_<ContainerAllocator> Type;

  measured_cv_()
    : header()
    , twist()  {
    }
  measured_cv_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , twist(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::geometry_msgs::Twist_<ContainerAllocator>  _twist_type;
  _twist_type twist;





  typedef boost::shared_ptr< ::dvrk2robosuite::measured_cv_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dvrk2robosuite::measured_cv_<ContainerAllocator> const> ConstPtr;

}; // struct measured_cv_

typedef ::dvrk2robosuite::measured_cv_<std::allocator<void> > measured_cv;

typedef boost::shared_ptr< ::dvrk2robosuite::measured_cv > measured_cvPtr;
typedef boost::shared_ptr< ::dvrk2robosuite::measured_cv const> measured_cvConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dvrk2robosuite::measured_cv_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dvrk2robosuite::measured_cv_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::dvrk2robosuite::measured_cv_<ContainerAllocator1> & lhs, const ::dvrk2robosuite::measured_cv_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.twist == rhs.twist;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::dvrk2robosuite::measured_cv_<ContainerAllocator1> & lhs, const ::dvrk2robosuite::measured_cv_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace dvrk2robosuite

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::dvrk2robosuite::measured_cv_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dvrk2robosuite::measured_cv_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dvrk2robosuite::measured_cv_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dvrk2robosuite::measured_cv_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dvrk2robosuite::measured_cv_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dvrk2robosuite::measured_cv_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dvrk2robosuite::measured_cv_<ContainerAllocator> >
{
  static const char* value()
  {
    return "98d34b0043a2093cf9d9345ab6eef12e";
  }

  static const char* value(const ::dvrk2robosuite::measured_cv_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x98d34b0043a2093cULL;
  static const uint64_t static_value2 = 0xf9d9345ab6eef12eULL;
};

template<class ContainerAllocator>
struct DataType< ::dvrk2robosuite::measured_cv_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dvrk2robosuite/measured_cv";
  }

  static const char* value(const ::dvrk2robosuite::measured_cv_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dvrk2robosuite::measured_cv_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Header header\n"
"geometry_msgs/Twist twist\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Twist\n"
"# This expresses velocity in free space broken into its linear and angular parts.\n"
"Vector3  linear\n"
"Vector3  angular\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::dvrk2robosuite::measured_cv_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dvrk2robosuite::measured_cv_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.twist);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct measured_cv_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dvrk2robosuite::measured_cv_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dvrk2robosuite::measured_cv_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "twist: ";
    s << std::endl;
    Printer< ::geometry_msgs::Twist_<ContainerAllocator> >::stream(s, indent + "  ", v.twist);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DVRK2ROBOSUITE_MESSAGE_MEASURED_CV_H
