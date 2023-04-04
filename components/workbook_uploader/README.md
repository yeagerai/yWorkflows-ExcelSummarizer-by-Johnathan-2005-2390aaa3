
# WorkbookUploader

This component accepts an Excel workbook file (.xlsx) uploaded by the user and stores it in-memory for further processing. The WorkbookUploader reads the entire workbook into memory and provides methods for accessing individual sheets and cells within the sheets. No external calls are made during this process to ensure data privacy.

## Initial generation prompt
description: This component accepts an Excel workbook file (.xlsx) uploaded by the
  user and stores it in-memory for further processing.
name: WorkbookUploader


## Transformer breakdown
- Initialize the in-memory workbook object
- Read the user-uploaded Excel workbook file
- If sheet_names parameter is 'All', load all sheets
- Else, only load the specified sheet names from the parameter
- Return the in-memory representation of the workbook

## Parameters
[{'name': 'sheet_names', 'default_value': 'All', 'description': "A list of sheet names to load from the Excel file, or 'All' to load all sheets", 'type': 'List[str]'}]

        