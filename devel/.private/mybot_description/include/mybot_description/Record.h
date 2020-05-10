// Generated by gencpp from file mybot_description/Record.msg
// DO NOT EDIT!


#ifndef MYBOT_DESCRIPTION_MESSAGE_RECORD_H
#define MYBOT_DESCRIPTION_MESSAGE_RECORD_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mybot_description
{
template <class ContainerAllocator>
struct Record_
{
  typedef Record_<ContainerAllocator> Type;

  Record_()
    : time(0.0)
    , input(0.0)
    , output(0.0)  {
    }
  Record_(const ContainerAllocator& _alloc)
    : time(0.0)
    , input(0.0)
    , output(0.0)  {
  (void)_alloc;
    }



   typedef double _time_type;
  _time_type time;

   typedef double _input_type;
  _input_type input;

   typedef double _output_type;
  _output_type output;





  typedef boost::shared_ptr< ::mybot_description::Record_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mybot_description::Record_<ContainerAllocator> const> ConstPtr;

}; // struct Record_

typedef ::mybot_description::Record_<std::allocator<void> > Record;

typedef boost::shared_ptr< ::mybot_description::Record > RecordPtr;
typedef boost::shared_ptr< ::mybot_description::Record const> RecordConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mybot_description::Record_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mybot_description::Record_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mybot_description

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/kinetic/share/nav_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'mybot_description': ['/home/varsh/mybot_ws/src/mybot_description/msg', '/home/varsh/mybot_ws/devel/.private/mybot_description/share/mybot_description/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mybot_description::Record_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mybot_description::Record_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mybot_description::Record_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mybot_description::Record_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mybot_description::Record_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mybot_description::Record_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mybot_description::Record_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b9c15b4326735ca7166c3d905ae5b1de";
  }

  static const char* value(const ::mybot_description::Record_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb9c15b4326735ca7ULL;
  static const uint64_t static_value2 = 0x166c3d905ae5b1deULL;
};

template<class ContainerAllocator>
struct DataType< ::mybot_description::Record_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mybot_description/Record";
  }

  static const char* value(const ::mybot_description::Record_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mybot_description::Record_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
float64 time\n\
float64 input\n\
float64 output\n\
";
  }

  static const char* value(const ::mybot_description::Record_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mybot_description::Record_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.time);
      stream.next(m.input);
      stream.next(m.output);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Record_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mybot_description::Record_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mybot_description::Record_<ContainerAllocator>& v)
  {
    s << indent << "time: ";
    Printer<double>::stream(s, indent + "  ", v.time);
    s << indent << "input: ";
    Printer<double>::stream(s, indent + "  ", v.input);
    s << indent << "output: ";
    Printer<double>::stream(s, indent + "  ", v.output);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MYBOT_DESCRIPTION_MESSAGE_RECORD_H
