## Advantages
1. scales in both direction
2. CI support out of the box
3. Runs existing unittest
4. Plugins pytest-xdist, pytest-capturelog, pytest-cov, pytest-django, pytest-twisted
5. has marks
6. Fixtures: dependencies out of test-case
7. Config Files: pytest.ini, tox.ini, nose.cfg
8. PDB on failure 
`from pytest import set_trace`

## Fixtures
1. At different levels
2. Scope: function, session, module
3. Chaining Fixtures
4. Interdependent Fixtures
5. Skip/Fails in fixtures
6. Marks signature passing
7. Autouse=True fixtures 
8. Parameterising Fixtures


#### BENEFITS
1. Dropping pdb on failures
2. Auto test-discovery
3. Supports unittest
4. Profiling test execution duration
5. JUnitXML / resultlog format files
6. Plugins
7. Integration with setuptools
8. Pretty failure report
9. TestCase Labelling


##### PARAMETRIZATION IMPLEMENTATIONS
1. Direct Parametrization - setup fixture
2. Indirect Parametrization
    1. Per class configuration
    2. Multiple Fixtures
    3. Optional Implementations

##### SUT
1. Reflektion webservices
    1. Are services available ?
    2. Are they returning valid (ignore genuin) output ?
    3. Are they getting displayed on customers website ?
    4. Are they looking nicely aligned ?
