from collections import OrderedDict

o_dict = OrderedDict()
o_dict['String'] = '1'
o_dict['Int'] = 12
o_dict['Float'] = 12.3
o_dict['Double'] = 12.34
print(o_dict['Int'])
for i, j in o_dict.items():
    print(i, j)


v_dict = {}
v_dict['String'] = '1'
v_dict['Int'] = 12
v_dict['Float'] = 12.3
v_dict['Double'] = 12.34
print(v_dict['Double'])
for i, j in v_dict.items():
    print(i, j)


# That's strange Ordered Dict remembers the order and Normal Dict doesn't but here these
# two don't make any difference.
