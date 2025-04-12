# How to Find the Cookies for Facebook API

Follow these steps to retrieve the necessary cookies for authentication:

## Steps:

1. **Login to Facebook**
   - Open your web browser and log in to your Facebook account.

2. **Open Developer Tools**
   - Press `F12` or `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac) to open Developer Tools.

3. **Go to the Network Tab**
- In Developer Tools, navigate to the **Network** tab.

4. **Expand Payload**
   - Under **Payload**, expand payload and find the **Form Data** section.
   - Select `view parsed` to view the parsed form data.

5. **Find `variables` and `doc_id`**
   - Look for `variables` and `doc_id` in the list of payload.

6. **Copy the Payload to `data.json`**
   - Create a `data.json` file and store the values in the following format:
   
   ```json
   {
      "variables": "YOUR VARIABLES",
      "doc_id": "DOCUMENT ID"
   }
   ```

7. **Run Your Code**
   - Ensure your script loads the `data.json` file and uses the stored values for authentication.


Now you're ready to use Facebook's API with authenticated requests! 🚀

