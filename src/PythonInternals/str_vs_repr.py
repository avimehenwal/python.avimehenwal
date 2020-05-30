def str_repr_fn(var):
    print('Var and Type    = {} {}'.format(var, type(var)))
    print('str(var)        = {}'.format(str(var)))
    print('repr(var)       = {}'.format(repr(var)))
    print('var.__str__()   = {}'.format(var.__str__()))
    print('var.__repr__()  = {}'.format(var.__repr__()))
    print('type(str(var))  = {}'.format(type(str(var))))
    print('type(repr(var)) = {}'.format(type(repr(var))))
    print('len(str(var))   = {}'.format(len(str(var))))
    print('len(repr(var))  = {}'.format(len(repr(var))))
    
    print('\n')

if __name__ == '__main__':
    str_repr_fn('avi')
    str_repr_fn(53)
    str_repr_fn([1, 2, 3, 4,])
    str_repr_fn(['a', 'b', 'c',])
    str_repr_fn((1, 2, 3))
    str_repr_fn(('p', 'q', 'r'))
    str_repr_fn({'x', 'y', 'z'})
    str_repr_fn({'one': 1, 2: 'two'})
