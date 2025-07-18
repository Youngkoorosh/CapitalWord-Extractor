# CapitalWord-Extractor
A Python-based tool designed to extract words starting with a capital letter (excluding sentence starters) from a given text, along with their word positions. This project is ideal for developers, text processing enthusiasts, or anyone interested in analyzing text patterns.

## Features

* Extract Capitalized Words: Identifies words starting with a capital letter, ignoring those at the start of sentences.

* Word Position Tracking: Outputs the position of each capitalized word in the text (starting from 1).

* Punctuation Handling: Removes trailing commas and periods from words before processing.

* Number Filtering: Excludes numbers from being considered as capitalized words.

* Simple Output Format: Displays results in a clean position:word format or None if no matches are found.

## Installation
Follow these steps to set up CapitalWord Extractor locally:
1. Clone the repository:
```bash
git clone https://github.com/username/capitalword-extractor.git
```
git clone https://github.com/username/capitalword-extractor.git

2. Navigate to the project directory:
```bash
cd capitalword-extractor
```
3.Install dependencies:

* Ensure you have Python 3.6 or higher installed.

* No additional dependencies are required, as the project uses only Python's standard library.

4.Run the script:
```bash
The main script is extractor.py (or the name of your main Python file).
```

##Usage

Run the script and provide a text input to extract capitalized words. Example:
```bash
python extractor.py
```
Input Example:
```plian
Enter text: The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. This video was captured by one of our heroes who wishes peace.
```
Output Example:
```plain
2:Persian
3:League
15:Iran
17:Persian
18:League
```
For more details, see the documentation folder (if applicable).

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.

2. Create a new branch (git checkout -b feature-branch).

3. Make your changes and commit (git commit -m 'Add some feature').

4. Push to the branch (git push origin feature-branch).

5. Open a Pull Request.

Please read our Contributing Guidelines for more details.

## Acknowledgments
* Built with Python's standard library for simplicity and accessibility.

* Inspired by text processing challenges and the need for simple, efficient tools.

## Contact
For questions or feedback, reach out to:
* Maintainer: koorosh.nrp@gmail.com

* Project Repository: CapitalWord Extractor
