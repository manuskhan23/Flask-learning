console.log("todo app js loaded");

// ============= LOCAL STORAGE FUNCTIONS =============

const StorageManager = {
  // Initialize - check on page load if user is logged in
  init() {
    this.checkLoginStatus();
  },

  // Check if user is logged in
  checkLoginStatus() {
    const isLoggedIn = localStorage.getItem("isloggedin") === "true";
    const userId = localStorage.getItem("userid");
    const currentPath = window.location.pathname;

    // If logged in and trying to access login/register, redirect to home
    if (isLoggedIn && userId && (currentPath === "/login" || currentPath === "/register" || currentPath === "/auth/login" || currentPath === "/auth/register")) {
      window.location.href = "/";
    }

    // If not logged in and trying to access task routes, redirect to login
    if (!isLoggedIn && currentPath === "/" || (currentPath.includes("/task") && currentPath !== "/logout")) {
      window.location.href = "/login";
    }
  },

  // Store login data
  storeLogin(userId, username) {
    localStorage.setItem("userid", userId);
    localStorage.setItem("isloggedin", "true");
    localStorage.setItem("username", username);
    console.log("Login stored in localStorage", { userId, username });
  },

  // Clear login data but keep userid
  storeLogout() {
    localStorage.setItem("isloggedin", "false");
    // userid remains the same
    console.log("Logout stored in localStorage");
  },

  // Clear all data
  clearAll() {
    localStorage.removeItem("userid");
    localStorage.removeItem("isloggedin");
    localStorage.removeItem("username");
  },

  // Get login status
  isLoggedIn() {
    return localStorage.getItem("isloggedin") === "true";
  },

  // Get user id
  getUserId() {
    return localStorage.getItem("userid");
  },

  // Get username
  getUsername() {
    return localStorage.getItem("username");
  }
};

// ============= LOGIN FORM HANDLING =============

const LoginHandler = {
  init() {
    // Find form on login page (with username and password inputs)
    const loginForm = document.querySelector("form input[name='username']")?.closest("form");
    if (loginForm) {
      loginForm.addEventListener("submit", (e) => this.handleLoginSubmit(e));
    }
  },

  handleLoginSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const username = form.querySelector("input[name='username']").value;
    const password = form.querySelector("input[name='password']").value;
    const formAction = form.action || window.location.href;

    fetch(formAction, {
      method: "POST",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: new URLSearchParams({
        username: username,
        password: password
      })
    })
    .then(response => {
      console.log("Response status:", response.status);
      return response.json().catch(() => response.text());
    })
    .then(data => {
      console.log("Response data:", data);
      if (typeof data === "object" && data.success) {
        StorageManager.storeLogin(data.user_id, data.username);
        console.log("Login successful, redirecting to /");
        window.location.href = "/";
      } else if (typeof data === "object" && !data.success) {
        alert(data.message || "Login failed");
      } else {
        // Fallback if response is not JSON
        console.log("Unexpected response type, using form fallback");
        form.submit();
      }
    })
    .catch(error => {
      console.error("Login error:", error);
      form.submit(); // Fallback to standard form submission
    });
  }
};

// ============= LOGOUT HANDLING =============

const LogoutHandler = {
  init() {
    const logoutLinks = document.querySelectorAll("a[href*='logout']");
    logoutLinks.forEach(link => {
      link.addEventListener("click", (e) => this.handleLogout(e));
    });
  },

  handleLogout(e) {
    e.preventDefault();
    
    const logoutUrl = e.target.getAttribute("href");

    fetch(logoutUrl, {
      method: "GET",
      headers: {
        "X-Requested-With": "XMLHttpRequest"
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        StorageManager.storeLogout();
        window.location.href = "/login";
      }
    })
    .catch(error => {
      console.error("Logout error:", error);
      // Fallback to standard redirect
      StorageManager.storeLogout();
      window.location.href = logoutUrl;
    });
  }
};

// ============= INITIALIZE ON PAGE LOAD =============

document.addEventListener("DOMContentLoaded", () => {
  StorageManager.init();
  LoginHandler.init();
  LogoutHandler.init();
});
