# 📥 How to Get HTTP Headers in Mozilla Firefox, Google Chrome, and Opera

Sometimes you need to check HTTP headers for debugging, development, or API testing. Here's a step-by-step guide for viewing headers in the most common browsers.



## 🌐 Google Chrome

### Steps:

1. Open **Google Chrome** and go to the desired webpage.
2. Right-click anywhere on the page and select **Inspect**, or press `Ctrl+Shift+I` / `Cmd+Option+I`.
3. Go to the **Network** tab.
4. Reload the page (`F5` or `Ctrl+R`).
5. Click on the **first request** (usually the document or `index`).
6. In the right panel, click on the **Headers** tab.
7. Scroll through the **Request Headers** and **Response Headers**.

> 🔍 Tip: You can also filter requests by type (e.g., XHR, JS, Doc) to narrow down what you're looking for.



## 🦊 Mozilla Firefox

### Steps:

1. Open **Firefox** and navigate to the desired webpage.
2. Press `F12` or `Ctrl+Shift+I` (`Cmd+Opt+I` on Mac) to open the Developer Tools.
3. Go to the **Network** tab.
4. Reload the page (`F5`).
5. Click on the first or relevant request.
6. On the right, click on **Headers**.
7. View **Request Headers** and **Response Headers**.

> 🛠️ Note: You can right-click a request and select **Copy → Copy as cURL** if needed.



## 🧭 Opera

Opera uses the same DevTools as Chrome, so the steps are nearly identical.

### Steps:

1. Open **Opera** and go to the desired webpage.
2. Right-click and choose **Inspect Element**, or press `Ctrl+Shift+I`.
3. Select the **Network** tab.
4. Reload the page.
5. Click on the first request.
6. Look under the **Headers** tab for:
   - General information
   - Request Headers
   - Response Headers

> ✅ Shortcut: Use `Ctrl+Shift+E` to go directly to the Network tab in Opera.



## ✅ Summary Table

| Browser       | DevTools Shortcut | Network Tab | Header Location         |
|---------------|-------------------|-------------|--------------------------|
| Chrome        | Ctrl+Shift+I      | Yes         | Network → Headers        |
| Firefox       | Ctrl+Shift+I      | Yes         | Network → Headers        |
| Opera         | Ctrl+Shift+I      | Yes         | Network → Headers        |
