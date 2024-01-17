# bulk_vcards
A Python script that generates vCard contact packages for easy importation. The tool is designed to create vCard files from a list of phone numbers, allowing users to organize contacts conveniently.

## Usage

1. **Install**: requirements
   
   `pip install -r requirements.txt`

3. **Prepare Contact List**: Import the contact list in the following format:

    ```
    +55 84 9999-1642
    +55 85 8156-8582
    +55 85 8523-9617
    ```

4. **Run the Script**: Execute the script and follow the prompts.

    ```bash
    python script_name.py
    ```

5. **Choose Contact List File**: Select the desired contact list file from the displayed options.

6. **Set Group Size**: Enter the desired number of contacts per vCard package.

7. **Set Default Contact Name**: Specify the default name for your leads.

8. **Review Output**: The script will create vCard files with contacts organized in groups based on the chosen size. The files will be stored in a timestamped directory.

## Additional Notes

- In the `criar_contato` function, a single quote (`'`) is prefixed to each name. This ensures that these contacts appear first in the contact list when imported.

## Requirements

- Python 3.x
- Colorama library (install using `pip install colorama`)

## Author

- **Gato**
  - Instagram: [@gato.ads](https://www.instagram.com/gato.ads/)

## Disclaimer

This tool is provided as-is, and the author assumes no responsibility for its usage or any consequences thereof. Use it responsibly and ensure compliance with applicable laws and regulations.
