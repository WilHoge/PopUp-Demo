# Generated by cpd_software_env

#wml_python_function
def my_averages_a_b_deploy():
    import os
    import cpd_software_env  # import auto-installer before other modules
    # install commands are run automatically as part of the import
    
    # In case the environment variables SPACE_ID and USER_ACCESS_TOKEN are set
    # in a new release of CP4D.
    try:
        cpd_software_env.download_pending_assets()
    except Exception:
        pass
            
    # access compute_averages after assets have been downloaded
    import compute_averages  # runs any initialization code in the user's module
    
    # Generated by cpd_software_env
    
    #wml_python_function
    def score(wml_data):
        # WStudio expects this function to be named "score"
        import os
        import cpd_software_env  
        # import auto-installer before other modules
        # install commands are run automatically as part of the import
        
        # An input data argument (usually the first one) may contain environment variables;
        # map them to the local session and download any pending assets.      
        for elem in wml_data['input_data']:
            assert isinstance(elem,dict)
            envdict = elem.get('environment_variables')
            if envdict:
                assert isinstance(envdict,dict)
                for var,val in envdict.items():
                    os.environ[var] = val
                cpd_software_env.download_pending_assets()
                
        # access compute_averages after assets have been downloaded
        from compute_averages import my_averages_a_b
        # map input data to function
        # my_averages_a_b(indata: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame
        data = wml_data['input_data']
        assert isinstance(data,list), 'input_data must be a list'
        if len(data)==1 and 'tail' in data[0]:
            assert isinstance(data[0]['tail'],list), 'input_data tail must be a list'
            data += data[0]['tail']
        import pandas as pd
        if 0>=len(data) : raise ValueError('Too few arguments in input data for deployed function my_averages_a_b')
        val_indata = pd.DataFrame(data[0]['values'],columns=data[0].get('fields'))
        scorefn_res = my_averages_a_b(indata=val_indata)
        # convert DataFrame to JSON serializable dict
        score_res = { 'fields':list(scorefn_res.columns), 'values':scorefn_res.values.tolist()}
    
        # WML expects { 'predictions': [some_dictionary] }
        if isinstance(score_res,dict):
            return { 'predictions': [score_res] }
        else:
            result = {}
            #result['autoinstall msgs'] = cpd_software_env.get_msgs()   
            result['score'] =  score_res
            return { 'predictions': [result] }

    return score

score = my_averages_a_b_deploy()
