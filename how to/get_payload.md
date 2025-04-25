# 📦 How to Get Network Payload (Request/Response) in Mozilla, Chrome, and Opera

This guide will walk you through inspecting and extracting network payloads (like API requests and responses) using the built-in developer tools in popular browsers.



## 🌐 Google Chrome

1. **Open Developer Tools**  
   Press `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac), or right-click on the page and select **Inspect**.

2. **Go to the Network Tab**  
   Click on the **Network** tab.

3. **Reload the Page**  
   Press `F5` or `Ctrl + R` to capture all network activity.

4. **Filter Requests (Optional)**  
   Use the filter (e.g., **XHR** or **Fetch**) to find API requests easily.

5. **Select a Request**  
   Click on the desired request in the list.

6. **View the Payload**  
   - **Request Payload**: Go to the **Headers** tab → scroll to **Request Payload** or **Form Data**.
   - **Response Payload**: Go to the **Response** tab to view the API response.



## 🦊 Mozilla Firefox

1. **Open Developer Tools**  
   Press `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac), or right-click and choose **Inspect**.

2. **Switch to the Network Tab**

3. **Refresh the Page**  
   Press `F5` to load network traffic.

4. **Filter Requests (Optional)**  
   Use filters like **XHR** to focus on API calls.

5. **Click a Request**

6. **Inspect Payloads**  
   - **Request Payload**: In the **Headers** section under **Request Payload** or **Post Data**.
   - **Response Payload**: In the **Response** tab.



## 🧭 Opera Browser

> Opera uses the **same DevTools** as Google Chrome since it's Chromium-based.

1. **Open Developer Tools**  
   Press `Ctrl + Shift + I` or right-click → **Inspect Element**.

2. **Open the Network Tab**

3. **Reload the Page**  
   Press `F5` to capture traffic.

4. **Filter and Choose a Request**

5. **Inspect the Payload**
   - **Request Payload**: Inside the **Headers** tab.
   - **Response Payload**: Inside the **Response** tab.



## ✅ Tips

- Use the **"Preserve log"** checkbox to retain logs after navigation.
- Right-click and choose **"Copy → Copy as cURL"** to replicate the request.
- Use **JSON Viewers** or formatters to better read payloads.


