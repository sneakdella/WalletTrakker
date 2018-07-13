#### WRITTEN BY JACOB YUHAS
#### IT485 CAPSTONE COURSE
#### UMASS BOSTON
#### SCRAPES TRACCAR SERVER LOGFILE FOR JUST THE LATEST ENTRY OF A LOCATION UPDATE
#### 7/12/2018

import re



def the_loop():
    log_file = "app/tracker-server.log"
    fh = open(log_file, "r")
    lines = fh.readlines()
    final_result = []
    for i in range(len(lines)):
        case = str(lines[i])
        regexp = re.compile(r'lat:')
        if regexp.search(case):
            #split the line by commas
            split_case = case.split(",")
            #create copy of matched case list lines so we can make modifications
            matched_lines = split_case[:]
            #First line has useless data, but I need just the ID
            # Uncomment below to see what I mean, I just want the "ID: 000000"
            #print(split_case[0])
            matched_lines[0] = matched_lines[0][-11:]
            #print out the matched lines and append them to a final list.
            # and init dictionary
            new_dictionary = {}
            for i in range(len(matched_lines)):
                #remove whitespace
                key_val_pair = matched_lines[i].replace(" ", "")
                #remove escape characters
                key_val_pair = key_val_pair.replace("\n", "")
                #split by the colon so it's key / value
                key_val_split = key_val_pair.split(":", 1)
                # Add to new dictionary
                new_dictionary[key_val_split[0]] = key_val_split[1]
            #append newly created dictionary to the list of dictionaries	
            final_result.append(new_dictionary)
    fh.close()

    """

    # DEBUG STUFF

    for i in range(len(final_result)):
	    print(final_result[i])
    """

    print()
    return final_result

def update_map():
    final_result = the_loop()
    last_entry = final_result[-1]
    dev_id = last_entry.get("id")
    geo_lat = last_entry.get("lat")
    geo_long = last_entry.get("lon")
    return dev_id, geo_lat, geo_long

print("MAP FUNCTION: " + str(update_map()))