# 100 Thousand Billion Bryn Mawrs

Web app for permutations workshop 4/5/25

## Note on static version

- This requires a json file [data/bmc.json] that is generated from a list of GIDs of the google sheet
- To update for the workshop, we would need to get a list of GIDs from the new sheet (using the google sheets api and security stuff) and run code that's on the other repository: digbmc/thousand-billion

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









