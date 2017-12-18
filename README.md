# pypsp

This is a Python module for control of GW-Instek PSP power supply units
over a serial interface.  It requires pyserial to be installed, and a recent
(3.3+ or newer) version of Python.

Note that a special cable may be necessary to interface with the power
supplies (they are optoisolated, so voltage is needed from the computer's
serial port for communications to work).  The power supplies communicate
at 2400 baud.

Full description of communication protocol and electrical connection is in [user manual](http://www.gwinstek.com/en-global/Download/DownloadFile/DownloadFile/download%23_%2304_DCPower%23_%23PSP%23_%23PSP_UserManual_EN_RevG_201702.pdf)

This module is fully working with USB to RS232 converters

## install:

    pip install .

## usage:

First create serial connection (with pyserial) and give this serial connection into Psp class.

Then use properties to access values in power supply.

## Example:

    >>> import serial
    >>> import psp
    >>> serial_port = serial.Serial('/dev/ttyS0', 2400)
    >>> psp = psp.Psp(serial_port)
    >>> psp.voltage = 4.2
    >>> psp.relay = True
    >>> print psp.current

Example Set the output voltage, close the output relay, then print the output current.
