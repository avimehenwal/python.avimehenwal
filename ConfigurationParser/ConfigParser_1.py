import ConfigParser

config = ConfigParser.RawConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.

##############################################################################
#Adding configuration to conf file

config.add_section('Section1')
config.set('Section1', 'an_int', '15')
config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

config.add_section('Section2')
config.set('Section2', 'an_2int', '15')
config.set('Section2', 'a_b2ool', 'true')
config.set('Section2', 'a_fl2oat', '3.1415')
config.set('Section2', 'ba2z', 'f2un')
config.set('Section2', 'ba2r', 'Pyt2hon')
config.set('Section2', 'foo22', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'example.cfg'
with open('example.cfg', 'wb') as configfile:
    config.write(configfile)

print "Done Creating Configuration Parser File [example.cfg]"


##############################################################################
# Reading the configuration File

config.read('example.cfg')

# getfloat() raises an exception if the value is not a float
# getint() and getboolean() also do this for their respective types
a_float = config.getfloat('Section1', 'a_float')
print "a_float",a_float
an_int = config.getint('Section1', 'an_int')
print "an_int",an_int
# Computation on Config Values
print a_float + an_int

# Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
# This is because we are using a RawConfigParser().
if config.getboolean('Section1', 'a_bool'):
    print config.get('Section1', 'foo')


###############################################################################
# https://wiki.python.org/moin/ConfigParserExamples
