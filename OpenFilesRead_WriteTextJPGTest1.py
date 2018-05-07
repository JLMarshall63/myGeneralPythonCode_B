with open('C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\smiley.jpg', 'rb') as rf:
    with open('C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\smiley200.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

with open('C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT2.txt', 'r') as rf:
    with open('C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\myScriptsT200.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\smiley.jpg', 'rb') as rf:
    with open('C:\University of Washington GIS\UOWSummer2017\GEOG565\FinalProject\ProjectProposal\script\smiley300.jpg', 'wb') as wf:
        chunk_size = 2500
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
            