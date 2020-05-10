// Auto-generated. Do not edit!

// (in-package mybot_description.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class MapPoint {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.mapPointID = null;
      this.position = null;
      this.angleOfApproach = null;
    }
    else {
      if (initObj.hasOwnProperty('mapPointID')) {
        this.mapPointID = initObj.mapPointID
      }
      else {
        this.mapPointID = 0;
      }
      if (initObj.hasOwnProperty('position')) {
        this.position = initObj.position
      }
      else {
        this.position = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('angleOfApproach')) {
        this.angleOfApproach = initObj.angleOfApproach
      }
      else {
        this.angleOfApproach = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MapPoint
    // Serialize message field [mapPointID]
    bufferOffset = _serializer.uint8(obj.mapPointID, buffer, bufferOffset);
    // Serialize message field [position]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.position, buffer, bufferOffset);
    // Serialize message field [angleOfApproach]
    bufferOffset = _serializer.float64(obj.angleOfApproach, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MapPoint
    let len;
    let data = new MapPoint(null);
    // Deserialize message field [mapPointID]
    data.mapPointID = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [position]
    data.position = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [angleOfApproach]
    data.angleOfApproach = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 33;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mybot_description/MapPoint';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '25d6001ca9760cc13d10b9eb4e3a92e8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Message file for nodes in map
    
    uint8 mapPointID
    geometry_msgs/Point position
    float64 angleOfApproach
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MapPoint(null);
    if (msg.mapPointID !== undefined) {
      resolved.mapPointID = msg.mapPointID;
    }
    else {
      resolved.mapPointID = 0
    }

    if (msg.position !== undefined) {
      resolved.position = geometry_msgs.msg.Point.Resolve(msg.position)
    }
    else {
      resolved.position = new geometry_msgs.msg.Point()
    }

    if (msg.angleOfApproach !== undefined) {
      resolved.angleOfApproach = msg.angleOfApproach;
    }
    else {
      resolved.angleOfApproach = 0.0
    }

    return resolved;
    }
};

module.exports = MapPoint;
