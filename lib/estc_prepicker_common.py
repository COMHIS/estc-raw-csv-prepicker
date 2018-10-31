import csv


def get_file_len(filename):
    with open(filename, 'r', encoding="utf-8") as countfile:
        for i, l in enumerate(countfile):
            pass
        return i + 1


def print_progress(current_i, max_i):
    percentage_str = str(round(current_i / float(max_i) * 100, 1)) + "%"
    print("Progress: " + percentage_str,
          end="\r", flush=True)


def read_estc_csv(estc_csv_location):
    with open(estc_csv_location, "r", encoding="utf-8") as csvfile:
        datareader = csv.DictReader(csvfile, delimiter="\t")
        for row in datareader:
            yield row


def get_n_distinct_entries_estc_csv(estc_csv_file):
    distinct_set = set()
    for row in read_estc_csv(estc_csv_file):
        distinct_set.add(row.get('Record_seq'))
    return len(distinct_set)


def create_prefilter_summary_file(sane_out_file,
                                  false_out_file,
                                  duplicated_out_file,
                                  summary_file_md):
    sane_out_n = get_n_distinct_entries_estc_csv(sane_out_file)
    false_out_n = get_n_distinct_entries_estc_csv(false_out_file)
    duplicated_out_n = get_n_distinct_entries_estc_csv(duplicated_out_file)
    with open(summary_file_md, 'w') as summaryfile:
        summaryfile.write("#Number of distinct entries\n")
        summaryfile.write("**Sane:** " + str(sane_out_n) + "\n")
        summaryfile.write("**Bad:** " + str(false_out_n) + "\n")
        summaryfile.write("**Duplicated:** " + str(duplicated_out_n) + "\n")
