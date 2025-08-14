# Core Values Recovery - Manual to PDF Conversion

This system converts your coaching manuals from Markdown to professionally branded HTML that can easily be converted to PDF.

## Features

- **CVR Branding**: Uses your company colors (#1d4486) and Bebas Neue font
- **Professional Layout**: Print-ready formatting with proper margins and page breaks
- **Time Block Highlighting**: Special formatting for session timing sections
- **Print Optimization**: CSS optimized for PDF generation

## Quick Start

### Convert a Single Manual
```bash
python scripts/manual-to-html.py path/to/your-manual.md
```

### Convert All Manuals at Once
```bash
python scripts/convert-all-manuals.py
```

### Preview in Browser
```bash
python scripts/manual-to-html.py path/to/your-manual.md --preview
```

## Convert HTML to PDF

### Method 1: Browser (Recommended)
1. Open the generated HTML file in your browser
2. Press `Cmd+P` (Mac) or `Ctrl+P` (PC)
3. Select "Save as PDF"
4. Choose "More settings" and set margins to "Minimum"
5. Save your PDF

### Method 2: Command Line (Advanced)
Install wkhtmltopdf and run:
```bash
wkhtmltopdf --page-size Letter --margin-top 0.5in --margin-bottom 0.5in --margin-left 0.5in --margin-right 0.5in your-manual.html your-manual.pdf
```

## File Structure

```
scripts/
├── manual-to-html.py      # Main conversion script
├── convert-all-manuals.py # Batch conversion script
└── README.md              # This file

executive_function/
├── week-1-coaches-manual.md    # Your markdown manual
├── week-1-coaches-manual.html  # Generated HTML
└── ...
```

## Customization

The branding and styling can be modified in the `get_css_styles()` function in `manual-to-html.py`:

- **Colors**: Modify the `get_brand_colors()` function
- **Fonts**: Change the Google Fonts import and font-family declarations
- **Layout**: Adjust margins, spacing, and print styles in the CSS

## Troubleshooting

**Q: The fonts don't look right**
A: Make sure you have an internet connection for Google Fonts, or the system will fall back to Arial.

**Q: Time blocks aren't formatting correctly**
A: The script looks for headers starting with numbers and dashes (e.g., "### 0–3 min — Welcome"). Make sure your timing sections follow this format.

**Q: PDF margins are too large**
A: In your browser's print dialog, select "More settings" and change margins to "Minimum" or "Custom" with smaller values.

## Logo Integration (Future Enhancement)

To add your logo to the header, modify the `create_header()` function to include:
```html
<img src="path/to/your/logo.png" alt="Core Values Recovery" class="logo">
```

Make sure to copy your logo file to a web-accessible location relative to the HTML file.