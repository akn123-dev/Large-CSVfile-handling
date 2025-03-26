

# CSV to MySQL Chunk Splitter and Importer

## Overview

This repository provides two Python scripts to **split large CSV files** into smaller chunks and **import those chunks** into a **MySQL database**. The scripts are designed to handle large datasets efficiently by processing the data in chunks, thus preventing memory overload during import.

### Features:
1. **CSV Splitting**: 
   - The script splits a large CSV file into smaller, manageable chunks (1GB per chunk by default).
   - The chunks are saved to a specified output directory for later use.

2. **MySQL Import**:
   - The script connects to a MySQL database and uses the `LOAD DATA LOCAL INFILE` command to import each chunk into a specified MySQL table.
   - The import process is logged, showing success or failure for each chunk.

## Prerequisites

Before running the scripts, make sure you have the following:

1. **Python 3.x** installed.
2. **MySQL Server** running and accessible from the machine where the script is being executed.
3. **MySQL Python Connector**: Install it using pip if you haven't already:

   ```bash
   pip install mysql-connector-python
   ```

4. **Pandas** for CSV file handling:

   ```bash
   pip install pandas
   ```

## Files

### 1. `chunks.py`

This script splits a large CSV file into smaller chunks based on the size of each chunk. The size of each chunk is set to approximately **1GB**.

- **Input**: Path to a large CSV file.
- **Output**: Chunks of CSV files saved in the specified output folder.

#### Example Usage:

```bash
python chunks.py
```

#### Configuration:
- **csv_file**: Specify the path to your large CSV file.
- **output_folder**: Specify the folder where you want to save the chunks.

### 2. `sqlupload.py`

This script imports the chunked CSV files into a MySQL database.

- **Input**: Path to the folder containing chunked CSV files.
- **Output**: Data imported into the specified MySQL table.

#### Example Usage:

```bash
python sqlupload.py
```

#### Configuration:
- **MYSQL_HOST**: MySQL host (e.g., `localhost`).
- **MYSQL_USER**: MySQL username (e.g., `root`).
- **MYSQL_PASSWORD**: MySQL password.
- **MYSQL_DATABASE**: Name of the database to use.
- **MYSQL_TABLE**: Name of the table to import data into.
- **chunk_folder**: Path to the folder containing the CSV chunks.

## How It Works

1. **Splitting CSV**:
   - The script reads the large CSV file in chunks, calculates the size of each chunk based on the specified target size (1GB), and saves them as separate CSV files.

2. **Importing to MySQL**:
   - The script loops through the chunked CSV files, loads them into the specified MySQL database table using the `LOAD DATA LOCAL INFILE` command, and logs success or failure for each file.

## Customization

- **Chunk Size**: You can adjust the chunk size by modifying the `target_size` in the **split CSV script**.
- **MySQL Configuration**: Update the MySQL connection details (`MYSQL_HOST`, `MYSQL_USER`, etc.) in the **import script** to match your MySQL server configuration.

## Notes

- **Error Handling**: Errors encountered during the import process are logged for debugging.
- **Performance**: The import process is optimized for handling large CSV files by breaking them into smaller chunks.
