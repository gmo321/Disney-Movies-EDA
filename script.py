def group_by_aggregate(data, grouping_col, action_col, action = 'mean'):
    import pandas as pd
    """
    Given a dataframe, a column and an action, return a dataframe that has been
    grouped by the column with the aggregate function applied.
    
    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The dataframe of interest
    grouping_col : str
        The column to group the data on
    action_col : str
        The column to applying the action to after grouping
    action : str, optional
        The action to apply to the action_col column. The default is the mean action.      
        
    Returns
    -------
    pandas.core.frame.DataFrame 
        A dataframe with the group by column and the result of the action applied
        
    Raises
    ------
    TypeError
        If the input argument dataframe is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument grouping_col is not in the data columns
    AssertError
        If the input argument action_col is not in the data columns
    
    Examples
    --------
    >>> custom_agg(helper_data, 'flavour')
    flavour     mean
    Chocolate    4
    Vanilla      6
    """
    
    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(data, pd.DataFrame): 
        raise TypeError("The dataframe argument is not of type DataFrame")
    
    # Tests that the the grouping column is in the dataframe
    assert grouping_col in data.columns, "The grouping column does not exist in the dataframe"
    
    # Tests that the the action column is in the dataframe
    assert action_col in data.columns, "The action column does not exist in the dataframe"
    
    
    # compute the groupby object
    result = data.groupby(grouping_col)[action_col].agg([action])
    
    # convert to a dataframe
    result = pd.DataFrame(result)
    
    # reset the index
    result = result.reset_index()
    
    # return the result
    return(result)
    