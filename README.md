# thousand-billion
1000 billion Bryn Mawrs web app

## Pseudocode 

```{python}

def request_cell(sheetname, row_num, sheet_id):
    result = (
        sheet.values()
        .get(spreadsheetID=sheet_id, range=f"{sheetname}!A:{row_num}")
        )
    cell_value = result

    # get 
    return cell_value

sheets = ['#4', '#1']
for s in sheets:
    r = random.randint(0, 10)
    cell = request_cell(s, r, sheet_id)
```

## Tasks
- [x] deploy to cloud stuff (alice) 
- [x] set up html iframe & troubleshoot (alice)
- [ ] create jinja template
- [ ] put request functions together
- [ ] put Emma's code in repo
- [ ] write code for sheet-by-sheet
- [ ] css to match wireframe
- [ ] test out with static







