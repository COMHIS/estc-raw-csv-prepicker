from lib.estc_prepicker_common import (
    get_file_len,
    print_progress,
    read_estc_csv
    )

from fieldpicker_conf_008 import (
    estc_csv,
    fields_keep,
    fields_outfile
    )

from lib.estc_marc import (
    ESTCMARCEntry,
    ESTCMARCEntryWriteBuffer)


def process_record_lines(record_lines,
                         fields_to_pick,
                         output_buffer,
                         force_write=False):
    new_estc_entry = ESTCMARCEntry(record_lines)
    new_estc_entry.keep_fields(fields_to_pick)
    output_buffer.add_marc_entry(new_estc_entry)
    if force_write:
        output_buffer.write_marc_entry_csv()


prev_record_seq = None
record_lines = list()
output_buffer = ESTCMARCEntryWriteBuffer(fields_outfile)

i = 0
file_lines = get_file_len(estc_csv)

print("Picking fields ...")
for row in read_estc_csv(estc_csv):

    i += 1
    if i % 1000 == 0:
        print_progress(i, file_lines)

    if prev_record_seq is None:
        prev_record_seq = row.get('Record_seq')
    current_record_seq = row.get('Record_seq')
    # Check if Record_seq changes. If changed, process record and start new

    if current_record_seq != prev_record_seq:
        process_record_lines(
            record_lines,
            fields_keep,
            output_buffer)
        record_lines = [row]
        prev_record_seq = current_record_seq
    # If record seq does not change, append to working record buffer.
    else:
        record_lines.append(row)

process_record_lines(
    record_lines,
    fields_keep,
    output_buffer,
    force_write=True)
