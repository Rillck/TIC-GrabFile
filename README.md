# 🤏 TIC-GrabFile

**TIC-GrabFile** is a lightweight Python utility that helps you automatically select and copy files related to a list of TESS targets (TICs) from a folder. It's ideal for organizing outputs from TESS data analysis workflows like TESS-Localize or light curve pipelines.

---

## 📦 Features

- 📂 Selects a `.txt` file containing a list of TIC IDs.
- 📁 Lets you choose the folder containing all result files (e.g., `.png`, `.dat`, `.fits`).
- 🔍 Automatically scans filenames for numeric blocks.
- 📌 Copies files that match any TIC number found within those blocks.
- 🗂 Creates a new folder named `Selected <original_folder>` with all matching files.

---

## 🧪 Example

If your `TICs.txt` contains:
```
741852
963258
```

And your folder has files like:
```
TIC741852_12_SNR.png
note_963258_prewhitening.dat
otherfile_000000000.fits
```

✅ Only the first two files will be copied to:
```
Selected <your-folder-name>/
```

---

## 🛠 How to Use

1. 📌 Place `TIC-GrabFile.py` in the folder with your `.txt` file and the target data folder.
2. 🐍 Run the script using:

```bash
python TIC-GrabFile.py
```

3. ✅ Follow the terminal prompts to:
   - Select your `.txt` file with TICs.
   - Select the folder with your files to filter.
4. 🎉 All matching files will be copied to the new folder automatically.

---

## 📎 Requirements

- Python 3.7+
- [inquirer](https://pypi.org/project/inquirer/)

Install with:

```bash
pip install inquirer
```

---

## 📁 Folder Structure Suggestion

```
project/
│
├── TIC-GrabFile.py
├── TICs.txt
└── <original_folder>/
```

---

## 🤖 Behind the Scenes

The script parses each filename, extracts numeric blocks using regex, and compares them to your list of TICs. It's smart enough to ignore prefixes like "TIC" or other characters.

---

## 🧠 Why “GrabFile”?

Because it's quick and efficient — just grab the files you need by TIC!

---

## 📃 License

MIT License

---

## 👤 Author

Developed by **De Amorim, R G S B**  
Inspired by TESS data analysis workflows.
