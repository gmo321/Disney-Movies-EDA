from sample_script import group_by_aggregate
import pandas as pd

def test_group_by_aggregate():

    # Create helper data and write tests for the function
    raw = {'id': [34, 52, 15, 16, 2,
                   67, 98, 22, 79, 5], 
           'name': ['Jane', 'Harry', 'Hannah', 
                    'Peter', 'Grace', 'Justin',
                    'Bryan', 'David', 'Lily',
                    'Thomas'], 
            'type': ['SUV', 'Sedan', 'Sedan', 'SUV', 'Sedan',
                     'Sedan', 'SUV', 'SUV', 'Sedan', 'Sedan'],
            'miles': [12934, 567, 2305, 256324, 10001,
                         3568, 99987, 2223, 12500, 1038]}

    helper_data = pd.DataFrame.from_dict(raw)

    res = group_by_aggregate(helper_data, 'type', 'name')

    assert res.shape == (2,2)
    assert list(res['mean']) == [6, 4]
    assert list(res['type']) == ['SUV', 'Sedan']