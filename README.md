This script converts an exported deck from AnkiApp (https://www.ankiapp.com/) — an XML file — into a TXT file that can be imported into Anki.
Tested only with simple cards (furigana/English).

 How it works

* The addon processes lines in the following format:

  ```
  And = Soshite / sorede  
  But = shikashi / demo / data
  ```
* The addon converts the part before the equal sign to one side of the card, and the part after — to the other side.

* Lines that **do not contain `=` or `-` are ignored**


---

### 📄 How to Convert AnkiApp XML Deck to Anki Import Format

Use this Python script to convert an `.xml` deck exported from **AnkiApp** into a `.txt` file that can be imported into the original **Anki**.

---

### ✅ Steps:

1. **Place the files in the same folder:**

   * `ankiapp_export.xml` (your exported AnkiApp file)
   * `convert_ankiapp_xml.py` (the script)

2. **Open Command Prompt** = cmd and navigate to the folder:

   ```bash
   cd /d "path\to\your\folder"
   ```

3. **Run the script**:

   ```bash
   python convert_ankiapp_xml.py
   ```

4. The script will create a file called:

   ```
   anki_import.txt

5. Use ChatGPT if it doesnt work
 


