# RULES ON INSERTION IMPLEMENTATION 🚨

    # DATA || day: start_time : end_time: [ DICTIONARY OR JSON]
    # LOGIC:
        # COUNT THE KEYS 
        # MAPPING KEYS: count the number of keys,
        #               insert the keys and values in the marked cell (based  on number of keys)
        #               number_of_keys + 1 (TOTAL (STRING INPUT)

# JSON FILE STRUCTURE FOR NEW ENTRIES.

SHEETNAME_data= {
    {
        "date": day_of_overtime,
        "weekend": day,
        "start": time,
        "finish": time,
        "MONTH": month
    }
    {
        "date": day_of_overtime,
        "weekend": day,
        "start": time,
        "finish": time,
        "MONTH": month // this will come in handly where there is need to update, a month other than a current one.
    }
}