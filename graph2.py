import svgwrite
from datetime import datetime
import csv


def parse_time_codes(time_code):
    start = datetime.strptime(time_code[0], timecode_format)
    end = datetime.strptime(time_code[1], timecode_format)
    seconds_in = (start - start_time).total_seconds()
    seconds_out = (end - start_time).total_seconds()
    return (start, end, seconds_in, seconds_out)


timecode_format = '%H:%M:%S'
start_time = datetime.strptime("00:00:00", timecode_format)

sequences = []
anotations = []

with open('bbegin.csv', 'rb') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        time_code = parse_time_codes((row['TimecodeIN '], row['TimecodeOUT ']))
        if row['Sequence # ']:
            sequences.append({
                'time_code': time_code,
                'justification': row['Justification'],
                'sequence_number': row['Sequence # ']
            })
        if row['Scene']:
            anotations.append({
                'time_code': time_code,
                'justification': row['Justification'],
                'scene': row['Scene'],
            })


last_time_code = start_time

for s in sequences:
    if s['time_code'][1] > last_time_code:
        last_time_code = s['time_code'][1]

total_seconds = (last_time_code-start_time).total_seconds()

margin = 30
drawing_width = 200
drawing_height = total_seconds + (margin * 2)

sequence_color = '#F5A623'
anotation_color = '#313CA3'


def get_sequence_shape(sequence):
    seconds_in = sequence['time_code'][2]
    seconds_out = sequence['time_code'][3]
    x = margin
    y = margin+seconds_in
    width = drawing_width - (margin * 2)
    height = seconds_out - seconds_in
    return svgwrite.shapes.Rect(
        insert=(x, y),
        size=(width, height),
        rx = width/4,
        ry = width/4,
        fill=sequence_color
    )


def get_annotaion_shape(anotation):
    seconds_in = anotation['time_code'][2]
    seconds_out = anotation['time_code'][3]
    x = margin
    y = margin+seconds_in
    width = drawing_width - (margin * 2)
    height = seconds_out - seconds_in
    return svgwrite.shapes.Rect(
        insert=(x, y),
        size=(width, height),
        rx = 2,
        ry = 2,
        fill=anotation_color
    )


drawing = svgwrite.Drawing('test1.svg', size=(drawing_width, drawing_height))

sequences_clip_path = svgwrite.masking.ClipPath()
sequences_clip_path['id'] = 'sequences-clip'
drawing.add(sequences_clip_path)

for s in sequences:
    drawing.add(get_sequence_shape(s))
    sequences_clip_path.add(get_sequence_shape(s))

for a in anotations:
    shape = get_annotaion_shape(a)
    shape['clip-path'] = "url(#sequences-clip)"
    drawing.add(shape)

drawing.save()
