class Arizona:
    '''
    Arizona maintains a single list of state-verified dispensaries, but uses javascript to display the table.
    Because javascipt is used, finding the AJAX pull is essential.
    This class uses regular expressions to parse the result.
    '''
    
    # Import request
    import requests
    
    url = 'https://arizonamedicalmarijuanaclinic.com/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=42643&target_action=get-all-data&default_sorting=old_first'
    
    page = requests.get(url)
    
    page_content = page.content
    
    
    # Clean text with regex
    
    import re
    
    dispensary_name = re.findall('(?<="dispensaryname":")(.+?)(?=","address":")', page_content)
    dispensary_address = re.findall('(?<="address":")(.+?)(?=","city":")', page_content)
    dispensary_city = re.findall('(?<="city":")(.+?)(?=","zip":")', page_content)
    dispensary_zip = re.findall('(?<="zip":")(.+?)(?=","phone":")', page_content)
    dispensary_phone = re.findall('(?<="phone":")(.+?)(?=","___id___":")', page_content)
    
    dispensary_list = list(zip(dispensary_name, dispensary_address, dispensary_city, dispensary_zip, dispensary_phone))
    
    all_dispensaries = []
    
    for tup in dispensary_list:
        dispensary_info = {"Name":tup[0], "Address":tup[1], "City":tup[2], "Zip":tup[3], "Phone":tup[4]}
        
        all_dispensaries.append(dispensary_info)
    
    
    # Create dataframe
    
    import pandas as pd
    
    df = pd.DataFrame(all_dispensaries, columns=['Name', 'Address', 'City', 'Zip', 'Phone'])
    


# Create instance of class

az = Arizona()

az.all_dispensaries


az.df
