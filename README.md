# 100 Thousand Billion Bryn Mawrs

Web app for permutations workshop 4/4/25

## Notes on versions

- Static: loads from json, not live
- Turtle: loads live, but very slowly (incredibly slowly on Cloud)

## Notes on this version

- GIDs must be updated with new sheet
- Needs some visual signifier of loading (or needs to partially load)

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
- [x] create jinja template
- [x] put request functions together
- [x] put Emma's code in repo
- [x] write code for sheet-by-sheet
- [x] css to match wireframe
- [x] test out with static
- [x] fix javascript problem
- [ ] finish style and content
- [ ] get final text from J&S
- [ ] work on request version







