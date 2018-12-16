# -----------------------
# Input conf
# -----------------------
# ESTC input csv location
estc_csv = "../estc-data-verified/estc-csv-raw-filtered/estc_raw_sane.csv"
#estc_csv = "data-temp/sample1-10000.csv"

# -----------------------
# Output conf
# -----------------------
# Only these fields (and subfields) will be preserved in the output.
# If subfield is omitted all subfields will be kept.
# Also, if subfield has the value 'all', all subfields will be kept.
# If you want to have multiple subfields, but not all per one field, add
# an entry for each combination.
fields_keep = [{'field': '035', 'subfield': 'a'},
               {'field': '260', 'subfield': 'c'}, # Publication year
               {'field': '310', 'subfield': 'a'}, # Publication freq.
               {'field': '362', 'subfield': 'a'} # Publication interv.
               # {'field': '041'} # This field is in use in other catalogues than ESTC
               ]
fields_outfile = "out/fields_picked_time.csv"

# field 035 a has the CU-RivES info. You'll prob want to keep that.
# examples:
# Cu-RivES and all publisher field info:
# fields_keep = [{'field': '035'},
#                {'field': '260', 'subfield': 'all'}]
# Cu-RivES and publication location only:
# fields_keep = [{'field': '035'},
#                {'field': '260', 'subfield': 'a'}]
# Cu-RivES, publication location and publication year:
# fields_keep = [{'field': '035'},
#                {'field': '260', 'subfield': 'a'},
#                {'field': '260', 'subfield': 'c'}]
