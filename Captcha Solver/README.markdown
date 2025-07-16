# CAPTCHA Solver Scripts for IRCTC and IISC Login

This repository contains two Python scripts designed to automate CAPTCHA solving and login processes for the IRCTC (Indian Railways Catering and Tourism Corporation) and IISC (Indian Institute of Science) login portals. Below is an overview of each script, their requirements, setup instructions, and usage.

## Scripts Overview

### 1. `irctc.py`
- **Purpose**: Automates the login process for the IRCTC meal booking portal by solving image-based CAPTCHAs using OCR (Optical Character Recognition).
- **Functionality**:
  - Opens the IRCTC meal booking page.
  - Captures and preprocesses CAPTCHA images.
  - Extracts text from CAPTCHAs using Tesseract OCR.
  - Fills the CAPTCHA input field and attempts login.
- **Target URL**: `https://www.irctc.co.in/nget/redirect?pnr=2108873329&service=PRS_MEAL_BOOKING`

### 2. `IISC_CAPTCHA.py`
- **Purpose**: Automates the login process for the IISC GOAPS portal by solving mathematical CAPTCHA expressions.
- **Functionality**:
  - Reads credentials from a file.
  - Captures and preprocesses CAPTCHA images.
  - Uses EasyOCR and Tesseract OCR to extract mathematical expressions.
  - Evaluates the expression and submits the result to log in.
- **Target URL**: `https://goaps.iisc.ac.in/login`

## Requirements

### Common Dependencies
- **Python**: Version 3.8 or higher
- **Selenium**: For browser automation
  ```bash
  pip install selenium
  ```
- **OpenCV (cv2)**: For image processing
  ```bash
  pip install opencv-python
  ```
- **Pillow (PIL)**: For image handling
  ```bash
  pip install Pillow
  ```
- **NumPy**: For numerical operations
  ```bash
  pip install numpy
  ```

### Script-Specific Dependencies

#### For `irctc.py`
- **Tesseract OCR**: For text extraction from CAPTCHAs
  - Download and install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki).
  - Update the `TESSERACT_PATH` variable in the script with the path to `tesseract.exe`.
- **ChromeDriver**: For Selenium to control Chrome
  - Download ChromeDriver compatible with your Chrome version from [here](https://chromedriver.chromium.org/downloads).
  - Update the `CHROMEDRIVER_PATH` variable in the script.
- **Google Chrome**: Ensure Chrome is installed, and update the `CHROME_PATH` variable with the path to `chrome.exe`.

#### For `IISC_CAPTCHA.py`
- **Tesseract OCR**: Same as above, update the `tesseract_path` variable.
- **EasyOCR**: For enhanced OCR capabilities
  ```bash
  pip install easyocr
  ```
- **ChromeDriver**: Same as above, update the `chrome_driver_path` variable.
- **Credentials File**: Create a `credential.txt` file with username and password pairs in the format:
  ```
  username1,password1
  username2,password2
  ```
  Update the `credentials_file` path in the script.

## Setup Instructions



1. **Install Tesseract OCR**:
   - Install Tesseract and add it to your system PATH or update the script paths accordingly.

2. **Download ChromeDriver**:
   - Place the `chromedriver.exe` in the specified directory and update the script paths.

3. **Configure Paths**:
   - Update the paths for Tesseract, ChromeDriver, Chrome, and credentials file in both scripts as per your system.

4. **Prepare Credentials (for `IISC_CAPTCHA.py`)**:
   - Create a `credential.txt` file with valid IISC login credentials.

## Usage

### Running `irctc.py`
1. Ensure all paths (`TESSERACT_PATH`, `CHROMEDRIVER_PATH`, `CHROME_PATH`) are correctly set.
2. Run the script:
   ```bash
   python irctc.py
   ```
3. The script will:
   - Open the IRCTC URL in Chrome.
   - Click the login button.
   - Capture, preprocess, and solve the CAPTCHA.
   - Fill the CAPTCHA input and wait for 30 seconds before closing the browser.

### Running `IISC_CAPTCHA.py`
1. Ensure all paths (`tesseract_path`, `chrome_driver_path`, `credentials_file`) are correctly set.
2. Ensure `credential.txt` contains valid credentials.
3. Run the script:
   ```bash
   python IISC_CAPTCHA.py
   ```
4. The script will:
   - Iterate through the credentials in `credential.txt`.
   - Open the IISC login page.
   - Capture and preprocess the CAPTCHA image.
   - Extract and evaluate the mathematical expression using EasyOCR and Tesseract.
   - Submit the login form and check for success.
   - Keep the browser open until manually closed (Ctrl+C).

## Notes
- **CAPTCHA Solving Accuracy**:
  - CAPTCHAs can be challenging due to noise and distortion. The scripts use preprocessing to improve accuracy but may fail on complex CAPTCHAs.
  - `IISC_CAPTCHA.py` uses a fallback answer (`1234`) if OCR fails.
- **Error Handling**:
  - Both scripts include error handling and logging. Check console output for debugging.
  - `IISC_CAPTCHA.py` saves screenshots and page source on errors for analysis.
- **Legal and Ethical Considerations**:
  - Ensure compliance with the terms of service of IRCTC and IISC portals.
  - These scripts are for educational purposes and should be used responsibly.
- **Performance**:
  - EasyOCR in `IISC_CAPTCHA.py` can be slow without GPU. Set `gpu=False` if no CUDA-compatible GPU is available.

## Troubleshooting
- **Tesseract not found**: Verify the Tesseract installation and path in the script.
- **ChromeDriver version mismatch**: Ensure ChromeDriver matches your Chrome browser version.
- **OCR failures**: Check the `processed_captcha.png` output to debug preprocessing issues.
- **Login failures**: Verify credentials and check for CAPTCHA changes on the target websites.
