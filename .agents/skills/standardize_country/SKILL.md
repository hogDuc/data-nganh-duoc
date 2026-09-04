---
name: standardize-country
description: >-
  Extracts and standardizes pharmaceutical manufacturing countries from raw text data into regex filter dictionaries for config/filter_config.py. Use this skill whenever the user asks to parse, extract, or standardize country names from raw production/packaging strings into regex dictionaries.
---

# Standardize Country Filter

Converts raw drug manufacturing location strings into normalized Python dictionary objects for `config['country_config']['filter']` in `config/filter_config.py`.

## Steps

1. **Analyze and Filter Roles**:
   - Identify the primary manufacturing location (CSSX, cơ sở sản xuất, NSX, nước SX, sản xuất ống thuốc, cơ sở trộn...).
   - Explicitly ignore secondary roles: packaging (CSĐG, đóng gói), quality control (KTCL, kiểm soát lô), and batch release (XX, CSXX).
   - If the line contains only domestic Vietnamese locations (e.g., Hà Tây, Hậu Giang) or company names without a distinct foreign manufacturing nation, skip it entirely.

2. **Format Output Dictionary**:
   - `output_value`: Standard Vietnamese country name (e.g., "Việt Nam", "Hoa Kỳ", "Đức", "Ukraine", "Áo", "Nhật Bản", "Séc"...).
   - `include_keyword`: Regex patterns in lowercase, without Vietnamese accents.
     - Always use non-capturing groups `(?:...)` instead of `(...)` to prevent pandas regex `UserWarning`.
     - Append word boundaries `\b` to words to prevent partial matching (e.g., `r"^y\b"`, `r"^duc\b"`).
   - `exclude_keyword`: Empty list `[]` by default, or specific regex to eliminate secondary packaging/release overlaps.
   - `is_regex`: Always set to `True`.
   - Ensure trailing commas are placed after each item and dictionary block.

3. **Check Existing Config**:
   - Inspect `config/filter_config.py`.
   - If the target country already exists under `country_config['filter']`, append the new regex to its existing `include_keyword` list instead of generating a duplicate dictionary block.

## Validation

- Verify that no capturing groups `(...)` exist in any regex pattern.
- Confirm valid Python dictionary syntax including trailing commas.

## Output Pattern

```python
{
    "output_value": "Ukraine",
    "include_keyword": [
        r"^(?:u-crai-na|ukraine|ukraina)\b",
    ],
    "exclude_keyword": [],
    "is_regex": True,
},
{
    "output_value": "Nhật Bản",
    "include_keyword": [
        r"(?:cssx|co so (?:san xuat|sx)|nuoc (?:san xuat|sx)|s(?:an )?x(?:uat)?)[^;:\n]*[:\s]+(?:nhat(?: ban)?|japan)\b",
    ],
    "exclude_keyword": [],
    "is_regex": True,
},