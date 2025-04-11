# How to Find the Cookies for Tiktok API

Follow these steps to retrieve the necessary cookies for authentication:

## Steps:

1. **Login to Tiktok**
   - Open your web browser and log in to your Tiktok account.

2. **Open Developer Tools**
   - Press `F12` or `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac) to open Developer Tools.

3. **Go to the Application Tab**
   - In Developer Tools, navigate to the **Network** tab and filter the requests.

4. **Expand Cookies**
   - Under **Search Bar**, Search the `api` section. The domain most likely `https://www.tiktok.com/api/`

5. **Find `msToken`,`X-Bogus` and `_Signature`**
   - Look for `msToken`,`X-Bogus` and `_Signature` in the url of the `API`.

6. **Copy the Token to `token.json`**
   - Create a `token.json` file and store the values in the following format:
   
   ```json
   {
      "msToken":"YOUR MS TOKEN",
      "X-Bogus":"YOUR X BOGUS",
      "_signature":"YOUR SIGNATURE"
   }
   ```

7. **Run Your Code**
   - Ensure your script loads the `token.json` file and uses the stored values for authentication.

Now you're ready to use Tiktok's API with authenticated requests! 🚀

