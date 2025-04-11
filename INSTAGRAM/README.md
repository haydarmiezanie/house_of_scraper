# How to Find the Cookies for Instagram API

Follow these steps to retrieve the necessary cookies for authentication:

## Steps:

1. **Login to Instagram**
   - Open your web browser and log in to your Instagram account.

2. **Open Developer Tools**
   - Press `F12` or `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac) to open Developer Tools.

3. **Go to the Application Tab**
   - In Developer Tools, navigate to the **Application** tab.

4. **Expand Cookies**
   - Under **Storage**, expand the **Cookies** section.
   - Select `https://www.instagram.com`.

5. **Find `session_id` and `csrf-token`**
   - Look for `session_id` and `csrf-token` in the list of cookies.

6. **Copy the Cookies to `cookies.json`**
   - Create a `cookies.json` file and store the values in the following format:
   
   ```json
   {
      "sessionid":"YOUR SESSION ID",
      "csrftoken":"YOUR CSRF TOKEN"
   }
   ```
7. **Go to the Network Tab**
   - In Developer Tools, navigate to the **API** tab.

8. **Find `X-Ig-App-Id` and `csrf-token`**
   - Look for `X-Ig-App-Id` and `csrf-token` in the list of headers.

9. **Copy the Headers to `headers.json`**
   - Create a `headers.json` file and store the values in the following format:
   
   ```json
   {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": "YOUR CSRF TOKEN",
      "X-Ig-App-Id":"YOUR IG APP ID"
   }
   ```

9. **Run Your Code**
   - Ensure your script loads the `cookies.json` file and uses the stored values for authentication.
   - Ensure your script loads the `headers.json` file and uses the stored values for authentication.


Now you're ready to use Instagram's API with authenticated requests! 🚀

