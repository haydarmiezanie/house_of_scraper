# How to Find the Cookies for X API

Follow these steps to retrieve the necessary cookies for authentication:

## Steps:

1. **Login to X**
   - Open your web browser and log in to your X account.

2. **Open Developer Tools**
   - Press `F12` or `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac) to open Developer Tools.

3. **Go to the Application Tab**
   - In Developer Tools, navigate to the **Application** tab.

4. **Expand Cookies**
   - Under **Storage**, expand the **Cookies** section.
   - Select `https://www.X.com`.

5. **Find `authorization`, `cookie` and `x-csrf-token`**
   - Look for `authorization`, `cookie` and `x-csrf-token` in the list of cookies.

6. **Copy the Cookies to `headers.json`**
   - Create a `headers.json` file and store the values in the following format:
   
   ```json
   {
       "authorization": "your_authorization_value",
       "x-csrf-token": "your_x-csrf-token_value",
       "cookie": "cookie"
   }
   ```

7. **Run Your Code**
   - Ensure your script loads the `authorization.json` file and uses the stored values for authentication.

Now you're ready to use X's API with authenticated requests! 🚀

