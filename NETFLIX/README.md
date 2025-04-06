# How to Find the Cookies for Netflix API

Follow these steps to retrieve the necessary cookies for authentication:

## Steps:

1. **Login to Netflix**
   - Open your web browser and log in to your Netflix account.

2. **Open Developer Tools**
   - Press `F12` or `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac) to open Developer Tools.

3. **Go to the Application Tab**
   - In Developer Tools, navigate to the **Application** tab.

4. **Expand Cookies**
   - Under **Storage**, expand the **Cookies** section.
- Select `https://www.netflix.com`.

5. **Find `NetflixId` and `SecureNetflixId`**
   - Look for `NetflixId` and `SecureNetflixId` in the list of cookies.

6. **Copy the Cookies to `cookies.json`**
   - Create a `cookies.json` file and store the values in the following format:
   
   ```json
   {
       "NetflixId": "your_NetflixId_value",
       "SecureNetflixId": "your_SecureNetflixId_value"
   }
   ```

7. **Run Your Code**
   - Ensure your script loads the `cookies.json` file and uses the stored values for authentication.

Now you're ready to use Netflix's API with authenticated requests! 🚀

