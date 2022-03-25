# This code is a function that predicts the 42 products of the pyrolysis products based on the inoputs in aspen 
def pyrolysis_ROM(feedstock_comp):
    import pickle
    '''
    
    This function takes the composition of biomass as input and returns the primary products of pyrolysis in a dictionary
    
    input: an array conntainging the biochemical composition of the biomass in the form
    [Cellulose, hemicellulose, ligninc,ligninh,lignino]  
    
    output: a dictionary containing the products of the pyrolysis process 
    '''
    
# The next line imports the ranzi data to extract the products 
    products = ['CELLA','HCEA1','HCEA2','LIG','LIGCC','LIGOH','GCO2','GCO','GCOH2','GH2','Char','HAA','GLYOX','C3H6O','C3H4O2','HMFU','LVG', 'XYL','pCOUMARYL','PHENOL','FE2MACR','CH3CHO','ETOH','CH3OH','CO','CO2','CH4','CH2O','H2','C2H4','H2O']
    # The next line creates an empty list, the products predicted are going to be stored in this list while we loop through each product model    
    predictions =[]

# The for loop will loop through the products models, predict and append each product to the prediction list 
    for name in products:
        model = 'model' + name + ".sav"
        model2 = pickle.load(open(model,'rb'))
        pred = model2.predict(feedstock_comp)
        predictions.append(pred)
    predictions_dict = dict(zip(products,predictions)) 
    return (predictions_dict)
