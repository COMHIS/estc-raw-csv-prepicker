# -----------------------
# Input conf
# -----------------------
# ESTC input csv location
estc_csv = "estc_raw_sane.csv"
#estc_csv = "./estc-data-verified/estc-csv-raw-filtered/estc_raw_sane.csv"
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
               {'field': '300', 'subfield': 'c'}]

fields_outfile = "./out/fields_picked_300c.csv"
