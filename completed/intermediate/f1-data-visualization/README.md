# F1 Data Visualization

A Streamlit application for visualizing Formula 1 race data.

## Features

- Race analysis dashboard
- Lap times comparison
- Position changes visualization
- Speed traces
- Gap analysis

## Setup

1. Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run src/app.py
```

## Project Structure

- `src/` - Source code
  - `data/` - Data fetching and processing
  - `visualization/` - Chart creation and display
  - `app.py` - Main Streamlit application
- `tests/` - Test files
