// Auto-generated. Do not edit!

// (in-package mybot_description.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Record {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.time = null;
      this.input = null;
      this.output = null;
    }
    else {
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = 0.0;
      }
      if (initObj.hasOwnProperty('input')) {
        this.input = initObj.input
      }
      else {
        this.input = 0.0;
      }
      if (initObj.hasOwnProperty('output')) {
        this.output = initObj.output
      }
      else {
        this.output = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Record
    // Serialize message field [time]
    bufferOffset = _serializer.float64(obj.time, buffer, bufferOffset);
    // Serialize message field [input]
    bufferOffset = _serializer.float64(obj.input, buffer, bufferOffset);
    // Serialize message field [output]
    bufferOffset = _serializer.float64(obj.output, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Record
    let len;
    let data = new Record(null);
    // Deserialize message field [time]
    data.time = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [input]
    data.input = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [output]
    data.output = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mybot_description/Record';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b9c15b4326735ca7166c3d905ae5b1de';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    float64 time
    float64 input
    float64 output
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Record(null);
    if (msg.time !== undefined) {
      resolved.time = msg.time;
    }
    else {
      resolved.time = 0.0
    }

    if (msg.input !== undefined) {
      resolved.input = msg.input;
    }
    else {
      resolved.input = 0.0
    }

    if (msg.output !== undefined) {
      resolved.output = msg.output;
    }
    else {
      resolved.output = 0.0
    }

    return resolved;
    }
};

module.exports = Record;
