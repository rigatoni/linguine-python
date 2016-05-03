#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import cogcomp.base.BaseService
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface(cogcomp.base.BaseService.Iface):
  """
  Parser service.

  """
  def parseRecord(self, record):
    """
    Parses the Record.


    Parameters:
     - record
    """
    pass


class Client(cogcomp.base.BaseService.Client, Iface):
  """
  Parser service.

  """
  def __init__(self, iprot, oprot=None):
    cogcomp.base.BaseService.Client.__init__(self, iprot, oprot)

  def parseRecord(self, record):
    """
    Parses the Record.


    Parameters:
     - record
    """
    self.send_parseRecord(record)
    return self.recv_parseRecord()

  def send_parseRecord(self, record):
    self._oprot.writeMessageBegin('parseRecord', TMessageType.CALL, self._seqid)
    args = parseRecord_args()
    args.record = record
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_parseRecord(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = parseRecord_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ex is not None:
      raise result.ex
    raise TApplicationException(TApplicationException.MISSING_RESULT, "parseRecord failed: unknown result");


class Processor(cogcomp.base.BaseService.Processor, Iface, TProcessor):
  def __init__(self, handler):
    cogcomp.base.BaseService.Processor.__init__(self, handler)
    self._processMap["parseRecord"] = Processor.process_parseRecord

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_parseRecord(self, seqid, iprot, oprot):
    args = parseRecord_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = parseRecord_result()
    try:
      result.success = self._handler.parseRecord(args.record)
    except cogcomp.base.ttypes.AnnotationFailedException, ex:
      result.ex = ex
    oprot.writeMessageBegin("parseRecord", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class parseRecord_args:
  """
  Attributes:
   - record
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'record', (cogcomp.curator.ttypes.Record, cogcomp.curator.ttypes.Record.thrift_spec), None, ), # 1
  )

  def __init__(self, record=None,):
    self.record = record

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.record = cogcomp.curator.ttypes.Record()
          self.record.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('parseRecord_args')
    if self.record is not None:
      oprot.writeFieldBegin('record', TType.STRUCT, 1)
      self.record.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class parseRecord_result:
  """
  Attributes:
   - success
   - ex
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (cogcomp.base.ttypes.Forest, cogcomp.base.ttypes.Forest.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'ex', (cogcomp.base.ttypes.AnnotationFailedException, cogcomp.base.ttypes.AnnotationFailedException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ex=None,):
    self.success = success
    self.ex = ex

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = cogcomp.base.ttypes.Forest()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ex = cogcomp.base.ttypes.AnnotationFailedException()
          self.ex.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('parseRecord_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.ex is not None:
      oprot.writeFieldBegin('ex', TType.STRUCT, 1)
      self.ex.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
