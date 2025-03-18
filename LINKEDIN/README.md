# How to Find the Cookies for LinkedIn API

Follow these steps to retrieve the necessary cookies for authentication:

## Steps:

1. **Login to LinkedIn**
   - Open your web browser and log in to your LinkedIn account.

2. **Open Developer Tools**
   - Press `F12` or `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac) to open Developer Tools.

3. **Go to the Application Tab**
   - In Developer Tools, navigate to the **Application** tab.

4. **Expand Cookies**
   - Under **Storage**, expand the **Cookies** section.
   - Select `https://www.linkedin.com`.

5. **Find `li_at` and `JSESSIONID`**
   - Look for `li_at` and `JSESSIONID` in the list of cookies.

6. **Copy the Cookies to `cookies.json`**
   - Create a `cookies.json` file and store the values in the following format:
   
   ```json
   {
       "li_at": "your_li_at_value",
       "JSESSIONID": "your_jsessionid_value"
   }
   ```

7. **Run Your Code**
   - Ensure your script loads the `cookies.json` file and uses the stored values for authentication.

Now you're ready to use LinkedIn's API with authenticated requests! 🚀

